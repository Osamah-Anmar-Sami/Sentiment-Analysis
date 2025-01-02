import numpy as np

def word_vector_(model_path, all_words, word_index):
   """
   Generates word vectors from a pre-trained word embedding model.
   Args:
      model_path (str): Path to the pre-trained word embedding model file.
      all_words (int): Total number of unique words in the dataset.
      word_index (dict): Dictionary mapping words to their corresponding indices.
   Returns:
      tuple: A tuple containing:
         - embedding_dim (int): The dimension of the word embeddings.
         - word_vector (numpy.ndarray): A 2D array where each row corresponds to the word vector of a word in the dataset.
   """
   word_embeddings = {}
   with open(model_path, encoding='utf-8') as f:
      for line in f:
         values = line.split()
         word = values[0]
         vector = np.array(values[1:], dtype='float32')
         word_embeddings[word] = vector

   embedding_dim = len(word_embeddings['?'])
   
   word_vector = np.zeros((all_words, embedding_dim))
   for word, idx in word_index.items():
      embedding_vector = word_embeddings.get(word)
      if embedding_vector is not None:
         word_vector[idx] = embedding_vector

   return embedding_dim, word_vector