import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score

# 1. Load data
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(script_dir, "advertisement_clean.csv")
df = pd.read_csv(csv_file_path)

X = df[['TV', 'Radio', 'Newspaper']]
y = df['Sales']

# 2. Transform features into Polynomials (Degree=2 adds the squared curves)
poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(X)

# 3. Train the new curved model
poly_model = LinearRegression()
poly_model.fit(X_poly, y)

# 4. Calculate the new metrics
predictions = poly_model.predict(X_poly)
residuals = y - predictions
new_r2 = r2_score(y, predictions)

print("\n🚀 --- Polynomial Upgrade Complete ---")
print(f"📊 New R-squared (Accuracy) Score: {new_r2 * 100:.2f}%")
print(f"📈 Old Linear R-squared Score: 89.94%")
print("---------------------------------------")

# 5. Plot the new residuals to check if the 'U' shape is gone
plt.figure(figsize=(8, 5))
plt.scatter(predictions, residuals, color='teal', alpha=0.6, edgecolors='k')
plt.axhline(y=0, color='red', linestyle='--', linewidth=2)
plt.title('Upgraded Residual Plot: Checking if Curve Flattened')
plt.xlabel('Predicted Sales Units')
plt.ylabel('Residuals (Errors)')
plt.grid(True, linestyle=':', alpha=0.6)

# Save the new plot
plot_path = os.path.join(script_dir, "poly_residual_plot.png")
plt.savefig(plot_path)
print(f"✅ New error chart saved as: {plot_path}\n")