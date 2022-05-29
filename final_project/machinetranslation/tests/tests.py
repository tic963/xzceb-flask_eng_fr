""" test module code from translator.py """
import unittest
from translator import english_to_french, french_to_english

class TestEnglishTrans(unittest.TestCase):
    """ Test module english_to_french """
    def test1(self):
        # test when "Hello" is given as input the output is "Bonjour".
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        # test when null is given as input the output is null.
        self.assertEqual(english_to_french(" "), " ")

class TestFrenchTrans(unittest.TestCase):
    """ Test module french_to_english """
    def test1(self):
        # test when "Bonjour" is given as input the output is "Hello".
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        # test w
        # hen null is given as input the output is null.
        self.assertEqual(french_to_english(" "), " ")

unittest.main()