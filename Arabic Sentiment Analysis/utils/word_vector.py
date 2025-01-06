import numpy as np
from gensim.models import Word2Vec, KeyedVectors
def word_vector_(all_words, word_index, model_path):
    """
    Generates word vectors from a loaded Word2Vec model.
    Args:
        model (Word2Vec): The loaded Word2Vec model.
        all_words (int): Total number of unique words in the dataset.
        word_index (dict): Dictionary mapping words to their corresponding indices.
    Returns:
        tuple: A tuple containing:
            - embedding_dim (int): The dimension of the word embeddings.
            - word_vector (numpy.ndarray): A 2D array where each row corresponds to the word vector of a word in the dataset.
    """
    model = Word2Vec.load(model_path)
    embedding_dim = model.vector_size
    word_vector = np.zeros((all_words, embedding_dim))
    
    for word, idx in word_index.items():
        if word in model.wv:
            word_vector[idx] = model.wv[word]

    return embedding_dim, word_vector
