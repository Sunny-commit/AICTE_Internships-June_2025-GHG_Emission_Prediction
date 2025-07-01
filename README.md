# AICTE_Internships-June_2025-GHG_Emission_Prediction
AICTE Internship Project - Predicting Greenhouse Gas Emissions using Machine Learning and Data Science.

🌿 Greenhouse Gas Emissions Prediction
AICTE Internship Project – June 2025

📌 Project Overview
This project aims to predict Greenhouse Gas (GHG) emissions based on historical data of U.S. commodities and industries using machine learning techniques. Developed as part of the AICTE Internship 2025, the goal is to leverage data analytics to model environmental impacts and support climate-conscious decision-making.

🎯 Problem Statement
Greenhouse gases significantly affect climate change, and industries are major contributors. The objective of this project is to:

Analyze GHG emission patterns from 2010 to 2016 across U.S. supply chains.
Predict future emissions using machine learning models.
Identify key factors contributing to high emissions in both commodity and industry sectors.
📚 Dataset
Name: Supply Chain GHG Emission Factors for US Commodities and Industries
Format: Excel spreadsheet with multiple sheets (2010–2016)
Sheets:
2010_Detail_Commodity
2010_Detail_Industry
... up to 2016
Each sheet contains GHG emission factors for different economic activities in CO₂ equivalent metrics.

💻 Technologies & Libraries Used
Language: Python 3.x
Tools: Jupyter Notebook
Libraries:
pandas – data manipulation
numpy – numerical operations
matplotlib & seaborn – data visualization
scikit-learn – machine learning
joblib – model serialization
⚙️ Machine Learning Workflow
Data Loading & Merging

Load yearly Excel sheets
Merge relevant columns and standardize formats
Data Cleaning

Handle missing values
Drop irrelevant or redundant columns
Feature Engineering

Encode categorical variables
Normalize numerical data
Model Training

Split data into training and testing sets
Train a Random Forest Regressor
Perform hyperparameter tuning using GridSearchCV
Model Evaluation

Evaluate using:
R² Score
RMSE (Root Mean Squared Error)
MAE (Mean Absolute Error)
Model Saving

Save the final model using joblib for deployment or reuse
📈 Results
Metric	Value
R² Score	0.87
RMSE	1.23
Best Model	Random Forest Regressor
