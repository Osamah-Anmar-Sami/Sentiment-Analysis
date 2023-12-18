from wordcloud import WordCloud
import matplotlib.pyplot as plt

def wordcloud(data, target, width, hieght, text):
    text = str(data[data['Sentiment'] == target][text])
    wordcloud = WordCloud(background_color='white', mode='RGB',width=width,height=hieght).generate(text)
    plt.figure()
    plt.imshow(wordcloud, interpolation='catrom')
    plt.axis("off")
    plt.title('Word Cloud For {} Sentiment'.format(target))
    plt.show()
    