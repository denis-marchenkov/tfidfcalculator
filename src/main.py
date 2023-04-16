#region imports
import logging
from time import gmtime

from document_parser import parser
from tf_idf_calculator import tfidf_calculator
from data_cache_repository import cache_repository
from document_loader_service import document_loader_service
#endregion


def main():
    #region configure logging
    logging.Formatter.converter = gmtime # for milliseconds in logging
    logging.basicConfig(filename='tfidf_app_log.log',
                        filemode='w',
                        format='%(asctime)s.%(msecs)03d | %(name)s | %(message)s', 
                        datefmt='%d/%m/%Y %H:%M:%S', 
                        level = logging.INFO)
    logger = logging.getLogger(__name__)
    #endregion

    logger.info('BEGIN')


    # full path to a text file (e.g. 'd:\\test\\text_sample.txt')
    # cache files will be created in the same folder
    file_path = "d:\\tf_df_test\\alice_in_wonderland_full.txt"

    dc = cache_repository()
    dp = parser()

    #sep = '[new chapter]'
    #dp.config(document_separator = '[new chapter]')
    
    ld = document_loader_service(dc, dp)
    data = ld.load_file(file_path, True)

    calc = tfidf_calculator(data)

    tf = calc.build_tf_data()
    df = calc.build_df_data()
    tfidf = calc.build_tf_idf_data(tf, df)
    flatten_tfidf = calc.flatten_data(['chapter 1', 'chapter 2'], doc_ids=[3],top_w=3)
    
    top_words = calc.get_top_words(0, 3)



    logger.info('END')

if __name__ == '__main__':
    main()