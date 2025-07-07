import streamlit as st
import joblib
import pandas as pd
from utils.preprocessor import preprocess_input

# Load model and scaler
model = joblib.load('models/LR_model.pkl')
scaler = joblib.load('models/scaler.pkl')

# ---- PAGE CONFIG ----
st.set_page_config(page_title="Supply Chain Emissions", layout="centered")

# ---- CUSTOM CSS STYLE ----
st.markdown("""
    <style>
    /* Clean light theme background */
    body, [data-testid="stAppViewContainer"] {
        background-color: #f6f9fc;
    }

    /* Gradient title bar */
    .title-container {
        background: linear-gradient(to right, #a0c4ff, #caffbf);
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 20px;
    }

    .title-container h1 {
        color: #1e3a8a;
        font-size: 2.2rem;
        margin: 0;
    }

    .stMarkdown h3 {
        color: #2c3e50;
    }

    .stSlider > div[data-baseweb="slider"] {
        background-color: #e0f7fa;
        padding: 5px;
        border-radius: 8px;
    }

    .stButton button {
        background-color: #4caf50;
        color: white;
        border-radius: 10px;
        padding: 8px 16px;
        font-weight: bold;
    }

    .stButton button:hover {
        background-color: #388e3c;
    }

    .stNumberInput input {
        background-color: #f0f4f8;
        border-radius: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# ---- HEADER ----
st.markdown('<div class="title-container"><h1>🌱 Supply Chain Emissions Prediction</h1></div>', unsafe_allow_html=True)

st.markdown("""
Welcome! This tool helps you predict **Supply Chain Emission Factors (with margins)**  
using DQ (Data Quality) metrics and supply chain variables.
""")

# ---- INPUT FORM ----
with st.form("prediction_form"):
    st.markdown("### 🧮 Input Parameters")

    substance = st.selectbox("Substance", ['carbon dioxide', 'methane', 'nitrous oxide', 'other GHGs'])
    unit = st.selectbox("Unit", ['kg/2018 USD, purchaser price', 'kg CO2e/2018 USD, purchaser price'])
    source = st.selectbox("Source", ['Commodity', 'Industry'])
    supply_wo_margin = st.number_input("📦 Supply Chain Emission Factors without Margins", min_value=0.0)
    margin = st.number_input("➕ Margins of Supply Chain Emission Factors", min_value=0.0)

    dq_reliability = st.slider("✅ DQ Reliability", 0.0, 1.0, 0.8)
    dq_temporal = st.slider("⏳ DQ Temporal Correlation", 0.0, 1.0, 0.7)
    dq_geo = st.slider("🌍 DQ Geographical Correlation", 0.0, 1.0, 0.6)
    dq_tech = st.slider("🛠️ DQ Technological Correlation", 0.0, 1.0, 0.75)
    dq_data = st.slider("📊 DQ Data Collection", 0.0, 1.0, 0.85)

    submit = st.form_submit_button("🌍 Predict Emission Factor")

# ---- PREDICTION ----
if submit:
    input_data = {
        'Substance': substance,
        'Unit': unit,
        'Supply Chain Emission Factors without Margins': supply_wo_margin,
        'Margins of Supply Chain Emission Factors': margin,
        'DQ ReliabilityScore of Factors without Margins': dq_reliability,
        'DQ TemporalCorrelation of Factors without Margins': dq_temporal,
        'DQ GeographicalCorrelation of Factors without Margins': dq_geo,
        'DQ TechnologicalCorrelation of Factors without Margins': dq_tech,
        'DQ DataCollection of Factors without Margins': dq_data,
        'Source': source,
    }

    input_df = preprocess_input(pd.DataFrame([input_data]))
    input_scaled = scaler.transform(input_df)
    prediction = model.predict(input_scaled)

    st.success(f"🌡️ **Predicted Emission Factor with Margin:** `{prediction[0]:.4f}` kg CO₂e")

# ---- FOOTER ----
st.markdown("---")
st.markdown("""
🔍 *Note*: These predictions are model-based and subject to variability depending on input accuracy and industry-specific data.

📚 Explore more on:  
- [Our World in Data](https://ourworldindata.org/co2-emissions)  
- [EPA Greenhouse Gas Center](https://www.epa.gov/ghgemissions)
""")
