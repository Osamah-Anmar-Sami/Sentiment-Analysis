import matplotlib.pyplot as plt
from bidi.algorithm import get_display
from arabic_reshaper import reshape
import seaborn as sns

def bar_plot(data, x, y, text):
    """
    creates a bar chart using Seaborn visualizes the relationship between a categorical variable on the x-axis and a quantitative variable on the y-axis.

    Args:
        data (pandas.DataFrame): A pandas DataFrame containing the data to be plotted.
        x (string): the name of the column in the DataFrame that contains the categorical data for the x-axis.
        y (string): the name of the column in the DataFrame that contains the quantitative data for the y-axis.

    """
    data[text] = [get_display(reshape(label)) for label in data[text]]
    fig, ax = plt.subplots(figsize=(20, 10))
    sns.barplot(data=data, x=x, y=y, width=0.6, palette = sns.color_palette("pastel", 15), ax=ax)
    plt.rcParams['font.family'] = 'Arial'