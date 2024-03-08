from gensim.models import Word2Vec
from utils.textnormalization import TextNormalization
import re
import os
from nltk.tokenize import word_tokenize

text_normalization = TextNormalization(string_lower = True,
                                       remove_emojis = True,
                                       remove_hashtags = True,
                                       remove_emails = True,
                                       remove_URLs = True,
                                       remove_mentions = True,
                                       remove_html_tags = True,
                                       remove_new_line_char = True,           
                                       decrease_number_of_consecutive_reapted_letter = True,
                                       remove_duplicate_word = True,
                                       remove_single_letter = True,
                                       remove_duplicated_letter = True,
                                       english_spell_coreccter = False,
                                       expand_contractions = True,
                                       remove_stop_words = False,
                                       remove_unicode_and_special_character = True,
                                       remove_puncuations = True,
                                       remove_numbers = True,
                                       remove_non_english = True,
                                       remove_longest_than = True,
                                       remove_whitespace = True,
                                       lemmatize = False,
                                       stemmer = False)

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
    data['Text_Normalization'] = data.apply(lambda x: text_normalization.normalization(x))
    data['Tok'] = data['Text_Normalization'].apply(word_tokenize)
    Word2Vec_1 = Word2Vec(data['Tok'], vector_size=vector_size, sg = sg, min_count=1, window = 1, workers = 4, negative=1)
    return Word2Vec_1.wv.save_word2vec_format('{}.txt'.format(name), binary=False)