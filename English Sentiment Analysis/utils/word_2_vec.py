from gensim.models import Word2Vec
from utils.textnormalization import TextNormalization
import pyarabic.arabrepr
import re
import os
from camel_tools.tokenizers.word import simple_word_tokenize

text_normalization = TextNormalization( string_lower = True,
                                        remove_emojis = True,
                                        remove_hashtags = True,
                                        remove_emails = True ,
                                        remove_url = True,
                                        remove_mention = True,
                                        remove_duplicate_char = True,
                                        remove_single_char = True,
                                        remove_special_character = True,
                                        remove_new_line_char = True,
                                        remove_number = True,
                                        remove_html_tags = True,
                                        remove_non_english = True,
                                        remove_whitespace = True,
                                        remove_unicode_characters = True,
                                        remove_longest_than = True,
                                        remove_stop_words = False,
                                        lemmatizer = False,
                                        stemmer = False)

def word_2_vec_(data, vector_size, sg, name):
    data = data.astype(str)
    data['Text_Normalization'] = data.apply(lambda x: text_normalization.normalization(x))
    data['Tok'] = data['Text_Normalization'].apply(simple_word_tokenize)
    Word2Vec_1 = Word2Vec(data['Tok'], vector_size=vector_size, sg = sg, min_count=1, window = 5, negative = 2)
    return Word2Vec_1.wv.save_word2vec_format('{}.txt'.format(name))