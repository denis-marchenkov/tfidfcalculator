from path_setup import path_config
path_config.add()

#region imports
import unittest
from unittest.mock import patch
from tf_idf_calculator import tfidf_calculator
#endregion


class test_parser(unittest.TestCase):
    
    sample_data = {
        0: ['alice', 'was', 'beginning', 'to', 'get', 'very', 'tired', 'of', 'sitting', 'by', 'her', 'sister', 'on', 'the', 'bank', 'and', 'of', 'having', 'nothing', 'to', 'do', 'once', 'or', 'twice', 'she', 'had', 'peeped', 'into', 'the', 'book', 'her', 'sister', 'was', 'reading', 'but', 'it', 'had', 'no', 'pictures', 'or', 'conversations', 'in', 'it', 'and', 'what', 'is', 'the', 'use', 'of', 'a', 'book', 'thought', 'alice', 'without', 'pictures', 'or', 'conversations'], 
        1: ['so', 'she', 'was', 'considering', 'in', 'her', 'own', 'mind', 'as', 'well', 'as', 'she', 'could', 'for', 'the', 'day', 'made', 'her', 'feel', 'very', 'sleepy', 'and', 'stupid', 'whether', 'the', 'pleasure', 'of', 'making', 'a', 'daisychain', 'would', 'be', 'worth', 'the', 'trouble', 'of', 'getting', 'up', 'and', 'picking', 'the', 'daisies', 'when', 'suddenly', 'a', 'white', 'rabbit', 'with', 'pink', 'eyes', 'ran', 'close', 'by', 'her']
    }

    def setUp(self) -> None:
        self.calc = tfidf_calculator(test_parser.sample_data)

    def test_build_tf_data(self):
        
        actual = self.calc.build_tf_data()
        
        self.assertEqual(2, len(actual))

    def test_build_df_data(self):
        
        actual = self.calc.build_df_data()
        
        self.assertGreater(len(actual), 0)

if __name__ == '__main__':
    unittest.main(exit=False)
    path_config.remove()