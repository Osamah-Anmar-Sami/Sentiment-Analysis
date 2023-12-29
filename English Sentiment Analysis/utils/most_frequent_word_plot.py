from plotly import graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns


color3 = ['Salmon', 'FireBrick', 'MediumVioletRed', 'Tomato', 'Orange', 'Gold', 'DarkKhaki', 'Lavender', 'Plum', 'LimeGreen', 'MediumSpringGreen', 'Green', 'DeepSkyBlue', 'Aquamarine', 'MediumSlateBlue']

def go_figure(data):
    fig = go.Figure(go.Funnel(
    y = data['Word'].tolist(),
    x = data['Count'].tolist(),
    marker = {"color": color3}))
    return fig.show()


def bar_plot(data):
    fig, ax = plt.subplots(figsize=(10, 10))
    sns.barplot(data, y='Word', x='Count',  orient='h', width=1, palette=sns.color_palette('pastel', 15), native_scale = True, ax=ax)
    return plt.show()
    