import nltk
from nltk.stem import  WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.stem import  SnowballStemmer
import re
import os
from nltk.tokenize import word_tokenize
import emoji
import string
from textblob import TextBlob
import contractions


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
                 remove_duplicate_char,
                 remove_duplicate_word,
                 english_spell_coreccter,
                 expand_contractions,
                 remove_stop_words,
                 remove_special_character,
                 remove_puncuations,
                 remove_single_char,
                 remove_numbers,
                 remove_non_english,
                 remove_meaningless_word,
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
          self.remove_duplicate_char = remove_duplicate_char
          self.remove_duplicate_word = remove_duplicate_word
          self.english_spell_coreccter = english_spell_coreccter
          self.expand_contractions = expand_contractions
          self.remove_stop_words = remove_stop_words
          self.remove_special_character = remove_special_character
          self.remove_puncuations = remove_puncuations
          self.remove_single_char = remove_single_char
          self.remove_numbers = remove_numbers
          self.remove_non_english = remove_non_english
          self.remove_meaningless_word = remove_meaningless_word
          self.remove_longest_than = remove_longest_than
          self.remove_whitespace = remove_whitespace
          self.lemmatize = lemmatize
          self.stemmer = stemmer


     def string_lower_(self,text):
        text = str(text)
        text = text.lower()
        return text

     def delete_emojis(self,text):
        "Remove All Emojis From Text"
        text = emoji.replace_emoji(text, replace="")
        return text

     def delete_hashtags(self,text):
        "Remove All Hashtags From Text"
        text =  re.sub("#[ا-ي٠-٩a-zA-Z0-9]+","", text)
        return text   

     def delete_emails(self,text):
        "Remove All Emails From Text"
        text = re.sub("[a-zA-Z0-9-_.]+@[a-zA-Z]+.[a-zA-Z]+","", text)  
        return text 

     def delete_url(self,text):
        "Remove All URL From Text"
        text = re.sub(r'http\S+', '', text, flags=re.MULTILINE)
        return text

     def delete_mention(self,text):
        "Remove All Mention From Text"
        text = re.sub("@[ا-ي٠-٩a-zA-Z0-9]+","", text)
        return text

     def delete_html_tags(self,text):
          "Delete All HTL Tags From Text"
          text = re.sub("<.*?>", ' ', text)
          return text

     def delete_new_line_char(self,text):
          "Delete New Line Symbols From Text"
          text = text.replace('\n', ' ')
          return text 
     
     def delete_duplicate_char(self,text):
          "Delete Chars Word Has More Than 2 Same Following Char"
          text = re.sub(r'(.)\1+', r'\1\1', text)
          return text

     def delete_duplicate_word(self,text):
          "Delete Followed Occurrences Of Duplicate Words"
          text = re.sub(r'\b(\w+)( \1)+', r'\1', text)
          return text

     def english_spell_correcter_(self, text):
          correcter = TextBlob(text)
          text = str(correcter.correct())
          return text 

     def expand_contractions_(self,text):
          text = contractions.fix(text)
          return text
     
     def delete_stop_words(self,text):
        "Remove StopWords From Text"
        StopWords1 = set(stopwords.words('english'))
        stop = open('EnglishStopWords.txt','r')
        StopWords2 = set(stop.read().split('\n'))
        stop.close()
        StopWords = StopWords1.union(StopWords2)
        text = word_tokenize(text)
        text = [word for word in text if word not in StopWords]
        return ' '.join(text)


     def delete_special_character(self,text):
          "Delete Special Character From Text"
          Pattern = re.compile('[^a-zA-Z0-9\s' + "{}_!-?.:;""''()،؟.." + ']')
          text = re.sub(Pattern, ' ', text)
          return text

     def delete_punctuations(self,text):
          "Delete Punctuations Words"
          Punctuations = "{}_!-?.:;""''()،؟,..[]"
          for punctuation in Punctuations:
            text = text.replace(punctuation, ' ')
          return text  

     def delete_single_char(self,text):
          "Delete Alone Chars From Text"
          text = ' '.join( [w for w in text.split() if len(w)>1] )
          return text

     def delete_number(self,text):
          "Delete All Number From Text"
          text = re.sub(r'\d+', '', text)
          return text

     def delete_non_english(self,text):
          "Remove Non English Word And Char"
          char = set(string.printable)
          for c in text:
            if c not in char:
                text = text.replace(c, ' ')
          return text

     def delete_meaningless_word(self,text):
          words = set(nltk.corpus.words.words())
          text = " ".join(w for w in nltk.wordpunct_tokenize(text) if w.lower() in words or not w.isalpha())
          return text

     def delete_longest_than(self,text):
        "Remove All Words That Longest Than The Longest Word In Englis"
        for word in text.split():
            if len(word) >=46:
                text = text.replace(word, '')
        return text

     def delete_whitespace(self,text):
          "Delete Extra WhiteSpace"
          text = text.strip()
          return text 

     def lemmatizer_(self,text):
          "Lowers Inflection In Words To Their Root Forms"
          lemmatizer = WordNetLemmatizer()
          text = " ".join([lemmatizer.lemmatize(word, pos='v') for word in text.split()])
          return text

     def stemmer_(self, text):
          "Lowers Inflection In Words To Their Root Forms"
          stemmer = SnowballStemmer('english')
          text = " ".join([stemmer.stem(word) for word in text.split()])
          return text



     def normalization(self, text):
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
          if self.remove_duplicate_char == True:
               text = self.delete_duplicate_char(text)
          if self.remove_duplicate_word == True:
               text = self.delete_duplicate_word(text)
          if self.english_spell_coreccter == True:
               text = self.english_spell_correcter_(text)
          if self.expand_contractions == True:
               text = self.expand_contractions_(text)
          if self.remove_stop_words == True:
               text = self.delete_stop_words(text)
          if self.remove_special_character == True:
               text = self.delete_special_character(text)
          if self.remove_puncuations == True:
               text = self.delete_punctuations(text)
          if self.remove_single_char == True:
               text = self.delete_single_char(text)
          if self.remove_numbers == True:
               text = self.delete_number(text)
          if self.remove_non_english == True:
               text = self.delete_non_english(text)
          if self.remove_meaningless_word == True:
               text = self.delete_meaningless_word(text)
          if self.remove_longest_than == True:
               text = self.delete_longest_than(text)
          if self.remove_whitespace == True:
               text = self.delete_whitespace(text)
          if self.lemmatizer_ == True:
               text = self.lemmatizer_(text)
          if self.stemmer == True:
               text = self.stemmer_(text)
          return text
          