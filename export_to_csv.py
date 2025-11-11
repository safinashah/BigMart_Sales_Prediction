import pymysql
import pandas as pd

# === 1️⃣ MySQL Connection ===
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='RAAJSHAIKH1720.',
    database='BigMart'
)

# === 2️⃣ Read all tables ===
df_item = pd.read_sql("SELECT * FROM item_info;", connection)
df_outlet = pd.read_sql("SELECT * FROM outlet_info;", connection)
df_sales = pd.read_sql("SELECT * FROM sales_info;", connection)

# === 3️⃣ Combine them safely ===
# Step 1: ensure all have same length
print("Rows count:", len(df_item), len(df_outlet), len(df_sales))

# Step 2: Combine side-by-side using concat (since ID matches order)
df = pd.concat([df_sales, df_item, df_outlet], axis=1)

# === 4️⃣ Export to CSV ===
df.to_csv("bigmart_data.csv", index=False)
print("✅ Data successfully exported to bigmart_data.csv!")

connection.close()
