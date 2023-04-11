from path_setup import path_config
path_config.add()

#region imports
import unittest
from unittest.mock import patch
from tf_idf_calculator import tfidf_calculator
#endregion


class test_parser(unittest.TestCase):
    
    #region test data
    sample_data = {
        '0': ['alice', 'was', 'beginning', 'to', 'get', 'very', 'tired', 'of', 'sitting', 'by', 'her', 'sister', 'on', 'the', 'bank', 'and', 'of', 'having', 'nothing', 'to', 'do', 'once', 'or', 'twice', 'she', 'had', 'peeped', 'into', 'the', 'book', 'her', 'sister', 'was', 'reading', 'but', 'it', 'had', 'no', 'pictures', 'or', 'conversations', 'in', 'it', 'and', 'what', 'is', 'the', 'use', 'of', 'a', 'book', 'thought', 'alice', 'without', 'pictures', 'or', 'conversations'], 
        '1': ['so', 'she', 'was', 'considering', 'in', 'her', 'own', 'mind', 'as', 'well', 'as', 'she', 'could', 'for', 'the', 'day', 'made', 'her', 'feel', 'very', 'sleepy', 'and', 'stupid', 'whether', 'the', 'pleasure', 'of', 'making', 'a', 'daisychain', 'would', 'be', 'worth', 'the', 'trouble', 'of', 'getting', 'up', 'and', 'picking', 'the', 'daisies', 'when', 'suddenly', 'a', 'white', 'rabbit', 'with', 'pink', 'eyes', 'ran', 'close', 'by', 'her']
    }

    expected_tf = {
        '0': {'alice': 0.035, 'was': 0.035, 'beginning': 0.018, 'to': 0.035, 'get': 0.018, 'very': 0.018, 'tired': 0.018, 'of': 0.053, 'sitting': 0.018, 'by': 0.018, 'her': 0.035, 'sister': 0.035, 'on': 0.018, 'the': 0.053, 'bank': 0.018, 'and': 0.035, 'having': 0.018, 'nothing': 0.018, 'do': 0.018, 'once': 0.018, 'or': 0.053, 'twice': 0.018, 'she': 0.018, 'had': 0.035, 'peeped': 0.018, 'into': 0.018, 'book': 0.035, 'reading': 0.018, 'but': 0.018, 'it': 0.035, 'no': 0.018, 'pictures': 0.035, 'conversations': 0.035, 'in': 0.018, 'what': 0.018, 'is': 0.018, 'use': 0.018, 'a': 0.018, 'thought': 0.018, 'without': 0.018}, 
        '1': {'so': 0.019, 'she': 0.037, 'was': 0.019, 'considering': 
0.019, 'in': 0.019, 'her': 0.056, 'own': 0.019, 'mind': 0.019, 'as': 0.037, 'well': 0.019, 'could': 0.019, 'for': 0.019, 'the': 0.074, 'day': 0.019, 'made': 0.019, 'feel': 0.019, 'very': 0.019, 'sleepy': 0.019, 'and': 0.037, 'stupid': 0.019, 'whether': 0.019, 'pleasure': 0.019, 'of': 0.037, 'making': 0.019, 'a': 0.037, 'daisychain': 0.019, 'would': 0.019, 'be': 0.019, 'worth': 0.019, 'trouble': 0.019, 'getting': 0.019, 'up': 0.019, 'picking': 0.019, 'daisies': 0.019, 'when': 0.019, 'suddenly': 0.019, 'white': 0.019, 'rabbit': 0.019, 'with': 0.019, 'pink': 0.019, 'eyes': 0.019, 'ran': 0.019, 'close': 0.019, 'by': 0.019}
                }
    
    expected_df = {'alice': 0.5, 'was': 1.0, 'beginning': 0.5, 'to': 0.5, 'get': 0.5, 'very': 1.0, 'tired': 0.5, 'of': 1.0, 'sitting': 0.5, 'by': 1.0, 'her': 1.0, 'sister': 0.5, 'on': 0.5, 'the': 1.0, 'bank': 0.5, 'and': 1.0, 'having': 0.5, 'nothing': 0.5, 'do': 0.5, 'once': 0.5, 'or': 0.5, 'twice': 0.5, 'she': 1.0, 'had': 0.5, 'peeped': 0.5, 'into': 0.5, 'book': 0.5, 'reading': 0.5, 'but': 0.5, 'it': 0.5, 'no': 0.5, 'pictures': 0.5, 'conversations': 0.5, 'in': 1.0, 'what': 0.5, 'is': 0.5, 'use': 0.5, 'a': 1.0, 'thought': 0.5, 'without': 0.5, 'so': 0.5, 'considering': 0.5, 'own': 0.5, 'mind': 0.5, 'as': 0.5, 'well': 0.5, 'could': 0.5, 'for': 0.5, 'day': 0.5, 'made': 0.5, 'feel': 0.5, 'sleepy': 0.5, 'stupid': 0.5, 'whether': 0.5, 'pleasure': 0.5, 'making': 0.5, 'daisychain': 0.5, 'would': 0.5, 'be': 0.5, 'worth': 0.5, 'trouble': 0.5, 'getting': 0.5, 'up': 0.5, 'picking': 0.5, 'daisies': 0.5, 'when': 0.5, 'suddenly': 0.5, 'white': 0.5, 'rabbit': 0.5, 'with': 0.5, 'pink': 0.5, 'eyes': 0.5, 'ran': 0.5, 'close': 0.5}

    expected_tf_idf = {
        '0': {'alice': 0.024, 'was': 0.0, 'beginning': 0.012, 'to': 0.024, 'get': 0.012, 'very': 0.0, 'tired': 0.012, 'of': 0.0, 'sitting': 0.012, 'by': 0.0, 'her': 0.0, 'sister': 0.024, 'on': 0.012, 'the': 0.0, 'bank': 0.012, 'and': 0.0, 'having': 0.012, 'nothing': 0.012, 'do': 0.012, 'once': 0.012, 'or': 0.037, 'twice': 0.012, 'she': 0.0, 'had': 0.024, 'peeped': 0.012, 'into': 0.012, 'book': 0.024, 'reading': 0.012, 'but': 0.012, 'it': 0.024, 'no': 0.012, 'pictures': 0.024, 'conversations': 0.024, 'in': 0.0, 'what': 0.012, 'is': 0.012, 'use': 0.012, 'a': 0.0, 'thought': 0.012, 'without': 0.012}, 
        '1': {'so': 0.013, 'she': 0.0, 'was': 0.0, 'considering': 0.013, 'in': 0.0, 'her': 0.0, 'own': 0.013, 'mind': 0.013, 'as': 0.026, 'well': 0.013, 'could': 0.013, 'for': 0.013, 'the': 0.0, 'day': 0.013, 'made': 0.013, 'feel': 0.013, 'very': 0.0, 'sleepy': 0.013, 'and': 0.0, 'stupid': 0.013, 'whether': 0.013, 'pleasure': 0.013, 'of': 0.0, 'making': 0.013, 'a': 0.0, 'daisychain': 0.013, 'would': 0.013, 'be': 0.013, 'worth': 0.013, 'trouble': 0.013, 'getting': 0.013, 'up': 0.013, 'picking': 0.013, 'daisies': 0.013, 'when': 0.013, 'suddenly': 0.013, 'white': 0.013, 'rabbit': 0.013, 'with': 0.013, 'pink': 0.013, 'eyes': 0.013, 'ran': 0.013, 'close': 0.013, 'by': 0.0}
                    }
    #endregion

    def setUp(self) -> None:
        self.calc = tfidf_calculator(test_parser.sample_data)


    def test_build_tf_data(self):
        
        actual = self.calc.build_tf_data(3)
        
        self.assertDictEqual(test_parser.expected_tf, self.calc.tf_data)


    def test_build_df_data(self):
        
        actual = self.calc.build_df_data(3)
        
        self.assertDictEqual(test_parser.expected_df, actual)


    def test_build_tf_idf_data(self):
        
        actual = self.calc.build_tf_idf_data(None, None, r=3)

        self.assertDictEqual(test_parser.expected_tf_idf, actual)
        self.assertDictEqual(test_parser.expected_tf, self.calc.tf_data)
        self.assertDictEqual(test_parser.expected_df, self.calc.df_data)

    
    def test_build_tf_idf_from_cache(self):

        actual = self.calc.build_tf_idf_data(test_parser.expected_tf, test_parser.expected_df, r=3)

        self.assertDictEqual(test_parser.expected_tf_idf, actual)
        


if __name__ == '__main__':
    unittest.main(exit=False)
    path_config.remove()