import re
import pandas as pd

with open('Emojis.txt','rb') as file:
            emoji = file.read()
            emojis = set(emoji.decode('utf-8'))



def text_normalization(text):
                        text = delete_emojis(text)
                        text = delete_hashtags(text)
                        text = delete_emails(text)
                        text = delete_url(text)
                        text = delete_mention(text)
                        text = delete_html_tags(text)
                        text = delete_new_line_char(text)
                        text = delete_english_letter(text)
                        text = delete_hindi_letter(text)
                        text = delete_urdu_letter(text)
                        text = delete_sindhi_letter(text)
                        text = delete_hebrew_letter(text)
                        text = delete_latin_letter(text)
                        text = delete_unwanted_char(text)
                        text = delete_arabic_diacritics(text)
                        text = delete_arabic_tatweel(text)
                        text = convert_gaf(text)
                        text = convert_pe(text)
                        text = convert_che(text)
                        text = convert_ve(text)
                        text = convert_alef(text)
                        text = convert_alef_maqsura(text)
                        text = convert_teh_marbuta(text)
                        text = convert_ayin(text)
                        text = convert_la(text)
                        text = convert_kurdish_waw(text)
                        text = delete_punctuations(text)
                        text = normalize_arabic_unicode_(text)
                        text = delete_unicode_and_special_character(text)
                        text = delete_stop_words(text)
                        text = delete_number(text)
                        text = delete_longest_than(text)
                        text = delete_duplicate_word(text)
                        text = delete_single_letter(text)
                        text = delete_duplicated_letter(text)
                        text = text.replace("\U00011e27", " ")
                        text = delete_whitespace(text)
                        return text

def delete_emojis(text):
        """remove all emojis from text
                Args:
                    text (string): input text containing emoijis to be removed
                Returns:
                    string: text without any emojis
        """  

        for emoji in text:
                if emoji in emojis:
                        text = text.replace(emoji, ' ')
        return text

def delete_hashtags(text):
        """remove all hashtags from text
                Args:
                    text (string): input text containing hashtags to be removed
                Returns:
                    string: text without any hashtags
        """   
        text =  re.sub("#[ٱأإٲٳٵآ-ي٠-٩a-zA-Z0-9]+"," ", text)
        return text   

def delete_emails(text):
        """
        remove all email address from text
                Args:
                    text (string): input text containing email address to be removed

                Returns:
                    string: text without any email address
        """   
        text = re.sub("[a-zA-Z0-9-_.]+@[a-zA-Z]+.[a-zA-Z]+"," ", text)  
        return text

def delete_url(text):
        """remove all URL from text
                Args:
                    text (string): input text containing URL address to be removed
                Returns:
                    string: text without any URL address
        """ 
        text = re.sub(r'http\S+', ' ', text, flags=re.MULTILINE)
        return text

def delete_mention(text):
        """remove all mention from text
                Args:
                    text (string): input text containing mention to be removed

                Returns:
                    string: text without any mention
        """   
        text = re.sub("@[ٱأإٲٳٵآ-ي٠-٩a-zA-Z0-9]+"," ", text)
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
        """
        delete new line character from text
                Args:
                    text (string): input text containing new line character to be removed

                Returns:
                    string: text without any new line character 
        """     
        Pattern = r'[\u000A\u000D]'
        text = re.sub(Pattern, ' ', text)
        return text

def delete_english_letter(text):
        """delete english words in a given text

                Args:
                    text (string): input text containing english words.

                Returns:
                    string: text without any english words
        """    
        text = re.sub('[A-Za-z]', "  ", text)
        return text

def delete_hindi_letter(text):
        """remove Hindi lettter from the text

                Args:
                    text (string): input text contining Hindi letter

                Returns:
                    text: text without Hindi letter
        """
        text = re.sub("[\u0900-\u097F]", " ", text)
        return text

def delete_urdu_letter(text):
        """remove Urdu lettter from the text

                Args:
                    text (string): input text contining Urdu letter

                Returns:
                    text: text without Urdu letter
        """
        pattern = "[\uFBAF\uFBB1\u0679\u067E\u0686\u0688\u0691\u0698\u06D2\u06D3\u06F5\u06F6\u076D\u069C\u0678]"
        text = re.sub(pattern, " ", text)
        return text

def delete_sindhi_letter(text):
    """Remove Sindhi letters from the text.

    Args:
        text (string): Input text containing Sindhi letters.

    Returns:
        string: Text without Sindhi letters.
    """
    pattern = r"[\u06FE\u06FD\u067A\u067B\u067D\u067E\u067F\u0680\u0683\u0684\u0686\u0687\u068A\u068C\u068D\u068F\u0699\u06A6\u06A9\u06AA\u06AF\u06B1\u06B3\u06BB]"
    text = re.sub(pattern, " ", text)  
    return text

def delete_hebrew_letter(text):
        """remove Hebrew lettter from the text

                Args:
                    text (string): input text contining Hebrew letter

                Returns:
                    text: text without Hebrew letter
        """
        pattern = "[\u0590-\u05FF]"
        text = re.sub(pattern, " ", text)
        return text

def delete_latin_letter(text):
        """remove Latin lettter from the text

                Args:
                    text (string): input text contining Latin letter

                Returns:
                    text: text without Latin letter
        """
        text = re.sub("[ößàħüéèôäïêç]", " ", text)
        return text

