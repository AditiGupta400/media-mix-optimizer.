import os
import pandas as pd
from statsmodels.stats.outliers_influence import variance_inflation_factor

# 1. Load the cleaned dataset
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(script_dir, "advertisement_clean.csv")
df = pd.read_csv(csv_file_path)

# 2. Isolate the independent variables (our features)
# We do not include the target variable (Sales) for VIF calculations
X = df[['TV', 'Radio', 'Newspaper']]

# 3. Create a clean DataFrame to hold the VIF results
vif_data = pd.DataFrame()
vif_data["Feature"] = X.columns

# 4. Calculate the VIF score for each feature
vif_data["VIF Score"] = [variance_inflation_factor(X.values, i) for i in range(len(X.columns))]

# 5. Print the results to the terminal
print("\n🔮 --- Model Health Check: VIF Scores ---")
print(vif_data.to_string(index=False))
print("------------------------------------------")

# Interpret the results using simple rules
for index, row in vif_data.iterrows():
    if row["VIF Score"] > 5:
        print(f"🚨 ALERT: '{row['Feature']}' has a high VIF score! It's a copycat feature.")
    else:
        print(f"✅ PASS: '{row['Feature']}' score looks stable and independent.")