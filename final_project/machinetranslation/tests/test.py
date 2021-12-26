"""
@author: Jeffrey
"""
from translator import *
import unittest

class TestTranslator(unittest.TestCase):
    def testEnglishToFrench(self):
        with self.assertRaises(ValueError):
            englishToFrench(None)
        self.assertEqual(englishToFrench("Hello"), "Bonjour")

    def testFrenchToEnglish(self):
        with self.assertRaises(ValueError):
            frenchToEnglish(None)
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")

unittest.main()