import pyarabic.arabrepr
import re
import os
from camel_tools.utils.dediac import dediac_ar
from camel_tools.utils.normalize import normalize_unicode
from camel_tools.utils.normalize import normalize_alef_maksura_ar
from camel_tools.utils.normalize import normalize_alef_ar
from camel_tools.utils.normalize import normalize_teh_marbuta_ar
from camel_tools.tokenizers.word import simple_word_tokenize
import arabicstopwords.arabicstopwords as stp
import qalsadi.lemmatizer 
from ruqiya import ruqiya
from nltk.stem.snowball import SnowballStemmer

class TextNormalization:
     def __init__(self,remove_emojis,
                    remove_hashtags,
                    remove_emails,
                    remove_url,
                    remove_mention,
                    remove_duplicate_char,
                    remove_single_char,
                    remove_special_character,
                    remove_new_line_char,
                    remove_number,
                    remove_html_tags,
                    remove_arabic_diacritics,
                    normalize_unicode_ar,
                    normalize_alef_maksura_ar,
                    normalize_alef_ar,
                    normalize_teh_marbuta_ar,
                    remove_non_arabic,
                    remove_whitespace,
                    remove_unicode_characters,
                    remove_longest_than,
                    remove_stop_words,
                    lemmatizer,
                    stemmer):
          
          self.remove_emojis = remove_emojis
          self.remove_hashtags = remove_hashtags
          self.remove_emails = remove_emails
          self.remove_url = remove_url
          self.remove_mention = remove_mention
          self.remove_duplicate_char = remove_duplicate_char
          self.remove_single_char = remove_single_char
          self.remove_special_character = remove_special_character
          self.remove_new_line_char = remove_new_line_char
          self.remove_number = remove_number
          self.remove_html_tags = remove_html_tags
          self.remove_arabic_diacritics = remove_arabic_diacritics
          self.normalize_unicode_ar = normalize_unicode_ar
          self.normalize_alef_maksura_ar = normalize_alef_maksura_ar
          self.normalize_alef_ar = normalize_alef_ar
          self.normalize_teh_marbuta_ar = normalize_teh_marbuta_ar
          self.remove_non_arabic = remove_non_arabic
          self.remove_whitespace = remove_whitespace
          self.remove_unicode_characters = remove_unicode_characters
          self.remove_longest_than = remove_longest_than
          self.remove_stop_words = remove_stop_words
          self.lemmatizer = lemmatizer
          self.stemmer = stemmer

     def delete_emojis(self,text):
          "Delete All Emojis From Text"
          text = ruqiya.remove_emojis(text)
          return text

     def delete_hashtags(self,text):
          "Delete All Hashtags From Text"
          text =  ruqiya.remove_hashtags(text)
          return text   

     def delete_emails(self,text):
          "Delete All Emails From Text"
          text = ruqiya.remove_emails(text)
          return text    

     def delete_url(self,text):
          "Delete All URL From Text"
          text = ruqiya.remove_URLs(text)
          return text

     def delete_mention(self,text):
          "Delete All Mention From Text"
          text = ruqiya.remove_mentions(text)
          return text

     def delete_duplicate_char(self,text):
          "Delete Chars Word Has More Than 2 Same Following Char"
          text = re.sub(r'(.)\1+', r'\1\1', text)
          return text

     def delete_single_char(self,text):
          "Delete Alone Chars From Text"
          text = ' '.join( [w for w in text.split() if len(w)>1] )
          return text

     def delete_special_character(self,text):
          "Delete Special Character From Text"
          text = ruqiya.remove_punctuations(text)
          return text   

     def delete_new_line_char(self,text):
          "Delete New Line Symbols From Text"
          text = text.replace('\n', ' ')
          return text  
     
     def delete_number(self,text):
          "Delete All Number From Text"
          text = re.sub(r'\d+', '', text)
          return text

     def delete_html_tags(self,text):
          "Delete All HTL Tags From Text"
          text = re.sub("<.*?>", ' ', text)
          return text

     def delete_arabic_diacritics(self,text):
          "Delete Arabic Dediacritization"
          text = dediac_ar(text)
          return text

     def normalize_arabic_unicode(self,text):
          "Converts A Composed Character Into Its Decomposed Form"
          text = normalize_unicode(text)
          return text

     def normalize_alef_maksura(self,text):
          "Normalize alef maksura 'ى' to yeh 'ي'"
          text = normalize_alef_maksura_ar(text)
          return text

     def normalize_alef(self,text):
          "Normalize alef variants to 'ا'"
          text = normalize_alef_ar(text)
          return text

     def normalize_teh_marbuta(self,text):
          "Normalize teh marbuta 'ة' to heh 'ه'"
          text = normalize_teh_marbuta_ar(text)
          return text

     def delete_non_arabic(self,text):
          "Delete Non Arabic Word And Char"
          text = re.sub('[a-zA-Z]', '', text)
          return text

     def delete_whitespace(self,text):
          "Delete Extra WhiteSpace"
          text = text.strip()
          return text 

     def delete_unicode_characters(self,text):
          "Delete Unicode Char"
          for character in text:
               if (ord(character) < 47) or ((ord(character) > 123 and ord(character) < 1568)) or ((ord(character) > 1641 and ord(character) < 8239)) :
                    text = text.replace(character, ' ')
          return text

     def delete_longest_than(self,text):
          "Delete All Words That Longest Than The Longest Word In Arabic"
          for word in text.split():
               if len(word) >=16:
                    text = text.replace(word, '')
          return text

     def delete_stop_words(self,text):
          "Delete StopWords From Text"
          StopWords1 = set(stp.stopwords_list())
          stop = open('ArabicStopWord.txt','r', encoding='Utf-8')
          StopWords2 = set(stop.read().split('\n'))
          stop.close()
          StopWords = StopWords1.union(StopWords2)
          text = simple_word_tokenize(text)
          text = [word for word in text if word not in StopWords]
          return ' '.join(text)

     def lemmatizer_(self,text):
          lem = qalsadi.lemmatizer.Lemmatizer()
          text = " ".join([lem.lemmatize(word) for word in text.split()])
          return text

     def stemmer_(self, text):
          stem = SnowballStemmer(language = 'arabic')
          text = " ".join([stem.stem(word) for word in text.split()])
          return text

     def normalization(self, text):
          if self.remove_emojis == True:
               text = self.delete_emojis(text)

          if self.remove_non_arabic == True:
               text = self.delete_non_arabic(text)

          if self.remove_hashtags == True:
               text = self.delete_hashtags(text)

          if self.remove_emails == True:
               text = self.delete_emails(text)

          if self.remove_url == True:
               text = self.delete_url(text)

          if self.remove_mention == True:
               text = self.delete_mention(text)

          if self.remove_duplicate_char == True:
               text = self.delete_duplicate_char(text)

          if self.remove_number == True:
               text = self.delete_number(text)

          if self.remove_html_tags == True:
               text = self.delete_html_tags(text)
               
          if self.normalize_unicode_ar == True:
               text = self.normalize_arabic_unicode(text)

          if self.remove_single_char == True:
               text = self.delete_single_char(text)

          if self.remove_special_character==True:
               text = self.delete_special_character(text)

          if self.remove_stop_words == True:
               text = self.delete_stop_words(text)

          if self.normalize_alef_maksura_ar == True:
               text = self.normalize_alef_maksura(text)

          if self.normalize_alef_ar == True:
               text = self.normalize_alef(text)

          if self.normalize_teh_marbuta_ar == True:
               text = self.normalize_teh_marbuta(text)

          if self.remove_arabic_diacritics == True:
               text = self.delete_arabic_diacritics(text)

          if self.remove_longest_than == True:
               text = self.delete_longest_than(text)

          if self.remove_new_line_char == True:
               text = self.delete_new_line_char(text)

          if self.remove_unicode_characters == True:
               text = self.delete_unicode_characters(text)

          if self.remove_whitespace == True:
               text = self.delete_whitespace(text)
               
          if self.lemmatizer == True:
               text = self.lemmatizer_(text)

          if self.stemmer == True:
               text = self.stemmer_(text)
          return text

          








