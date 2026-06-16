import os
import pandas as pd
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# 1. Setup paths and load variables
script_dir = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(script_dir, ".env"))

def run_gemini_eda():
    csv_file_path = os.path.join(script_dir, "advertisement_clean.csv")
    if not os.path.exists(csv_file_path):
        print(f"⚠️ Error: Could not find {csv_file_path}")
        return
        
    df = pd.read_csv(csv_file_path)
    print(f"✅ Cleaned Data Loaded. Shape: {df.shape}")
    
    # 2. RUN THE FORTUNE TELLER MODEL (Machine Learning)
    print("\n🔮 --- Training the Sales Fortune Teller Machine ---")
    
    # What inputs do we use to predict? (TV, Radio, Newspaper)
    X = df[['TV', 'Radio', 'Newspaper']]
    # What target are we trying to predict? (Sales)
    y = df['Sales']
    
    # Split: Hide 20% of the data in our pocket to test the model later
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Create the model machine and let it learn the weights!
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    print("🎯 Model Training Complete!")
    print(f"   -> TV Weight Knob: {model.coef_[0]:.4f}")
    print(f"   -> Radio Weight Knob: {model.coef_[1]:.4f}")
    print(f"   -> Newspaper Weight Knob: {model.coef_[2]:.4f}")
    
    # Test our model against the data we hid in our pocket
    accuracy_score = model.score(X_test, y_test)
    print(f"📊 Model Accuracy Score (R-squared): {accuracy_score:.2%}")
    
    # 3. TEST AN EXAMPLE FUTURE PREDICTION
    # Let's pretend next week we spend: $100 on TV, $50 on Radio, $10 on Newspaper
    future_budget = pd.DataFrame([[100, 50, 10]], columns=['TV', 'Radio', 'Newspaper'])
    predicted_sales = model.predict(future_budget)[0]
    
    print(f"\n✨ --- Live Fortune Teller Prediction ---")
    print(f"   If you spend $100 on TV, $50 on Radio, and $10 on Newspaper...")
    print(f"   🔮 Predicted Sales: {predicted_sales:.2f} units!")

if __name__ == "__main__":
    run_gemini_eda()