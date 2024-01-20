import matplotlib.pyplot as plt
import seaborn as sns

def bar_plot(data, x, y):
    fig, ax = plt.subplots(figsize=(8, 8))
    pl = sns.barplot(data=data, x=x, y=y, width=0.6, palette = sns.color_palette("muted", 15), ax=ax)
    pl.set_xticklabels(pl.get_xticklabels(), rotation=45)
    return plt.show()