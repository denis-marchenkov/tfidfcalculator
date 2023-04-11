#region imports
import logging
#endregion

logger = logging.getLogger(__name__)

class tfidf_calculator():

    def __init__(self, document_data: dict) -> None:
        
        self.document_data = document_data
        self.total_documents = len(document_data)
        self.tf_data = None
        self.df_data = None
        self.tf_idf_data = None
        logger.info('Initialized')


    def configure(self, **kwargs) -> None:
        """
        Optional.                                                                                               \n
        Initialize calculator with already existing tf, df, tf_idf data collections.                               \n

        Accepts the following parameters:                                                                       \n

        tf - dictionary where key - document index, value - dictionary where key - word, value - term frequency of this word in document. \n
        df
        tf_idf

        """

        logger.info(f'Calculator configured with following args: {kwargs}')
        pass


    # TF stands for 'Term Frequency' - represents the frequency of the word in each document.
    # The number of times the word appears in the document divided by total amount of words in the document. 
    def build_tf_data(self, r = 0) -> dict:
        """
        Builds dictionary where key - document index, value - dictionary where key - word, value - term frequency of this word in document.     \n
        Rounds TF values to 'r' if r > 0                                                                                                        \n
                                                                                                                                                \n
        Example:                                                                                                                                \n
        {0:{'the':1, 'quick':22, 'brown':10}, 1:{'fox':1, 'jumped':3, 'over':5},...} 
        """

        logger.info("Begin building tf dictionary")

        result = {}

        # self.document_data is a dictionary {'document_index': ['document_word1', 'document_word2'...], ...}
        for document_index in self.document_data:
            
            if document_index not in result:
                result[document_index] = {}

            # current_doc is a list of words
            current_doc = self.document_data[document_index]

            for word in current_doc:
                if word in result[document_index]:
                    continue
                freq = current_doc.count(word) / len(current_doc)
                freq = round(freq, r) if r > 0 else freq

                result[document_index].update({word: freq})
            
        return result