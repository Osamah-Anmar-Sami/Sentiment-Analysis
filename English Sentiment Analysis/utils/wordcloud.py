from wordcloud import WordCloud
import matplotlib.pyplot as plt
import arabic_reshaper
from bidi.algorithm import get_display

def wordcloud(data, target, width, hieght, review):
    df = data[data['Sentiment'] == target]
    text = " ".join(txt for txt in df[review])
    wordcloud = WordCloud(font_path='arial.ttf',background_color='white', mode='RGB',width=width,height=hieght).generate(text)
    plt.figure()
    plt.imshow(wordcloud, interpolation='catrom')
    plt.axis("off")
    plt.title('Word Cloud For {} Sentiment'.format(target))
    return plt.show()