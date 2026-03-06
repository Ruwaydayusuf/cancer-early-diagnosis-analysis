import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Load dataset
# -----------------------------
df = pd.read_csv("data/cancers-diagnosed-at-stage-1-or-2-chart-data.csv")

# Display first rows
print("First 5 rows of dataset:")
print(df.head())

# -----------------------------
# Data Cleaning
# -----------------------------
# Convert columns to correct format
df["Time period"] = pd.to_numeric(df["Time period"], errors="coerce")
df["England Value"] = pd.to_numeric(df["England Value"], errors="coerce")

# Remove missing values
df = df.dropna()

# -----------------------------
# Summary Statistics
# -----------------------------
print("\nSummary statistics:")
print(df["England Value"].describe())

# -----------------------------
# Calculate yearly change
# -----------------------------
df["Yearly Change"] = df["England Value"].diff()

print("\nYearly change in early cancer diagnosis:")
print(df[["Time period", "Yearly Change"]])

# -----------------------------
# Plot trend over time
# -----------------------------
plt.figure(figsize=(10,6))

plt.plot(
    df["Time period"],
    df["England Value"],
    marker="o"
)

plt.title("Early Stage Cancer Diagnosis in England (Stage 1 or 2)")
plt.xlabel("Year")
plt.ylabel("Percentage Diagnosed Early")
plt.grid(True)

plt.show()
