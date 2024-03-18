import numpy as np

def word_vector_(model_path, vocab_size, tokenizer):
   """
   Loads pre-trained word embeddings from a text file and creates an embedding matrix for a given tokenizer's vocabulary.

   Args:
       model_path (string): path to the text file containing word embeddings
       vocab_size (integer): size of the tokenizer's vocabulary
       tokenizer: A fitted tokenizer object (e.g., from Keras or TensorFlow) that maps words to indices.

   Returns:
       tuple: A tuple containing:
           - embedding_dim (integer): dimensionality of the word embeddings
           - word_vector (numpy.ndarray): Embedding matrix of shape (vocab_size + 1, embedding_dim)
             containing the loaded embeddings for words in the tokenizer's vocabulary.

   """
   word_embeddings = {}
   with open(model_path, encoding='utf-8') as f:
      for line in f:
         values = line.split()
         word = values[0]
         vector = np.array(values[1:], dtype='float32')
         word_embeddings[word] = vector

   embedding_dim = len(word_embeddings['كل'])
   
   word_vector = np.zeros((vocab_size + 1, embedding_dim))
   for word, idx in tokenizer.word_index.items():
      embedding_vector = word_embeddings.get(word)
      if embedding_vector is not None:
         word_vector[idx] = embedding_vector

   return embedding_dim, word_vector

