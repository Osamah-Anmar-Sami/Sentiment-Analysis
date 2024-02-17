import matplotlib.pyplot as plt
import seaborn as sns

def bar_plot(data, x, y):
    fig, ax = plt.subplots(figsize=(20, 10))
    sns.barplot(data=data, x=x, y=y, width=0.6, palette = sns.color_palette("husl", 15), ax=ax)
    plt.rcParams['font.family'] = 'Arial'