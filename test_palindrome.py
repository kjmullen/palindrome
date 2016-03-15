from unittest import TestCase

from palindrome import palindrome


class PalindromeTests(TestCase):

    def test_even(self):
        self.assertTrue(palindrome("toot"))

    def test_odd(self):
        self.assertTrue(palindrome("tot"))

    def test_simple(self):
        self.assertTrue(palindrome("stunt nuts"))

    def test_complete_sentences(self):
        self.assertTrue(palindrome("Lisa Bonet ate no basil."))

    def test_complex_sentences(self):
        self.assertTrue(palindrome("A man, a plan, a cat, a ham, a yak, a yam, a hat, a canal: Panama!"))

    def test_multiple_sentences(self):
        self.assertTrue(palindrome("Doc, note, I dissent. A fast never prevents a fatness. I diet on cod."))

    def test_non_palindrome(self):
        self.assertFalse(palindrome("i am not a palindrome"))