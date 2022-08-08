import unittest
from io import StringIO
import TestQuiz


class MyTestCase(unittest.TestCase):
    def test_previous(self):
        words = TestQuiz.read_file('tests/test_list.txt')
        self.assertEqual(1, len(words))
