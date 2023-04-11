#region imports
import os
import json
import logging
import pathlib
#endregion

logger = logging.getLogger(__name__)

# simple repository to save data to a file
class cache_repository():

    def __init__(self) -> None:
        
        self.cache_ext = '.cache'

        logger.info('Initialized')


    # save file
    def save(self, data, file_path: str) -> str:
        """ 
        Saves 'data' as a json into file 'file_path', adds extension '.cache'.      \n
                                                                                    \n
        Returns full cache file path.                                               \n
        """

        cache_name = self.get_cached_file_path(file_path)

        logger.info(f'Caching data into file: {cache_name}')

        json_result = json.dumps(data)
        
        with open(cache_name, "w") as f:
            f.write(json_result)
        
        return cache_name


    # load file
    def load(self, file_path: str) -> str:
        """
        Loads cached object from cached file 'file_path'. Cached files have '.cache' extension.     \n
                                                                                                    \n
        If file is not found returns None.                                                          \n
        """

        cache_name = self.get_cached_file_path(file_path)
        
        logger.info(f'Loading data from a cache file: {cache_name}')

        if os.path.exists(cache_name) == False:
            logger.warn(f'Cache file is not found: {cache_name}')
            return None

        with open(cache_name, "r") as f:
            result = json.load(f)
        
        return result
    

    # check if cache file exists
    def is_cache_exists(self, file_path) -> bool:
        """ Check if cache for file 'file_path' exists on disk """

        cache_name = self.get_cached_file_path(file_path)

        return pathlib.Path(cache_name).is_file()


    # append '.cache' extension to the original file name to get cache file name
    def get_cached_file_path(self, file_path) -> str:
        """ Convert 'file_path' to cache file path by appending '.cache' extension """

        f, ext = os.path.splitext(file_path)

        if ext == self.cache_ext:
            return file_path
        
        return f'{file_path}{self.cache_ext}'

