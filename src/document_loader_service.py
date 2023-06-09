#region imports
import logging
from document_parser import parser
from data_cache_repository import cache_repository
#endregion

logger = logging.getLogger(__name__)

# service layer over cache repository for loading file and parsing it's data into dictionary to pass tf_idf calculator
class document_loader_service():

    def __init__(self, cache_repo: cache_repository, data_parser: parser) -> None:
      
        self.parser = data_parser
        self.cache = cache_repo

        logger.info('Initialized')


    # load text file from disk, parse and cache parsed data
    def load_file(self, file_path: str, force_load: bool = False):
        """ 
        file_path                           - full path to a data file              \n
        force_load                          - force to load original data file      \n
                                                                                    \n
        Loads 'file_path' file from cache if cache exists.                          \n
        Otherwise loads original file, parses and caches it.                        \n
        """

        logger.info(f'Load file: {file_path}')

        data = None

        is_absent_in_cache = self.cache.is_cache_exists(file_path) == False

        if force_load or is_absent_in_cache:
            
            if is_absent_in_cache:
                logger.info('File not found in cache.')

            logger.info(f'Forcing to load original data file')
            
            raw_data = document_loader_service.read_file(file_path)
            parsed_data = self.parser.parse(raw_data)
            cache_file_path = self.cache.save(parsed_data, file_path)

            data = self.cache.load(cache_file_path)

        else:

            logger.info(f'Loading cached data')

            data = self.cache.load(file_path)

            if data is None:
                error = f'Failed to load cached data for file: {file_path}'
                logger.error(error)
                raise Exception(error)

        return data


    # read file in specified encoding
    @staticmethod
    def read_file(file_path, encoding='utf-8'):
        """ Read file lines into a string. Default encoding is utf-8 """

        result = None

        with open(file_path, 'r', encoding=encoding) as f:
            result = f.readlines()

        return result
    

        