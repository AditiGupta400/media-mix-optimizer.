import os
import pandas as pd
import streamlit as st
import joblib

# 1. Page Configurations
st.set_page_config(
    page_title="Ad Spend ROI Optimizer V2",
    page_icon="📊",
    layout="wide"
)

# 2. Path handling & Loading the Saved Engines
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(script_dir, "advertisement_clean.csv")
model_path = os.path.join(script_dir, "final_sales_model.pkl")
poly_path = os.path.join(script_dir, "poly_transformer.pkl")

@st.cache_resource  # Caches the model loading so it doesn't slow down the site
def load_production_assets():
    df = pd.read_csv(csv_file_path)
    model = joblib.load(model_path)
    poly = joblib.load(poly_path)
    return model, poly, df

try:
    model, poly, df = load_production_assets()
except FileNotFoundError:
    st.error("🚨 Production assets missing! Please run 'python save_model.py' in your terminal first to generate the files.")
    st.stop()

# Get slider limits from our data limits
max_tv = float(df['TV'].max())
max_radio = float(df['Radio'].max())
max_newspaper = float(df['Newspaper'].max())

# --- HEADER ---
st.title("📊 Upgraded Media Mix Optimizer (Production V2)")
st.write("This dashboard is now running your optimized, non-linear Polynomial Regression model.")

st.markdown("---")

# --- INPUT CONTROLS ---
st.subheader("🛠️ Step 1: Adjust Your Advertising Budgets")
slider_col1, slider_col2, slider_col3 = st.columns(3)

with slider_col1:
    tv_input = st.slider("📺 TV Budget ($)", min_value=0.0, max_value=max_tv, value=100.0, step=1.0)
with slider_col2:
    radio_input = st.slider("📻 Radio Budget ($)", min_value=0.0, max_value=max_radio, value=50.0, step=1.0)
with slider_col3:
    newspaper_input = st.slider("📰 Newspaper Budget ($)", min_value=0.0, max_value=max_newspaper, value=10.0, step=1.0)

st.markdown("---")

# --- PRODUCTION LIVE INFERENCE PIPELINE ---
# 1. Format raw inputs from sliders into a dataframe row
raw_features = pd.DataFrame([[tv_input, radio_input, newspaper_input]], columns=['TV', 'Radio', 'Newspaper'])

# 2. Transform the raw inputs into polynomial curves using our saved mathematical transformer
curved_features = poly.transform(raw_features)

# 3. Predict using our frozen model engine weights
predicted_sales = model.predict(curved_features)[0]

total_spend = tv_input + radio_input + newspaper_input

# --- DISPLAY PERFORMANCE OUTPUT ---
st.subheader("✨ Step 2: High-Accuracy Forecast")
col1, col2 = st.columns(2)

with col1:
    st.container(border=True)
    st.metric(label="🔮 Predicted Sales Yield", value=f"{predicted_sales:.2f} Units")

with col2:
    st.container(border=True)
    st.metric(label="💵 Total Budget Spent", value=f"${total_spend:,.2f}")

st.markdown("---")

# --- EXECUTIVE SUMMARY INSIGHTS ---
st.subheader("📝 Strategic Recommendations")
if predicted_sales > 22:
    st.balloons()
    st.success("🏆 **Optimal Matrix Achieved:** This budget configuration takes perfect advantage of the media channel synergy curves. Highly recommended strategy.")
elif tv_input < (max_tv * 0.3) and radio_input > (max_radio * 0.7):
    st.warning("⚠️ **Diminishing Returns Alert:** Radio spend is hitting its curve limits. Consider reallocating some budget over to TV to scale up more efficiently.")
else:
    st.info("💡 **Operational Balance:** Your configuration is running within stable, predictable margins.")