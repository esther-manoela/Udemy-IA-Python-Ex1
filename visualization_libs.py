import seaborn as sns
import matplotlib.pyplot as plt

datasetNames = sns.get_dataset_names()
print(datasetNames)

flights = sns.load_dataset("flights")
print(flights)

# line chart
sns.lineplot(
    data=flights,
    x="year",
    y="passengers",
    errorbar=None,
    hue="month"
)
plt.show()

# vertical bar chart
sns.barplot (
    data=flights,
    x="month",
    y="passengers",
    errorbar=None
)
plt.show()

# horizontal bar chart
sns.barplot (
    data=flights,
    x="passengers",
    y="month",
    errorbar=None,
    orient="y"
)
plt.show()

# scatter chart
sns.scatterplot (
    data=flights,
    x="year",
    y="passengers"
)
plt.show()