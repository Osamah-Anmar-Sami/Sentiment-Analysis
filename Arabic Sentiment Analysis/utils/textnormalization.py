import re
import pandas as pd

class Text_Normalization:
        def __init__(self, 
                    remove_emojis,
                    remove_hashtags,
                    remove_url,
                    remove_mention,
                    remove_html_tags,
                    remove_new_line_char,
                    remove_english_letter,
                    remove_hindi_letter,
                    remove_urdu_letter,
                    remove_sindhi_letter,
                    remove_hebrew_letter,
                    remove_latin_letter,
                    remove_unwanted_char,
                    remove_arabic_diacritics,
                    remove_arabic_tatweel,
                    convert_gaf,
                    convert_pe,
                    convert_che,
                    convert_ve,
                    convert_alef,
                    convert_alef_maqsura,
                    convert_teh_marbuta,
                    convert_ayin,
                    convert_la,
                    convert_kurdish_waw,
                    remove_punctuations,
                    normalize_arabic_unicode,
                    remove_unicode_and_special_character,
                    remove_stop_words,
                    remove_number,
                    remove_longest_than,
                    remove_duplicate_word,
                    remove_single_letter,
                    remove_duplicated_letter,
                    remove_whitespace):
                    
                    self.remove_emojis = remove_emojis
                    self.remove_hashtags = remove_hashtags
                    self.remove_url = remove_url
                    self.remove_mention = remove_mention
                    self.remove_html_tags = remove_html_tags
                    self.remove_new_line_char = remove_new_line_char
                    self.remove_english_letter = remove_english_letter
                    self.remove_hindi_letter = remove_hindi_letter
                    self.remove_urdu_letter = remove_urdu_letter
                    self.remove_sindhi_letter = remove_sindhi_letter
                    self.remove_hebrew_letter = remove_hebrew_letter
                    self.remove_latin_letter = remove_latin_letter
                    self.remove_unwanted_char = remove_unwanted_char
                    self.remove_arabic_diacritics = remove_arabic_diacritics
                    self.remove_arabic_tatweel = remove_arabic_tatweel
                    self.convert_gaf = convert_gaf
                    self.convert_pe = convert_pe
                    self.convert_che = convert_che
                    self.convert_ve = convert_ve
                    self.convert_alef = convert_alef
                    self.convert_alef_maqsura = convert_alef_maqsura
                    self.convert_teh_marbuta = convert_teh_marbuta
                    self.convert_ayin = convert_ayin
                    self.convert_la = convert_la
                    self.convert_kurdish_waw = convert_kurdish_waw
                    self.remove_punctuations = remove_punctuations
                    self.normalize_arabic_unicode = normalize_arabic_unicode
                    self.remove_unicode_and_special_character = remove_unicode_and_special_character
                    self.remove_stop_words = remove_stop_words
                    self.remove_number = remove_number
                    self.remove_longest_than = remove_longest_than
                    self.remove_duplicate_word = remove_duplicate_word
                    self.remove_single_letter = remove_single_letter
                    self.remove_duplicated_letter = remove_duplicated_letter
                    self.remove_whitespace = remove_whitespace


        def text_normalization(self, text):
                text = text.replace("\U00011e27", " ")
                if self.remove_emojis == True:
                        text = self.remove_emojis_(text)
                if self.remove_hashtags == True:
                        text = self.remove_hashtags_(text)
                if self.remove_url == True:
                        text = self.remove_url_(text)
                if self.remove_mention == True:
                        text = self.remove_mention_(text)
                if self.remove_html_tags == True:
                        text = self.remove_html_tags_(text)
                if self.remove_new_line_char == True:
                        text = self.remove_new_line_char_(text)
                if self.remove_english_letter == True:
                        text = self.remove_english_letter_(text)
                if self.remove_hindi_letter == True:
                        text = self.remove_hindi_letter_(text)
                if self.remove_urdu_letter == True:
                        text = self.remove_urdu_letter_(text)
                if self.remove_sindhi_letter == True:
                        text = self.remove_sindhi_letter_(text)
                if self.remove_hebrew_letter == True:
                        text = self.remove_hebrew_letter_(text)
                if self.remove_latin_letter == True:
                        text = self.remove_latin_letter_(text)
                if self.remove_unwanted_char == True:
                        text = self.remove_unwanted_char_(text)
                if self.remove_arabic_diacritics == True:
                        text = self.remove_arabic_diacritics_(text)
                if self.remove_arabic_tatweel == True:
                        text = self.remove_arabic_tatweel_(text)
                if self.convert_gaf == True:
                        text = self.convert_gaf_(text)
                if self.convert_pe == True:
                        text = self.convert_pe_(text)
                if self.convert_che == True:
                        text = self.convert_che_(text)
                if self.convert_ve == True:
                        text = self.convert_ve_(text)
                if self.convert_alef == True:
                        text = self.convert_alef_(text)
                if self.convert_alef_maqsura == True:
                        text = self.convert_alef_maqsura_(text)
                if self.convert_teh_marbuta == True:
                        text = self.convert_teh_marbuta_(text)
                if self.convert_ayin == True:
                        text = self.convert_ayin_(text)
                if self.convert_la == True:
                        text = self.convert_la_(text)
                if self.convert_kurdish_waw == True:
                        text = self.convert_kurdish_waw_(text)
                if self.remove_punctuations == True:
                        text = self.remove_punctuations_(text)
                if self.normalize_arabic_unicode_ == True:
                        text = self.normalize_arabic_unicode_(text)
                if self.remove_unicode_and_special_character == True:
                        text = self.remove_unicode_and_special_character_(text)
                if self.remove_stop_words == True:
                        text = self.remove_stop_words_(text)
                if self.remove_number == True:
                        text = self.remove_number_(text)
                if self.remove_longest_than == True:
                        text = self.remove_longest_than_(text)
                if self.remove_duplicate_word == True:
                        text = self.remove_duplicate_word_(text)
                if self.remove_single_letter == True:
                        text = self.remove_single_letter_(text)
                if self.remove_duplicated_letter == True:
                        text = self.remove_duplicated_letter_(text)
                if self.remove_whitespace == True:
                        text = self.remove_whitespace_(text)
                return text
            

        def remove_emojis_(self,text):
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

        def remove_hashtags_(self,text):
                """remove all hashtags from text
                        Args:
                            text (string): input text containing hashtags to be removed
                        Returns:
                            string: text without any hashtags
                """   
                text =  re.sub("#[ٱأإٲٳٵآ-ي٠-٩a-zA-Z0-9]+"," ", text)
                return text   

        def remove_emails_(self,text):
                """
                remove all email address from text
                        Args:
                            text (string): input text containing email address to be removed

                        Returns:
                            string: text without any email address
                """   
                text = re.sub("[a-zA-Z0-9-_.]+@[a-zA-Z]+.[a-zA-Z]+"," ", text)  
                return text

        def remove_url_(self,text):
                """remove all URL from text
                        Args:
                            text (string): input text containing URL address to be removed
                        Returns:
                            string: text without any URL address
                """ 
                text = re.sub(r'http\S+', ' ', text, flags=re.MULTILINE)
                return text

        def remove_mention_(self,text):
                """remove all mention from text
                        Args:
                            text (string): input text containing mention to be removed

                        Returns:
                            string: text without any mention
                """   
                text = re.sub("@[ٱأإٲٳٵآ-ي٠-٩a-zA-Z0-9]+"," ", text)
                return text

        def remove_html_tags_(self,text):
                """remove all html tags from text
                        Args:
                            text (string): input text containing html tags to be removed

                        Returns:
                            string: text without any html tags
                """ 
                text = re.sub("<.*?>", ' ', text)
                return text

        def remove_new_line_char_(self,text):
                """
                remove new line character from text
                        Args:
                            text (string): input text containing new line character to be removed

                        Returns:
                            string: text without any new line character 
                """     
                Pattern = r'[\u000A\u000D]'
                text = re.sub(Pattern, ' ', text)
                return text

        def remove_english_letter_(self,text):
                """remove english words in a given text

                        Args:
                            text (string): input text containing english words.

                        Returns:
                            string: text without any english words
                """    
                text = re.sub('[A-Za-z]', "  ", text)
                return text

        def remove_hindi_letter_(self,text):
                """remove Hindi lettter from the text

                        Args:
                            text (string): input text contining Hindi letter

                        Returns:
                            text: text without Hindi letter
                """
                text = re.sub("[\u0900-\u097F]", " ", text)
                return text

        def remove_urdu_letter_(self,text):
                """remove Urdu lettter from the text

                        Args:
                            text (string): input text contining Urdu letter

                        Returns:
                            text: text without Urdu letter
                """
                pattern = "[\uFBAF\uFBB1\u0679\u067E\u0686\u0688\u0691\u0698\u06D2\u06D3\u06F5\u06F6\u076D\u069C\u0678]"
                text = re.sub(pattern, " ", text)
                return text

        def remove_sindhi_letter_(self,text):
            """Remove Sindhi letters from the text.

            Args:
                text (string): Input text containing Sindhi letters.

            Returns:
                string: Text without Sindhi letters.
            """
            pattern = r"[\u06FE\u06FD\u067A\u067B\u067D\u067E\u067F\u0680\u0683\u0684\u0686\u0687\u068A\u068C\u068D\u068F\u0699\u06A6\u06A9\u06AA\u06AF\u06B1\u06B3\u06BB]"
            text = re.sub(pattern, " ", text)  
            return text

        def remove_hebrew_letter_(self,text):
                """remove Hebrew lettter from the text

                        Args:
                            text (string): input text contining Hebrew letter

                        Returns:
                            text: text without Hebrew letter
                """
                pattern = "[\u0590-\u05FF]"
                text = re.sub(pattern, " ", text)
                return text

        def remove_latin_letter_(self,text):
                """remove Latin lettter from the text

                        Args:
                            text (string): input text contining Latin letter

                        Returns:
                            text: text without Latin letter
                """
                text = re.sub("[ößàħüéèôäïêç]", " ", text)
                return text

        def remove_unwanted_char_(self,text):
                """remove Unwanted char from the text

                        Args:
                            text (string): input text contining Unwanted char

                        Returns:
                            text: text without Unwanted char
                """
                text = re.sub("[눇ﻣ̲ﻥ̴ ٰھہノ§ヾ̯͡ ڼίɴ ٔ ٕﭿ눉مٓـ]", " ", text)
                return text

        def remove_arabic_diacritics_(self,text):
                """removes diacritics (harakat) from Arabic text
                            Args:
                                    text (string): the Arabic text to remove diacritics from

                            Returns:
                                    string: the modified text without diacritics
                """
                pattern = r'[\u0618\u0619\\u061A\u064B\u064C\u064D\u064E\u064F\u0650\u0651\u0652\u0653\u00AB\u00B7\uFDFC\u0651]+'
                text = re.sub(pattern, ' ', text)
                return text


        def remove_arabic_tatweel_(self,text):
                """remove Arabic Tatweel
                            Args:
                                text (string): text with Arabic Tatweel
                            Returns:
                                text after removing Arabic Tatweel
                """
                text = re.sub('[\u0640]', '', text)
                return text

        def convert_gaf_(self,text):
                """converts Gaf (گ) to Kaph (ك) in Arabic text.
                        Args:
                            text (string): the Arabic text to convert

                        Returns:
                            string: the modified text with Gaf replaced by Kaf
                """
                text = re.sub("گ", "ك", text)
                return text

        def convert_pe_(self,text):
                """converts Pe (پ) to  Bet (ب) in Arabic text.
                    Args:
                            text (string): the Arabic text to convert
                        Returns:
                            string: the modified text with Pe replaced by Kaf
                """
                text = re.sub("پ", "ب", text)
                return text


        def convert_che_(self,text):
                """converts Che (چ) to Gimel (ج) in Arabic text.
                        Args:
                            text (string): the Arabic text to convert

                        Returns:
                            string: the modified text with Che replaced by Kaf
                """
                text = re.sub("چ", "ج", text)
                return text


        def convert_ve_(self,text):
                """converts Ve (ﭪ) to  Fa (ف) in Arabic text.
                    Args:
                            text (string): the Arabic text to convert
                        Returns:
                            string: the modified text with Ve replaced by Fa
                """
                text = re.sub("ڤ", "ف", text)
                return text

        def convert_alef_(self,text):
                """
                        converts various Alef representations (including Alef with Hamza Above/Below, Alef with Madda Above, etc.) to the basic Alef ('ا') in Arabic text

                            Args:
                                    text (string): the Arabic text to convert

                        Returns:
                                    string: the modified text with all Alef variants replaced by the basic Alef
                """
                text = re.sub("[ٱأإٲٳٵآﺂ]+", "ا", text)
                return text

        def convert_alef_maqsura_(self,text):
                """converts Alef Maksura (ﻰ,ﱝ,ۍ) to (ى) in Arabic text

                        Args:
                            text (string): the Arabic text to convert

                        Returns:
                            string: the modified text with Alef Maksura replaced by (ى)
                """
                text = text = re.sub("[ﻰﱝۍ]", "ى", text)
                return text

        def convert_teh_marbuta_(self,text):
                """converts Teh Marbuta (ة) to Heh (ه) in Arabic text.
                        Args:
                            text (string): the Arabic text to convert

                        Returns:
                            string: the modified text with Teh Marbuta replaced by Heh
                """
                text = re.sub("ة", "ه", text)
                return text

        def convert_ayin_(self,text):
                """converts Ayin (؏) to (ع) in Arabic text.
                        Args:
                            text (string): the Arabic text to convert

                        Returns:
                            string: the modified text with ayin
                """
                text = re.sub("؏", "ع", text)
                return text

        def convert_la_(self,text):
                """converts La (لآلألإ) to (لا) in Arabic text.
                        Args:
                            text (string): the Arabic text to convert

                        Returns:
                            string: the modified text with La
                """
                text = re.sub("[\uFEF5\uFEF7\uFEF9]", "\uFEFB", text)
                text = re.sub("[\uFEF6\uFEF8\uFEFA]", "\uFEFC", text)
                text = re.sub('لﻻ', 'للا', text)
                return text

        def convert_kurdish_waw_(self,text):
                """converts Kurdish Waw (ۆ) to Waw (و) in Arabic text.
                        Args:
                            text (string): the Arabic text to convert

                        Returns:
                            string: the modified text with Che replaced by Kaf
                """
                text = re.sub("ۆ", "و", text)
                return text

        def remove_punctuations_(self,text):
                """remove punctuation from the text
                        Args:
                            text (string): input text contining punctuation

                        Returns:
                            text: text without punctuation
                """         
                Punctuation  = '''`”؛،؟¿¡۔，.,-!"\“'()-./٬:;?[]^_`{}'''
                for punctuation in Punctuation:
                        text = text.replace(punctuation, ' ')
                return text

        def normalize_arabic_unicode_(self,text):
                """
                    Normalize Arabic Unicode characters in the given text.

                    Parameters:
                        text (str): The input text containing Arabic Unicode characters to normalize.

                    Returns:
                        str: The normalized text with Arabic Unicode characters replaced by their corresponding phrases.

                """
                arabic_unicode = [(r'ﷺ', 'صلى الله عليه و سلم'),
                                    (r'ﷻ', 'جل جلاله'),
                                    (r'﷽', 'بسم الله الرحمن الرحيم')]

                for unicode, word in arabic_unicode:
                        text = re.sub(unicode, word, text)
                return text 

        def remove_unicode_and_special_character_(self,text):
                """remove special and unicode characters from the text
                        Args:
                            text (string): input text contining special characters

                        Returns:
                            text: text without special characters
                """          
                Pattern = r'[\u2000-\u206F\u2460-\u24FF\u2070-\u218F\u2022-\u221E\u0E3F\u00A9\u00AE\u2117\u2120\u03B1-\u03C9\u0391-\u039F\u00BC-\u00BE\u0022-\u0027\u002A\u002B\u002F\u003C-\u003E\u0040\u005C\u005E\u0060\u007C\u007E\u00BC-\u00BE\u066A\u250A-\u25FF\u2B07\u02DB\u00A3\u0328\u300A\u300B\u00B2\uFF3E\u00B0\u032C\u0329\u0303\u030A\u0300-\u036F\u00BB\u200D\u0337\u0334\u032C\u0329\u0303\u030A\uFE0F]'
                text = re.sub(Pattern, ' ', text)
                return text

        def remove_stop_words_(self,text):
                """remove all stopword from text
                        Args:
                            text (string): input text containing stopwords

                        Returns:
                            string: text without stopwords
                """  
                stop = open('ArabicStopWord.txt','r', encoding='Utf-8')
                StopWords = set(stop.read().split('\n'))
                stop.close()
                text = text.split()
                text =' '.join(word for word in text if word not in StopWords)
                return text
                    
        def remove_number_(self,text):
                """remove numbers from the text

                        Args:
                            text (string): input text contining numbers

                        Returns:
                            text: text without numbers
                """
                text = re.sub(r'\d+', ' ', text)
                return text
        def remove_longest_than_(self,text):
                """remove words that has length more than the longest word in arabic from the text

                        Args:
                            text (string): input text contining words that has length more than the longest word in arabic

                        Returns:
                            text: text without words that has length more than the longest word in arabic
                """ 
                for word in text.split():
                        if len(word) >=16:
                                text = text.replace(word, ' ')
                return text
        def remove_duplicate_word_(self, text):
                """remove consecutive duplicate words in a given text

                        Args:
                            text (string): input text containing duplicate words separated by spaces.

                        Returns:
                            string: text without any duplicate words
                """          ""
                pattern = r'\b(\w+)(\s+)(\1+)\b'
                text = re.sub(pattern, r'\1', text)
                return text

        def remove_single_letter_(self,text):
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

        def remove_duplicated_letter_(self,text):
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

        def remove_whitespace_(self,text):
                """remove extra whitespaces at the beginning and end of the text

                        Args:
                            text (text): input text contating extra whitespaces

                        Returns:
                            string: text without extra whitespaces
                """  
                text = re.sub('          +', ' ', text)
                text = re.sub(' +', ' ', text)
                text = text.strip()
                return text 