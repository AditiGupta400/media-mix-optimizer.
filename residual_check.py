import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 1. Load data
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(script_dir, "advertisement_clean.csv")
df = pd.read_csv(csv_file_path)

# 2. Train the model to get predictions
X = df[['TV', 'Radio', 'Newspaper']]
y = df['Sales']
model = LinearRegression()
model.fit(X, y)

# 3. Calculate predictions and residuals
predictions = model.predict(X)
residuals = y - predictions

# 4. Plot the Residuals
plt.figure(figsize=(8, 5))
plt.scatter(predictions, residuals, color='purple', alpha=0.6, edgecolors='k')
plt.axhline(y=0, color='red', linestyle='--', linewidth=2)
plt.title('Residual Plot: Check for Random Scatter')
plt.xlabel('Predicted Sales Units')
plt.ylabel('Residuals (Errors)')
plt.grid(True, linestyle=':', alpha=0.6)

# Save the plot image to your folder
plot_path = os.path.join(script_dir, "residual_plot.png")
plt.savefig(plot_path)
print("\n🔮 --- Residual Check Complete ---")
print(f"✅ Success! Your error chart has been saved as: {plot_path}")
print("Open 'residual_plot.png' in VS Code to view it!")