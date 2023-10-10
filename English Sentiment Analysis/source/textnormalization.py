import nltk
from nltk.stem import  WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.stem import  SnowballStemmer
import re
import os
from nltk.tokenize import word_tokenize
import emoji
import string


class TextNormalization:
    def __init__(self, 
                 _string_lower, 
                 _remove_emojis, 
                 _remove_hashtags, 
                 _remove_emails,
                 _remove_url, 
                 _remove_mention, 
                 _remove_duplicate_char,
                 _remove_single_char, 
                 _remove_special_character, 
                 _remove_new_line_char, 
                 _remove_number, 
                 _remove_html_tags, 
                 _remove_longest_than, 
                 _remove_whitespace, 
                 _remove_unicode_characters,
                 _stemmer, 
                 _remove_non_english, 
                 _remove_stop_words, 
                 _lemmatizer):
        
        self._string_lower = _string_lower
        self._remove_emojis = _remove_emojis
        self._remove_hashtags = _remove_hashtags
        self._remove_emails = _remove_emails
        self._remove_url = _remove_url
        self._remove_mention = _remove_mention
        self._remove_duplicate_char = _remove_duplicate_char
        self._remove_single_char = _remove_single_char
        self._remove_special_character = _remove_special_character 
        self._remove_new_line_char = _remove_new_line_char
        self._remove_number = _remove_number
        self. _remove_html_tags = _remove_html_tags
        self._remove_longest_than = _remove_longest_than
        self._remove_whitespace = _remove_whitespace
        self._remove_unicode_characters = _remove_unicode_characters
        self._stemmer = _stemmer
        self._remove_non_english = _remove_non_english
        self._remove_stop_words = _remove_stop_words
        self._lemmatizer = _lemmatizer
        

    def string_lower(self,text):
        text = str(text)
        text = text.lower()
        return text

    def remove_emojis(self,text):
        "Remove All Emojis From Text"
        text = emoji.replace_emoji(text, replace="")
        return text

    def remove_hashtags(self,text):
        "Remove All Hashtags From Text"
        text =  re.sub("#[ا-ي٠-٩a-zA-Z0-9]+","", text)
        return text   

    def remove_emails(self,text):
        "Remove All Emails From Text"
        text = re.sub("[a-zA-Z0-9-_.]+@[a-zA-Z]+.[a-zA-Z]+","", text)  
        return text    

    def remove_url(self,text):
        "Remove All URL From Text"
        text = re.sub(r'http\S+', '', text, flags=re.MULTILINE)
        return text

    def remove_mention(self,text):
        "Remove All Mention From Text"
        text = re.sub("@[ا-ي٠-٩a-zA-Z0-9]+","", text)
        return text

    def remove_duplicate_char(self,text):
        "Remove Chars Word Has More Than 2 Same Following Char"
        text = re.sub(r'(.)\1+', r'\1\1', text)
        return text

    def remove_single_char(self,text):
        "Remove Alone Chars From Text"
        text = ' '.join( [w for w in text.split() if len(w)>1] )
        return text

    def remove_html_tags(self,text):
        "Remove All HTL Tags From Text"
        text = re.sub("<.*?>", ' ', text)
        return text

    def remove_special_character_(self,text):
        "Remove Special Character From Text"
        Punctuations = '`؛،؟.,«»÷-' + string.punctuation
        for punctuation in Punctuations:
            text = text.replace(punctuation, ' ')
        return text   

    def remove_new_line_char(self,text):
        "Remove New Line Symbols From Text"
        text = text.replace('\n', ' ')
        return text  
    
    def remove_number(self,text):
        "Remove All Number From Text"
        text = re.sub(r'\d+', '', text)
        return text

    def remove_longest_than_(self,text):
        "Remove All Words That Longest Than The Longest Word In Englis"
        for word in text.split():
            if len(word) >=46:
                text = text.replace(word, '')
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

    def stemmer_(self,text):
        "Lowers Inflection In Words To Their Root Forms"
        stemmer = SnowballStemmer('english')
        text = " ".join([stemmer.stem(word) for word in text.split()])
        return text

    def remove_non_english(self,text):
        "Remove Non English Word And Char"
        char = set(string.printable)
        for c in text:
            if c not in char:
                text = text.replace(c, ' ')
        return text

    def remove_stop_words(self,text):
        "Remove StopWords From Text"
        StopWords1 = set(stopwords.words('english'))
        stop = open('EnglishStopWords.txt','r')
        StopWords2 = set(stop.read().split('\n'))
        stop.close()
        StopWords = StopWords1.union(StopWords2)
        text = word_tokenize(text)
        text = [word for word in text if word not in StopWords]
        return ' '.join(text)

    def lemmatizer_(self,text):
        "Lowers Inflection In Words To Their Root Forms"
        lemmatizer = WordNetLemmatizer()
        text = " ".join([lemmatizer.lemmatize(word, pos='v') for word in text.split()])
        return text
    
    def normalization(self, text):
        if self._string_lower == True:
            text = self.string_lower(text)
        if self._remove_emojis == True :
            text = self.remove_emojis(text)
        if self._remove_hashtags == True:
            text = self.remove_hashtags(text)
        if self._remove_emails == True:
            text = self.remove_emails(text)
        if self._remove_url == True:
            text = self.remove_url(text)
        if self._remove_mention == True:
            text =self.remove_mention(text)
        if self._remove_duplicate_char == True:
            text = self.remove_duplicate_char(text)
        if self._remove_single_char == True:
            text = self.remove_single_char(text)
        if  self._remove_html_tags == True:
            text = self.remove_html_tags(text)
            
        if self._remove_special_character == True:
            text = self.remove_special_character_(text)
        if self._remove_new_line_char == True:
            text = self.remove_new_line_char(text)
        if self._remove_number == True:
            text = self.remove_number(text)
        if self._remove_longest_than==True:
            text = self.remove_longest_than_(text)
        if self._remove_whitespace == True:
            text = self.remove_whitespace(text)
        if self._remove_unicode_characters == True:
            text = self.remove_unicode_characters_(text)
        if self._stemmer == True:
            text = self.stemmer_(text)
        if self._remove_non_english == True:
            text = self.remove_non_english(text)
        if self._remove_stop_words == True:
            text = self.remove_stop_words(text)
        if self._lemmatizer == True:
            text = self.lemmatizer_(text)
        return ''.join(text)