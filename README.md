# 🦠 COVID-19 Global & India Data Analysis Project

This project provides an in-depth analysis and interactive visualization of the global and India-specific spread of COVID-19. It uses real-world data from public datasets (Kaggle) and powerful tools like Plotly, Streamlit, and Facebook Prophet to explore case trends, build machine learning models, and forecast future outbreaks.

---

## 📌 Features

### 📊 Exploratory Data Analysis (EDA)
- Total confirmed, deaths, recovered cases globally
- Country-wise statistics
- Time-series plots for global and individual country trends
- Pie charts, bar charts, donut charts, and scatter plots

### 🤖 Machine Learning
- **K-Means Clustering** of countries based on case stats
- **Random Forest** classification to detect high-risk zones
- **XGBoost** classification with ROC-AUC and Confusion Matrix
- Feature importance visualization

### 🔮 Time Series Forecasting
- Future prediction of confirmed cases using **Facebook Prophet**
- Visual trend components for long-term analysis

### 🌍 Choropleth Maps
- World map showing the spread of COVID-19 (interactive)
- Animated time-based choropleth

### 🌐 Streamlit Dashboard App
A live interactive dashboard built with **Streamlit**:
- Dropdown to select any country
- Live case metrics (Confirmed, Deaths, Recovered)
- Time-series trend graphs
- Animated global spread
- Interactive heatmap

---

## 📁 Files in this Repository

| File | Description |
|------|-------------|
| `Covid19.ipynb` | Jupyter Notebook with full data analysis, ML, forecasting, and visualizations |
| `Covid.py`      | Streamlit app code for an interactive COVID-19 dashboard |
| `README.md`     | Project documentation |

---

## 🛠️ Tools & Technologies Used

- **Python**
- **Pandas & NumPy** – data manipulation
- **Matplotlib & Seaborn** – charts
- **Plotly Express** – interactive visuals and maps
- **Facebook Prophet** – time series forecasting
- **Scikit-learn** – ML models (Random Forest, KMeans)
- **XGBoost** – advanced classification
- **Streamlit** – for interactive dashboard app
---

## 🚀 How to Run

### 📌 Option 1: Notebook
1. Clone the repo or upload files to Google Colab
2. Open `Covid19.ipynb` and run the cells

### 📌 Option 2: Streamlit App
1. Install Streamlit: `pip install streamlit`
2. Run app:
   ```bash
   streamlit run Covid.py

🧠 Author
Vishal Ramsuchit Bhagat
📍 India
💬 Ask me anything on GitHub
________________________________________
🏁 Final Thoughts
This project not only analyzes the spread and impact of COVID-19 but also demonstrates how data science, machine learning, and modern web tools like Streamlit can come together to produce insightful dashboards and predictions.

