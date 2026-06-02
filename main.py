import pandas as pd
import sqlite3 as sql

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

'''SAVE DATA'''
# Save the DataFrame to a CSV file without the index
df.to_csv('dataframe.csv', index=False)

# Save the DataFrame to an Excel file without the index
df.to_excel('dataframe.xlsx')

# Save the DataFrame to a JSON file with records orientation and line-delimited format
df.to_json('dataframe.json', orient='records', lines=True)

'''LOAD DATA'''
# Load the DataFrame from a CSV file
df_csv = pd.read_csv('dataframe.csv')
print(df_csv)


'''SQL'''   
conn = sql.connect('dataframe.db')

# Save the DataFrame to a SQL database table named 'people', replacing it if it already exists, and without including the index as a column in the database         
df.to_sql('people', conn, if_exists='replace', index=False)
conn.close()

conn =  sql.connect('dataframe.db')

# Retrieve the data from the 'people' table in the SQL database and load it into a new DataFrame        
retrieve_df = pd.read_sql('SELECT * FROM people', conn)
print('from DB')
print (retrieve_df)
conn.close()

print('mean: ' + str(df['Age'].mean()))
print('median: ' + str(df['Age'].median()))
print('mode: ' + str(df['Age'].mode()))
print('variance: ' + str(df['Age'].var()))
print('standard deviation: ' + str(df['Age'].std()))

df['Age'].min(), df['Age'].max()
print(abs(df['Age'].min() - df['Age'].max()))
print(abs(df['Age'].quantile(q=0.25) - df['Age'].quantile(q=0.75)))