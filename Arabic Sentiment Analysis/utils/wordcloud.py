from wordcloud import WordCloud
import matplotlib.pyplot as plt
import arabic_reshaper
from bidi.algorithm import get_display

def wordcloud(data, target, width, hieght, review, max_words):
    """
    creates a word cloud visualization of frequently appearing words in reviews
    associated with a specific sentiment label from a pandas DataFrame

    Args:
        data (pandas.DataFrame): DataFrame containing the text data and sentiment labels
        target (string): the specific sentiment label to filter reviews for
        width (integer): width of the word cloud image
        height (integer): height of the word cloud image
        review (string): the column name in the DataFrame containing review text
        max_words (integer): maximum number of unique words to include in the word cloud

    Returns:
       matplotlib.pyplot.Figure: the generated plot object
    """
    df = data[data['Sentiment'] == target]
    arabic_text = " ".join(txt for txt in df[review])
    arabic_text = arabic_reshaper.reshape(arabic_text)
    arabic_text = get_display(arabic_text)
    wordcloud = WordCloud(font_path='Amiri-Bold.ttf',background_color='white', mode='RGB',width=width,height=hieght, max_words = max_words).generate(arabic_text)
    plt.figure(figsize=(20,10))
    plt.imshow(wordcloud, interpolation='catrom')
    plt.axis("off")
    plt.title('Word Cloud For {} Sentiment'.format(target))
    return plt.show()