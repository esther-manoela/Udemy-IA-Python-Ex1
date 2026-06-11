import pandas as pd
import numpy as np

# Create a time series DataFrame
df = pd.DataFrame({
    'Date': pd.date_range(start='2025-01-01', periods=60),
    'Value': np.random.randint(0, 100, size=60)
})

# Month/Year base value
df["Month/Year"] = df["Date"].dt.strftime("%b/%Y")

# Week/Year base value
df["Week/Year"] = df["Date"].dt.strftime("%U/%Y")


groupWeek = df.groupby("Week/Year")["Value"].max()
groupWeek2 = df.groupby("Week/Year")["Value"].agg(["mean", "sum", "std"])
print(df)
print(groupWeek)
print(groupWeek2)