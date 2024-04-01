import re
import pandas as pd
import difflib
emojis = pd.read_csv('Emojis.csv')
arabic_words = set(open('arabic_data.txt','r').read().split('\n'))
consecutive_repeated_letters = set(open('arabic_consecutive_repeated_letters.txt', 'r').read().split('\n'))



class TextNormalization:
        def __init__(self,
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
                     normalize_gaf,
                     normalize_pe,
                     normalize_che,
                     decrease_number_of_consecutive_reapted_letter,
                     remove_punctuations,
                     normalize_arabic_unicode,
                     remove_unicode_and_special_character,
                     remove_stop_words,
                     remove_number,
                     arabic_spell_correction,
                     remove_arabic_diacritics,
                     remove_non_arabic,
                     remove_arabic_tatweel,
                     normalize_alef,
                     normalize_alef_maqsura,
                     normalize_teh_marbuta,
                     remove_longest_than,
                     remove_whitespace):

                
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
                self.normalize_gaf = normalize_gaf
                self.normalize_pe = normalize_pe
                self.normalize_che = normalize_che
                self.decrease_number_of_consecutive_reapted_letter = decrease_number_of_consecutive_reapted_letter
                self.remove_punctuations = remove_punctuations
                self.normalize_arabic_unicode = normalize_arabic_unicode
                self.remove_unicode_and_special_character = remove_unicode_and_special_character
                self.remove_stop_words = remove_stop_words
                self.remove_number = remove_number
                self.arabic_spell_correction = arabic_spell_correction
                self.remove_arabic_diacritics = remove_arabic_diacritics
                self.remove_non_arabic = remove_non_arabic
                self.remove_arabic_tatweel = remove_arabic_tatweel
                self.normalize_alef = normalize_alef
                self.normalize_alef_maqsura = normalize_alef_maqsura
                self.normalize_teh_marbuta = normalize_teh_marbuta
                self.remove_longest_than = remove_longest_than
                self.remove_whitespace = remove_whitespace


        def text_normalization(self, text):
                if  self.remove_emojis == True:
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
                if self.decrease_number_of_consecutive_reapted_letter == True:
                        text = self.decrease_number_of_consecutive_repeated_letter_(text)
                if self.normalize_gaf == True:
                        text = self.convert_gaf(text)
                if self.normalize_pe  == True:
                        text = self.convert_pe(text)
                if self.normalize_che == True:
                        text = self.convert_che(text)
                if self.remove_punctuations == True:
                        text = self.delete_punctuations(text)
                if self.normalize_arabic_unicode == True:
                        text = self.normalize_arabic_unicode_(text)
                if self.remove_unicode_and_special_character == True:
                        text = self.delete_unicode_and_special_character(text)
                if self.remove_stop_words == True:
                        text = self.delete_stop_words(text)
                if self.remove_number == True:
                        text = self.delete_number(text)
                if self.arabic_spell_correction == True:
                        text = self.arabic_spell_correction_(text)
                if self.remove_arabic_diacritics == True:
                        text = self.delete_arabic_diacritics(text)
                if self.remove_non_arabic == True:
                        text = self.delete_non_arabic(text)
                if self.remove_arabic_tatweel == True:
                        text = self.delete_arabic_tatweel(text)
                if self.normalize_alef == True:
                        text = self.convert_alef(text)
                if self.normalize_alef_maqsura == True:
                        text = self.convert_alef_maqsura(text)
                if self.normalize_teh_marbuta == True:
                        text = self.convert_teh_marbuta(text)
                if self.remove_duplicate_word == True:
                        text = self.delete_duplicate_word(text)
                if self.remove_single_letter  == True:
                        text = self.delete_single_letter(text)
                if self.remove_duplicated_letter == True:
                        text = self.delete_duplicated_letter(text)
                if self.remove_longest_than == True:
                        text = self.delete_longest_than(text)
                if self.remove_whitespace == True:
                        text = self.delete_whitespace(text)
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
                text =  re.sub("#[[ٱأإٲٳٵآ-ي٠-٩a-zA-Z0-9]+","", text)
                return text   

        def delete_emails(self, text):
                """remove all email address from text

                Args:
                    text (string): input text containing email address to be removed

                Returns:
                    string: text without any email address
                """   
                text = re.sub("[a-zA-Z0-9-_.]+@[a-zA-Z]+.[a-zA-Z]+"," ", text)  
                return text

        def delete_url(self, text):
                """remove all URL from text

                Args:
                    text (string): input text containing URL address to be removed

                Returns:
                    string: text without any URL address
                """ 
                text = re.sub(r'http\S+', ' ', text, flags=re.MULTILINE)
                return text

        def delete_mention(self, text):
                """remove all mention from text

                Args:
                    text (string): input text containing mention to be removed

                Returns:
                    string: text without any mention
                """   
                text = re.sub("@[[ٱأإٲٳٵآ-ي٠-٩a-zA-Z0-9]+"," ", text)
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

                    pattern = r"\b([ٱأإٲٳٵآ-ي])\b(?!\w)"  
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

                    pattern = r"\b([ٱأإٲٳٵآ-ى])\1+\b(?!\w)"  
                    text = re.sub(pattern, " ", text)
                    return text

        def convert_gaf(self, text):
                """converts Gaf (گ) to Kaph (ك) in Arabic text.


                Args:
                    text (string): the Arabic text to convert

                Returns:
                    string: the modified text with Gaf replaced by Kaf
                """
                text = re.sub("گ", "ك", text)
                return text

        def convert_pe(self, text):
                """converts Pe (پ) to  Bet (ب) in Arabic text.


                Args:
                    text (string): the Arabic text to convert

                Returns:
                    string: the modified text with Pe replaced by Kaf
                """
                text = re.sub("پ", "ب", text)
                return text

        def convert_che(self, text):
                """converts Che (چ) to Gimel (ج) in Arabic text.


                Args:
                    text (string): the Arabic text to convert

                Returns:
                    string: the modified text with Che replaced by Kaf
                """
                text = re.sub("چ", "ج", text)
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

        def delete_punctuations(self, text):
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

        def normalize_arabic_unicode_(self, text):
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

        def delete_stop_words(self, text):
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
            
        def delete_number(self, text):
                """remove numbers from the text

                Args:
                    text (string): input text contining numbers

                Returns:
                    text: text without numbers
                """
                text = re.sub(r'\d+', '', text)
                return text

        def arabic_spell_correction_(self, text):
                    """correct spelloing of arabic words

                        Args:
                            text (string): input text containing word with wrong spelling

                        Returns:
                            string: text with correct spelling
                        """         
                    
                    corrected_word = []
                    for word in text.split():
                            if word in arabic_words:
                                    corrected_word.append(word)
                            else:
                                    match = difflib.get_close_matches(word, arabic_words, n=1, cutoff=0.7)
                                    corrected_word.append(match[0] if match else word)
                                    text = ' '.join(corrected_word)
                    return text

        def delete_arabic_diacritics(self, text):
                """removes diacritics (harakat) from Arabic text


                    Args:
                            text (string): the Arabic text to remove diacritics from

                    Returns:
                            string: the modified text without diacritics
                """
                pattern = r'[\u0618\u0619\\u061A\u064B\u064C\u064D\u064E\u064F\u0650\u0651\u0652\u0653]+'
                text = re.sub(pattern, ' ', text)
                return text

        def delete_non_arabic(self, text):
                """remove non arabic words from the text

                Args:
                    text (string): input text contining non arabic words

                Returns:
                    text: text without non arabic words
                """ 
                
                punctuation = "{}_!-?.:؛;""''()،؟,..[\]"
                text =  ' '.join(word for word in text.split() if word in arabic_words or word in punctuation or word.isnumeric() == True)
                return text

        def delete_arabic_tatweel(self, text):
                """delete Arabic Tatweel

                    Args:
                    
                        text (string): text with Arabic Tatweel

                    Returns:
                        text after removing Arabic Tatweel
                """
                text = re.sub('_', ' ', text)
                return text

        def convert_alef(self, text):
                """
                    converts various Alef representations (including Alef with Hamza Above/Below, Alef with Madda Above, etc.) to the basic Alef ('ا') in Arabic text


                    Args:
                            text (string): the Arabic text to convert

                    Returns:
                            string: the modified text with all Alef variants replaced by the basic Alef
                """
                text = re.sub("[ٱأإٲٳٵآ]+", "ا", text)
                return text

        def convert_alef_maqsura(self, text):
                """converts Alef Maksura (ى) to Yeh (ي) in Arabic text

                Args:
                    text (string): the Arabic text to convert

                Returns:
                    string: the modified text with Alef Maksura replaced by Yeh
                """
                text = text = re.sub("ى", "ي", text)
                return text

        def convert_teh_marbuta(self, text):
                """converts Teh Marbuta (ة) to Heh (ه) in Arabic text.


                Args:
                    text (string): the Arabic text to convert

                Returns:
                    string: the modified text with Teh Marbuta replaced by Heh
                """
                text = re.sub("ة", "ه", text)
                return text

        def delete_longest_than(self, text):
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

        def delete_whitespace(self, text):
                """remove extra whitespaces at the beginning and end of the text

                Args:
                    text (self, text): input text contating extra whitespaces

                Returns:
                    string: text without extra whitespaces
                """  
                text = re.sub(r"\s+", " ", text)
                return text 
