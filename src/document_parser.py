#region imports
from data_cache_service import data_cache_service
#endregion

class parser():
    
    def __init__(self, cache_service: data_cache_service) -> None:
        self.cache = cache_service

    def parse(self):
        print("test")