import re
pattern = re.compile(r'[\U0001F600-\U0001F64F\U0001F970-\U0001F9D0\
                           \U0001F60B-\U0001F60D\U0001F44B\U0001F91D\
                           \U0001F610-\U0001F615\U0001F636\U0001F62A\
                           \U0001F634\U0001F912-\U0001F927\U0001F920-\U0001F921\
                           \U0001F9E2\U0001F913\U0001F9D0\U0001F641-\U0001F643\
                           \U0001F928-\U0001F92B\U0001F611-\U0001F631\U0001F633-\U0001F635\
                           \U0001F9D9-\U0001F9DD\U0001F408-\U0001F43F\U0001F464-\U0001F468\
                           \U0001F64B-\U0001F64F\U0001F482-\U0001F487\U0001F9B9-\U0001F9DF\
                           \U0001F3C3-\U0001F3C4\U0001F6B4-\U0001F6B6\U0001F3CB-\U0001F3CC\
                           \U0001F9D1-\U0001F9D2\U0001F46A-\U0001F46C\U0001F9D1-\U0001F9DD\
                           \U0001F9B0-\U0001F9B3\U0001F408-\U0001F426\U0001F400-\U0001F433\
                           \U0001F41B-\U0001F41C\U0001F33C-\U0001F37F\U0001F957-\U0001F9AA\
                           \U0001F5FA-\U0001F6B2\U0001F3E8\U0001F550-\U0001F567\
                           \U0001F30D-\U0001F32C\U0001F947-\U0001F948\
                           \U0001F3C3-\U0001F3D3\U0001F3A8-\U0001F3B7\
                           \U0001F451-\U0001F4AF\U0001F4F1\U0001F4F7-\U0001F4FE\
                           \U0001F4D6-\U0001F4EA\U0001F58A-\U0001F5CF\U0001FA9D\
                           \U0001F52D-\U0001F52F\U0001F9ED\U0001F6D1-\U0001F6F3\
                           \U000026A0-\U000026FF\U00002B05-\U00002B1C\U00002B50\U0001F503\
                           \U0001F004\U0001F0CF\U0001F18E\U0001F191-\U0001F19A\U0001F201-\U0001F23A\
                           \U0001F250-\U0001F251\U0001F300-\U0001F3FF\U0001F480-\U0001F9FF\
                           \U0001F1E6-\U0001F1FF\U00002700-\U000027BF\U00002640-\U000026A7\U00002000-\U00002BFF]')

def remove_emojis_(text):
        """remove all emojis from text

          Args:
              text (string): input text containing emoijis to be removed

          Returns:
              string: text without any emojis
        """ 

        text = re.sub(pattern, ' ', text)
        return text