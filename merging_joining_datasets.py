import pandas as pd

# Example of datasets
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'ID': [2, 3, 4], 'Score': [85, 90, 95]})
df3 = pd.DataFrame({'ID_column': [2, 3, 4], 'Score': [85, 90, 95]})

### Merge examples
#merge = pd.merge(df1, df2, on='ID', how='inner')  # Inner join (Only matching rows (intersection))
#print(merge)

#left = pd.merge(df1, df2, on='ID', how='left') # Left (All rows from df1, fills with NaN where df2 has no matches)
#print(left)

#right = pd.merge(df1, df2, on='ID', how='right') # Right (All rows from df2, fills with NaN where df1 has no matches)   
#print(right)

#outer = pd.merge(df1, df2, on='ID', how='outer') # Outer (All rows from both DataFrames, fills with NaN where there are no matches)
#print(outer)

#outer2 = pd.merge(df1, df3, left_on='ID', right_on='ID_column', how='outer') # Outer (All rows from both DataFrames, fills with NaN where there are no matches)
#print(outer2)


### Join examples
join1 = df1.join(df2, on='ID', lsuffix='_left', rsuffix='_right', how='inner')
print(join1)

df1_index = df1.set_index('ID')
df2_index = df2.set_index('ID')

df1_index_join = df1_index.join(df2_index, how='inner')
print(df1_index_join)


### Concatenation examples
concat = pd.concat([df1, df2], axis=0, ignore_index=True)  # Concatenate along rows (axis=0)
print(concat)

concat = pd.concat([df1, df2], axis=1)  # Concatenate along columns (axis=1)
print(concat)