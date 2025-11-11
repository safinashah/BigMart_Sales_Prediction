import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle

# === 1. Load Data ===
df = pd.read_csv("bigmart_data.csv")
print("✅ Data loaded successfully! Shape:", df.shape)

# === 2. Choose Features (X) and Target (y) ===
X = df[['Item_Weight', 'Item_MRP', 'Outlet_Establishment_Year']]
y = df['Item_Outlet_Sales']

# === 3. Split Data ===
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# === 4. Train Model ===
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)
print("✅ Model trained successfully!")

# === 5. Save Model ===
with open("bigmart_model.pkl", "wb") as f:
    pickle.dump(model, f)
print("💾 Model saved as bigmart_model.pkl")
