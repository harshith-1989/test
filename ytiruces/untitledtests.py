'''

import re

fh = open("/Users/a391141/Desktop/test.txt")
keys = ["allowBackup\s*[:=]\s*true","CN=Android Debug","android:debuggable = true","exported:true","permissions"]
for line in fh:
	for key in keys:
		if re.search(key,line):
			print (line.rstrip())
fh.close()
'''
import os
import zipfile
import Constants

'''
def unzip_app_and_move_contents_to_output_folder(zip_path,dst_directory):
	try:
		if os.path.exists(zip_path):
			zip_reference = zipfile.ZipFile(zip_path, 'r')
			ret = zip_reference.testzip()
			if ret is None:
				print ("zip s corrupt")
			else:
				zip_reference.extractall(Constants.OUTPUT_FOLDER)
			zip_reference.close()
			
	except Exception as e:
		if Constants.ENCRYPTED in str(e):
			print ("file is encrypted")
		if Constants.NOT_A_ZIP in str(e):
			print ("not a zip file")

'''
#unzip_app_and_move_contents_to_output_folder("/Users/a391141/a.zip","/Users/a391141/")
'''
import commands

isexecutable = commands.getoutput("if [ -x /Users/a391141/Downloads/Tool/tool-23rdNov/SecurityTestAutomation/testdata/2.2LandingGear/lib/arm64-v8a/libsqlc-native-driver.so  ]\nthen echo true\nfi")

if "true" in isexecutable:
    return True
else:
    return False
'''

import re

p = re.compile('uses-(.*) android:name="(.*)"')
#p = re.compile('uses')
s = """
   <uses-permission android:name="android.permission.CALL_PHONE"/>
    <uses-feature android:name="android.hardware.telephony" android:required="false"/>
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>
    <uses-permission android:name="android.permission.READ_CONTACTS"/>
    <uses-permission android:name="android.permission.WRITE_CONTACTS"/>
    <uses-permission android:name="android.permission.WRITE_SETTINGS"/>
    <uses-permission android:name="android.permission.GET_ACCOUNTS"/>
    <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION"/>
    <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION"/>
    <uses-feature android:name="android.hardware.location.gps"/>
    <uses-permission android:name="android.permission.RECORD_AUDIO"/>
    <uses-permission android:name="android.permission.MODIFY_AUDIO_SETTINGS"/>
    <uses-permission android:name="android.permission.READ_PHONE_STATE"/>
    <uses-permission android:name="android.permission.RECORD_VIDEO"/>
    <uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE"/>
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>
    <uses-permission android:name="android.permission.VIBRATE"/>
    <uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED"/>
    <uses-permission android:name="android.permission.INTERNET"/>
    <uses-permission android:name="com.google.android.providers.gsf.permission.READ_GSERVICES"/>
    <uses-feature android:glEsVersion="0x00020000" android:required="true"/>
    <uses-feature android:name="android.hardware.location"/>
    <meta-data android:name="android.support.VERSION" android:value="26.0.0-alpha1"/>
    <uses-permission android:name="android.permission.WAKE_LOCK"/>
    <uses-permission android:name="com.google.android.c2dm.permission.RECEIVE"/>
    <permission android:name="com.tcs.landinggear.permission.C2D_MESSAGE" android:protectionLevel="signature"/>
    <uses-permission android:name="com.tcs.landinggear.permission.C2D_MESSAGE"/>
"""
print(p.findall(s))