from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize

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
    data['Tok'] = data.apply(word_tokenize)
    Word2Vec_1 = Word2Vec(data['Tok'], vector_size=vector_size, sg = sg, min_count=1, window = 5, workers = 4, negative=20)
    return Word2Vec_1.wv.save_word2vec_format('{}.txt'.format(name), binary=False)