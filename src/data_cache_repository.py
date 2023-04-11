#region imports
import os
import json
import logging
import pathlib
#endregion

logger = logging.getLogger(__name__)

class cache_repository():

    def __init__(self) -> None:
        
        self.cache_ext = '.cache'

        logger.info('Initialized')


    def save(self, data, file_path: str) -> str:
        """ 
        Saves 'data' as a json into file 'file_path' adds extension 'cache'. 

        Returns full cache file path.
        """

        cache_name = self.get_cached_file_path(file_path)

        logger.info(f'Caching data into file: {cache_name}')

        json_result = json.dumps(data)
        
        with open(cache_name, "w") as f:
            f.write(json_result)
        
        return cache_name


    def load(self, file_path: str) -> str:
        """
        Loads cached object from cached file 'file_path' in work folder.
        If file is not found returns None.
        """

        cache_name = self.get_cached_file_path(file_path)
        
        logger.info(f'Loading data from a cache file: {cache_name}')

        if os.path.exists(cache_name) == False:
            logger.warn(f'Cache file is not found: {cache_name}')
            return None

        with open(cache_name, "r") as f:
            result = json.load(f)
        
        return result
    

    def is_cache_exists(self, file_path) -> bool:
        """ Check if cache for file 'file_path' exists on disk """

        cache_name = self.get_cached_file_path(file_path)

        return pathlib.Path(cache_name).is_file()


    def get_cached_file_path(self, file_path) -> str:
        """ Convert 'file_path' to cache file path """

        f, ext = os.path.splitext(file_path)

        if ext == self.cache_ext:
            return file_path
        
        return f'{file_path}{self.cache_ext}'

