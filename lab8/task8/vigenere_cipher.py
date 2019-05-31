class VigenereCipher:
    """
    Class for representing vigenere cipher
    """
    def __init__(self, keyword):
        """
        initialization of the class
        """
        self.keyword = keyword

    def extend_keyword(self, number):
        """
        Method for making needed long key
        :param number: length of out key
        :return: extend keyword
        """
        repeats = number // len(self.keyword) + 1
        return (self.keyword * repeats)[:number]

    def _code(self, text, combine_func):
        """
        method for coding the text
        :param text: text to code
        :param combine_func:
        :return:
        """
        text = text.replace(" ", "").upper()
        combined = []
        keyword = self.extend_keyword(len(text))
        for p, k in zip(text, keyword):
            combined.append(combine_func(p, k))
        return "".join(combined)

    def encode(self, plaintext):
        """
        method for encoding the text
        :param plaintext: text for coding
        :return: coded text
        """
        return self._code(plaintext, self.combine_character)

    def decode(self, ciphertext):
        """
        method for decoding the text
        :param plaintext: text for decoding
        :return: decoded text
        """
        return self._code(ciphertext, self.separate_character)

    @staticmethod
    def combine_character(plain, keyword):
        """
        method for combination character
        """
        plain = plain.upper()
        keyword = keyword.upper()
        plain_num = ord(plain) - ord('A')
        keyword_num = ord(keyword) - ord('A')
        return chr(ord('A') + (plain_num + keyword_num) % 26)

    @staticmethod
    def separate_character(cypher, keyword):
        """
        Method for separate character
        """
        cypher = cypher.upper()
        keyword = keyword.upper()
        cypher_num = ord(cypher) - ord('A')
        keyword_num = ord(keyword) - ord('A')
        return chr(ord('A') + (cypher_num - keyword_num) % 26)
