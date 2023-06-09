# region imports
import logging
from math import log
# endregion imports

logger = logging.getLogger(__name__)


class tfidf_calculator():

    def __init__(self, document_data: dict) -> None:
        self.document_data = document_data
        self.total_documents = len(document_data)
        self.tf_data = None
        self.df_data = None
        self.tf_idf_data = None

        logger.info('Initialized')

    # optional configuration with already existing cached tf-idf data
    def configure(self, **kwargs) -> None:
        """
        Optional.                                                                                                                                           \n
                                                                                                                                                            \n
        Initialize calculator with already existing tf, df, tf_idf data collections.                                                                        \n
                                                                                                                                                            \n
        Accepts the following parameters:                                                                                                                   \n
                                                                                                                                                            \n
        tf - dictionary where key - document index, value - dictionary where key - word, value - TF this word in document.                                  \n
        Example:                                                                                                                                            \n
        { '0' : {'the':1, 'quick':22, 'brown':10}, '1' : {'fox':1, 'jumped':3, 'over':5},...}                                                               \n
                                                                                                                                                            \n
        df - dictionary where key - word, value - document frequency of the word.                                                                           \n
        Example:                                                                                                                                            \n
        { 'the':0.123, 'quick':0.05, 'brown':0.003 ... }                                                                                                    \n
                                                                                                                                                            \n
        tfidf - dictionary where key - document index, value - dictionary with key - word, value - TFIDF score of the word                                  \n
        Example:                                                                                                                                            \n
        { '0': {'the':0.01106, 'quick':0.003, 'brown':0.002}, '1': {'fox':0.05, 'jumped':0.6, 'over':0.11}, '2': {'lazy':0.123, 'dog':0.112} ... }          \n
        """

        tf = kwargs.pop('tf', False)
        df = kwargs.pop('df', False)
        tfidf = kwargs.pop('tfidf', False)

        if tf is not False:
            self.tf_data = tf
        if df is not False:
            self.df_data = df
        if tfidf is not False:
            self.tf_idf_data = tfidf

        logger.info(f'Calculator configured with following args: {kwargs}')

    # TF stands for 'Term Frequency' - represents the frequency of the word in each document.
    # The number of times the word appears in the document divided by total amount of words in the document. 
    def build_tf_data(self, r=0) -> dict:

        """
        Builds dictionary where key - document index, \n
        value - dictionary where key - word, value - term frequency of this word in document.     \n
        Rounds TF values to 'r' if r > 0                                                                                                        \n
                                                                                                                                                \n
        Example:                                                                                                                                \n
        { '0' : {'the':1, 'quick':22, 'brown':10}, '1' : {'fox':1, 'jumped':3, 'over':5},...}                                                   \n
        """

        if self.tf_data is not None:
            logger.info('Instance was initialized with cached TF data. Returning cache.')
            return self.tf_data

        logger.info("Begin building TF dictionary")

        result = {}

        # self.document_data is a dictionary:
        # {'document_index': ['document_word1', 'document_word2'...], ...}
        for document_index in self.document_data:

            if document_index not in result:
                result[document_index] = {}

            # current_doc is a list of words
            current_doc = self.document_data[document_index]

            for word in current_doc:
                if word in result[document_index]:
                    continue
                tf = current_doc.count(word) / len(current_doc)
                tf = round(tf, r) if r > 0 else tf

                result[document_index].update({word: tf})

        logger.info("End building TF dictionary")

        self.tf_data = result

        return result

    # DF stands for 'Document Frequency' - the proportion of documents that contain certain word.
    # The amount documents containing certain word divided by the total amount of documents.
    def build_df_data(self, r=0) -> dict:
        """
        Builds dictionary where key - word, value - document frequency of the word.         \n
        Rounds DF values to 'r' if r > 0                                                    \n
                                                                                            \n
        Example:                                                                            \n
        { 'the':0.123, 'quick':0.05, 'brown':0.003 ... }                                    \n
        """
        if self.df_data is not None:
            logger.info('Instance was initialized with cached DF data. Returning cache.')
            return self.df_data

        logger.info("Begin building DF dictionary")

        result = {}

        for document_index in self.document_data:
            # words already seen in this document
            found_words = []
            # current_doc is a list of words
            current_doc = self.document_data[document_index]

            for word in current_doc:

                if word not in result:
                    result[word] = 0

                # we saw this word once already and increased document counter for it
                if word in found_words:
                    continue

                # count documents which have this word
                result[word] += 1
                found_words.append(word)

        # at this stage 'result[key]' values contain the amount of documents we saw 'key' word in
        # divide amount of documents by total amount of documents
        for key in result:

            df = result[key] / self.total_documents
            result[key] = round(df, r) if r > 0 else df

        logger.info("End building DF dictionary")

        self.df_data = result

        return result

    # TF-IDF score for each word in a document.
    # IDF stands for "Inverse Document Frequency" and essentially 1/DF.
    # TF-IDF = TF * log(IDF)
    def build_tf_idf_data(self, tf_data: dict = None, df_data: dict = None, r = 0) -> dict:
        """
        Build dictionary where key - document index, value - dictionary with key - word, value - TFIDF score of the word                                     \n
        Rounds TF-IDF values to 'r' if r > 0                                                                                                                 \n
                                                                                                                                                             \n
        Example:                                                                                                                                             \n
        { '0' : {'the':0.01106, 'quick':0.003, 'brown':0.002}, '1' : {'fox':0.05, 'jumped':0.6, 'over':0.11}, '2': {'lazy':0.123, 'dog':0.112} ... }         \n
        """

        logger.info("Begin building TFIDF score dictionary")

        tfdata = None
        dfdata = None

        if tf_data is None:
            if self.tf_data is None:
                self.build_tf_data(r)
            tfdata = self.tf_data
        else:
            tfdata = tf_data

        if df_data is None:
            if self.df_data is None:
                self.build_df_data(r)
            dfdata = self.df_data
        else:
            dfdata = df_data

        result = {}

        for document_index in self.document_data:

            if document_index not in result:
                result[document_index] = {}
            
            for word in self.document_data[document_index]:
                
                if word in result[document_index]:
                    continue

                tf = tfdata[document_index].get(word)

                if tf is None:
                    logger.warn(f"TF data has no such entry at: [{document_index}][{word}]")
                    continue

                df = dfdata.get(word)

                if df is None:
                    logger.warn(f"DF data has no such entry at: [{word}]")
                    continue

                tfidf_score = tf * log(1/df)
                tfidf_score = round(tfidf_score, r) if r > 0 else tfidf_score

                result[document_index].update({word: tfidf_score})

        self.tf_idf_data = result

        logger.info("End building TFIDF score dictionary")

        return result

    # get 'top' of the most significant words for specific document
    def get_top_words(self, document_index: int, top = 1, r = 0) -> dict:
        """
        Returns dictionary of words with highest tf-idf score for specific document     \n
                                                                                        \n
        Example:                                                                        \n
        {'quick': 0.0364, 'brown': 0.0243, 'fox': 0.0243}                               \n
        """

        logger.info(f"Get top {top} most significant words for document index {document_index}")

        self.build_tf_idf_data(self.tf_data, self.df_data, r)

        top_words = {}

        index = str(document_index)
        dct = self.tf_idf_data[index]

        i = 0
        while(i < top):

            tmpVal=0
            tmpWord=''

            for word in dct:
                if word in top_words:
                    continue
                if dct[word] > tmpVal:
                    tmpVal = dct[word]
                    tmpWord = word

            if tmpVal and len(tmpWord):
                top_words.update({tmpWord: tmpVal})

            i += 1

        return top_words

    # flattens all TFIDF data for specific documents and selected top_w top words,
    # suitable for datasets
    def flatten_data(self, document_names: list = None, doc_ids = [], top_w = 10, r=0) -> dict:
        """
        Flattens all TFIDF data for top_w words with biggest TFIDF for documents specified in doc_ids    \n
        Atttaches specified in document_names title to every row                                         \n
        Returns dictionary                                                                               \n

        Example:
            {
                'id': [0,0,0,
                    1,1,1],
                'title': ['a', 'a', 'a', 
                        'b', 'b', 'b'],
                'word': ['alice', 'rabbit','book',
                        'something','alice', 'here'],
                'tfidf': [0, 0.2, 0.3,
                        0.02, 0.8, 0.5],
                'df': [0, 0.2, 0.3,
                        0.02, 0.8, 0.5]
                'tfidf': [0, 0.2, 0.3,
                        0.02, 0.8, 0.5]
            }
                                                                                                          \n
        """

        logger.info(f"Flatten data into one normalized table")
        if document_names is None:
            document_names = []

        self.build_tf_idf_data(self.tf_data, self.df_data, r)

        has_titles = len(document_names) >= len(self.tf_idf_data)

        result = {'id':[], 'title':[], 'word':[],'tf':[], 'df':[], 'tfidf':[]}


        for document_index in self.tf_idf_data:
            if len(doc_ids):
                if int(document_index) not in doc_ids:
                    continue
            top_words = self.get_top_words(document_index, top_w, r)

            for word in top_words:
                result['id'].append(document_index)
                if has_titles:
                    result['title'].append(document_names[int(document_index)])
                else:
                    result['title'].append(f'Document {document_index}')
                result['word'].append(word)
                result['tf'].append(self.tf_data[document_index][word])
                result['df'].append(self.df_data[word])
                result['tfidf'].append(top_words[word])

            blanks_count = top_w - len(top_words)

            while blanks_count > 0:
                result['id'].append(document_index)
                if has_titles:
                    result['title'].append(document_names[int(document_index)])
                else:
                    result['title'].append(f'Document {document_index}')
                result['word'].append('')
                result['tf'].append(-1)
                result['df'].append(-1)
                result['tfidf'].append(-1)

                blanks_count -= 1

        return result