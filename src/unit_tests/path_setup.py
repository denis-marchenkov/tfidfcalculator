# region imports
import os
import sys
#endregion

# quick and dirty solution to add module folders to sys.path so they become visible in unit_tests folder
# when running individual test modules ModuleNotFoundError being thrown
# running everything from test_runner.py works fine though. 
# TODO: Need to figure out those __init__.py files
class path_config():
    paths = [f'{os.getcwd()}\\src']

    @staticmethod
    def add():
        for p in path_config.paths:
            if p not in sys.path:
                sys.path.append(p)

    @staticmethod
    def remove():
        for p in path_config.paths:
            if p in sys.path:
                sys.path.remove(p)