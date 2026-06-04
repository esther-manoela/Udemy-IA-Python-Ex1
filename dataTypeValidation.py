import pandas as pd
import numpy as np

# Create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [28, 24, 35, 42, 90],
    'City': ['New York', 'Los Angeles', np.nan, 'Houston', 5]
}

df = pd.DataFrame(data)

# Check data types of each column
print(df['City'].apply(type).value_counts())

### Identify outliers

# Using ranges
print(df['Age'].apply(lambda x: 'Outlier' if x < 20 or x > 50 else ''))

# Using Z-score
result = (df['Age'] - df['Age'].mean())/df['Age'].std()
print(result)
print(result.apply(lambda x: 'Outlier' if x<-1 or x>1 else '')) 


# Identify outliers using IQR
Q1 = df['Age'].quantile(0.25)
Q3 = df['Age'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print('Lower bound: ' + str(lower_bound))
print('Upper bound: ' + str(upper_bound))
print(df['Age'].apply(lambda age: 'Outlier' if age < lower_bound or age > upper_bound else ''))


# Isolation forecast
from sklearn.ensemble import IsolationForest as IS

model = IS(contamination="auto")
result = model.fit_predict(df[['Age']])
print('Isolation Forest Result: ' + str(result))

### Handling outliers
# Delete
print(df.query('Age >= 25 and Age <= 70'))

# Replacing/correcting outliers
result = df['Age'].apply(lambda x: min(x, 65))
print(result)