import pandas as pd

# Create a series
data = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(data)

# Create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [55, 30, 65, 20, 45],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'New York']
}
df = pd.DataFrame(data)
print(df)

# check the first few rows of the DataFrame
df.head(2)

# check the last few rows of the DataFrame
df.tail(2)

'''Get the number of rows and columns in the DataFrame'''
df.info()

# Get the data types of each column
df.dtypes

# Get the number of rows and columns in the DataFrame
print("Shape: " + str(df.shape))

# Get summary statistics for the numerical columns in the DataFrame
print(df.describe())

# Sort the DataFrame by the 'Age' column in ascending order and reset the index
df = df.sort_values(by='Age').reset_index(drop=True)
print(df)

# Filter the DataFrame to include only rows where the 'Age' column is greater than 30
print(df.query('Age > 30'))

# Filter the DataFrame to include only rows where the 'Age' column is greater than 50   
print(df[df['Age'] > 50])

# Group the DataFrame by the 'City' column and calculate the mean age for each city
print(df.groupby('City')['Age'].mean())

# Get the unique values in the 'City' column
print(df["City"].unique())

# Get the number of unique values in the 'City' column
print(df["City"].nunique())