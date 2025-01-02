import numpy as np
import re
from itertools import chain


def data_words(data, filter=None):
    """
    Processes a list of text data and returns the number of unique words plus two, 
    along with the set of unique words.

    Args:
        data (list of str): A list of text strings to be processed.
        filter (callable, optional): A function to filter the data. Defaults to None.

    Returns:
        tuple: A tuple containing:
            - int: The number of unique words plus two.
            - set: A set of unique words found in the data.
    """
    def filter_data(data, pattern):
        """
        Filters out characters from each word in the data based on the given pattern.

        Args:
            data (list of str): A list of words to be filtered.
            pattern (str): A string containing characters to be removed from each word.

        Returns:
            list of str: A list of words with the specified characters removed.
        """
        translator = str.maketrans('', '', pattern)
        filtered_data = [word.translate(translator) for word in data]
        return filtered_data
    if filter:
        data = filter_data(data, filter)
    words = set()
    for txt in data:
        for word in txt.split():
            words.add(word)
    all_words = len(words)
    return all_words + 2, words
    

def words_to_index_(words):
        """
        Converts a list of words into a dictionary mapping each word to a unique index.

        Args:
            words (list of str): A list of words to be indexed.

        Returns:
            dict: A dictionary where keys are words from the input list and values are unique indices starting from 2.
                  The dictionary also includes a special token 'UNK' mapped to the index 1.
        """
        words_to_index = {word:index+2 for index, word in enumerate(words)} 
        words_to_index['UNK'] = 1
        words_to_index = dict(sorted(words_to_index.items(), key=lambda item: item[1]))
        return words_to_index
    
def index_to_word_(words):
        """
        Converts a list of words into a dictionary mapping indices to words.

        This function takes a list of words and creates a dictionary where each word is assigned an index starting from 2.
        The index 1 is reserved for the token "UNK" which stands for unknown words.

        Args:
            words (list): A list of words to be indexed.

        Returns:
            dict: A dictionary where keys are indices and values are words, with index 1 mapped to "UNK".
        """
        index_to_word = {index+2:word for index, word in enumerate(words)}  
        index_to_word[1] = "UNK"
        index_to_word = dict(sorted(index_to_word.items(), key=lambda item: item[0]))
        return index_to_word
    
def word_counts(data):
        """
        Calculate the frequency of each word in the given list of sentences.

        Args:
            data (list of str): A list of sentences where each sentence is a string.

        Returns:
            dict: A dictionary where keys are words and values are their corresponding frequencies, sorted in descending order by frequency.
        """
        word_count = dict()
        for sentence in data:
            for word_ in sentence.split():
                if word_ in word_count:
                    word_count[word_] += 1
                else:
                    word_count[word_] = 1
        word_count = dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))
        return word_count
    
def text_to_sequence(word_index, data):
    """
    Converts a list of sentences into sequences of integers based on a given word index.

    Args:
        word_index (dict): A dictionary mapping words to their corresponding integer indices.
        data (list of str): A list of sentences to be converted into sequences.

    Returns:
        list of list of int: A list where each element is a list of integers representing the words in the corresponding sentence.
                             Words not found in the word_index are replaced with the index of the "UNK" token.
    """
    sequence_text = [[word_index[word] if word in word_index else  word_index["UNK"]  for word in sentences.split()] for sentences in data]
    return sequence_text
    
def sequences_padding(padding = 'post', input_sequence = None, max_length = None, truncating = 'post'):
        """
            Pads and truncates sequences to a specified maximum length.

            Parameters:
            padding (str): Specifies whether padding should be added to the 'pre' (beginning) or 'post' (end) of the sequences. Default is 'post'.
            input_sequence (list of lists): The sequences to be padded and truncated.
            max_length (int): The maximum length of the sequences after padding and truncating.
            truncating (str): Specifies whether truncating should be done at the 'pre' (beginning) or 'post' (end) of the sequences. Default is 'post'.

            Returns:
            np.array: The padded and truncated sequences as a NumPy array.
        """
        for i in range(0, len(input_sequence)):
           while len(input_sequence[i]) < max_length:
                if padding == "post":
                    input_sequence[i].insert(len(input_sequence[i]), 0)
                if padding == 'pre':
                    input_sequence[i].insert(0, 0)
                if truncating == 'pre':
                    input_sequence[i] =  input_sequence[i][-max_length:]
                if truncating == 'post':
                    input_sequence[i] =  input_sequence[i][:max_length]
        return  np.array(input_sequence)
    
def word_sequence_to_text(index_to_words, sequence):
    """
    Converts a sequence of word indices into a text string.

    Args:
        index_to_words (dict): A dictionary mapping word indices to words.
        sequence (iterable): An iterable of word index sequences.

    Returns:
        str: A string representation of the word sequence.

    Example:
        index_to_words = {0: '<PAD>', 1: '<UNK>', 2: 'hello', 3: 'world'}
        sequence = [[2, 3], [0, 1]]
        result = word_sequence_to_text(index_to_words, sequence)
        # result: 'hello world <PAD> <UNK>'
    """
    sequence = list(sequence)   
    sequence = list(chain.from_iterable(sequence))
    word_sequence_to_text_ = [index_to_words[index] if index in index_to_words else index_to_words[1] for index in sequence]
    return " ".join(word_sequence_to_text_)

def one_hot_encoding(data, num_labels):
    """
    Converts a list of labels into a one-hot encoded matrix.

    Parameters:
    data (list of int): List of integer labels to be one-hot encoded.
    num_labels (int): Total number of unique labels.

    Returns:
    numpy.ndarray: A 2D array where each row corresponds to the one-hot encoded representation of the input labels.
    """
    label = np.zeros((len(data), num_labels))
    for i, j in enumerate(data):
            label[i, j] = 1
    return label