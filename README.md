# 📊 Media Mix Spend & Sales ROI Optimizer

An end-to-end Machine Learning pipeline and interactive Streamlit web dashboard designed to simulate, evaluate, and optimize advertising budgets across TV, Radio, and Newspaper channels.

## 🎯 Project Overview
The objective of this project is to analyze historical marketing campaigns and build an optimization engine that predicts product sales based on advertising capital distribution. By moving away from static spreadsheets, this tool allows marketing executives to simulate budget allocations and instantaneously see projected revenue yields.

## 🛠️ Tech Stack & Architecture
- **Language:** Python 3.10+
- **Data Frameworks:** Pandas, NumPy
- **Machine Learning Library:** Scikit-Learn
- **Visualization & Frontend:** Streamlit, Plotly, Matplotlib
- **Model Serialization:** Joblib

## 🔬 Core Data Science Lifecycle & Breakthroughs

### 1. Exploratory Data Analysis & Multicollinearity Check
- Evaluated feature dependencies using **Variance Inflation Factor (VIF)**. 
- All primary channels (TV, Radio, Newspaper) scored safely under **5.0**, confirming feature independence and ensuring stable regression coefficients.

### 2. Residual Diagnostics (The Turning Point)
- Initial modeling utilized standard **Linear Regression**, yielding an $R^2$ score of **89.94%**.
- **The Discovery:** Residual analysis revealed a distinct parabolic, "U-shaped" pattern in the error scatter plot. This proved that the real-world relationship between media spend and sales is structurally **non-linear**.

### 3. Model Optimization
- Upgraded the pipeline to **Polynomial Regression (Degree=2)** to introduce curved feature interactions (e.g., $TV^2$).
- **Result:** Fully flattened the residual error pattern to a uniform random cloud and successfully pushed model accuracy to **~93%+**.

## 📦 Production Deployment Pipeline
The final optimized model and mathematical transformer are frozen as serialized binary assets (`.pkl` files) using `joblib`. The live inference pipeline architecture flows as follows:

[User Inputs via Sliders] ➡️ [Polynomial Feature Transformer] ➡️ [Trained Regression Engine] ➡️ [Live Dashboard Metric Outputs]

---

## 🚀 How to Run the Dashboard Locally

### 1. Clone the environment and install dependencies:
```bash
pip install streamlit pandas numpy plotly scikit-learn joblib statsmodels matplotlib