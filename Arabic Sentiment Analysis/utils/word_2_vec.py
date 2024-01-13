from gensim.models import Word2Vec
from utils.textnormalization import TextNormalization
import pyarabic.arabrepr
import re
import os
from camel_tools.tokenizers.word import simple_word_tokenize

text_normalization = TextNormalization(_remove_emojis = True,
                                        _remove_hashtags = True,
                                        _remove_emails = True ,
                                        _remove_url = True,
                                        _remove_mention = True,
                                        _remove_duplicate_char = True,
                                        _remove_single_char = True,
                                        _remove_special_character_ = True,
                                        _remove_new_line_char = True,
                                        _remove_number = True,
                                        _remove_html_tags = True,
                                        _remove_arabic_diacritics_ = True,
                                        _normalize_arabic_unicode_ = True,
                                        _normalize_alef_maksura_ar_ = True,
                                        _normalize_alef_ar_ = True,
                                        _normalize_teh_marbuta_ar_ = True,
                                        _remove_non_arabic = True,
                                        _remove_whitespace_ = True,
                                        _remove_unicode_characters_ = True,
                                        _remove_longest_than_ = True,
                                        _remove_stop_words = False,
                                        _lemmatizer_ = False,
                                        _stemmer_ = False)

def word_2_vec_(data, vector_size, sg, name):
    data = data.astype(str)
    data['Text_Normalization'] = data.apply(lambda x: text_normalization.normalization(x))
    data['Tok'] = data['Text_Normalization'].apply(simple_word_tokenize)
    Word2Vec_1 = Word2Vec(data['Tok'], vector_size=vector_size, sg = sg, min_count=1, window = 5, negative = 2)
    return Word2Vec_1.wv.save_word2vec_format('{}.txt'.format(name))