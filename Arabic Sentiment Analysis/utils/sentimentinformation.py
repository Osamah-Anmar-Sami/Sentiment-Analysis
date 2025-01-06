import matplotlib.pyplot as plt
import seaborn as sns

def sentiment_percentage(data, target, figsize):
    """
    Creates a pie chart visualizing the percentage distribution of
    sentiment categories within the specified target column of a pandas DataFrame.

    Args:
        data (pandas.DataFrame): the pandas DataFrame containing the data
        target (string): the name of the column containing the sentiment categories
        figsize (tuple): The desired figure size for the pie chart
    Returns:
        matplotlib.pyplot.Figure: the generated plot object
    """
    fig, ax = plt.subplots(figsize = figsize)
    wedges, texts, autotexts = ax.pie(data[target].value_counts(), 
                                      labels=data[target].unique(),
                                      colors=['#07D107', '#068D06', '#08B208'], 
                                      autopct='%1.1f%%',
                                      textprops={'size': 'large'})
    for autotext in autotexts:
        autotext.set_color('white')
    plt.title('{} Percentage'.format(target))
    return plt.show()

def sentiment_counts(data, target, figsize):
    """
    creates a bar chart visualizing the sentiment category counts within
    the specified target column of a pandas DataFrame

    Args:
        data (pandas.DataFrame): the pandas DataFrame containing the data
        target (str): the name of the column containing the sentiment categories
        figsize (tuple, optional): the desired figure size for the bar chart
      
    Returns:
         matplotlib.pyplot.Figure: the generated plot object
    """
    ax, fig = plt.subplots(figsize = figsize)
    ax =sns.countplot(x=target, data=data, dodge=False, hue=target,  order= data[target].value_counts().index, hue_order =data[target].value_counts().index,  palette=sns.color_palette("Set2",3), legend='full');
    ax.set(xticklabels=[]) 
    ax.set(ylabel=None) 
    plt.title('{} Count'.format(target))
    sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))
    return plt.show()