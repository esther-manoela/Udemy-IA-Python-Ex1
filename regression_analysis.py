import statsmodels.api as sm
import pandas as pd

# Create a DataFrame
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda', 'Maria', 'Daniel', 'Simon', 'Monica'],
    'Age': [55, 30, 20, 45, 35, 25, 50, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'New York', 'Los Angeles', 'Chicago', 'Houston']}
df = pd.DataFrame(data)

df['City_encode'] = df['City'].astype("category").cat.codes  # Ensure City is numeric
df['Name_encode'] = df['Name'].astype("category").cat.codes  # Ensure Name is numeric

print(df)

x = df['City_encode']  # Independent variable
y = df['Age']  # Dependent variable

x = sm.add_constant(x)  # Add a constant term to the independent variable
model = sm.OLS(y, x).fit()  # Fit the OLS regression model
print(model.summary())  # Print the summary of the regression results



x = df[['City_encode', 'Name_encode']]  # Independent variable
y = df['Age']  # Dependent variable

x = sm.add_constant(x)  # Add a constant term to the independent variable
model = sm.OLS(y, x).fit()  # Fit the OLS regression model
print(model.summary())  # Print the summary of the regression results

