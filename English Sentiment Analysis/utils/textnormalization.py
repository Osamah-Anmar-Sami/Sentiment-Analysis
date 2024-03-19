import re
from utils.contraction_expand import contractions_
from utils.remove_emojis import remove_emojis_


def text_normalization(text):
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

            - Removing non-English words.
            - Removing words longer than a specified length.
            - Removing whitespace.
            """
          
          text = string_lower_(text)
          text = delete_emojis(text)
          text = delete_hashtags(text)
          text = delete_emails(text)
          text = delete_url(text)
          text = delete_mention(text)
          text = delete_html_tags(text)
          text = delete_new_line_char(text)
          text = decrease_number_of_consecutive_reapted_letter_(text)
          text = delete_duplicate_word(text)
          text = delete_single_letter(text)
          text = delete_duplicated_letter(text)
          text = delete_number(text)
          text = delete_stop_words(text)
          text = delete_unicode_and_special_character(text)
          text = delete_punctuations(text)
          text = expand_contractions_(text)
          text = delete_non_english(text)
          text = delete_longest_than(text)
          text = delete_whitespace(text)

          return text

def string_lower_(text):
          """convert all words into word with lower letter format

          Args:
              text (str): input text containing words with capital letters

          Returns:
              string: text containing words with lower letters
          """        ""
          text = str(text)
          text = text.lower()
          return text

def delete_emojis(text):
        """remove all emojis from text

          Args:
              text (string): input text containing emoijis to be removed

          Returns:
              string: text without any emojis
        """ 
        text = remove_emojis_(text)
        return text

def delete_hashtags(text):
          """remove all hashtags from text

          Args:
              text (string): input text containing hashtags to be removed

          Returns:
              string: text without any hashtags
          """        
          text =  re.sub("#[ا-ي٠-٩a-zA-Z0-9]+","", text)
          return text   

def delete_emails(text):
          """remove all email address from text

          Args:
              text (string): input text containing email address to be removed

          Returns:
              string: text without any email address
          """        ""
          text = re.sub("[a-zA-Z0-9-_.]+@[a-zA-Z]+.[a-zA-Z]+"," ", text)  
          return text 

def delete_url(text):
          """remove all URL from text

          Args:
              text (string): input text containing URL address to be removed

          Returns:
              string: text without any URL address
          """        " "
          text = re.sub(r'http\S+', ' ', text, flags=re.MULTILINE)
          return text

def delete_mention(text):
          """remove all mention from text

          Args:
              text (string): input text containing mention to be removed

          Returns:
              string: text without any mention
          """        ""
          text = re.sub("@[ا-ي٠-٩a-zA-Z0-9]+"," ", text)
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
          Pattern = r'[\u000D\u000A]'
          text = re.sub(Pattern, ' ', text)
          return text
     

def decrease_number_of_consecutive_reapted_letter_(text):
          """decrease number consecutive characters reapeted more than 2 times in a each word for given text

          Args:
              text (string): input text containing reapeted characters


          Returns:
              string: text without characters reapeted more than 2 times
          """
          text = re.sub(r'(.)\1+', r'\1', text)
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

            pattern = r"\b([b-dfhj-np-tv-z]|[B-DFHJ-NP-TV-Z])\b(?!\w)"   
            text = re.sub(pattern, " ", text)
            return text
     
def delete_duplicated_letter(text):
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

def expand_contractions_(text):
          """replace contracted forms with their expanded equivalents.

          Args:
              text (string): input text containing contractions

          Returns:
              string: text with contractions expanded to their full forms
          """          ""
          text = contractions_(text)
          return text
     
def delete_stop_words(text):
          """remove all stopword from text

          Args:
              text (string): input text containing stopwords

          Returns:
              string: text without stopwords
          """   
          StopWords=open('EnglishStopWords.txt','r').read().split('\n')
          text = text.split()
          text = [word for word in text if word not in StopWords]
          return ' '.join(text)


def delete_unicode_and_special_character(text):
          """remove special and unicode characters from the text

          Args:
              text (string): input text contining special characters

          Returns:
              text: text without special characters
          """          
          Pattern = r'[\u2460-\u24FF\u2070-\u218F\u2022-\u221E\u0E3F\u00A9\u00AE\u2117\u2120\u03B1-\u03C9\u0391-\u039F\u00BC-\u00BE\u0022-\u0027\u002A\u002B\u002F\u003C-\u003E\u0040\u005C\u005E\u0060\u007C\u007E\u00BC-\u00BE]'
          text = re.sub(Pattern, ' ', text)
          return text

     
def delete_punctuations(text):
          """remove punctuation from the text

          Args:
              text (string): input text contining punctuation

          Returns:
              text: text without punctuation
          """         
          Punctuation  = "{}_!-?.:؛;""''()،؟,..[]"
          Punctuations= str.maketrans(' ', ' ', Punctuation)
          text = text.translate(Punctuations)
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

def delete_non_english(text):
        """remove non english words from the text

          Args:
              text (string): input text contining non english words

          Returns:
              text: text without non english words
        """ 
        english_letters = "\u0020-\u007E"
        punctuation = "{}_!-?.:؛;""''()،؟,..[\]"
        pattern = f"[{english_letters}\d{punctuation}]+"
        text =  ' '.join(re.findall(pattern, text))
        return text

def delete_longest_than(text):
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

def delete_whitespace(text):
          """remove extra whitespaces at the beginning and end of the text

          Args:
              text (text): input text contating extra whitespaces

          Returns:
              string: text without extra whitespaces
          """          ""
          text = re.sub(r"\s+", " ", text)
          return text 
