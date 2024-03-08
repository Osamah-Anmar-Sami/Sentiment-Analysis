import pyarabic.arabrepr
import re
import os
from pyarabic.araby import strip_tashkeel, strip_tatweel, tokenize
import arabicstopwords.arabicstopwords as stp
import qalsadi.lemmatizer 
from ruqiya import ruqiya
from nltk.stem import  SnowballStemmer
from ar_corrector.corrector import Corrector
corr = Corrector()
import fasttext
import string
Punctuation  = set(string.punctuation).union("{}_!-?.:;""''()،؟,..[]")

class TextNormalization:
     def __init__(self,
                 remove_emojis,
                 remove_hashtags,
                 remove_emails,
                 remove_url,
                 remove_mention,
                 remove_html_tags,
                 remove_new_line_char,
                 arabic_spell_correcter,
                 decrease_number_of_consecutive_reapted_letter,
                 remove_duplicate_word,
                 remove_single_letter,
                 remove_duplicated_letter,
                 remove_punctuations,
                 remove_special_character,
                 removee_stop_words,
                 remove_number,
                 remove_non_arabic,
                 remove_arabic_diacritics,
                 normlize_alef_maqsura,
                 normlize_alef,
                 normlize_teh_marbuta,
                 remove_arabic_tashkeel,
                 remove_arabic_tatweel,
                 remove_longest_than,
                 remove_whitespace,
                 lemmatizer,
                 stemmer,):
          
          self.remove_emojis = remove_emojis,
          self.remove_hashtags = remove_hashtags,
          self.remove_emails = remove_emails,
          self.remove_url = remove_url,      
          self.remove_mention = remove_mention,
          self.remove_html_tags = remove_html_tags,
          self.remove_new_line_char = remove_new_line_char,
          self.arabic_spell_correcter = arabic_spell_correcter,
          self.decrease_number_of_consecutive_reapted_letter = decrease_number_of_consecutive_reapted_letter,
          self.remove_duplicate_word = remove_duplicate_word,
          self.remove_duplicate_word = remove_duplicate_word,
          self.remove_single_letter = remove_single_letter,
          self.remove_duplicated_letter = remove_duplicated_letter,
          self.remove_punctuations = remove_punctuations,
          self.remove_special_character = remove_special_character,
          self.removee_stop_words = removee_stop_words,
          self.remove_number = remove_number,
          self.remove_non_arabic = remove_non_arabic,
          self.remove_arabic_diacritics = remove_arabic_diacritics,
          self.normlize_alef_maqsura = normlize_alef_maqsura,
          self.normlize_alef = normlize_alef,
          self.normlize_teh_marbuta = normlize_teh_marbuta,
          self.remove_arabic_tashkeel = remove_arabic_tashkeel,
          self.remove_arabic_tatweel = remove_arabic_tatweel,
          self.remove_longest_than = remove_longest_than,
          self.remove_whitespace = remove_whitespace,
          self.lemmatizer = lemmatizer,
          self.stemmer = stemmer,

  

     def delete_emojis(self,text):
          """remove all emojis from text

          Args:
              text (string): input text containing emoijis to be removed

          Returns:
              string: text without any emojis
          """ 
          text = ruqiya.remove_emojis(text)
          return text
     
     def delete_hashtags(self,text):
          """remove all hashtags from text

          Args:
              text (string): input text containing hashtags to be removed

          Returns:
              string: text without any hashtags
          """   
          text =  ruqiya.remove_hashtags(text)
          return text
     
     def delete_emails(self,text):
          """remove all email address from text

          Args:
              text (string): input text containing email address to be removed

          Returns:
              string: text without any email address
          """   
          text = ruqiya.remove_emails(text)
          return text
     
     def delete_url(self,text):
          """remove all URL from text

          Args:
              text (string): input text containing URL address to be removed

          Returns:
              string: text without any URL address
          """ 
          text = ruqiya.remove_URLs(text)
          return text
     
     def delete_mention(self,text):
          """remove all mention from text

          Args:
              text (string): input text containing mention to be removed

          Returns:
              string: text without any mention
          """   
          text = ruqiya.remove_mentions(text)
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
          """     
          text = text.replace('\n', ' ')
          return text
     
     def arabic_spell_correcter_(self, text):
          """correct the spelling of english word

          Args:
              text (string): input text with incorrect english words spelling

          Returns:
              string: text without any word with incorrect spelling
          """          ""
          
          text = corr.contextual_correct(text)
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
     
     def delete_duplicate_word(text):
          """delete consecutive duplicate words in a given text

          Args:
              text (string): input text containing duplicate words separated by spaces.

          Returns:
              string: text without any duplicate words
          """          ""
          pattern = r'\b(\w+)(\s+)(\1+)\b'
          text = re.sub(pattern, r'\1', text)
          return text
     
     def delete_single_letter(text):
            """
                removes single letters that aren't part of words from the given text

                Args:
                    text(string): The text to process

                Returns:
                   string: the modified text with single letters removed
            """

            pattern = r"\b([ا-ي])\b(?!\w)"  
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

            pattern = r"\b([ا-ى])\1+\b(?!\w)"  
            text = re.sub(pattern, " ", text)
            return text
     
     def delete_punctuations(self,text):
          """remove punctuation from the text

          Args:
              text (string): input text contining punctuation

          Returns:
              text: text without punctuation
          """         
          
          
          text = ruqiya.remove_punctuations(text)
          return text
     
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
     
     def delete_stop_words(self,text):
          """remove all stopword from text

          Args:
              text (string): input text containing stopwords

          Returns:
              string: text without stopwords
          """  
          StopWords1 = set(stp.stopwords_list())
          stop = open('ArabicStopWord.txt','r', encoding='Utf-8')
          StopWords2 = set(stop.read().split('\n'))
          stop.close()
          StopWords = StopWords1.union(StopWords2)
          text = tokenize(text)
          text = [word for word in text if word not in StopWords]
          return ' '.join(text)
     
     def delete_number(self,text):
          """remove numbers from the text

          Args:
              text (string): input text contining numbers

          Returns:
              text: text without numbers
          """
          text = re.sub(r'\d+', '', text)
          return text
     
     
     def delete_non_arabic(self, text):
          """remove non arabic words from the text

          Args:
              text (string): input text contining non english words

          Returns:
              text: text without non english words
          """ 
          pretrained_model_path = "lid.176.bin"
          model = fasttext.load_model(pretrained_model_path)
          words = text.split() 
          text = ' '.join(word for word in words if( model.predict(word, k=1)[0][0] == '__label__ar') or word in Punctuation)

          return text
     
     def delete_arabic_diacritics(self,text):
          """removes diacritics (harakat) from Arabic text


               Args:
                    text (string): the Arabic text to remove diacritics from

               Returns:
                    string: the modified text without diacritics
          """
          text = ruqiya.remove_diacritics(text)
          return text

     
     def convert_alef_maqsura(self,text):
          """converts Alef Maksura (ى) to Yeh (ي) in Arabic text

           Args:
               text (string): the Arabic text to convert

           Returns:
               string: the modified text with Alef Maksura replaced by Yeh
          """
          text = text = re.sub("ى", "ي", text)
          return text

     def convert_alef(self,text):
          """
               converts various Alef representations (including Alef with Hamza Above/Below, Alef with Madda Above, etc.) to the basic Alef ('ا') in Arabic text


               Args:
                    text (string): the Arabic text to convert

               Returns:
                    string: the modified text with all Alef variants replaced by the basic Alef
          """
          text = re.sub("[ٱأإٲٳٵآ]", "ا", text)
          return text

     def convert_teh_marbuta(self,text):
          """converts Teh Marbuta (ة) to Heh (ه) in Arabic text.


          Args:
               text (string): the Arabic text to convert

          Returns:
               string: the modified text with Teh Marbuta replaced by Heh
          """
          text = re.sub("ة", "ه", text)
          return text

     def delete_arabic_tashkeel(self,text):
          """delete Arabic Tashkeel

               Args:
               
                text (string): text with Arabic Tashkeel marks

               Returns:
                   text after removing Arabic Tashkeel
          """
          text = strip_tashkeel(text)
          return text

     def delete_arabic_tatweel(self,text):
          """delete Arabic Tatweel

               Args:
               
                text (string): text with Arabic Tatweel

               Returns:
                  text after removing Arabic Tatweel
          """
          text = strip_tatweel(text)
          return text

     def delete_longest_than(self,text):
          """remove words that has length more than the longest word in arabic from the text

          Args:
              text (string): input text contining words that has length more than the longest word in arabic

          Returns:
              text: text without words that has length more than the longest word in arabic
          """ 
          for word in text.split():
               if len(word) >=16:
                    text = text.replace(word, '')
          return text

     def delete_whitespace(self,text):
          """remove extra whitespaces at the beginning and end of the text

          Args:
              text (text): input text contating extra whitespaces

          Returns:
              string: text without extra whitespaces
          """  
          text = re.sub(r"\s+", " ", text)
          return text 

     def lemmatizer_(self,text):
          """applies lemmatization to lower inflections in words, transforming them to their root forms.

          Args:
              text (string): input text to be lemmatized

          Returns:
              string: The lemmatized text, where each word is reduced to its base form
          """ 
          lem = qalsadi.lemmatizer.Lemmatizer()
          text = " ".join([lem.lemmatize(word) for word in text.split()])
          return text

     def stemmer_(self, text):
          """applies stemming to lower inflections in words, reducing them to their root forms.

          Args:
              text (string): input text to be stemmed

          Returns:
              string: The stemmed text, where each word is reduced to its base form
          """
          stemmer = SnowballStemmer('arabic')
          text = " ".join([stemmer.stem(word) for word in text.split()])
          return text
     


     def normalization(self, text):
          """Normalizes text based on various configurable options.

          **Available options:**

          - `remove_emojis`: Remove emojis from the text (True/False)
          - `remove_hashtags`: Remove hashtags from the text (True/False)
          - `remove_emails`: Remove email addresses from the text (True/False)
          - `remove_URLs`: Remove URLs from the text (True/False)
          - `remove_new_line_char`: Remove newline characters from the text (True/False)
          - `remove_mentions`: Remove mentions from the text (True/False)
          - `remove_single_letter`: Remove single-character words from the text (True/False)
          - `remove_repeated_char`: Remove words with repeated characters (e.g., "yesss") (True/False)
          - `remove_duplicate_word`: Remove duplicate words consecutively appearing in the text (True/False)
          - `remove_stop_words`: Remove stop words from the text (True/False)
          - `remove_special_character`: Remove special characters from the text (True/False)
          - `remove_puncuations`: Remove punctuation marks from the text (True/False)
          - `remove_html_tags`: Remove HTML tags from the text (True/False)
          - `remove_numbers`: Remove numbers from the text (True/False)
          - `remove_non_arabic`: Remove non-Arabic characters from the text (True/False)
          - `remove_arabic_diacritics`: Remove diacritics (harakat) from Arabic text (True/False)
          - `normalize_alef_maqsura`: Normalize Alef Maqsura (ى) to Yeh (ي) in Arabic text (True/False)
          - `normalize_alef`: Convert various Alef representations to the basic Alef (ا) in Arabic text (True/False)
          - `normalize_teh_marbuta`: Normalize Teh Marbuta (ة) to Heh (ه) in Arabic text (True/False)
          - `normalize_arabic_tashkeel`: Remove diacritics (tashkeel) from Arabic text (True/False)
          - `normalize_arabic_tatweel`: Remove Tatweel (آ) from Arabic text (True/False)
          - `remove_longest_than`: Remove words longer than a specified length (True/False) 
          - `remove_whitespace`: Remove extra whitespace characters from the text (True/False)
          - `lemmatizer_`: Apply a lemmatizer function to the text 
          - `stemmer`: Apply a stemmer function to the text 
         
          Args:
          text (string): the text to be normalized

          Returns:
          string: the normalized text
          """
          if self.remove_emojis == True:
               text = self.delete_emojis(text)
          if self.remove_hashtags == True:
               text = self.delete_hashtags(text)
          if self.remove_emails == True:
               text = self.delete_hashtags(text)
          if self.remove_url == True:
               text = self.delete_url(text)
          if self.remove_mention == True:
               text = self.delete_mention(text)
          if self.remove_html_tags == True:
               text = self.delete_html_tags(text)
          if self.remove_new_line_char == True:
               text = self.delete_new_line_char(text)
          if self.arabic_spell_correcter == True:
               text = self.arabic_spell_correcter_(text)
          if self.decrease_number_of_consecutive_reapted_letter == True:
               text = self.decrease_number_of_consecutive_reapted_letter_(text)
          if self.remove_duplicate_word == True:
               text = self.delete_duplicate_word(text)
          if self.remove_single_letter == True:
               text = self.delete_single_letter(text)
          if self.remove_duplicated_letter == True:
               text = self.delete_duplicated_letter(text)
          if self.remove_punctuations == True:
               text = self.delete_punctuations(text)
          if self.remove_special_character == True:
               text = self.delete_special_character(text)
          if self.removee_stop_words == True:
               text = self.delete_stop_words(text)
          if self.remove_number == True:
               text = self.delete_number(text)
          if self.remove_non_arabic == True:
               text = self.delete_non_arabic(text)
          if self.remove_arabic_diacritics == True:
               text = self.delete_arabic_diacritics(text)
          if self.normlize_alef_maqsura == True:
               text = self.convert_alef_maqsura(text)
          if self.normlize_alef == True:
               text = self.convert_alef(text)
          if self.normlize_teh_marbuta == True:
               text = self.convert_teh_marbuta(text)
          if self.remove_arabic_tashkeel == True:
               text = self.delete_arabic_tashkeel(text)
          if self.remove_arabic_tatweel == True:
               text = self.delete_arabic_tatweel(text)
          if self.remove_longest_than == True:
               text = self.delete_longest_than(text)
          if self.remove_whitespace == True:
               text = self.delete_whitespace(text)
          if self.lemmatizer == True:
               text = self.lemmatizer_
          if self.stemmer == True:
               text = self.stemmer_(text)
          return text
               
          
          
