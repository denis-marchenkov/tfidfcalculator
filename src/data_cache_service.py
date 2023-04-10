#region imports
import os
import json
import logging
#endregion

logger = logging.getLogger(__name__)

class data_cache_service():
    
    def __init__(self, work_folder: str = None) -> None:
        
        f = work_folder

        if f == None:
            f = os.getcwd()

        self.folder = f

        self.__init_work_folder()

        logger.info('Initialized')
        

    def save(self, data, file_name: str) -> str:
        """ 
        Saves 'data' as a json into file 'file_name'. 
        File will be created inside 'work_folder'. 
        Returns full file path.
        """

        logger.info('Saving data')

        file_path = os.path.join(self.folder, file_name)

        json_result = json.dumps(data)

        logger.info(f'Saving data to a file: {file_path}')
        
        with open(file_path, "w") as f:
            f.write(json_result)
        
        return file_path

    def load(self, file_name: str) -> str:
        """
        Loads cached object from cached file 'file_name' in work folder.
        If file is not found returns None.
        """

        logger.info('Loading data')
        
        result = None
        
        # if full file path was passed instad of name - it's fine, try load file
        file_path = None
        if os.path.exists(file_name) == True:
             file_path = file_name
        else:
             file_path = os.path.join(self.folder, file_name)

             if os.path.exists(file_path) == False:
                 logger.warn(f'File path does not exist: {file_path}')
                 return result

        logger.info(f'Loading data from a file: {file_path}')

        with open(file_path, "r") as f:
            result = json.load(f)
        
        return result
    

    def __init_work_folder(self):
            
            logger.info(f'Initializing work folder: {self.folder}')
            
            if  self.folder[-1] != '\\': 
                self.folder += '\\'

            if os.path.exists(self.folder) == False:
                os.mkdir(self.folder)

