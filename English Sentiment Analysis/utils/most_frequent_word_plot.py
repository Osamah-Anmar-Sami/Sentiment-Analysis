import matplotlib.pyplot as plt
import seaborn as sns

def bar_plot(data, x, y):
    """
    creates a bar chart using Seaborn visualizes the relationship between a categorical variable on the x-axis and a quantitative variable on the y-axis.

    Args:
        data (pandas.DataFrame): A pandas DataFrame containing the data to be plotted.
        x (string): the name of the column in the DataFrame that contains the categorical data for the x-axis.
        y (string): the name of the column in the DataFrame that contains the quantitative data for the y-axis.

    """
    
    fig, ax = plt.subplots(figsize=(20, 10))
    sns.barplot(data=data, x=x, y=y, width=0.6, palette = sns.color_palette("husl", 15), ax=ax)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.rcParams['font.family'] = 'Arial'

