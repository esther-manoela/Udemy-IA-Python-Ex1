import pandas as pd
import numpy as np

# Create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [55, 30, np.nan, 20, np.nan],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'New York']
}

df = pd.DataFrame(data)
print(df)

# Check for null values in the DataFrame
print('Has null values: ' + str(df.isnull().values.any()))

# Get the total number of null values in the DataFrame
print('Total null values: ' + str(df.isnull().sum().sum()))

# Get the number of null values in each column
print('Null values per column:')
print(df.isnull().sum())

# Get the number of null values in each row
print(df.isnull())

# Get the number of null values in each row
print(df.isnull().any(axis=1))

# Get the number of null values in each column
print(df.isnull().any(axis=0))


### Dealing with missing values
print('Null values per column:')
print(df.isnull().sum())

print('Drop Rows with missing values:')
print(df.dropna(axis=0))  # Drop rows with missing values
print('Drop Columns with missing values:')
print(df.dropna(axis=1))  # Drop columns with missing values

print('Drop Rows with all missing values:')
print(df.dropna(axis=0, how='all'))  # Drop rows with all missing values
print('Drop Columns with all missing values:')
print(df.dropna(axis=1, how='all'))  # Drop columns with all missing values

# Filter the DataFrame to include only rows where the 'Age' column is not null
print('Filter rows where Age is not null:')
print(df[df['Age'].notnull()])

# Fiill missing values with a specific value
print('Fill missing values with 0:')
print(df.fillna(0))

# Fill missing values with the mean of the 'Age' column 
print('Fill missing values with the mean of the Age column:')
print(df.fillna(df['Age'].mean())) 

# Forward fill missing values in the 'Age' column
print('Forward fill missing values in the Age column:')
print(df['Age'].ffill()) 

# Backward fill missing values in the 'Age' column
print('Backward fill missing values in the Age column:')
print(df['Age'].bfill())

# Interpolate missing values in the 'Age' column
print('Interpolate missing values in the Age column:')
print(df['Age'].interpolate())