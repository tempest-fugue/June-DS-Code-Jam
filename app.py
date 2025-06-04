import pandas as pd
import numpy as np
import plotly.express as px
from dash import Dash, dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import kagglehub
from kagglehub import KaggleDatasetAdapter
import joblib
import difflib
import os

# Load data
df = pd.read_csv("data/spotify_final.csv")

# Build model table of metrics
model_scores = pd.DataFrame({
    'Model': [
        'Gradient Boosting', 
        'Random Forest', 
        'Decision Tree', 
        'CatBoostClassifier', 
        'Logistic Regression'
    ],
    'Accuracy': [0.694, 0.689, 0.680, 0.676, 0.571],
    'F1 Score': [0.671, 0.655, 0.653, 0.645, 0.595],
    'AUC-ROC': [0.939, 0.943, 0.803, 0.941, 0.930],
    'Training Time (s)': [2.6375, 0.2671, 0.0083, 4.7575, 0.0387]
})

# Load saved model + preprocessing tools
model = joblib.load("models/genre_model.pkl")          # Random Forest
scaler = joblib.load("models/scaler.pkl")
encoder = joblib.load("models/label_encoder.pkl")

feature_order = [
    'Year',
    'Beats Per Minute (BPM)',
    'Energy',
    'Danceability',
    'Loudness (dB)',
    'Liveness',
    'Valence',
    'Length (Duration)',
    'Acousticness',
    'Speechiness',
    'Popularity'
]

# Initialize Dash app
app = Dash(__name__, external_stylesheets=[dbc.themes.LUX], suppress_callback_exceptions=True)
app.title = "Spotify Genre Dashboard by The Beat Seekers"

app.layout = dbc.Container([
    html.H1("Spotify Genre Dashboard by The Beat Seekers", className="text-center my-4"),
    
    dcc.Dropdown(
        id='view-selector',
        options=[
            {'label': 'Model Performance & Prediction', 'value': 'models'},
            {'label': 'Valence Over Time', 'value': 'valence'},
            {'label': 'Top 3 Most Popular Songs', 'value': 'audio'}
        ],
        value='models',
        clearable=False
    ),
    html.Div(id='main-content', className="my-4")
], fluid=True)

# Section 1: Model Performance and Prediction
def model_performance_layout():
    fig = px.bar(model_scores, x='Model', y=['Accuracy', 'F1 Score', 'AUC-ROC'],
             barmode='group', title='Model Performance Comparison')

    return html.Div([
        dcc.Graph(figure=fig),

        html.H4("Predict a Genre from Songs in the Dataset:"),
        dbc.Row([
            dbc.Col(
                dcc.Dropdown(
                    id='song-name-input',
                    options=[{'label': title, 'value': title} for title in sorted(df['Title'].unique())],
                    placeholder='Select a Song Title'
                ),
                width=6
            ),
            dbc.Col(html.Button("Predict", id="predict-btn"), width=3),
        ], className="my-2"),
        html.Div(id="prediction-output",className="mt-2")
        ])
    
# Section 2: Valence Over Time
def valence_over_time_layout():
    fig = px.scatter(
        df,
        x="Energy", 
        y="Valence",
        animation_frame="Year",
        color="Top Genre",
        hover_name="Title",
        size="Popularity",
        title="Valence (Mood) of Songs Over Time",
        range_x=[0, 100],
        range_y=[0, 100],
        color_discrete_sequence=px.colors.qualitative.Safe
    )
    return dcc.Graph(figure=fig)

# Section 3: Audio Players
def audio_embed_layout():
    top_tracks = [
        {
            "title": "Dance Monkey",
            "artist": "Tones and I",
            "spotify_id": "2XU0oxnq2qxCpomAAuJY8K"
        },
        {
            "title": "Memories",
            "artist": "Maroon 5",
            "spotify_id": "4cktbXiXOapiLBMprHFErI"
        },
        {
            "title": "All I Want for Christmas Is You",
            "artist": "Mariah Carey",
            "spotify_id": "0bYg9bo50gSsH3LtXe2SQn"
        }
    ]

    return html.Div([
        html.H4("Top 3 Most Popular Songs (Embed View)"),
        *[
            html.Div([
                html.P(f"{track['title']} by {track['artist']}"),
                html.Iframe(
                    src=f"https://open.spotify.com/embed/track/{track['spotify_id']}",
                    width="100%",
                    height="80",
                    style={"border": "none"},
                    allow="encrypted-media"
                )
            ], className="mb-4") for track in top_tracks
        ]
    ])
    
# Dropdown selector for each section
@app.callback(
    Output('main-content', 'children'),
    Input('view-selector', 'value')
)
def update_view(selected_view):
    if selected_view == 'models':
        return model_performance_layout()
    elif selected_view == 'valence':
        return valence_over_time_layout()
    elif selected_view == 'audio':
        return audio_embed_layout()

# Song/Artist Prediction
@app.callback(
    Output('prediction-output', 'children'),
    Input('predict-btn', 'n_clicks'),
    State('song-name-input', 'value')
)
def predict_genre_from_df(n_clicks, title):
    if not n_clicks:
        return ""

    if not title:
        return "Please select a song title."

    # Fuzzy match to find the best matching title
    matched_title = difflib.get_close_matches(title, df["Title"], n=1)
    if not matched_title:
        return f"No matching song found for '{title}'."

    # Get the matched row (do NOT use genre for prediction)
    row = df[df["Title"] == matched_title[0]].iloc[0]
    actual_genre = row["Top Genre"]  # Save actual genre for comparison
    row = row.drop("Top Genre", errors="ignore")  # Drop it to prevent leakage

    try:
        feature_vector = np.array([[
            row["Year"],
            row["Beats Per Minute (BPM)"],
            row["Energy"],
            row["Danceability"],
            row["Loudness (dB)"],
            row["Liveness"],
            row["Valence"],
            row["Length (Duration)"],
            row["Acousticness"],
            row["Speechiness"],
            row["Popularity"]
        ]])

        scaled = scaler.transform(feature_vector)
        prediction = model.predict(scaled)[0]
        decoded_genre = encoder.inverse_transform([prediction])[0]

        return (
            f"Predicted Genre for **{matched_title[0]}**: **{decoded_genre}**\n\n"
            f"Actual Genre in Dataset: **{actual_genre}**"
        )

    except Exception as e:
        return f"Prediction error: {str(e)}"

# Run the app
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8050))
    app.run(host="0.0.0.0", port=port, debug=True)