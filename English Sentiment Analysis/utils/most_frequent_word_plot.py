import plotly.express as px
from plotly import graph_objects as go
color3 = ['Salmon', 'FireBrick', 'MediumVioletRed', 'Tomato', 'Orange', 'Gold', 'DarkKhaki', 'Lavender', 'Plum', 'LimeGreen', 'MediumSpringGreen', 'Green', 'DeepSkyBlue', 'Aquamarine', 'MediumSlateBlue']

def go_figure(data):
    fig = go.Figure(go.Funnel(
    y = data['Word'].tolist(),
    x = data['Count'].tolist(),
    marker = {"color": color3}))
    return fig.show()

def bar_plot(data):
    fig = px.bar(data, y='Word', x='Count',  orientation='h')
    return fig.show()