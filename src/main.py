#region imports
import os
import logging
from document_parser import parser
from tf_idf_calculator import tfidf_calculator
from data_cache_service import data_cache_service
#endregion


def main():
    logging.basicConfig(filename='tfidf_app_log.log', format='%(asctime)s | %(name)s | %(message)s', datefmt='%d/%m/%Y %H:%M:%S', level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.info('BEGIN')

    dc = data_cache_service()


    l = [1,2,3]
    # d = {1:1, 2:2}
    # dl = {0:[1,2], 1:[3,4]}
    # dd = {0:{'a':'b'}, 1:{'c':'d'}}

    #dc.save(l, "cache_list.tfidf_cache")
   


    # tfidf = tfidf_calculator()

    
    logger.info('END')

if __name__ == '__main__':
    main()