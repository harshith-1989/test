import os
from enum import Enum

from HelperFunctions import *

class FolderStructure(Enum):
	ROOT_FOLDER = ""
	LOGGING_FOLDER = "logging"
	CONFIG_FOLDER = "config"
	INPUT_FOLDER = "input"
	OUTPUT_FOLDER = "output"
	TMP_FOLDER = "tmp"


def get_root_folder():
	return os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

def delete_existing_keys_for_folder_structure(constants_file_path):
		folder_structure_names = [FolderStructure.LOGGING_FOLDER.name,
								FolderStructure.CONFIG_FOLDER.name,
								FolderStructure.INPUT_FOLDER.name,
								FolderStructure.OUTPUT_FOLDER.name,
								FolderStructure.TMP_FOLDER.name]
		for folder in folder_structure_names:
			delete_line_containing_the_string(constants_file_path, folder)

def write_folder_structure_to_constants_file(constants_file_path,project_root_folder):
	folder_structure_list = ["{} = \"{}/{}\"\n".format(FolderStructure.LOGGING_FOLDER.name,project_root_folder,FolderStructure.LOGGING_FOLDER.value),
							"{} = \"{}/{}\"\n".format(FolderStructure.CONFIG_FOLDER.name,project_root_folder,FolderStructure.CONFIG_FOLDER.value),
							"{} = \"{}/{}\"\n".format(FolderStructure.INPUT_FOLDER.name,project_root_folder,FolderStructure.INPUT_FOLDER.value),
							"{} = \"{}/{}\"\n".format(FolderStructure.OUTPUT_FOLDER.name,project_root_folder,FolderStructure.OUTPUT_FOLDER.value),
							"{} = \"{}/{}\"\n".format(FolderStructure.TMP_FOLDER.name,project_root_folder,FolderStructure.TMP_FOLDER.value),
							"{} = \"{}\"\n".format(FolderStructure.ROOT_FOLDER.name,project_root_folder)]
	for folder in folder_structure_list:
		if not check_string_exists_in_file (constants_file_path ,folder):
			append_line_at_end_of_file(constants_file_path ,folder)

def prepare_constants_file():
	project_root_folder = get_root_folder()
	constants_file_path = "{}{}".format(project_root_folder,"/PythonFiles/Constants.py")

	delete_existing_keys_for_folder_structure(constants_file_path)
	write_folder_structure_to_constants_file(constants_file_path,project_root_folder)

prepare_constants_file()