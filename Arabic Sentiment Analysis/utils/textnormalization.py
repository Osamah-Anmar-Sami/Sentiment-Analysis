import re
import pandas as pd

class Text_Normalization:
        """
                A class for performing text normalization tasks to preprocess and clean text data.

                - remove_emojis (bool): Whether to remove emojis from the text.
                - remove_hashtags (bool): Whether to remove hashtags from the text.
                - remove_url (bool): Whether to remove URLs from the text.
                - remove_mention (bool): Whether to remove mentions (@username) from the text.
                - remove_html_tags (bool): Whether to remove HTML tags from the text.
                - remove_new_line_char (bool): Whether to remove newline characters from the text.
                - remove_english_letter (bool): Whether to remove English letters from the text.
                - remove_stop_words (bool): Whether to remove common stop words from the text.
                - remove_al (bool): Whether to remove the Arabic definite article "al".
                - remove_arabic_diacritics (bool): Whether to remove Arabic diacritics.
                - remove_arabic_tatweel (bool): Whether to remove Arabic tatweel (kashida).
                - convert_gaf (bool): Whether to convert the Arabic letter "gaf" to its alternative.
                - convert_pe (bool): Whether to convert the Arabic letter "pe" to its alternative.
                - convert_che (bool): Whether to convert the Arabic letter "che" to its alternative.
                - convert_ve (bool): Whether to convert the Arabic letter "ve" to its alternative.
                - convert_alef (bool): Whether to convert the Arabic letter "alef" to its alternative.
                - convert_alef_maqsura (bool): Whether to convert the Arabic letter "alef maqsura" to its alternative.
                - convert_teh_marbuta (bool): Whether to convert the Arabic letter "teh marbuta" to its alternative.
                - convert_kurdish_rah (bool): Whether to convert the Kurdish letter "rah" to its alternative.
                - convert_ayin (bool): Whether to convert the Arabic letter "ayin" to its alternative.
                - convert_la (bool): Whether to convert the Arabic letter "la" to its alternative.
                - convert_kurdish_tah (bool): Whether to convert the Kurdish letter "tah" to its alternative.
                - convert_kurdish_waw (bool): Whether to convert the Kurdish letter "waw" to its alternative.
                - convert_kurdish_kha (bool): Whether to convert the Kurdish letter "kha" to its alternative.
                - convert_kurdish_ga (bool): Whether to convert the Kurdish letter "ga" to its alternative.
                - remove_greek_letter (bool): Whether to remove Greek letters from the text.
                - remove_mathematical_operators (bool): Whether to remove mathematical operators from the text.
                - remove_cyrillic_letter (bool): Whether to remove Cyrillic letters from the text.
                - remove_latin_letter (bool): Whether to remove Latin letters from the text.
                - remove_currency (bool): Whether to remove currency symbols from the text.
                - remove_punctuations (bool): Whether to remove punctuation marks from the text.
                - remove_number (bool): Whether to remove numbers from the text.
                - remove_longest_than (int): The maximum length of a word to keep in the text.
                - remove_duplicate_word (bool): Whether to remove duplicate words from the text.
                - remove_single_letter (bool): Whether to remove single letters from the text.
                - remove_duplicated_letter (bool): Whether to remove duplicated letters in a word.
                - remove_unwanted_char (bool): Whether to remove unwanted characters from the text.
                - normalize_arabic_unicode (bool): Whether to normalize Arabic unicode characters.
                - remove_unicode_and_special_character (bool): Whether to remove unicode and special characters from the text.
                - remove_whitespace (bool): Whether to remove excessive whitespace from the text.
         """
        def __init__(self, 
                    remove_emojis,
                    remove_hashtags,
                    remove_url,
                    remove_mention,
                    remove_html_tags,
                    remove_new_line_char,
                    remove_english_letter,
                    remove_stop_words,
                    remove_al,
                    remove_arabic_diacritics,
                    remove_arabic_tatweel,
                    convert_gaf,
                    convert_pe,
                    convert_che,
                    convert_ve,
                    convert_alef,
                    convert_alef_maqsura,
                    convert_teh_marbuta,
                    convert_kurdish_rah,
                    convert_ayin,
                    convert_la,
                    convert_kurdish_tah,
                    convert_kurdish_waw,
                    convert_kurdish_kha,
                    convert_kurdish_ga,
                    remove_greek_letter,
                    remove_mathematical_operators,
                    remove_cyrillic_letter,
                    remove_latin_letter,
                    remove_currency,
                    remove_punctuations,
                    remove_number,
                    remove_longest_than,
                    remove_duplicate_word,
                    remove_single_letter,
                    remove_duplicated_letter,
                    remove_unwanted_char,
                    normalize_arabic_unicode,
                    remove_unicode_and_special_character,
                    remove_whitespace):
                    
                self.remove_emojis = remove_emojis
                self.remove_hashtags = remove_hashtags
                self.remove_url = remove_url
                self.remove_mention = remove_mention
                self.remove_html_tags = remove_html_tags
                self.remove_new_line_char = remove_new_line_char
                self.remove_english_letter = remove_english_letter
                self.remove_stop_words = remove_stop_words
                self.remove_al = remove_al
                self.remove_arabic_diacritics = remove_arabic_diacritics
                self.remove_arabic_tatweel = remove_arabic_tatweel
                self.convert_gaf = convert_gaf
                self.convert_pe = convert_pe
                self.convert_che = convert_che
                self.convert_ve = convert_ve
                self.convert_alef = convert_alef
                self.convert_alef_maqsura = convert_alef_maqsura
                self.convert_teh_marbuta = convert_teh_marbuta
                self.convert_kurdish_rah = convert_kurdish_rah
                self.convert_ayin = convert_ayin
                self.convert_la = convert_la
                self.convert_kurdish_tah = convert_kurdish_tah
                self.convert_kurdish_waw = convert_kurdish_waw
                self.convert_kurdish_kha = convert_kurdish_kha
                self.convert_kurdish_ga = convert_kurdish_ga
                self.remove_greek_letter = remove_greek_letter
                self.remove_mathematical_operators = remove_mathematical_operators
                self.remove_cyrillic_letter = remove_cyrillic_letter
                self.remove_latin_letter = remove_latin_letter
                self.remove_currency = remove_currency
                self.remove_punctuations = remove_punctuations
                self.remove_number = remove_number
                self.remove_longest_than = remove_longest_than
                self.remove_duplicate_word = remove_duplicate_word
                self.remove_single_letter = remove_single_letter
                self.remove_duplicated_letter = remove_duplicated_letter
                self.remove_unwanted_char = remove_unwanted_char
                self.normalize_arabic_unicode = normalize_arabic_unicode
                self.remove_unicode_and_special_character = remove_unicode_and_special_character
                self.remove_whitespace = remove_whitespace


        def text_normalization(self, text):
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
                if self.remove_stop_words == True:
                        text = self.remove_stop_words_(text)
                if self.remove_al == True:
                        text = self.remove_al_(text)
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
                if self.convert_kurdish_rah == True:
                        text = self.convert_kurdish_rah_(text)
                if self.convert_ayin == True:
                        text = self.convert_ayin_(text)
                if self.convert_la == True:
                        text = self.convert_la_(text)
                if self.convert_kurdish_tah == True:
                        text = self.convert_kurdish_tah_(text)
                if self.convert_kurdish_waw == True:
                        text = self.convert_kurdish_waw_(text)
                if self.convert_kurdish_kha == True:
                        text = self.convert_kurdish_kha_(text)
                if self.convert_kurdish_ga == True:
                        text = self.convert_kurdish_ga_(text)
                if self.remove_punctuations == True:
                        text = self.remove_punctuations_(text)
                if self.remove_greek_letter == True:
                        text = self.remove_greek_letter_(text)
                if self.remove_mathematical_operators == True:
                        text = self.remove_mathematical_operators_(text)
                if self.remove_cyrillic_letter == True:
                        text = self.remove_cyrillic_letter_(text)
                if self.remove_latin_letter == True:
                        text = self.remove_latin_letter_(text)
                if self.remove_currency == True:
                        text = self.remove_currency_(text)
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
                if self.remove_unwanted_char == True:
                        text = self.remove_unwanted_char_(text)
                if self.normalize_arabic_unicode == True:
                        text = self.normalize_arabic_unicode_(text)
                if self.remove_unicode_and_special_character == True:
                        text = self.remove_unicode_and_special_character_(text)
                if self.remove_whitespace == True:
                        text = self.remove_whitespace_(text)
                return text
            

        def remove_emojis_(self,text):
                """
                Remove emojis from the given text.

                Args:
                        text (str): The input text from which emojis need to be removed.

                Returns:
                        str: The text with emojis removed, with words separated by spaces.
                """
                with open("Emojis.txt", "r", encoding="utf-8") as file:
                        emojis = file.read()
                        emojis = set(emojis)
                
                text = "".join([word if word not in emojis else " " for word in text]  )
                return text
        
        def remove_hashtags_(self,text):
                """remove all hashtags from text
                        Args:
                            text (string): input text containing hashtags to be removed
                        Returns:
                            string: text without any hashtags
                """   
                text =  re.sub("#[\u0600-\u06FF\u0030-\u0039\u0041-\u005A\u0061-\u007A]+"," ", text)
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
                text = re.sub("@[\u0600-\u06FF\u0030-\u0039\u0041-\u005A\u0061-\u007A]+"," ", text)
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
        
        def remove_al_(self, text):
                """
                Remove occurrences of the Arabic definite article 'ال' from the text, 
                except when it is part of the word 'الله' (Allah).

                Args:
                    text (str): The input text from which 'ال' should be removed.

                Returns:
                    str: The text with 'ال' removed, except in the word 'الله'.
                """
                text = re.sub(r'ال(?!له)', " ", text)
                return text

        def remove_arabic_diacritics_(self,text):
                """removes diacritics (harakat) from Arabic text
                            Args:
                                    text (string): the Arabic text to remove diacritics from

                            Returns:
                                    string: the modified text without diacritics
                """
                pattern = r'[\u0618\u0619\u061A\u064B\u064C\u064D\u064E\u064F\u0650\u0651\u0652\u0653\u00AB\u00B7\uFDFC\u0651]+'
                text = re.sub(pattern, ' ', text)
                return text


        def remove_arabic_tatweel_(self,text):
                """remove Arabic Tatweel
                            Args:
                                text (string): text with Arabic Tatweel
                            Returns:
                                text after removing Arabic Tatweel
                """
                text = re.sub('[\u0640]', ' ', text)
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
                text = re.sub('ﯙ', 'و', text)
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
                text = re.sub('ﷺ', 'صلى الله عليه و سلم', text)
                text = re.sub('ﷻ', 'جل جلاله', text)
                text = re.sub('﷽', 'بسم الله الرحمن الرحيم', text)
                return text 

        def remove_unicode_and_special_character_(self, text):
                """
                Remove special and unicode characters from the text.

                Args:
                    text (string): Input text containing special characters.

                Returns:
                    text: Text without special characters.
                """
                Pattern = r'[\u2460-\u24FF\u2070-\u218F\u2022-\u221E\u0E3F\u00A9\u00AE\u2117\u2120\u03B1-\u03C9\u0391-\u039F\u00BC-\u00BE\u0022-\u0027\u002A\u002B\u002F\u003C-\u003E\u0040\u005C\u005E\u0060\u007C\u007E\u00BC-\u00BE\x96]'
                text = re.sub(Pattern, ' ', text)
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

                pattern = r"\b([\u0600-\u06FF])\b(?!\w)"  
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
                pattern = r"\b([\u0600-\u06FF])\1+\b(?!\w)"  
                text = re.sub(pattern, " ", text)
                return text
        
        def remove_currency_(self,text):
                """
                Removes currency symbols from the given text.

                This method uses a predefined regular expression pattern to identify and 
                replace various currency symbols (e.g., $, €, ¥, ₹, etc.) with a space (' '). 

                Args:
                        text (str): The input string from which currency symbols should be removed.

                Returns:
                        str: The processed string with all currency symbols replaced by a space.

                """
                Pattern ='[$¢£¤¥֏؋߾߿৲৳৻૱௹฿៛₠₡₢₣₤₥₦₧₨₩₪₫€₮₯₰₱₲₳₴₵₶₷₸₹₺₻₼₽₾₿꠸＄￠﷼＄￡￥￦𑿝𑿞𑿟𑿠𞋿DZDBHDKMFDJFEGPIQDJODKWDLBPLYDMRUMADOMRQARSARSOSSDGSYPTNDAEDYER]' 
                text = re.sub(Pattern, ' ', text)
                return text

        def remove_cyrillic_letter_(self,text):
                """
                Removes Cyrillic characters from the given text.

                This method uses a regular expression to identify and replace all 
                characters in the Cyrillic Unicode block (U+0400 to U+04FF) with a space (' '). 

                Args:
                        text (str): The input string from which Cyrillic characters should be removed.

                Returns:
                        str: The processed string with all Cyrillic characters replaced by a space.              ."
                """
                text = re.sub("[\u0400-\u04FF]", " ", text)
                return text

        def remove_greek_letter_(self,text):
                """
                Removes Greek characters from the given text.

                This method uses a regular expression to identify and replace all 
                characters in the Greek Unicode block (U+0370 to U+03FF) with a space (' '). 

                Args:
                        text (str): The input string from which Cyrillic characters should be removed.

                Returns:
                        str: The processed string with all Greek characters replaced by a space.              ."
                """
                text = re.sub("[\u0370-\u03FF]", " ", text)
                return text
                

        def remove_mathematical_operators_(self,text):
                 """
                Removes Mathmetical operators from the given text.

                This method uses a regular expression to identify and replace all 
                characters in the  Mathmetical operators Unicode block (U+0370 to U+03FF) with a space (' '). 

                Args:
                        text (str): The input string from which Cyrillic characters should be removed.

                Returns:
                        str: The processed string with all  Mathmetical operators replaced by a space.              ."
                """
                text = re.sub("[\u2200-\u22FF]", " ", text)
                return text

        def remove_latin_letter_(self,text):
                """
                        Removes extended Latin characters from the given text.

                        This method uses regular expressions to identify and replace all 
                        characters in the following Latin Unicode blocks with a space (' '):
                                - Latin Extended-A (U+0100 to U+017F)
                                - Latin-1 Supplement (U+0080 to U+00FF)
                                - Phonetic Extensions (U+1D00 to U+1D7F)

                        Args:
                                text (str): The input string from which extended Latin characters should be removed.

                        Returns:
                                str: The processed string with all extended Latin characters replaced by a space.
                """
                text = re.sub("[\u0100-\u017F]", " ", text)
                text = re.sub("[\u0080-\u00FF]", " ", text)
                text = re.sub("[\u1D00-\u1D7F]", " ", text)
                return text

        def remove_unwanted_char_(self, text):
                 """
                        Removes specific unwanted characters from the given text.

                        This method uses a predefined regular expression pattern to identify 
                        and replace specific characters (defined by their Unicode code points) 
                        with a space (' '). These characters may include symbols, marks, or 
                        script-specific characters.

                        Args:
                                text (str): The input string from which unwanted characters should be removed.

                        Returns:
                                str: The processed string with the specified unwanted characters replaced by a space.
                """
                text = re.sub('[\u06B1\u069C\u1F592\u06FD\u06D2\u06D3\u066D\uA9C2\u05DD\u05D1\u0780\u0788\u1D17\uB791\uD558\uC0AC\uFBAF\u02DD\uFD3E\uFF1A\uFD3F\uA9C1\u06DD]', ' ', text)
                return text

        def convert_kurdish_tah_(self, text):
                """
                        Converts Kurdish-specific 'Tah' (ٺ, ټ) characters to the standard Arabic 'Tah' character (ت).

                        Args:
                                text (str): The input string containing Kurdish-specific 'Tah' characters.

                        Returns:
                                str: The processed string with all instances of U+067A and U+067C replaced by U+062A.
                """
                text = re.sub('[\u067A\u067C]', '\u062A', text)
                return text
        
        def convert_kurdish_kha_(self, text):
                """
                        Converts Kurdish-specific 'Kha' (څ) characters to the standard Arabic 'Kha' character (خ).

                        Args:
                                text (str): The input string containing Kurdish-specific 'Kha' characters.

                        Returns:
                                str: The processed string with all instances of څ replaced by خ.
                """
                text = re.sub('څ', 'خ', text)
                return text
        
        def convert_kurdish_rah_(self,text):
                """
                        Converts Kurdish-specific 'Rah' (ڕڑژ) characters to the standard Arabic 'Rah' character (ر).

                        Args:
                                text (str): The input string containing Kurdish-specific 'Rah' characters.

                        Returns:
                                str: The processed string with all instances of ڕڑژ replaced by ر.
                """
                text = re.sub('[ڕڑژ]', 'ر', text)
                return text

        def convert_kurdish_ga_(self , text):
                 """
                        Converts Kurdish-specific 'Ga' (ڪ) characters to the standard Arabic 'Kaf' character (ك).

                        Args:
                                text (str): The input string containing Kurdish-specific 'Ga' characters.

                        Returns:
                                str: The processed string with all instances of ڪ replaced by ك.
                """
                text = re.sub('ڪ', 'ك', text)
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