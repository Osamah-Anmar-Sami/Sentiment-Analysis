from wordcloud import WordCloud
import matplotlib.pyplot as plt


def wordcloud(data, target, width, hieght, review, max_words):
    """
    Generate and display a word cloud for a specific sentiment.

    Parameters:
    data (pd.DataFrame): The dataset containing the text data and sentiment labels.
    target (str): The sentiment label to filter the data by (e.g., 'positive', 'negative').
    width (int): The width of the word cloud image.
    hieght (int): The height of the word cloud image.
    review (str): The column name in the dataframe that contains the text data.
    max_words (int): The maximum number of words to include in the word cloud.

    Returns:
    None: Displays the generated word cloud using matplotlib.
    """
    df = data[data['Sentiment'] == target]
    text = " ".join(txt for txt in df[review])
    wordcloud = WordCloud(font_path='arial.ttf',background_color='white', mode='RGB',width=width,height=hieght, max_words = max_words).generate(text)
    plt.figure(figsize=(20,10))
    plt.imshow(wordcloud, interpolation='catrom')
    plt.axis("off")
    plt.title('Word Cloud For {} Sentiment'.format(target))
    return plt.show()