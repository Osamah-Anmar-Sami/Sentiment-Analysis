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
from tashaphyne.stemming import ArabicLightStemmer
from ruqiya import ruqiya

class TextNormalization:
     def __init__(self,_remove_emojis,
                    _remove_hashtags,
                    _remove_emails,
                    _remove_url,
                    _remove_mention,
                    _remove_duplicate_char,
                    _remove_single_char,
                    _remove_special_character_,
                    _remove_new_line_char,
                    _remove_number,
                    _remove_html_tags,
                    _remove_arabic_diacritics_,
                    _normalize_arabic_unicode_,
                    _normalize_alef_maksura_ar_,
                    _normalize_alef_ar_,
                    _normalize_teh_marbuta_ar_,
                    _remove_non_arabic,
                    _remove_whitespace_,
                    _remove_unicode_characters_,
                    _remove_longest_than_,
                    _remove_stop_words,
                    _lemmatizer_,
                    _stemmer_):
          
          self._remove_emojis = _remove_emojis
          self._remove_hashtags = _remove_hashtags
          self._remove_emails = _remove_emails
          self._remove_url = _remove_url
          self._remove_mention = _remove_mention
          self._remove_duplicate_char = _remove_duplicate_char
          self._remove_single_char = _remove_single_char
          self._remove_special_character_ = _remove_special_character_
          self._remove_new_line_char = _remove_new_line_char
          self._remove_number = _remove_number
          self._remove_html_tags = _remove_html_tags
          self._remove_arabic_diacritics_ = _remove_arabic_diacritics_
          self._normalize_arabic_unicode_ = _normalize_arabic_unicode_
          self._normalize_alef_maksura_ar_ = _normalize_alef_maksura_ar_
          self._normalize_alef_ar_ = _normalize_alef_ar_
          self._normalize_teh_marbuta_ar_ = _normalize_teh_marbuta_ar_
          self._remove_non_arabic = _remove_non_arabic
          self._remove_whitespace_ = _remove_whitespace_
          self._remove_unicode_characters_ = _remove_unicode_characters_
          self._remove_longest_than_ = _remove_longest_than_
          self._remove_stop_words = _remove_stop_words
          self._lemmatizer_ = _lemmatizer_
          self._stemmer_ = _stemmer_

     def remove_emojis(self,text):
          "Remove All Emojis From Text"
          text = ruqiya.remove_emojis(text)
          return text

     def remove_hashtags(self,text):
          "Remove All Hashtags From Text"
          text =  remove_hashtags(text)
          return text   

     def remove_emails(self,text):
          "Remove All Emails From Text"
          text = ruqiya.remove_emails(text)
          return text    

     def remove_url(self,text):
          "Remove All URL From Text"
          text = ruqiya.remove_URLs(text)
          return text

     def remove_mention(self,text):
          "Remove All Mention From Text"
          text = ruqiya.remove_mentions(text)
          return text

     def remove_duplicate_char(self,text):
          "Remove Chars Word Has More Than 2 Same Following Char"
          text = re.sub(r'(.)\1+', r'\1\1', text)
          return text

     def remove_single_char(self,text):
          "Remove Alone Chars From Text"
          text = ' '.join( [w for w in text.split() if len(w)>1] )
          return text

     def remove_special_character_(self,text):
          "Remove Special Character From Text"
          text = ruqiya.remove_punctuations(text)
          return text   

     def remove_new_line_char(self,text):
          "Remove New Line Symbols From Text"
          text = text.replace('\n', ' ')
          return text  
     
     def remove_number(self,text):
          "Remove All Number From Text"
          text = re.sub(r'\d+', '', text)
          return text

     def remove_html_tags(self,text):
          "Remove All HTL Tags From Text"
          text = re.sub("<.*?>", ' ', text)
          return text

     def remove_arabic_diacritics_(self,text):
          "Remove Arabic Dediacritization"
          text = dediac_ar(text)
          return text

     def normalize_arabic_unicode_(self,text):
          "Converts A Composed Character Into Its Decomposed Form"
          text = normalize_unicode(text)
          return text

     def normalize_alef_maksura_ar_(self,text):
          "Normalize alef maksura 'ى' to yeh 'ي'"
          text = normalize_alef_maksura_ar(text)
          return text

     def normalize_alef_ar_(self,text):
          "Normalize alef variants to 'ا'"
          text = normalize_alef_ar(text)
          return text

     def normalize_teh_marbuta_ar_(self,text):
          "Normalize teh marbuta 'ة' to heh 'ه'"
          text = normalize_teh_marbuta_ar(text)
          return text

     def remove_non_arabic(self,text):
          "Remove Non Arabic Word And Char"
          text = re.sub('[a-zA-Z]', '', text)
          return text

     def remove_whitespace(self,text):
          "Remove Extra WhiteSpace"
          text = text.strip()
          return text 

     def remove_unicode_characters_(self,text):
          "Remove Unicode Char"
          for character in text:
               if (ord(character) < 47) or ((ord(character) > 123 and ord(character) < 1568)) or ((ord(character) > 1641 and ord(character) < 8239)) :
                    text = text.replace(character, ' ')
          return text

     def remove_longest_than_(self,text):
          "Remove All Words That Longest Than The Longest Word In Arabic"
          for word in text.split():
               if len(word) >=16:
                    text = text.replace(word, '')
          return text

     def remove_stop_words(self,text):
          "Remove StopWords From Text"
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
          stem = ArabicLightStemmer()
          text = " ".join([stem.light_stem(word) for word in text.split()])
          return text

     def normalization(self, text):
          if self._remove_emojis == True:
               text = self.remove_emojis(text)
          if self._remove_non_arabic == True:
               text = self.remove_non_arabic(text)
          if self._remove_hashtags == True:
               text = self.remove_hashtags(text)
          if self._remove_emails == True:
               text = self.remove_emails(text)
          if self._remove_url == True:
               text = self.remove_url(text)
          if self._remove_mention == True:
               text = self.remove_mention(text)
          if self._remove_duplicate_char == True:
               text = self.remove_duplicate_char(text)
          if self._remove_number == True:
               text = self.remove_number(text)
          if self._remove_html_tags == True:
               text = self.remove_html_tags(text)
          if self._normalize_arabic_unicode_ == True:
               text = self.normalize_arabic_unicode_(text)
          if self._remove_single_char == True:
               text = self.remove_single_char(text)
          if self._remove_special_character_==True:
               text = self.remove_special_character_(text)
          if self._remove_stop_words == True:
               text = self.remove_stop_words(text)
          if self._normalize_alef_maksura_ar_ == True:
               text = self.normalize_alef_maksura_ar_(text)
          if self._normalize_alef_ar_ == True:
               text = self.normalize_alef_ar_(text)
          if self._normalize_teh_marbuta_ar_ == True:
               text = self.normalize_teh_marbuta_ar_(text)
          if self._remove_arabic_diacritics_ == True:
               text = self.remove_arabic_diacritics_(text)
          if self._remove_longest_than_ == True:
               text = self.remove_longest_than_(text)
          if self._remove_new_line_char == True:
               text = self.remove_new_line_char(text)
          if self._remove_unicode_characters_ == True:
               text = self.remove_unicode_characters_(text)
          if self._remove_whitespace_ == True:
               text = self.remove_whitespace(text)
          if self._lemmatizer_ == True:
               text = self.lemmatizer_(text)
          if self._stemmer_ == True:
               text = self.stemmer_ (text)
          return ''.join(text)

          








