def remove_emojis_(text):
        """remove all emojis from text

          Args:
              text (string): input text containing emoijis to be removed

          Returns:
              string: text without any emojis
        """ 
        with open('Emojis.txt', 'r', encoding='utf-8') as file:
            emojis = file.read()
            text = [word for word in text if word not in list(emojis)]
            return ''.join(text)