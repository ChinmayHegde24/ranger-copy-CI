#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License. See accompanying LICENSE file.
#

import os
import re
import sys
import errno
import shlex
import logging
import subprocess
import platform
import fileinput
import getpass
import shutil
from xml.etree import ElementTree as ET
from os.path import basename
from subprocess import Popen,PIPE
from datetime import date
from datetime import datetime
try: input = raw_input
except NameError: pass

os_name = platform.system()
os_name = os_name.upper()

RANGER_ADMIN_HOME = os.getenv("RANGER_ADMIN_HOME")
if RANGER_ADMIN_HOME is None:
	RANGER_ADMIN_HOME = os.getcwd()

def log(msg,type):
	if type == 'info':
		logging.info(" %s",msg)
	if type == 'debug':
		logging.debug(" %s",msg)
	if type == 'warning':
		logging.warning(" %s",msg)
	if type == 'exception':
		logging.exception(" %s",msg)
	if type == 'error':
		logging.error(" %s",msg)

def password_validation(password):
	if password:
		if re.search("[\\`'\"]",password):
			log("[E] password contains one of the unsupported special characters like \" ' \\ `","error")
			sys.exit(1)


def main(argv):
	FORMAT = '%(asctime)-15s %(message)s'
	logging.basicConfig(format=FORMAT, level=logging.DEBUG)
	ews_lib = os.path.join(RANGER_ADMIN_HOME,"ews","lib")
	app_home = os.path.join(RANGER_ADMIN_HOME,"ews","webapp")
	ranger_log = os.path.join(RANGER_ADMIN_HOME,"ews","logs")

	if os.environ['JAVA_HOME'] == "":
		log("[E] ---------- JAVA_HOME environment property not defined, aborting installation. ----------", "error")
		sys.exit(1)
	JAVA_BIN=os.path.join(os.environ['JAVA_HOME'],'bin','java')
	if os_name == "WINDOWS" :
		JAVA_BIN = JAVA_BIN+'.exe'
	if os.path.isfile(JAVA_BIN):
		pass
	else:
		while os.path.isfile(JAVA_BIN) == False:
			log("Enter java executable path: :","info")
			JAVA_BIN=input()
	log("[I] Using Java:" + str(JAVA_BIN),"info")

	JAVA_OPTS = os.getenv("JAVA_OPTS")
	if JAVA_OPTS is None:
		JAVA_OPTS = ""

	USERNAME = ''
	OLD_PASSWORD = ''
	NEW_PASSWORD=''

	if len(argv)==4:
		userName=argv[1]
		oldPassword=argv[2]
		newPassword=argv[3]
	else:
		log("[E] Invalid argument list.", "error")
		log("[I] Usage : python changepasswordutil.py <loginID> <currentPassword> <newPassword>","info")
		sys.exit(1)

	while userName == "":
		print("Enter user name:")
		userName=input()

	while oldPassword == "":
		oldPassword=getpass.getpass("Enter current password:")

	while newPassword == "":
		newPassword=getpass.getpass("Enter new password:")

	if oldPassword==newPassword:
		log("[E] Old Password and New Password argument are same. Exiting!!", "error")
		sys.exit(1)

	if userName != "" and oldPassword != "" and newPassword != "":
		password_validation(newPassword)
		if os_name == "LINUX":
			path = os.path.join("%s","WEB-INF","classes","conf:%s","WEB-INF","classes","lib","*:%s","WEB-INF",":%s","META-INF",":%s","WEB-INF","lib","*:%s","WEB-INF","classes",":%s","WEB-INF","classes","META-INF:%s/*")%(app_home ,app_home ,app_home, app_home, app_home, app_home ,app_home,ews_lib)
		elif os_name == "WINDOWS":
			path = os.path.join("%s","WEB-INF","classes","conf;%s","WEB-INF","classes","lib","*;%s","WEB-INF",";%s","META-INF",";%s","WEB-INF","lib","*;%s","WEB-INF","classes",";%s","WEB-INF","classes","META-INF" )%(app_home ,app_home ,app_home, app_home, app_home, app_home ,app_home)
		get_java_cmd = "%s %s -Dlogdir=%s -Dlogback.configurationFile=db_patch.logback.xml -cp %s org.apache.ranger.patch.cliutil.%s %s %s %s"%(JAVA_BIN,JAVA_OPTS,ranger_log,path,'ChangePasswordUtil','"'+userName+'"','"'+oldPassword+'"','"'+newPassword+'"')
		if os_name == "LINUX":
			ret = subprocess.call(shlex.split(get_java_cmd))
		elif os_name == "WINDOWS":
			ret = subprocess.call(get_java_cmd)
		if ret == 0:
			log("[I] Password updated successfully","info")
		else:
			log("[E] Unable to update password of user:"+userName,"error")
			sys.exit(1)
	else:
		log("[E] Input Error","error")

main(sys.argv)
