import nltk
from nltk.stem import  WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.stem import  SnowballStemmer
import re
from nltk.tokenize import word_tokenize
import emoji
import contractions
from autocorrect import Speller
import string
import langdetect
import fasttext




class TextNormalization:
     def __init__(self,
                 string_lower,
                 remove_emojis,
                 remove_hashtags,
                 remove_emails,
                 remove_URLs,
                 remove_mentions,
                 remove_html_tags,
                 remove_new_line_char,
                 decrease_number_of_consecutive_reapted_letter,
                 remove_duplicate_word,
                 remove_single_letter,
                 remove_duplicated_letter,
                 expand_contractions,
                 remove_stop_words,
                 remove_unicode_and_special_character,
                 remove_puncuations,
                 remove_numbers,
                 english_spell_coreccter,
                 remove_non_english,
                 remove_longest_than,
                 remove_whitespace,
                 lemmatize,
                 stemmer,
                 ):
          self.string_lower = string_lower
          self.remove_emojis = remove_emojis
          self.remove_hashtags = remove_hashtags
          self.remove_emails = remove_emails
          self.remove_URLs = remove_URLs
          self.remove_mentions = remove_mentions
          self.remove_html_tags = remove_html_tags
          self.remove_new_line_char = remove_new_line_char
          self.decrease_number_of_consecutive_reapted_letter = decrease_number_of_consecutive_reapted_letter
          self.remove_duplicate_word = remove_duplicate_word
          self.remove_single_letter = remove_single_letter
          self.remove_duplicated_letter = remove_duplicated_letter
          self.expand_contractions = expand_contractions
          self.remove_stop_words = remove_stop_words
          self.remove_unicode_and_special_character = remove_unicode_and_special_character
          self.remove_puncuations = remove_puncuations
          self.remove_numbers = remove_numbers
          self.remove_non_english = remove_non_english
          self.english_spell_coreccter = english_spell_coreccter
          self.remove_longest_than = remove_longest_than
          self.remove_whitespace = remove_whitespace
          self.lemmatize = lemmatize
          self.stemmer = stemmer


    

     def normalization(self, text):
          """normalizes text by applying a series of cleaning and standardization techniques


            Args:
                text (string): the input text to be normalized

            Returns:
                string: The normalized text after applying the specified transformations

            Normalization techniques:

            - Converting text to lowercase.
            - Removing emojis, hashtags, emails, URLs, mentions, newline characters, and HTML tags.
            - Decreasing the number of consecutive repeated letters.
            - Removing duplicate words.
            - Expanding contractions.
            - Removing stop words.
            - Removing unicode and special characters.
            - Removing punctuation.
            - Removing single letters and duplicated letters.
            - Removing numbers.
            - Correcting English spelling.
            - Removing non-English words.
            - Removing words longer than a specified length.
            - Removing whitespace.
            - Applying lemmatization.
            - Applying stemming.
            """
         
          if self.string_lower == True:
               text = self.string_lower_(text)
          if self.remove_emojis == True:
               text = self.delete_emojis(text)
          if self.remove_hashtags == True:
               text = self.delete_hashtags(text)
          if self.remove_emails == True:
               text = self.delete_emails(text)
          if self.remove_URLs == True:
               text = self.delete_url(text)
          if self.remove_mentions == True:
               text = self.delete_mention(text)
          if self.remove_new_line_char == True:
               text = self.delete_new_line_char(text)
          if self.remove_html_tags == True:
               text = self.delete_html_tags(text)
          if self.decrease_number_of_consecutive_reapted_letter == True:
               text = self.decrease_number_of_consecutive_reapted_letter_(text)
          if self.remove_duplicate_word == True:
               text = self.delete_duplicate_word(text)
          if self.expand_contractions == True:
               text = self.expand_contractions_(text)
          if self.remove_stop_words == True:
               text = self.delete_stop_words(text)
          if self.remove_unicode_and_special_character == True:
               text = self.delete_unicode_and_special_character(text)
          if self.remove_puncuations == True:
               text = self.delete_punctuations(text)
          if self.remove_single_letter == True:
               text = self.delete_single_letter(text)
          if self.remove_duplicated_letter == True:
               text = self.delete_duplicated_letter(text)
          if self.remove_numbers == True:
               text = self.delete_number(text)
          if self.english_spell_coreccter == True:
               text = self.english_spell_correcter_(text)
          if self.remove_non_english == True:
               text = self.delete_non_english(text)
          if self.remove_longest_than == True:
               text = self.delete_longest_than(text)
          if self.remove_whitespace == True:
               text = self.delete_whitespace(text)
          if self.lemmatizer_ == True:
               text = self.lemmatizer_(text)
          if self.stemmer == True:
               text = self.stemmer_(text)
          return text
          

     def string_lower_(self,text):
          """convert all words into word with lower letter format

          Args:
              text (str): input text containing words with capital letters

          Returns:
              string: text containing words with lower letters
          """        ""
          text = str(text)
          text = text.lower()
          return text

     def delete_emojis(self,text):
          """remove all emojis from text

          Args:
              text (string): input text containing emoijis to be removed

          Returns:
              string: text without any emojis
          """       
          text = emoji.replace_emoji(text, replace="")
          return text

     def delete_hashtags(self,text):
          """remove all hashtags from text

          Args:
              text (string): input text containing hashtags to be removed

          Returns:
              string: text without any hashtags
          """        
          text =  re.sub("#[ا-ي٠-٩a-zA-Z0-9]+","", text)
          return text   

     def delete_emails(self,text):
          """remove all email address from text

          Args:
              text (string): input text containing email address to be removed

          Returns:
              string: text without any email address
          """        ""
          text = re.sub("[a-zA-Z0-9-_.]+@[a-zA-Z]+.[a-zA-Z]+"," ", text)  
          return text 

     def delete_url(self,text):
          """remove all URL from text

          Args:
              text (string): input text containing URL address to be removed

          Returns:
              string: text without any URL address
          """        " "
          text = re.sub(r'http\S+', ' ', text, flags=re.MULTILINE)
          return text

     def delete_mention(self,text):
          """remove all mention from text

          Args:
              text (string): input text containing mention to be removed

          Returns:
              string: text without any mention
          """        ""
          text = re.sub("@[ا-ي٠-٩a-zA-Z0-9]+"," ", text)
          return text

     def delete_html_tags(self,text):
          """remove all html tags from text

          Args:
              text (string): input text containing html tags to be removed

          Returns:
              string: text without any html tags
          """       
          text = re.sub("<.*?>", ' ', text)
          return text

     def delete_new_line_char(self,text):
          """delete new line character from text

          Args:
              text (string): input text containing new line character to be removed

          Returns:
              string: text without any new line character 
          """          ""
          text = text.replace('\n', ' ')
          return text 
     
     def decrease_number_of_consecutive_reapted_letter_(self,text):
          """decrease number consecutive characters reapeted more than 2 times in a each word for given text


          Args:
              text (string): input text containing reapeted characters


          Returns:
              string: text without characters reapeted more than 2 times
          """          ""
          text = re.sub(r'(.)\1+', r'\1\1', text)
          return text

     def delete_duplicate_word(self,text):
          """delete consecutive duplicate words in a given text

          Args:
              text (string): input text containing duplicate words separated by spaces.

          Returns:
              string: text without any duplicate words
          """          ""
          pattern = r'\b(\w+)(\s+)(\1+)\b'
          text = re.sub(pattern, r'\1', text)
          return text
     
     def delete_single_letter(self, text):
            """
                removes single letters that aren't part of words from the given text

                Args:
                    text(string): The text to process

                Returns:
                   string: the modified text with single letters removed
            """

            pattern = r"\b([b-dfhj-np-tv-z]|[B-DFHJ-NP-TV-Z])\b(?!\w)"   
            text = re.sub(pattern, " ", text)
            return text
     
     def delete_duplicated_letter(self, text):
            """
                removes duplicated letters that aren't part of words from the given text

                Args:
                    text(string): The text to process

                Returns:
                   string: the modified text with duplicated letters removed
            """

            pattern = r"\b([a-zA-Z])\1+\b(?!\w)"  
            text = re.sub(pattern, " ", text)
            return text


     def english_spell_correcter_(self, text):
          """correct the spelling of english word

          Args:
              text (string): input text with incorrect english words spelling

          Returns:
              string: text without any word with incorrect spelling
          """          ""
          spell = Speller()
          text = spell(text)
          return text

     def expand_contractions_(self,text):
          """replace contracted forms with their expanded equivalents.

          Args:
              text (string): input text containing contractions

          Returns:
              string: text with contractions expanded to their full forms
          """          ""
          text = contractions.fix(text)
          return text
     
     def delete_stop_words(self,text):
          """remove all stopword from text

          Args:
              text (string): input text containing stopwords

          Returns:
              string: text without stopwords
          """   
          StopWords1 = set(stopwords.words('english'))
          stop = open('EnglishStopWords.txt','r')
          StopWords2 = set(stop.read().split('\n'))
          stop.close()
          StopWords = StopWords1.union(StopWords2)
          text = word_tokenize(text)
          text = [word for word in text if word not in StopWords]
          return ' '.join(text)


     def delete_unicode_and_special_character(self,text):
          """remove special and unicode characters from the text

          Args:
              text (string): input text contining special characters

          Returns:
              text: text without special characters
          """          
          Pattern = r'([\u2460-\u24FF\u2070-\u218F\u2022-\u221E\u0E3F\u00A9\u00AE\u2117\u2120\u03B1-\u03C9\u0391-\u039F])'
          text = re.sub(Pattern, ' ', text)
          return text

     
     def delete_punctuations(self,text):
          """remove punctuation from the text

          Args:
              text (string): input text contining punctuation

          Returns:
              text: text without punctuation
          """         
          
          Punctuations= str.maketrans(' ', ' ', string.punctuation)
          text = text.translate(Punctuations)
          return text 

     def delete_number(self,text):
           """remove numbers from the text

          Args:
              text (string): input text contining numbers

          Returns:
              text: text without numbers
          """ 
           text = re.sub(r'\d+', '', text)
           return text

     def delete_non_english(self, text):
            """remove non english words from the text

          Args:
              text (string): input text contining non english words

          Returns:
              text: text without non english words
          """ 
            text = ' '.join(word for word in text.split() if(langdetect.detect(word) == 'en') or word in string.punctuation)

            return text

     def delete_longest_than(self,text):
        """remove words that has length more than the longest word in english from the text

          Args:
              text (string): input text contining words that has length more than the longest word in english

          Returns:
              text: text without words that has length more than the longest word in english
          """ 
        for word in text.split():
            if len(word) >=46:
                text = text.replace(word, '')
        return text

     def delete_whitespace(self,text):
          """remove extra whitespaces at the beginning and end of the text

          Args:
              text (text): input text contating extra whitespaces

          Returns:
              string: text without extra whitespaces
          """          ""
          text = re.sub(r"\s+", " ", text)
          return text 

     def lemmatizer_(self,text):
          """applies lemmatization to lower inflections in words, transforming them to their root forms.

          Args:
              text (string): input text to be lemmatized

          Returns:
              string: The lemmatized text, where each word is decreased to its base form
          """          ""
          lemmatizer = WordNetLemmatizer()
          text = " ".join([lemmatizer.lemmatize(word, pos='v') for word in text.split()])
          return text

     def stemmer_(self, text):
          """applies stemming to lower inflections in words, reducing them to their root forms.

          Args:
              text (string): input text to be stemmed

          Returns:
              string: The stemmed text, where each word is decreased to its base form
          """          ""
          stemmer = SnowballStemmer('english')
          text = " ".join([stemmer.stem(word) for word in text.split()])
          return text


