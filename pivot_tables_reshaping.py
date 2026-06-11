import pandas as pd

df = pd.DataFrame({
    "A": ["foo", "foo", "foo", "foo", "bar", "bar"],
    "B": ["one", "one", "one", "one", "two", "three"],
    "D": [1, 1, 2, 2, 2, 3],
    "E": [5, 6, 3, 7, 9, 0],
    "F": [0, 1, 2, 3, 4, 5]
})

print(df)

df2 = df.melt(
    id_vars=["A", "B"],
    var_name="Metrics",
    value_name="Value"
)

print(df2)

stack = df.stack()
print(stack)

unstack = df.stack().unstack()
print(unstack)

pivot = df.pivot(
    columns="B",
    index="F",
    values="E"
)
print(pivot)

pivotTable = df.pivot_table(
    values="D",
    index="A",
    columns="B",
    aggfunc="sum"
)
print(pivotTable)
