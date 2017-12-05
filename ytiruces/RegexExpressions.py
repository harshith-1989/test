
#REGEX EXPRESSIONS

PERMISSIONS_REGEX = 'uses-(.*) android:name=(.*)/'

ANDROID_DEBUGGABLE = 'android:*debuggable\s*=\s*"*true"*'

ANDROID_ALLOW_BACKUP = 'allowBackup\s*=\s*"*true"*'

ANDROID_FULL_BACKUP_CONTENT = 'android:*fullBackupContent\s*=\s*"true"*'

ANDROID_EXPORTED = '<([a-zA-Z]*) .*android:name="([a-zA-Z.]*)" .*android:exported="true"'


def get_permissions_regex():
    return PERMISSIONS_REGEX

def get_manifest_xml_regex():
    regex_array = {}
    regex_array['android_debuggable'] = ANDROID_DEBUGGABLE
    regex_array['android_allow_backup'] = ANDROID_ALLOW_BACKUP
    regex_array['android_full_backup'] = ANDROID_FULL_BACKUP_CONTENT
    regex_array['android_exported'] = ANDROID_EXPORTED

    return regex_array