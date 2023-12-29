from gensim.models import Word2Vec
from utils.textnormalization import TextNormalization
from nltk.tokenize import word_tokenize, sent_tokenize

text_normalization = TextNormalization(_string_lower = True, 
                        _remove_emojis = True, 
                        _remove_hashtags = True, 
                        _remove_emails = True,
                        _remove_url = True, 
                        _remove_mention = True, 
                        _remove_duplicate_char = True,
                        _remove_single_char = True, 
                        _remove_new_line_char = True, 
                        _remove_number = True, 
                        _remove_html_tags = True, 
                        _remove_special_character = True, 
                        _remove_longest_than = True, 
                        _remove_whitespace = True, 
                        _remove_unicode_characters = True,
                        _stemmer = False, 
                        _remove_non_english = True, 
                        _remove_stop_words = False, 
                        _lemmatizer = False)



def word_2_vec_(data, vector_size, sg, name):
    data['Text_Normalization'] = data.apply(lambda x: text_normalization.normalization(x))
    data['Tok'] = data['Text_Normalization'].apply(word_tokenize)
    Word2Vec_1 = Word2Vec(data['Tok'], vector_size=vector_size, sg = sg, min_count=1)
    return Word2Vec_1.wv.save_word2vec_format('{}.txt'.format(name))