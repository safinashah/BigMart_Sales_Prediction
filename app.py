import streamlit as st
import pandas as pd
import pickle
import zipfile, os

# 🔓 Automatically extract model if ZIP exists
if not os.path.exists("bigmart_model.pkl") and os.path.exists("bigmart_model.zip"):
    with zipfile.ZipFile("bigmart_model.zip", "r") as zip_ref:
        zip_ref.extractall(".")


# === Load Model ===
with open("bigmart_model.pkl", "rb") as f:
    model = pickle.load(f)
sklearn_version = "unknown"

# === 🌈 Page Background Style ===
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #f8d7ff, #ffe6f0);
}
[data-testid="stSidebar"] {
    background-color: #f0f0f0;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# === Title with Glow ===
st.markdown(
    "<h1 style='text-align: center; color: #FF69B4;'>🛒 BigMart Sales Prediction App — By <i>Safina</i> 💫</h1>",
    unsafe_allow_html=True
)
st.markdown("""
<style>
@keyframes glow {
  from {text-shadow: 0 0 10px #ff9ee3, 0 0 20px #ff9ee3;}
  to {text-shadow: 0 0 20px #ff4dc4, 0 0 30px #ff4dc4;}
}
h1 {
  animation: glow 1.5s ease-in-out infinite alternate;
}
</style>
""", unsafe_allow_html=True)

st.markdown(f"Using **scikit-learn v{sklearn_version}** model to predict item sales.")

# === Input Card Start ===
st.markdown("""
<div style="background-color:white; padding:25px; border-radius:20px; 
box-shadow:0 0 20px rgba(0,0,0,0.1); margin-bottom:25px;">
""", unsafe_allow_html=True)

# === User Inputs (Only 3 Used for Prediction) ===
Item_Weight = st.number_input("Item Weight", min_value=0.0, value=12.5)
Item_MRP = st.number_input("Item MRP", min_value=0.0, value=150.0)
Outlet_Establishment_Year = st.number_input("Outlet Establishment Year", min_value=1980, max_value=2025, value=2005)

# === Predict Button ===
if st.button("Predict Sales"):
    input_df = pd.DataFrame([{
        "Item_Weight": Item_Weight,
        "Item_MRP": Item_MRP,
        "Outlet_Establishment_Year": Outlet_Establishment_Year
    }])

    # Make prediction
    prediction = model.predict(input_df)[0]
    st.success(f"📈 Predicted Item Outlet Sales: ₹{prediction:.2f}")

# === Close Input Card ===
st.markdown("</div>", unsafe_allow_html=True)

# === Stylish Predict Button CSS ===
st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #FF69B4;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 1.1em;
    font-weight: bold;
    box-shadow: 0px 4px 10px rgba(255, 105, 180, 0.4);
    transition: all 0.3s ease;
}
div.stButton > button:hover {
    background-color: #ff85c2;
    color: black;
    transform: scale(1.05);
}
</style>
""", unsafe_allow_html=True)
