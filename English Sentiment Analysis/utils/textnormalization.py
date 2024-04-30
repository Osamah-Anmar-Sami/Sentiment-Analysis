import re
from utils.contraction_expand import contractions_
import pandas as pd
import difflib
english_data = set(open('english_data.txt','r').read().split('\n'))
consecutive_repeated_letters = set(open('english_consecutive_repeated_words.txt', 'r').read().split('\n'))
emojis = pd.read_csv('Emojis.csv')

class Text_Normalization:
        def __init__(self, 
                     string_lower,
                     remove_emojis,
                     remove_hashtags,
                     remove_emails,
                     remove_url,
                     remove_mention,
                     remove_html_tags,
                     remove_new_line_char,
                     english_spell_correction,
                     decrease_number_of_consecutive_repeated_letter,
                     remove_duplicate_word,
                     remove_single_letter,
                     remove_duplicated_letter,
                     expand_contractions,
                     remove_stop_words,
                     remove_unicode_and_special_character,
                     remove_punctuations,
                     remove_number,
                     remove_non_english,
                     remove_longest_than,
                     remove_extra_whitespace) :
                
                     self.string_lower = string_lower 
                     self.remove_emojis = remove_emojis
                     self.remove_hashtags = remove_hashtags
                     self.remove_emails = remove_emails
                     self.remove_url = remove_url
                     self.remove_mention = remove_mention
                     self.remove_html_tags = remove_html_tags
                     self.remove_new_line_char = remove_new_line_char
                     self.english_spell_correction = english_spell_correction
                     self.decrease_number_of_consecutive_repeated_letter = decrease_number_of_consecutive_repeated_letter
                     self.remove_duplicate_word = remove_duplicate_word
                     self.remove_single_letter = remove_single_letter
                     self.remove_duplicated_letter = remove_duplicated_letter
                     self.expand_contractions = expand_contractions
                     self.remove_stop_words = remove_stop_words
                     self.remove_unicode_and_special_character = remove_unicode_and_special_character
                     self.remove_punctuations = remove_punctuations
                     self.remove_number = remove_number
                     self.remove_non_english = remove_non_english
                     self.remove_longest_than = remove_longest_than
                     self.remove_extra_whitespace = remove_extra_whitespace


        """
        Initializes the Text_Normalization object with various normalization options.

        Parameters:
        - string_lower: Whether to convert the text to lowercase.
        - remove_emojis: Whether to remove emojis from the text.
        - remove_hashtags: Whether to remove hashtags from the text.
        - remove_emails: Whether to remove email addresses from the text.
        - remove_url: Whether to remove URLs from the text.
        - remove_mention: Whether to remove mentions (e.g., @username) from the text.
        - remove_html_tags: Whether to remove HTML tags from the text.
        - remove_new_line_char: Whether to remove newline characters from the text.
        - english_spell_correction: Whether to perform English spell correction.
        - decrease_number_of_consecutive_repeated_letter: Whether to decrease the number of consecutive repeated letters.
        - remove_duplicate_word: Whether to remove duplicate words from the text.
        - remove_single_letter: Whether to remove single-letter words from the text.
        - remove_duplicated_letter: Whether to remove duplicated letters within words.
        - expand_contractions: Whether to expand contractions (e.g., can't to cannot).
        - remove_stop_words: Whether to remove stop words from the text.
        - remove_unicode_and_special_character: Whether to remove Unicode and special characters from the text.
        - remove_punctuations: Whether to remove punctuation marks from the text.
        - remove_number: Whether to remove numerical digits from the text.
        - remove_non_english: Whether to remove non-English characters from the text.
        - remove_longest_than: Whether to remove words longer than a specified length from the text.
        - remove_extra_whitespace: Whether to remove extra whitespace from the text.
        """
        
        def text_normalization(self, text):
                if self.string_lower == True:
                        text = self.string_lower_(text)
                if self.remove_emojis == True:
                        text = self.delete_emojis(text)
                if self.remove_hashtags == True:
                        text = self.delete_hashtags(text)
                if self.remove_emails == True:
                        text = self.delete_emails(text)
                if self.remove_url == True:
                        text = self.delete_url(text)
                if self.remove_mention == True:
                        text = self.delete_mention(text)
                if self.remove_html_tags == True:
                        text = self.delete_html_tags(text)
                if self.remove_new_line_char == True:
                        text = self.delete_new_line_char(text)
                if self.expand_contractions == True:
                        text = self.expand_contractions_(text)
                if self.remove_duplicate_word == True:
                        text = self.delete_duplicate_word(text)
                if self.remove_single_letter == True:
                        text = self.delete_single_letter(text)
                if self.remove_duplicated_letter == True:
                        text = self.delete_duplicated_letter(text)
                if self.english_spell_correction == True:
                        text = self.english_spell_correction_(text)
                if self.decrease_number_of_consecutive_repeated_letter == True:
                        text = self.decrease_number_of_consecutive_repeated_letter_(text)
                if self.remove_unicode_and_special_character == True:
                        text = self.delete_unicode_and_special_character(text)
                if self.remove_punctuations == True:
                        text = self.delete_punctuations(text)
                if self.remove_stop_words == True:
                        text = self.delete_stop_words(text)
                if self.remove_number == True:
                        text = self.delete_number(text)
                if self.remove_non_english == True:
                        text = self.delete_non_english(text)
                if self.remove_longest_than == True:
                        text = self.delete_longest_than(text)    
                if self.remove_extra_whitespace == True:
                        text = self.delete_extra_whitespace(text)

                return text
                
        def string_lower_(self, text):
                """convert all words into word with lower letter format

                Args:
                    text (str): input text containing words with capital letters

                Returns:
                    string: text containing words with lower letters
                """        ""
                text = str(text)
                text = text.lower()
                return text

        def delete_emojis(self, text):
                """remove all emojis from text

                Args:
                    text (string): input text containing emoijis to be removed

                Returns:
                    string: text without any emojis
                """ 
                for emoji in text:
                    if emoji in emojis.values:
                        text = text.replace(emoji, ' ')
                return text

        def delete_hashtags(self, text):
                """remove all hashtags from text

                Args:
                    text (string): input text containing hashtags to be removed

                Returns:
                    string: text without any hashtags
                """        
                text =  re.sub("#[ا-ي٠-٩a-zA-Z0-9]+","", text)
                return text   

        def delete_emails(self, text):
                """remove all email address from text

                Args:
                    text (string): input text containing email address to be removed

                Returns:
                    string: text without any email address
                """        ""
                text = re.sub("[a-zA-Z0-9-_.]+@[a-zA-Z]+.[a-zA-Z]+"," ", text)  
                return text 

        def delete_url(self, text):
                """remove all URL from text

                Args:
                    text (string): input text containing URL address to be removed

                Returns:
                    string: text without any URL address
                """        " "
                text = re.sub('http\S+', ' ', text)
                text = re.sub('www.+', ' ', text)
                return text

        def delete_mention(self, text):
                """remove all mention from text

                Args:
                    text (string): input text containing mention to be removed

                Returns:
                    string: text without any mention
                """        ""
                text = re.sub("@[ا-ي٠-٩a-zA-Z0-9]+"," ", text)
                return text

        def delete_html_tags(self, text):
                """remove all html tags from text

                Args:
                    text (string): input text containing html tags to be removed

                Returns:
                    string: text without any html tags
                """       
                text = re.sub("<.*?>", ' ', text)
                return text

        def delete_new_line_char(self, text):
                """delete new line character from text

                Args:
                    text (string): input text containing new line character to be removed

                Returns:
                    string: text without any new line character 
                """     
                Pattern = r'[\u000D\u000A]'
                text = re.sub(Pattern, ' ', text)
                return text
        
        def delete_unicode_and_special_character(self, text):
                """remove special and unicode characters from the text

                Args:
                    text (string): input text contining special characters

                Returns:
                    text: text without special characters
                """          
                Pattern = r'[\u2460-\u24FF\u2070-\u218F\u2022-\u221E\u0E3F\u00A9\u00AE\u2117\u2120\u03B1-\u03C9\u0391-\u039F\u00BC-\u00BE\u0022-\u0027\u002A\u002B\u002F\u003C-\u003E\u0040\u005C\u005E\u0060\u007C\u007E\u00BC-\u00BE]'
                text = re.sub(Pattern, ' ', text)
                return text
        
        def delete_number(self, text):
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
                # pattern = re.compile(r'[^a-zA-Z\s]')
                # text = re.sub(pattern, '', text)
                
                
                punctuation = "{}_!-?.:؛;""''()،؟,..[\]"
                text =  ' '.join(word for word in text.split() if word in english_data or word in punctuation or word.isnumeric() == True)
                return text

        def delete_longest_than(self, text):
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
            
        def english_spell_correction_(self, text):
            """correct spelloing of english words

                Args:
                    text (string): input text containing word with wrong spelling

                Returns:
                    string: text with correct spelling
                """         
            
            corrected_word = []
            for word in text.split():
                    if word in english_data:
                            corrected_word.append(word)
                    else:
                            match = difflib.get_close_matches(word, english_data, n=1, cutoff=0.7)
                            corrected_word.append(match[0] if match else word)
                            text = ' '.join(corrected_word)
            return text

        def decrease_number_of_consecutive_repeated_letter_(self, text):
                """decrease number consecutive characters repeated more than 2 times in a each word for given text

                Args:
                    text (string): input text containing repeated characters


                Returns:
                    string: text without characters repeated more than 2 times
                """
                
                result = []
                for word in text.split():
                    word = re.sub(r'(.)\1+', r'\1\1', word)
                    if word not in consecutive_repeated_letters:
                        word = re.sub(r'(.)\1+', r'\1', word) 
                    result.append(word)
                    text = ' '.join(result)
                return text

        def delete_duplicate_word(self, text):
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

        def expand_contractions_(self, text):
                """replace contracted forms with their expanded equivalents.

                Args:
                    text (string): input text containing contractions

                Returns:
                    string: text with contractions expanded to their full forms
                """          ""
                text = contractions_(text)
                return text
            
        def delete_stop_words(self, text):
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

        def delete_punctuations(self, text):
                """remove punctuation from the text

                Args:
                    text (string): input text contining punctuation

                Returns:
                    text: text without punctuation
                """         
                Punctuation  = '''`؛،؟.,-!"\'(),-./:;?[]^_`{}'''
                for punctuation in Punctuation:
                    text = text.replace(punctuation, ' ')
                return text

        def delete_extra_whitespace(self, text):
                """remove extra whitespaces at the beginning and end of the text

                Args:
                    text (text): input text contating extra whitespaces

                Returns:
                    string: text without extra whitespaces
                """          ""
                text = text.strip()
                return text 
