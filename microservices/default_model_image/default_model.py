import importlib
import pickle
from concurrent.futures import ThreadPoolExecutor
from utils import Metadata, Database
from constants import *

class DefaultModel:
    __WRITE_MODEL_OBJECT_OPTION = "wb"
    __READ_MODEL_OBJECT_OPTION = "rb"

    def __init__(self, metadata_creator: Metadata,
                 database_connector: Database):
        self.__metadata_creator = metadata_creator
        self.__thread_pool = ThreadPoolExecutor()
        self.__database_connector = database_connector

    def create(self, model_name: str, module_path: str, class_name: str,
               description: str,
               class_parameters: dict):
        self.__metadata_creator.create_file(model_name, module_path,
                                            class_name)

        self.__create_model_document(model_name, description,
                                     class_parameters)

        '''self.__thread_pool.submit(self.__pipeline, model_name, module_path,
                                  class_name,
                                  class_parameters)'''
        self.__pipeline(model_name, module_path,
        class_name,
        class_parameters)

    def update(self, model_name: str, module_path: str, class_name: str,
               description: str,
               class_parameters: dict):
        self.__metadata_creator.update_finished_flag(model_name, False)

        self.__create_model_document(model_name, description,
                                     class_parameters)

        '''self.__thread_pool.submit(self.__pipeline, model_name, module_path,
                                  class_name,
                                  class_parameters)'''

        self.__thread_pool.submit(self.__pipeline, model_name, module_path,
                                  class_name,
                                  class_parameters)

    @staticmethod
    def available_tools() -> list:
        return AVAILABLE_MODULES

    def __create_model_document(self, model_name, description,
                                class_parameters):
        model_document = {
            DESCRIPTION_FIELD_NAME: description,
            CLASS_PARAMETERS_FIELD_NAME: class_parameters
        }
        self.__database_connector.insert_one_in_file(model_name, model_document)

    def __pipeline(self, model_name: str, module_path: str, class_name: str,
                   class_parameters: dict):
        module = importlib.import_module(module_path)
        module_function = getattr(module, class_name)
        function_instance = module_function(**class_parameters)
        self.__save(function_instance, model_name)
        self.__metadata_creator.update_finished_flag(model_name, flag=True)

    def __save(self, model_instance, model_name: str):
        model_output = open(model_name, self.__WRITE_MODEL_OBJECT_OPTION)
        pickle.dump(model_instance, model_output)
        model_output.close()