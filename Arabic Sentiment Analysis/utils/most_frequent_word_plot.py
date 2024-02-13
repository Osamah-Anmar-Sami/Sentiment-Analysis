import matplotlib.pyplot as plt
from bidi.algorithm import get_display
from arabic_reshaper import reshape
import seaborn as sns

def bar_plot(data, x, y, text):
    data[text] = [get_display(reshape(label)) for label in data[text]]
    fig, ax = plt.subplots(figsize=(20, 10))
    sns.barplot(data=data, x=x, y=y, width=0.6, palette = sns.color_palette("husl", 15), ax=ax)
    plt.rcParams['font.family'] = 'Arial'