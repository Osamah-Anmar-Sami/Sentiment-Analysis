import re
from utils.contraction_expand import contractions_
import pandas as pd
import string



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
                     remove_duplicate_word,
                     remove_single_letter,
                     remove_duplicated_letter,
                     expand_contractions,
                     remove_stop_words,
                     remove_unicode_and_special_character,
                     remove_non_english,
                     remove_punctuations,
                     remove_number,
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
                     self.remove_duplicate_word = remove_duplicate_word
                     self.remove_single_letter = remove_single_letter
                     self.remove_duplicated_letter = remove_duplicated_letter
                     self.expand_contractions = expand_contractions
                     self.remove_stop_words = remove_stop_words
                     self.remove_unicode_and_special_character = remove_unicode_and_special_character
                     self.remove_non_english = remove_non_english
                     self.remove_punctuations = remove_punctuations
                     self.remove_number = remove_number
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
                if self.remove_unicode_and_special_character == True:
                        text = self.delete_unicode_and_special_character(text)
                if self.remove_non_english == True:
                        text = self.delete_non_english(text)
                if self.remove_punctuations == True:
                        text = self.delete_punctuations(text)
                if self.remove_stop_words == True:
                        text = self.delete_stop_words(text)
                if self.remove_number == True:
                        text = self.delete_number(text)
                if self.remove_longest_than == True:
                        text = self.delete_longest_than(text)    
                if self.remove_extra_whitespace == True:
                        text = self.delete_extra_whitespace(text)

                return text
                
        def string_lower_(self, text):
                """
                Converts the input text to lowercase.

                Parameters:
                    text (str): The input text to be converted to lowercase.

                Returns:
                    str: The input text converted to lowercase.
                """
                text = str(text)
                text = text.lower()
                return text

        def delete_emojis(self,text):
            """
            Remove emojis from the given text.

            This function reads a list of emojis from a CSV file named 'Emojis.csv' 
            and removes any occurrences of these emojis from the input text.

            Args:
                text (str): The input text from which emojis need to be removed.

            Returns:
                str: The text with emojis removed.
            """
            emojis = set(pd.read_csv('Emojis.csv')['Emojis'])
            text = [word for word in text if word not in emojis]
            return ''.join(text)

        def delete_hashtags(self, text):   
                """
                Remove hashtags from the given text.

                This method uses a regular expression to find and remove all hashtags
                from the input text. Hashtags are defined as any sequence of characters
                starting with the '#' symbol, followed by Arabic letters (ا-ي), Arabic 
                numerals (٠-٩), English letters (a-z, A-Z), or English numerals (0-9).

                Args:
                    text (str): The input text from which hashtags need to be removed.

                Returns:
                    str: The text with all hashtags removed.
                """
                text =  re.sub("#[ا-ي٠-٩a-zA-Z0-9]+","", text)
                return text   

        def delete_emails(self, text):
                """
                Remove email addresses from the given text.

                This function uses a regular expression to find and replace email addresses
                in the input text with a space.

                Args:
                    text (str): The input text from which email addresses need to be removed.

                Returns:
                    str: The text with email addresses removed.
                """
                text = re.sub("[a-zA-Z0-9-_.]+@[a-zA-Z]+.[a-zA-Z]+"," ", text)  
                return text 

        def delete_url(self, text):
                """
                Remove URLs from the given text.

                This method uses regular expressions to find and replace URLs starting with 'http' or 'www' with a space.

                Args:
                    text (str): The input text from which URLs need to be removed.

                Returns:
                    str: The text with URLs removed.
                """
                text = re.sub('http\S+', ' ', text)
                text = re.sub('www.+', ' ', text)
                return text

        def delete_mention(self, text):
                """
                Remove mentions from the given text.

                This function uses a regular expression to find and remove all mentions
                (words starting with '@') from the input text. Mentions can include 
                Arabic characters, English letters, and digits.

                Args:
                    text (str): The input text from which mentions need to be removed.

                Returns:
                    str: The text with mentions removed.
                """
                text = re.sub("@[ا-ي٠-٩a-zA-Z0-9]+"," ", text)
                return text

        def delete_html_tags(self, text):    
                """
                Remove HTML tags from the given text.

                Args:
                    text (str): The input string containing HTML tags.

                Returns:
                    str: The text with HTML tags removed.
                """
                text = re.sub("<.*?>", ' ', text)
                return text

        def delete_new_line_char(self, text):    
                """
                Removes newline characters from the given text.

                This method replaces all occurrences of carriage return (\u000D) and line feed (\u000A) characters
                with a space in the provided text.

                Args:
                    text (str): The input text from which newline characters need to be removed.

                Returns:
                    str: The text with newline characters replaced by spaces.
                """
                Pattern = r'[\u000D\u000A]'
                text = re.sub(Pattern, ' ', text)
                return text
        
        def delete_unicode_and_special_character(self, text):    
                """
                Remove unicode and special characters from the given text.

                This function uses a regular expression pattern to identify and replace
                a range of unicode and special characters with a space.

                Args:
                    text (str): The input text from which unicode and special characters
                                need to be removed.

                Returns:
                    str: The text with unicode and special characters replaced by spaces.
                """
                Pattern = r'[\u2460-\u24FF\u2070-\u218F\u2022-\u221E\u0E3F\u00A9\u00AE\u2117\u2120\u03B1-\u03C9\u0391-\u039F\u00BC-\u00BE\u0022-\u0027\u002A\u002B\u002F\u003C-\u003E\u0040\u005C\u005E\u0060\u007C\u007E\u00BC-\u00BE\x96]'
                text = re.sub(Pattern, ' ', text)
                return text
        
        def delete_number(self, text):
                """
                Remove all numeric characters from the given text.

                Args:
                    text (str): The input string from which numeric characters are to be removed.

                Returns:
                    str: The text with all numeric characters removed.
                """
                text = re.sub(r'\d+', '', text)
                return text

        def delete_non_english(self,text):
                """
                Remove non-English characters from the input text.

                This function filters out any characters that are not part of the English alphabet,
                digits, or common punctuation marks. It splits the input text into words and retains
                only those words that consist entirely of English letters, digits, or punctuation.

                Args:
                    text (str): The input text to be normalized.

                Returns:
                    str: The normalized text containing only English letters, digits, and punctuation.
                """
                pattern = re.compile(r'[^a-zA-Z0-9\s' + re.escape(string.punctuation) + ']')
                text = re.sub(pattern, ' ', text)
                return text

        def delete_longest_than(self, text):
                """
                Removes words from the input text that are longer than or equal to 46 characters.

                Args:
                    text (str): The input text from which long words need to be removed.

                Returns:
                    str: The text with words longer than or equal to 46 characters removed.
                """
                for word in text.split():
                    if len(word) >=46:
                        text = text.replace(word, '')
                return text

        def delete_duplicate_word(self, text):
                """
                Remove consecutive duplicate words from the given text.

                Args:
                    text (str): The input string from which duplicate words need to be removed.

                Returns:
                    str: The text with consecutive duplicate words removed.
                """
                pattern = r'\b(\w+)(\s+)(\1+)\b'
                text = re.sub(pattern, r'\1', text)
                return text
            
        def delete_single_letter(self, text):
                    """
                    Remove single letter words from the given text.

                    This method uses a regular expression to find and remove single letter words 
                    (excluding vowels) from the input text. Both uppercase and lowercase single 
                    letter words are removed.

                    Args:
                        text (str): The input text from which single letter words need to be removed.

                    Returns:
                        str: The text with single letter words removed.
                    """
                    pattern = r"\b([b-dfhj-np-tv-z]|[B-DFHJ-NP-TV-Z])\b(?!\w)"   
                    text = re.sub(pattern, " ", text)
                    return text
            
        def delete_duplicated_letter(self, text):
                    """
                    Remove duplicated consecutive letters in each word of the given text.

                    Args:
                        text (str): The input text from which duplicated letters need to be removed.

                    Returns:
                        str: The text with duplicated consecutive letters removed.
                    """
                    pattern = r"\b([a-zA-Z])\1+\b(?!\w)"  
                    text = re.sub(pattern, " ", text)
                    return text

        def expand_contractions_(self, text):
                """
                Expands contractions in the given text.

                Args:
                    text (str): The input text containing contractions.

                Returns:
                    str: The text with contractions expanded.
                """
                text = contractions_(text)
                return text
            
        def delete_stop_words(self, text):  
                """
                Remove stop words from the given text.

                Args:
                    text (str): The input text from which stop words need to be removed.

                Returns:
                    str: The text with stop words removed.
                """
                StopWords=open('EnglishStopWords.txt','r').read().split('\n')
                text = text.split()
                text = [word for word in text if word not in StopWords]
                return ' '.join(text)

        def delete_punctuations(self, text):       
                """
                Remove punctuations from the given text.

                This method takes a string as input and removes all punctuation characters
                defined in the Punctuation variable, replacing them with a space.

                Args:
                    text (str): The input string from which punctuations need to be removed.

                Returns:
                    str: The text with punctuations replaced by spaces.
                """
                Punctuation  = '''`؛،؟.,-!"\'(),-./:;?[]^_`{}'''
                for punctuation in Punctuation:
                    text = text.replace(punctuation, ' ')
                return text

        def delete_extra_whitespace(self, text):
                """
                remove extra whitespaces at the beginning and end of the text

                    text (str): input text containing extra whitespaces

                    str: text without extra whitespaces
                """
                """remove extra whitespaces at the beginning and end of the text

                Args:
                    text (text): input text contating extra whitespaces

                Returns:
                    string: text without extra whitespaces
                """          ""
                text = text.strip()
                return text 
