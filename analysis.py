import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/cancers-diagnosed-at-stage-1-or-2-chart-data.csv")

# View first rows
print(df.head())

# Plot trend
plt.figure(figsize=(10,6))
plt.plot(df["Time period"], df["England Value"], marker="o")

plt.title("Early Stage Cancer Diagnosis in England (2013–2022)")
plt.xlabel("Year")
plt.ylabel("Percentage Diagnosed at Stage 1 or 2")

plt.grid(True)
plt.show()

