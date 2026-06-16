import os
import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# 1. Load Data
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(script_dir, "advertisement_clean.csv")
df = pd.read_csv(csv_file_path)

X = df[['TV', 'Radio', 'Newspaper']]
y = df['Sales']

# 2. Setup the exact math transformations we built
poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(X)

# 3. Train the final model
final_model = LinearRegression()
final_model.fit(X_poly, y)

# 4. Save BOTH the polynomial transformer and the model engine
# We use joblib because it handles large numpy arrays perfectly
model_path = os.path.join(script_dir, "final_sales_model.pkl")
poly_path = os.path.join(script_dir, "poly_transformer.pkl")

joblib.dump(final_model, model_path)
joblib.dump(poly, poly_path)

print("\n📦 --- Model Export Complete ---")
print(f"💾 Saved Model Engine to: {model_path}")
print(f"💾 Saved Feature Transformer to: {poly_path}")
print("Your model is now frozen and ready to deploy anywhere!")