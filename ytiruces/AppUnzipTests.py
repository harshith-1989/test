import re

from RegexExpressions import *
from HelperFunctions import *
import Constants


def check_signing_info(verification_keys):
    # return boolean by checking if the signing key is debug key
    original_folder_path = "{}/{}".format(Constants.OUTPUT_FOLDER, "original")
    if os.path.exists(original_folder_path):
        execution_output = execute_shell_command(
            "keytool -printcert -file {}/META-INF/CERT.RSA".format(original_folder_path))

        if verification_keys in execution_output['OUTPUT']:
            logging.info("App signed using a debug key")
            return "{} found in signing key. App signed using a debug keystore\n".format(verification_keys)
        else:
            logging.info("App signed using a debug key")
            return "{} not found in signing key. App not signed using a debug keystore\n".format(verification_keys)
    else:
        log_error_and_exit("{} not found to check the signing".format(original_folder_path))

def android_xml_content_verification():
    # return as a dictionary in the form (verification key : Bool)
    android_manifest_xml_path = "{}/{}".format(Constants.OUTPUT_FOLDER, "AndroidManifest.xml")
    if os.path.exists(android_manifest_xml_path):
        with open(android_manifest_xml_path, 'r') as file:
            # read android manifest xml file into string variable
            android_xml_file_contents = file.read()
        execution_output = ""
        verification_keys = get_manifest_xml_regex()
        regex_expression_variable = ""
        for key in verification_keys.keys():
            regex_expression_variable = re.compile(verification_keys[key])
            if Constants.ANDROID_EXPORTED in key:
                component = 0
                component_name =1

                for application_components in regex_expression_variable.findall(android_xml_file_contents):
                    logging.info("{} with name {} has android:exported set to true".format(application_components[component],application_components[component_name]))
                    execution_output = "{}\n{} with name {} has android:exported set to true".format(execution_output,application_components[component],application_components[component_name])
            else:
                for regex_matches in regex_expression_variable.findall(android_xml_file_contents):
                    logging.info("{} set to true : {}".format(key, regex_matches))
                    execution_output = "{}\n{} set to true : {}".format(execution_output,key, regex_matches)

        if len(execution_output) == 0:
            logging.info("No issues foung in {}".format(android_manifest_xml_path))
            execution_output = "No issues foung in {}".format(android_manifest_xml_path)

        return execution_output
    else:
        log_error_and_exit("{} not found to check the signing".format(original_folder_path))

def check_smali_files():
    # check for the extension of the files if any other file is present other than that with smali extension
    execution_output = ""
    for root, subdirs, files in os.walk("{}/{}".format(Constants.OUTPUT_FOLDER, "smali")):
        logging.info("Checking folder : {}".format(root))
        for file in files:
            if "smali" not in file:
                logging.info("{}/{} is not a smali file".format(root, file))
                execution_output = "{}\n{}/{} is not a smali file\n".format(execution_output, root, file)
    if len(execution_output) == 0:
        logging.info("No unencrypted files found")
        execution_output = "No unencrypted files found\n"
    return execution_output


def check_permissions():
    android_manifest_xml_path = "{}/{}".format(Constants.OUTPUT_FOLDER, "AndroidManifest.xml")
    standard_android_permission_file_path = "{}/{}".format(Constants.ROOT_FOLDER, "pythonFiles/Permissionsfile.txt")

    # construct regex to match the user features/permissions
    regex_string_for_matching_permissions_and_features_in_android_manifest_xml = 'uses-(.*) android:name=(.*)/'
    permissions_list_from_android_xml_path = re.compile(
        regex_string_for_matching_permissions_and_features_in_android_manifest_xml)

    execution_output = ""
    android_xml_file_contents = ""

    # Constants
    permission_or_feature_id = 0
    permission_or_feature_name = 1

    with open(android_manifest_xml_path, 'r') as file:
        # read android manifest xml file into string variable
        android_xml_file_contents = file.read()

    # iterate over every permissions and feature from android manifest xml
    for permission_or_feature in permissions_list_from_android_xml_path.findall(android_xml_file_contents):

        with open(standard_android_permission_file_path, 'r') as standard_android_permission_file:
            # open standard permissions file and iterate over every permission in it
            for standard_android_permission in standard_android_permission_file.read().split('::'):
                # if the permission matches any entry in the permissions file, log it
                if (standard_android_permission.split(':')[permission_or_feature_id] in
                        permission_or_feature[permission_or_feature_name]):

                    logging.info("{} name : {} present in android_manifest.xml file".format(
                        permission_or_feature[permission_or_feature_id],
                        permission_or_feature[permission_or_feature_name])
                    )

                    execution_output = "{}\n{} name : {} present in android_manifest.xml file".format(
                        execution_output,
                        permission_or_feature[permission_or_feature_id],
                        permission_or_feature[permission_or_feature_name]
                    )
                    # skip to next iteration if entry found
                    break
            if permission_or_feature[permission_or_feature_name] not in execution_output:
                # if no matches found, log the custom permission
                logging.info("{} name : {} is a custom-permission /feature present in android_manifest.xml file".format(
                    permission_or_feature[permission_or_feature_id],
                    permission_or_feature[permission_or_feature_name])
                )

                execution_output = "{}\n{} name : {} is custom-permission/feature present in android_manifest.xml file".format(
                    execution_output,
                    permission_or_feature[permission_or_feature_id],
                    permission_or_feature[permission_or_feature_name]
                )

    if len(execution_output) == 0:
        logging.info("No permissions entries found")
        execution_output = "No permissions entries found\n"

    return execution_output


def check_assets_folder():
    pass
    # iterate over contents and return bool if any js files present


def check_lib_folder():
    pass
    # iterate over the contents and check if they can be decompiled


def check_res_folder():
    pass


def execute_tests(test_dictionary):
    # iterate over the folder structure in the output folder
    # match the name of the folder from the test dictionary and execute tests
    # add the result to the test dictionary with result as the key
    # return the dictionary
    folders_array = test_dictionary['Folder']
    execution_result = ""
    for folder in folders_array:
        if folder['FolderName'] in "assets":
            logging.info("*********\n******** Assets Folder Check *************\n\n")
            check_assets_folder()
        elif folder['FolderName'] in "lib":
            logging.info("*********\n******** lib Folder Check *************\n\n")
            check_lib_folder()
        elif folder['FolderName'] in "original":
            logging.info("*********\n******** original Folder Check *************\n\n")
            execution_result = check_signing_info(folder['verification_keys'])
        elif folder['FolderName'] in "res":
            logging.info("*********\n******** res Folder Check *************\n\n")
            check_res_folder()
        elif folder['FolderName'] in "smali":
            logging.info("*********\n******** smali Folder Check *************\n\n")
            check_smali_files()
        elif folder['FolderName'] in "AndroidManifest":
            logging.info("*********\n******** AndroidManifest xml Check *************\n\n")
            execution_result = android_xml_content_verification()
        elif folder['FolderName'] in "permissions":
            logging.info("*********\n******** permissions Check *************\n\n")
            execution_result = check_permissions()
        folder['execution_result'] = execution_result
