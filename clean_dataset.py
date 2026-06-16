import os

# 1. Get the path to your current folder
script_dir = os.path.dirname(os.path.abspath(__file__))
raw_csv_path = os.path.join(script_dir, "advertisement.csv")
clean_csv_path = os.path.join(script_dir, "advertisement_clean.csv")

print("Cleaning dataset formatting...")

# 2. Read the raw text line by line and clean up the extra quotes
cleaned_lines = []
with open(raw_csv_path, 'r', encoding='utf-8') as file:
    for line in file:
        # Remove extra double quotes and spaces from each line
        clean_line = line.replace('""', '').replace('"', '').strip()
        if clean_line:
            cleaned_lines.append(clean_line)

# 3. Handle the header missing an index label
# The header line looks like: ,TV,Radio,Newspaper,Sales
# We will replace that leading comma with 'Index'
if cleaned_lines[0].startswith(','):
    cleaned_lines[0] = 'Index' + cleaned_lines[0]

# 4. Save the beautifully formatted data to a new file
with open(clean_csv_path, 'w', encoding='utf-8') as file:
    for line in cleaned_lines:
        file.write(line + '\n')

print(f"✅ Success! Cleaned data saved as: {clean_csv_path}")

# 5. Let's verify the new shape using Pandas
import pandas as pd
df = pd.read_csv(clean_csv_path)
print(f"New Data Shape: {df.shape}")
print(f"Cleaned Columns Found: {list(df.columns)}")