#region imports
import unittest
from unittest.mock import patch
from document_parser import parser
#endregion


#region sample text
sample_text = """
Alice! was beginning to get very tired of sitting by her sister on the          \n
bank, and of having @ nothing to do. Once - or` twice she had peeped into the   \n
book her sister \ was reading, but it had no pict_ures or conversations in      \n
it, "and what is the use of a book," thought Alice, * "without pictures or      \n
conversations?"                                                                 \n
==============                                                                  \n
So she was considering in her own\ mind (as well as she could, for the          \n
day made her feel very sleepy and stupid), whether the pleasure of              \n
making a daisy-chain would * be worth - the! trouble ? of getting_ up and       \n
picking the daisies, when suddenly a White Rabbit with pink eyes ran            \n
close by her.                                                                   \n
"""
#endregion

class test_parser(unittest.TestCase):
    
    @patch('data_cache_service.data_cache_service')
    def setUp(self, mock_cache_service) -> None:
        self.parser = parser(mock_cache_service)

    def test_parser_config(self):
        expected_file_path = "d:\\test\\file.txt"
        expected_separator = "==============="
        expected_strip_chars = [',','!','^']
        
        self.parser.config(file_path = expected_file_path, document_separator = expected_separator, strip_chars = expected_strip_chars)

        actual_file_path = self.parser.file_path
        actual_separator = self.parser.document_separator
        actual_strip_chars = self.parser.strip_chars

        self.assertEqual(expected_file_path, actual_file_path)
        self.assertEqual(expected_separator, actual_separator)
        self.assertListEqual(expected_strip_chars, actual_strip_chars)

    def test_parser_parse(self):
        self.parser.read_file = lambda x: sample_text.split('\n')
        self.parser.parse()


if __name__ == '__main__':
    unittest.main()
