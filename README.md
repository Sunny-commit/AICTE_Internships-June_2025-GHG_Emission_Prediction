# AICTE_Internships-June_2025-GHG_Emission_Prediction
# 🌿 Greenhouse Gas Emissions Prediction
**AICTE Internship Project – June 2025**

---

## 📌 Project Overview
This project aims to predict Greenhouse Gas (GHG) emissions based on historical data of U.S. commodities and industries using machine learning techniques. Developed as part of the **AICTE Internship 2025**, the goal is to leverage data analytics to model environmental impacts and support climate-conscious decision-making.

---

## 🎯 Problem Statement

Greenhouse gases significantly affect climate change, and industries are major contributors.

The objectives of this project are to:
- Analyze GHG emission patterns from **2010 to 2016** across U.S. supply chains.
- Predict future emissions using **machine learning models**.
- Identify key factors contributing to high emissions in both **commodity and industry sectors**.

---

## 📚 Dataset

- **Name**: Supply Chain GHG Emission Factors for US Commodities and Industries  
- **Format**: Excel spreadsheet with multiple sheets (2010–2016)

### 📄 Sheets:
- `2010_Detail_Commodity`
- `2010_Detail_Industry`
- ...
- `2016_Detail_Commodity`
- `2016_Detail_Industry`

Each sheet contains **GHG emission factors** for different economic activities in **CO₂ equivalent metrics**.

---

## 💻 Technologies & Libraries Used

- **Language**: Python 3.x  
- **Environment**: Jupyter Notebook  

### 🛠️ Libraries:
- `pandas` – Data manipulation
- `numpy` – Numerical operations
- `matplotlib`, `seaborn` – Data visualization
- `scikit-learn` – Machine learning
- `joblib` – Model serialization

---

## ⚙️ Machine Learning Workflow

### 1. **Data Loading & Merging**
- Load all yearly Excel sheets
- Merge relevant columns
- Standardize formats across sheets

### 2. **Data Cleaning**
- Handle missing values
- Drop irrelevant/redundant columns

### 3. **Feature Engineering**
- Encode categorical variables
- Normalize numerical data

### 4. **Model Training**
- Split data into train/test sets
- Train a **Random Forest Regressor**
- Apply **GridSearchCV** for hyperparameter tuning

### 5. **Model Evaluation**
- Metrics used:
  - R² Score
  - RMSE (Root Mean Squared Error)
  - MAE (Mean Absolute Error)

### 6. **Model Saving**
- Save the final model using `joblib` for reuse/deployment

---

## 📈 Results

| **Metric**     | **Value**              |
|----------------|------------------------|
| R² Score       | `0.87`                 |
| RMSE           | `1.23`                 |
| Best Model     | `Random Forest Regressor` |
| Important Features | `Sector Type`, `Emission Type`, `Year`, `Commodity Code` |

---
