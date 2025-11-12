# 🛒 BigMart Sales Prediction App

A Streamlit web app that predicts **BigMart item sales** using machine learning.

---

## 🚀 Project Overview

This project predicts sales of retail products at different BigMart outlets using product and store-related attributes.

**Tech Stack:**
- Python 🐍  
- Streamlit 🌈  
- Pandas & NumPy  
- Scikit-learn  
- MySQL (for data storage)

---

## 🧠 Model Training

Model used: **RandomForestRegressor**  
Trained on features like:
- Item_Weight  
- Item_MRP  
- Outlet_Establishment_Year  

Saved as: `bigmart_model.pkl`

---

## 💻 Run Locally

To run this project on your system, open your terminal or VS Code and run all the following commands **one by one** 👇

```bash
# Clone this repository
git clone https://github.com/safinashah/BigMart_Sales_Prediction.git

# Navigate to the project folder
cd BigMart_Sales_Prediction

# Create and activate virtual environment (optional but recommended)
python -m venv venv
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
