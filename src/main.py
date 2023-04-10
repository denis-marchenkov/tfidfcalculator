#region imports
import os
import logging
from document_parser import parser
from tf_idf_calculator import tfidf_calculator
from data_cache_service import data_cache_service
from time import gmtime
#endregion


def main():
    logging.Formatter.converter = gmtime # for milliseconds in logging
    logging.basicConfig(filename='tfidf_app_log.log',
                        filemode='w',
                        format='%(asctime)s.%(msecs)03d | %(name)s | %(message)s', 
                        datefmt='%d/%m/%Y %H:%M:%S', 
                        level = logging.INFO)
    logger = logging.getLogger(__name__)

    logger.info('BEGIN')

    # dc = data_cache_service()
    # dp = parser(dc)

    # l = [1,2,3]

    # dc.save(l, "cache_list.tfidf_cache")


    
    logger.info('END')

if __name__ == '__main__':
    main()