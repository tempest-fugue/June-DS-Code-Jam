# June-DS-Code-Jam
🎵 SoundScape: Interactive Spotify Dashboard & ML Insights
Ever wondered what makes a hit song? Is it the tempo, the genre, or just pure chance? In this project, we dive into Spotify’s treasure trove of audio features to decode patterns in popular music from the 2000s onward.

Using a publicly available dataset of over 2,000 top Spotify tracks from Kaggle, we built an interactive dashboard using Plotly Dash that visualizes trends across genres and decades—and went one step further by training a predictive model to estimate a song's popularity based on its features. Our goal: to blend exploratory analysis, model-driven insight, and seamless UX in one compelling app.

🚀 Project Highlights
🎛 Interactive Dashboard: Built with Plotly Dash, users can filter by genre, year, and artist to explore the evolution of musical characteristics.
Deployed via Render: https://june-ds-code-jam.onrender.com

🧠 Machine Learning Model: A supervised model predicts song popularity and explains feature contributions.

🎧 Bonus Exploration: We implemented K-means clustering to uncover genre-like song groups and theoretical similarity across tracks.

🔍 Human-Centered Analysis: Beyond metrics, we interpret why the model performs the way it does—its strengths, its blind spots, and real-world usability.

🧠 Industry-Ready Techniques Demonstrated
| Technique Category       | Method / Example                                                                  |
| ------------------------ | --------------------------------------------------------------------------------- |
| **Linear Algebra**       | Feature vector construction, PCA for dimensionality reduction                     |
| **Vector Operations**    | K-means distance calculations, cosine similarity in clustering                    |
| **Vector Distance**      | Euclidean distances used in K-means                                               |
| **Matrix Operations**    | Feature normalization, correlation matrices                                       |
| **Supervised Learning**  | Random Forest Regressor to predict popularity                                     |
| **Model Evaluation**     | R² score, residual plots, SHAP values for interpretability                        |
| **Visualization**        | Plotly bar plots, heatmaps, scatter plots, cluster graphs                         |
| **Pipeline**             | End-to-end: data cleaning → feature selection → modeling → prediction → dashboard |
| **Feature Engineering**  | Year bucketing, one-hot encoding for genres, scaling numerical features           |
| **EDA**                  | Descriptive statistics, outlier detection, genre counts                           |
| **Dashboard Planning**   | Structured for clean integration into Plotly Dash (with toggles and filters)      |
| **Context-Aware Design** | Considered RAG-style context planning for chatbot integration                     |


🧪 How It Works
Step 1: Data Cleaning & Exploration
We prepared the dataset by cleaning anomalies, converting time to datetime, standardizing genre labels, and exploring trends in genre distribution, song energy, and tempo across time.

Step 2: Dashboard Development
Using Plotly Dash, we created a single-page app that includes dropdowns, sliders, and graphs updating in real-time. Users can filter by:

Genre

Year Range

Artists

Step 3: Model Training & Evaluation
We trained a Random Forest Regressor on audio features like danceability, valence, acousticness, and energy to predict song popularity. The model was tuned and evaluated using R² score and visual diagnostics.

Step 4: Clustering Analysis (Bonus)
With K-means, we grouped songs into clusters that highlight similarities across tempo, mood, and genre. This revealed hidden structures in musical taste over time.

Step 5: Prediction Function
New song rows can be inputted to the model, with predicted popularity explained by the most influential features.

## 🎨 Visuals & Assets Screenshots
## 🎨 Visuals & Assets Screenshots

### 🎼 Distribution of Musical Features
![Distribution](visualizations/distribution.png)

### 📊 Mood Score Distribution
![Mood](visualizations/mood.png)

### 🧠 Random Forest Genre Confusion Matrix
![Confusion Matrix](visualizations/random%20forest%20confusion%20matrix.png)

### 🧩 Genre-Based 3D Plotly Visualization
![Plotly Genre](visualizations/plotly%20genre)

### 📈 Feature Distributions (Histograms)
![Feature Histograms](visualizations/visualization_1.png)

### 📉 Feature Distributions (Boxplots)
![Feature Boxplots](visualizations/visualization_2.png)

### 🎤 Top Titles, Artists, and Genres
![Artist & Genre Plots](visualizations/visualization_3.png)

### ⏳ Feature Trends Over Time
![Temporal Trends](visualizations/visualization_4.png)

### 🔥 Correlation Heatmap
![Correlation Heatmap](visualizations/visualization_5.png)

### 🔗 Pairwise Feature Relationships
![Pairplot](visualizations/visualization_6.png)





| Feature                             | Result / Insight                                                                 |
|-------------------------------------|----------------------------------------------------------------------------------|
| Most Popular Genre (by average pop)| Dance Pop                                                                        |
| Year with Peak Popularity           | 2016                                                                             |
| Top Contributing Feature (Popularity Prediction) | Energy                                                      |
| Model Used                          | Random Forest Regressor                                                          |
| Model R² Score                      | 0.74                                                                             |
| Key Clusters Identified             | 5 major clusters based on energy, valence, and tempo                            |
| Dashboard Functionalities           | Dropdown by genre, year range slider, multi-artist filter, cluster visualizer   |

🧪 Model Results
| Model               | Accuracy | F1 Score | AUC-ROC | Training Time (s) |
| ------------------- | -------- | -------- | ------- | ----------------- |
| Gradient Boosting   | 0.694    | 0.671    | 0.939   | 2.64              |
| Random Forest       | 0.689    | 0.655    | 0.943   | 0.27              |
| Decision Tree       | 0.680    | 0.653    | 0.803   | 0.01              |
| CatBoostClassifier  | 0.676    | 0.645    | 0.941   | 4.76              |
| Logistic Regression | 0.571    | 0.595    | 0.930   | 0.04              |

🧪 Conclusion 
This project explores music trends through the lens of Spotify song data, using features like energy, danceability, speechiness, and popularity. The primary goal was to build an interactive Plotly Dash dashboard that allows users to visualize how musical characteristics vary across genres and over time. The analysis includes extensive feature engineering, clustering by mood and genre, and training several supervised learning models to predict a song’s popularity. With visualizations ranging from 3D mood mapping to temporal genre trends, the project not only showcases data storytelling but also integrates real-world machine learning workflows suitable for production environments.

🤝 Contributing
If you’d like to extend this project or automate more insight generation, feel free to fork and submit a pull request.

🧭 Project Structure
📁 June-DS-Code-Jam/
│
├── Spotify Genre Classification EDA-checkpoint 2.0.ipynb  ← Feature engineering & model pipeline
├── README.md                                               ← You're here
├── /visualizations                                         ← Graph assets
├── /models                                                 ← Trained model artifacts
└── /data                                                   ← Spotify song dataset

📚 Data Source & Challenge Criteria
This project was built as part of a bootcamp capstone challenge.
🔗 Challenge Description & Rules
🪪 License
Licensed under the MIT License

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Platform](https://img.shields.io/badge/Platform-JupyterLab%20%7C%20Notebook-lightgrey.svg)
![Status](https://img.shields.io/badge/Status-Exploratory-blueviolet.svg)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)

