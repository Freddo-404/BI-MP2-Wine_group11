import matplotlib.pyplot as plt
import seaborn as sns

def histogram(data, title="Histogram"):
    plt.hist(data, bins=10, edgecolor='black')
    plt.title(title)
    plt.xlabel("Values")
    plt.ylabel("Frequency")
    plt.show()

def boxplot(data, title="Box Plot"):
    sns.boxplot(data=data)
    plt.title(title)
    plt.show()

def scatter_plot(x, y, title="Scatter Plot"):
    plt.scatter(x, y)
    plt.title(title)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()
