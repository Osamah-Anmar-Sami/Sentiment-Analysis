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
import spacy_fastlang
import spacy
nlp = spacy.load("xx_ent_wiki_sm")
nlp.add_pipe("language_detector")
import string
Punctuation  = set(string.punctuation).union("{}_!-?.:;""''()،؟,..[]")


def delete_emojis(text):
          """remove all emojis from text

          Args:
              text (string): input text containing emoijis to be removed

          Returns:
              string: text without any emojis
          """ 
          text = ruqiya.remove_emojis(text)
          return text
     
def delete_hashtags(text):
          """remove all hashtags from text

          Args:
              text (string): input text containing hashtags to be removed

          Returns:
              string: text without any hashtags
          """   
          text =  ruqiya.remove_hashtags(text)
          return text
     
def delete_emails(text):
          """remove all email address from text

          Args:
              text (string): input text containing email address to be removed

          Returns:
              string: text without any email address
          """   
          text = ruqiya.remove_emails(text)
          return text
     
def delete_url(text):
          """remove all URL from text

          Args:
              text (string): input text containing URL address to be removed

          Returns:
              string: text without any URL address
          """ 
          text = ruqiya.remove_URLs(text)
          return text
     
def delete_mention(text):
          """remove all mention from text

          Args:
              text (string): input text containing mention to be removed

          Returns:
              string: text without any mention
          """   
          text = ruqiya.remove_mentions(text)
          return text
     
def delete_html_tags(text):
          """remove all html tags from text

          Args:
              text (string): input text containing html tags to be removed

          Returns:
              string: text without any html tags
          """ 
          text = re.sub("<.*?>", ' ', text)
          return text
     
def delete_new_line_char(text):
          """delete new line character from text

          Args:
              text (string): input text containing new line character to be removed

          Returns:
              string: text without any new line character 
          """     
          text = text.replace('\n', ' ')
          return text
     
def arabic_spell_correcter_( text):
          """correct the spelling of english word

          Args:
              text (string): input text with incorrect english words spelling

          Returns:
              string: text without any word with incorrect spelling
          """          ""
          
          text = corr.contextual_correct(text)
          return text
     
def decrease_number_of_consecutive_reapted_letter_(text):
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

            pattern = r"\b([ٱأإٲٳٵآ-ي])\b(?!\w)"  
            text = re.sub(pattern, " ", text)
            return text
     
def delete_duplicated_letter( text):
            """
                removes duplicated letters that aren't part of words from the given text

                Args:
                    text(string): The text to process

                Returns:
                   string: the modified text with duplicated letters removed
            """

            pattern = r"\b([ٱأإٲٳٵآ-ى])\1+\b(?!\w)"  
            text = re.sub(pattern, " ", text)
            return text
     
def delete_punctuations(text):
          """remove punctuation from the text

          Args:
              text (string): input text contining punctuation

          Returns:
              text: text without punctuation
          """         
          
          
          text = ruqiya.remove_punctuations(text)
          return text
     
def delete_unicode_and_special_character(text):
          """remove special and unicode characters from the text

          Args:
              text (string): input text contining special characters

          Returns:
              text: text without special characters
          """          
          Pattern = r'([\u2460-\u24FF\u2070-\u218F\u2022-\u221E\u0E3F\u00A9\u00AE\u2117\u2120\u03B1-\u03C9\u0391-\u039F])'
          text = re.sub(Pattern, ' ', text)
          return text
     
def delete_stop_words(text):
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
          text =' '.join(word for word in text if word not in StopWords)
          return text
     
def delete_number(text):
          """remove numbers from the text

          Args:
              text (string): input text contining numbers

          Returns:
              text: text without numbers
          """
          text = re.sub(r'\d+', '', text)
          return text
     
     
def delete_non_arabic(text):
          """remove non arabic words from the text

          Args:
              text (string): input text contining non english words

          Returns:
              text: text without non english words
          """ 
          words = text.split()
          text = ' '.join(word for word in words if nlp(word)._.language == 'ar' or nlp(word)._.language == 'fa' or word in Punctuation)
          return text
     
def delete_arabic_diacritics(text):
          """removes diacritics (harakat) from Arabic text


               Args:
                    text (string): the Arabic text to remove diacritics from

               Returns:
                    string: the modified text without diacritics
          """
          text = ruqiya.remove_diacritics(text)
          return text

     
def convert_alef_maqsura(text):
          """converts Alef Maksura (ى) to Yeh (ي) in Arabic text

           Args:
               text (string): the Arabic text to convert

           Returns:
               string: the modified text with Alef Maksura replaced by Yeh
          """
          text = text = re.sub("ى", "ي", text)
          return text

