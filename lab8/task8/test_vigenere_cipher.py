from unittest import TestCase
from vigenere_cipher import *


class TestVigenereCipher(TestCase):
    def test_extend_keyword(self):
        cipher = VigenereCipher("TRAIN")
        extended = cipher.extend_keyword(16)
        self.assertEqual(extended, "TRAINTRAINTRAINT")

    def test_combine_character(self):
        self.assertEqual(VigenereCipher.combine_character("E", "T"), "X")
        assert VigenereCipher.combine_character("N", "R") == "E"

    def test_encode_lowercase(self):
        cipher = VigenereCipher("TRain")
        encoded = cipher.encode("encoded in Python")
        self.assertEqual(encoded, "XECWQXUIVCRKHWA")

    def test_encode_spaces(self):
        cipher = VigenereCipher("TRAIN")
        encoded = cipher.encode("ENCODED IN PYTHON")
        self.assertEqual(encoded, "XECWQXUIVCRKHWA")

    def letter_encode(self):
        cipher = VigenereCipher("TRAIN")
        encoded = cipher.encode("ENCODEDINPYTHON")
        self.assertEqual(encoded, "XECWQXUIVCRKHWA")
