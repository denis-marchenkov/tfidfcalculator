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

    # dc = data_cache_service()
    # dp = parser(dc)

    # l = [1,2,3]

    # dc.save(l, "cache_list.tfidf_cache")


    
    logger.info('END')

if __name__ == '__main__':
    main()