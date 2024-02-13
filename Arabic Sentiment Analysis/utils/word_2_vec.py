from gensim.models import Word2Vec
from utils.textnormalization import TextNormalization
import pyarabic.arabrepr
import re
import os
from pyarabic import araby
from nltk.tokenize import word_tokenize

text_normalization = TextNormalization(remove_emojis = True,
                                       remove_hashtags = True,
                                       remove_emails = True,
                                       remove_URLs = True,
                                       remove_new_line_char = True,
                                       remove_mentions = True,
                                       remove_single_char = True,
                                       remove_duplicate_char = True,
                                       remove_duplicate_word = True,
                                       remove_stop_words = False,
                                       remove_special_character = True,
                                       remove_puncuations = True,
                                       remove_html_tags = True,
                                       remove_numbers = True,
                                       remove_non_arabic = True,
                                       remove_arabic_diacritics = True,
                                       normalize_alef_maqsura = True,
                                       normalize_alef = True,
                                       normalize_teh_marbuta = True,
                                       normalize_arabic_tashkeel = True,
                                       normalize_arabic_tatweel = True,
                                       remove_longest_than = True,
                                       remove_whitespace = True,
                                       lemmatize = False,
                                       stemmer = False)
def word_2_vec_(data, vector_size, sg, name):
    data = data.astype(str)
    data['Text_Normalization'] = data.apply(lambda x: text_normalization.normalization(x))
    data['Tok'] = data['Text_Normalization'].apply(word_tokenize)
    Word2Vec_1 = Word2Vec(data['Tok'], vector_size=vector_size, sg = sg, min_count=1, window = 1, negative = 2)
    return Word2Vec_1.wv.save_word2vec_format('{}.txt'.format(name))