from gensim.models import Word2Vec
import string
import emoji
import re
import os
from nltk.tokenize import word_tokenize

def remove_non_english(text):
    pattern = re.compile(r'[^a-zA-Z0-9]+')
    text = re.sub(pattern, ' ', text)
    return text

def delete_punctuations(text):
    Punctuations= str.maketrans(' ', ' ', string.punctuation)
    text = text.translate(Punctuations)
    return text 

def string_lower_(text):
        text = str(text)
        text = text.lower()
        return text

def delete_emojis(text):
    text = emoji.replace_emoji(text, replace="")
    return text

def delete_url(text):
    text = re.sub(r'http\S+', ' ', text, flags=re.MULTILINE)
    return text

def delete_html_tags(text):     
          text = re.sub("<.*?>", ' ', text)
          return text


def delete_single_letter(text):
    pattern = r"\b([b-dfhj-np-tv-z]|[B-DFHJ-NP-TV-Z])\b(?!\w)" 
    text = re.sub(pattern, " ", text)
    return text

def simple_normalization(text):
    text = string_lower_(text)
    text = remove_non_english(text)
    text = delete_punctuations(text)
    text = delete_emojis(text)
    text = delete_url(text)
    text = delete_html_tags(text)
    text = delete_single_letter(text)
    return text

def word_2_vec_(data, vector_size, sg, name):
    """
   Trains a Word2Vec model on a text dataset and saves the trained word embeddings.

   Args:
       data (pandas.DataFrame): dataFrame containing a column of text data to train on
       vector_size (integer): dimensionality of the word vectors
       sg (integer): training algorithm to use: 0 for CBOW (default), 1 for Skip-gram
       name (string): base filename for saving the model (without extension)

   Returns:
       text file: file containing the vector of each word
   """
    data = data.astype(str)
    data['Text_Normalization'] = data.apply(lambda x: simple_normalization(x))
    data['Tok'] = data['Text_Normalization'].apply(word_tokenize)
    Word2Vec_1 = Word2Vec(data['Tok'], vector_size=vector_size, sg = sg, min_count=1, window = 1, workers = 6, negative=5)
    return Word2Vec_1.wv.save_word2vec_format('{}.txt'.format(name), binary=False)