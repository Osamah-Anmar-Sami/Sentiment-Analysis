import matplotlib.pyplot as plt
import seaborn as sns

def sentiment_percentage(data, target, figsize):
    """
    Plots a pie chart showing the percentage distribution of sentiment categories in the given data.

    Parameters:
    data (pd.DataFrame): The input data containing sentiment information.
    target (str): The column name in the data that contains sentiment categories.
    figsize (tuple): The size of the figure to be created (width, height).

    Returns:
    None: Displays the pie chart.
    """
    fig, ax = plt.subplots(figsize = figsize)
    ax.pie(data[target].value_counts(), 
            labels=data[target].unique(),
            colors=['#a1de70', '#d7f0c1', '#80B159'], 
            autopct='%1.1f%%',
            textprops = {'size': 'large'})
    plt.title('{} Percentage'.format(target))
    return plt.show()

def sentiment_counts(data, target, figsize):
    """
    Plots the count of each sentiment category in the given data.

    Parameters:
    data (pd.DataFrame): The input data containing sentiment information.
    target (str): The column name in the data that contains sentiment labels.
    figsize (tuple): The size of the figure to be created.

    Returns:
    None: Displays the count plot of sentiment categories.
    """
    ax, fig = plt.subplots(figsize = figsize)
    ax =sns.countplot(x=target, data=data, dodge=False, hue=target,  order= data[target].value_counts().index, hue_order =data[target].value_counts().index,  palette=sns.color_palette("pastel", 3), legend='full');
    ax.set(xticklabels=[]) 
    ax.set(ylabel=None) 
    plt.title('{} Count'.format(target))
    sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))
    return plt.show()