def delete_unwanted_char(text):
        """remove Unwanted char from the text

                Args:
                    text (string): input text contining Unwanted char

                Returns:
                    text: text without Unwanted char
        """
        text = re.sub("[눇ﻣ̲ﻥ̴ ٰھہノ§ヾ̯͡ ڼίɴ ٔ ٕﭿ눉مٓـ]", " ", text)
        return text

def delete_arabic_diacritics(text):
        """removes diacritics (harakat) from Arabic text
                    Args:
                            text (string): the Arabic text to remove diacritics from

                    Returns:
                            string: the modified text without diacritics
        """
        pattern = r'[\u0618\u0619\\u061A\u064B\u064C\u064D\u064E\u064F\u0650\u0651\u0652\u0653\u00AB\u00B7\uFDFC\u0651]+'
        text = re.sub(pattern, ' ', text)
        return text


def delete_arabic_tatweel(text):
        """delete Arabic Tatweel
                    Args:
                        text (string): text with Arabic Tatweel
                    Returns:
                        text after removing Arabic Tatweel
        """
        text = re.sub('[\u0640]', '', text)
        return text

def convert_gaf(text):
        """converts Gaf (گ) to Kaph (ك) in Arabic text.
                Args:
                    text (string): the Arabic text to convert

                Returns:
                    string: the modified text with Gaf replaced by Kaf
        """
        text = re.sub("گ", "ك", text)
        return text

def convert_pe(text):
        """converts Pe (پ) to  Bet (ب) in Arabic text.
               Args:
                    text (string): the Arabic text to convert
                Returns:
                    string: the modified text with Pe replaced by Kaf
        """
        text = re.sub("پ", "ب", text)
        return text


def convert_che(text):
        """converts Che (چ) to Gimel (ج) in Arabic text.
                Args:
                    text (string): the Arabic text to convert

                Returns:
                    string: the modified text with Che replaced by Kaf
        """
        text = re.sub("چ", "ج", text)
        return text


def convert_ve(text):
        """converts Ve (ﭪ) to  Fa (ف) in Arabic text.
               Args:
                    text (string): the Arabic text to convert
                Returns:
                    string: the modified text with Ve replaced by Fa
        """
        text = re.sub("ڤ", "ف", text)
        return text

def convert_alef(text):
        """
                converts various Alef representations (including Alef with Hamza Above/Below, Alef with Madda Above, etc.) to the basic Alef ('ا') in Arabic text

                    Args:
                            text (string): the Arabic text to convert

                Returns:
                            string: the modified text with all Alef variants replaced by the basic Alef
        """
        text = re.sub("[ٱأإٲٳٵآﺂ]+", "ا", text)
        return text

def convert_alef_maqsura(text):
        """converts Alef Maksura (ﻰ,ﱝ,ۍ) to (ى) in Arabic text

                Args:
                    text (string): the Arabic text to convert

                Returns:
                    string: the modified text with Alef Maksura replaced by (ى)
        """
        text = text = re.sub("[ﻰﱝۍ]", "ى", text)
        return text

def convert_teh_marbuta(text):
        """converts Teh Marbuta (ة) to Heh (ه) in Arabic text.
                Args:
                    text (string): the Arabic text to convert

                Returns:
                    string: the modified text with Teh Marbuta replaced by Heh
        """
        text = re.sub("ة", "ه", text)
        return text

def convert_ayin(text):
        """converts Ayin (؏) to (ع) in Arabic text.
                Args:
                    text (string): the Arabic text to convert

                Returns:
                    string: the modified text with ayin
        """
        text = re.sub("؏", "ع", text)
        return text

def convert_la(text):
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

def convert_kurdish_waw(text):
        """converts Kurdish Waw (ۆ) to Waw (و) in Arabic text.
                Args:
                    text (string): the Arabic text to convert

                Returns:
                    string: the modified text with Che replaced by Kaf
        """
        text = re.sub("ۆ", "و", text)
        return text

def delete_punctuations(text):
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

def normalize_arabic_unicode_(text):
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

def delete_unicode_and_special_character(text):
        """remove special and unicode characters from the text
                Args:
                    text (string): input text contining special characters

                Returns:
                    text: text without special characters
        """          
        Pattern = r'[\u2000-\u206F\u2460-\u24FF\u2070-\u218F\u2022-\u221E\u0E3F\u00A9\u00AE\u2117\u2120\u03B1-\u03C9\u0391-\u039F\u00BC-\u00BE\u0022-\u0027\u002A\u002B\u002F\u003C-\u003E\u0040\u005C\u005E\u0060\u007C\u007E\u00BC-\u00BE\u066A\u250A-\u25FF\u2B07\u02DB\u00A3\u0328\u300A\u300B\u00B2\uFF3E\u00B0\u032C\u0329\u0303\u030A\u0300-\u036F\u00BB\u200D\u0337\u0334\u032C\u0329\u0303\u030A\uFE0F]'
        text = re.sub(Pattern, ' ', text)
        return text

def delete_stop_words(text):
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
            
def delete_number(text):
        """remove numbers from the text

                Args:
                    text (string): input text contining numbers

                Returns:
                    text: text without numbers
        """
        text = re.sub(r'\d+', ' ', text)
        return text
def delete_longest_than(text):
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

        pattern = r"\b([ٱأإٲٳٵآ-ي])\b(?!\w)"  
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
        pattern = r"\b([ٱأإٲٳٵآ-ى])\1+\b(?!\w)"  
        text = re.sub(pattern, " ", text)
        return text

def delete_whitespace(text):
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
