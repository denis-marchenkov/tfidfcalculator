from path_setup import path_config
path_config.add()

#region imports
import unittest
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
    
    def setUp(self, ) -> None:
        self.parser = parser()


    def test_parser_config(self):

        expected_separator = "==============="
        expected_strip_chars = [',','!','^']
        
        self.parser.config(document_separator = expected_separator, strip_chars = expected_strip_chars)

        actual_separator = self.parser.document_separator
        actual_strip_chars = self.parser.strip_chars

        self.assertEqual(expected_separator, actual_separator)
        self.assertListEqual(expected_strip_chars, actual_strip_chars)


    def test_parser_parse(self):

        raw_data = sample_text.split('\n')

        actual = self.parser.parse(raw_data)
        
        self.assertEqual(2, len(actual))
        self.assertEqual(58, len(actual[0]))
        self.assertEqual(55, len(actual[1]))
        self.assertEqual("alice", actual[0][0])
        self.assertEqual("conversations", actual[0][-1])
        self.assertEqual("so", actual[1][0])
        self.assertEqual("her", actual[1][-1])


    def test_parser_strip_characters(self):
        
        expected = "expected"

        strip = ' '.join(self.parser.strip_chars)
        raw_data = [
            f'{strip} {expected}',
            self.parser.document_separator,
            strip
        ]

        actual = self.parser.parse(raw_data)

        self.assertEqual(1, len(actual))
        self.assertEqual(1, len(actual[0]))
        self.assertEqual(expected, actual[0][0])


    def test_parser_no_separator(self):

        self.parser.config(document_separator='')

        raw_data = sample_text.split('\n')

        actual = self.parser.parse(raw_data)

        self.assertEqual(1, len(actual))
        self.assertEqual(114, len(actual[0]))



if __name__ == '__main__':
    unittest.main(exit=False)
    path_config.remove()