import matplotlib.pyplot as plt
import seaborn as sns

def bar_plot(data, x, y):
    """
    Creates a bar plot using seaborn and matplotlib.

    Parameters:
    data (DataFrame): The data to be plotted.
    x (str): The name of the column to be used for the x-axis.
    y (str): The name of the column to be used for the y-axis.

    Returns:
    None
    """
    fig, ax = plt.subplots(figsize=(15, 10))
    sns.barplot(data=data, x=x, y=y, width=0.6, palette =sns.color_palette("Set2", 15), ax=ax)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.rcParams['font.family'] = 'Arial'

