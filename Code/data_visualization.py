import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from biokit.viz import corrplot

# load data
dataframe = pd.read_csv("preprocessed_data.csv")
# find correlation
co_relation = dataframe.corr()
# generate correlation plot
cp = corrplot.Corrplot(co_relation)
cp.plot(method='pie', shrink=.9, grid=False)
plt.savefig('correlation.png')
# generate pair plot for all attributes
sns.pairplot(dataframe)
sns.plt.savefig('data_distribution.png')
sns.plt.clf()
# generate heatmap based on correlation
sns.heatmap(co_relation, linewidths=.5, cmap="YlGnBu")
sns.plt.savefig('correlation_heatmap.png')