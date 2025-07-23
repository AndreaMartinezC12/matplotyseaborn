#testing
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("flights")

print(sns.get_dataset_names())

sns.barplot(x="month", y="passengers", data=df)
#sns.boxplot(x="month", y="passengers", data=df)
#sns.violinplot(x="month", y="passengers", data=df)
plt.title("Cantidad de pasajeros en vuelos por mes entre los anios 1949 y 1960")

plt.show()