from path_setup import path_config
path_config.add()

#region imports
import unittest
from unittest.mock import patch
from document_loader_service import document_loader_service
#endregion


class test_loader(unittest.TestCase):

    expected_data = [1,2,3]

    @patch('data_cache_repository.cache_repository')
    @patch('document_parser.parser')
    def setUp(self, mock_cache_repository, mock_parser) -> None:
        
        mc = mock_cache_repository.return_value
        mc.load.return_value = test_loader.expected_data

        mp = mock_parser.return_value
        mp.parse.return_value = test_loader.expected_data

        self.loader = document_loader_service(mc, mp)
        document_loader_service.read_file = lambda x: []


    def tearDown(self) -> None:
        path_config.remove()


    def test_load_file(self):
        actual = self.loader.load_file('', True)
        self.assertListEqual(test_loader.expected_data, actual)


    def test_load_file_cache(self):
        actual = self.loader.load_file('')
        self.assertListEqual(test_loader.expected_data, actual)
    

if __name__ == '__main__':
    unittest.main(exit=False)
    path_config.remove()