#region imports
import logging
from data_cache_service import data_cache_service
#endregion

logger = logging.getLogger(__name__)

class parser():
    
    def __init__(self, cache_service: data_cache_service) -> None:
        self.cache = cache_service
        self.file_path = None
        self.document_separator = '=============='
        self.strip_chars = ['\'','?', '!', '.', ',', ':', '"', '-', '_', ';', '*']

        logger.info('Initialized')

    def config(self, **kwargs):
        """
        Configure document parser with following parameters:

        file_path                   - full name of a data file to parse                                         \n
        document_separator          - special marker present in text to divide it into partial documents        \n
        strip_chars                 - list of characters to remove from text                                    \n
        """

        logger.info(f'Parser configured with following args: {kwargs}')
        
        fp = kwargs.pop('file_path')
        ds =  kwargs.pop('document_separator')
        sc =  kwargs.pop('strip_chars')

        if fp:
            self.file_path = fp
        if ds: 
            self.document_separator  = ds
        if sc:
            self.strip_chars = sc


    def parse(self):
        """
        Split text file 'file_path' into documents by specified 'document_separator' separator,            \n
        split documents into words by whitespace,                                                          \n
        trim characters specified in 'strip_chars'                                                         \n
        """

        logger.info(f'Parsing: {self.file_path}')

        raw_data = self.read_file(self.file_path)
        

        # splitting by \n adds empty entries into list
        if '' in raw_data:
            raw_data = [i for i in raw_data if i!='']

        


    def read_file(file_path):
        """
        Read file into a string
        """

        result = None

        with open(file_path) as f:
            result = f.readlines()

        return result