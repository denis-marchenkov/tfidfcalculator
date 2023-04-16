#region imports
import logging
#endregion

logger = logging.getLogger(__name__)

# text parser, prepares dictionary data for tf_idf calculator,
# splits original text by document_separator into documents,
# splits documents into words and forms a dictionary where key - document index, value - list of words in document
class parser():
    
    def __init__(self) -> None:
        self.document_separator = '=============='
        self.strip_chars = ['\'','?', '!', '.', ',', ':', '"', '_', ';', '*', '`', '\n', '#', "@", "$", '\\', '(', ')']

        logger.info('Initialized')


    # optional config, allows to customize document separator line
    # and list of characters to be stripped from text
    def config(self, **kwargs):
        """
        Optional.                                                                                               \n
        Configure document parser with following parameters:                                                    \n
                                                                                                                \n
        document_separator          - special marker present in text to divide it into partial documents        \n
        strip_chars                 - list of characters to remove from text                                    \n
        """


        ds =  kwargs.pop('document_separator', False)
        sc =  kwargs.pop('strip_chars', False)

        if ds == False:
            logger.info(f'Using default separator: {self.document_separator}')
        else:
            self.document_separator = ds
            
        if sc != False:
            self.strip_chars = sc

        logger.info(f'Parser configured with following args: {kwargs}')


    # parse text data, strip characters, split into documents and documents into words
    def parse(self, raw_data) -> dict:
        """
        Split text file 'file_path' into documents by specified 'document_separator' separator,            \n
        split documents into words by whitespace,                                                          \n
        trim characters specified in 'strip_chars'.
        
        Returns dictionary of documents where key - document index, value - list of words in document:     \n
        { 0:['quick', 'brown'], 1:['fox', 'jumps'] }
        """

        logger.info('Parsing raw data')

        data = self.__remove_empty_entries(raw_data)

        documents = {}
        doc_words = []
        doc_count = 0

        for line in data:

            l = line.lower().strip('\n').strip(' ').strip('\'')

            if len(self.document_separator) > 0 and l == self.document_separator:
                
                if len(doc_words) > 0:
                    documents[doc_count] = doc_words
                    doc_count += 1
                    doc_words = []
                
                continue
            
            for c in self.strip_chars:
                if c in l:
                    l = l.replace(c, '')
        
            words = l.split(' ')

            words = self.__remove_empty_entries(words)

            doc_words += words

        if len(doc_words) > 0:
             documents[doc_count] = doc_words

        logger.info(f'Data parsed: {len(documents)} documents')

        return documents
    
    
    # removes empty entries from list of words
    # (splitting by \n may add empty entries into list)   
    def __remove_empty_entries(self, input: list) -> None:
        
        result = input.copy()

        empty_lines = ['','\n']
        if any(el in result for el in empty_lines):
            result = [i for i in result if i not in empty_lines]
        
        return result

        