def convert_alef(text):
          """
               converts various Alef representations (including Alef with Hamza Above/Below, Alef with Madda Above, etc.) to the basic Alef ('ا') in Arabic text


               Args:
                    text (string): the Arabic text to convert

               Returns:
                    string: the modified text with all Alef variants replaced by the basic Alef
          """
          text = re.sub("[ٱأإٲٳٵآ]", "ا", text)
          return text

def convert_teh_marbuta(text):
          """converts Teh Marbuta (ة) to Heh (ه) in Arabic text.


          Args:
               text (string): the Arabic text to convert

          Returns:
               string: the modified text with Teh Marbuta replaced by Heh
          """
          text = re.sub("ة", "ه", text)
          return text

def delete_arabic_tashkeel(text):
          """delete Arabic Tashkeel

               Args:
               
                text (string): text with Arabic Tashkeel marks

               Returns:
                   text after removing Arabic Tashkeel
          """
          text = strip_tashkeel(text)
          return text

def delete_arabic_tatweel(text):
          """delete Arabic Tatweel

               Args:
               
                text (string): text with Arabic Tatweel

               Returns:
                  text after removing Arabic Tatweel
          """
          text = strip_tatweel(text)
          return text

def delete_longest_than(text):
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

def delete_whitespace(text):
          """remove extra whitespaces at the beginning and end of the text

          Args:
              text (text): input text contating extra whitespaces

          Returns:
              string: text without extra whitespaces
          """  
          text = re.sub(r"\s+", " ", text)
          return text 

def lemmatizer_(text):
          """applies lemmatization to lower inflections in words, transforming them to their root forms.

          Args:
              text (string): input text to be lemmatized

          Returns:
              string: The lemmatized text, where each word is reduced to its base form
          """ 
          lem = qalsadi.lemmatizer.Lemmatizer()
          text = " ".join([lem.lemmatize(word) for word in text.split()])
          return text

def stemmer_(text):
          """applies stemming to lower inflections in words, reducing them to their root forms.

          Args:
              text (string): input text to be stemmed

          Returns:
              string: The stemmed text, where each word is reduced to its base form
          """
          stemmer = SnowballStemmer('arabic')
          text = " ".join([stemmer.stem(word) for word in text.split()])
          return text
     


def text_normalization(text):
          """Normalizes text based on various configurable options.

          **Available options:**

          - `remove_emojis`: Remove emojis from the text 
          - `remove_hashtags`: Remove hashtags from the text 
          - `remove_emails`: Remove email addresses from the text 
          - `remove_URLs`: Remove URLs from the text 
          - `remove_new_line_char`: Remove newline characters from the text 
          - `remove_mentions`: Remove mentions from the text 
          - `remove_single_letter`: Remove single-character words from the text 
          - `remove_repeated_char`: Remove words with repeated characters (e.g., "yesss") 
          - `remove_duplicate_word`: Remove duplicate words consecutively appearing in the text 
          - `remove_stop_words`: Remove stop words from the text 
          - `remove_special_character`: Remove special characters from the text 
          - `remove_puncuations`: Remove punctuation marks from the text 
          - `remove_html_tags`: Remove HTML tags from the text 
          - `remove_numbers`: Remove numbers from the text 
          - `remove_non_arabic`: Remove non-Arabic characters from the text 
          - `remove_arabic_diacritics`: Remove diacritics (harakat) from Arabic text 
          - `normalize_alef_maqsura`: Normalize Alef Maqsura (ى) to Yeh (ي) in Arabic text 
          - `normalize_alef`: Convert various Alef representations to the basic Alef (ا) in Arabic text 
          - `normalize_teh_marbuta`: Normalize Teh Marbuta (ة) to Heh (ه) in Arabic text 
          - `normalize_arabic_tashkeel`: Remove diacritics (tashkeel) from Arabic text 
          - `normalize_arabic_tatweel`: Remove Tatweel (آ) from Arabic text 
          - `remove_longest_than`: Remove words longer than a specified length  
          - `remove_whitespace`: Remove extra whitespace characters from the text """

          
          text = delete_emojis (text)
          text = delete_hashtags(text)
          text = delete_emails( text)
          text = delete_url(text)
          text = delete_mention(text)
          text = delete_html_tags(text)
          text = delete_new_line_char(text)
          text = decrease_number_of_consecutive_reapted_letter_(text)
          text = delete_duplicate_word(text)
          text = delete_single_letter(text)
          text = delete_duplicated_letter(text)
          text = delete_punctuations(text)
          text = delete_unicode_and_special_character(text)
          text = arabic_spell_correcter_(text)
          text = delete_stop_words( text)
          text = delete_number(text)
          text = delete_non_arabic(text)
          text = delete_arabic_diacritics(text)
          text = convert_alef_maqsura(text)
          text = convert_alef(text)
          text = convert_teh_marbuta(text)
          text = delete_arabic_tashkeel(text)
          text = delete_arabic_tatweel(text)
          text = delete_longest_than(text)
          text = delete_whitespace(text)
          text = lemmatizer_(text)

          return text






