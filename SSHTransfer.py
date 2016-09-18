'''
Created on Sep 16, 2016

@author: dylan
'''
# -*- coding: utf-8 -*-
import os, paramiko, sys

##############################
#        Global
##############################


paramiko.util.log_to_file('/tmp/sftpConnection.log')


###############################
#       Progress Bar
###############################


# Print iterations progress
def printProgress (iteration, total, prefix = '', suffix = '', decimals = 1, barLength = 100):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        barLength   - Optional  : character length of bar (Int)
    """
    formatStr       = "{0:." + str(decimals) + "f}"
    percents        = formatStr.format(100 * (iteration / float(total)))
    filledLength    = int(round(barLength * iteration / float(total)))
    bar             = 'X' * filledLength + '-' * (barLength - filledLength)
    sys.stdout.write('\r%s |%s| %s%s %s' % (prefix, bar, percents, '%', suffix)),
    if iteration == total:
        sys.stdout.write('\n')
    sys.stdout.flush()


def createSftpConnection(ip,u,pw):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(ip, username=u, password=pw)
    except paramiko.SSHException:
        print "Connection Error"
    sftp = ssh.open_sftp()
    return sftp


def put_dir(sftp, source, target, numFiles, progress=0):
    ''' Uploads the contents of the source directory to the target path. The
        target directory needs to exists. All subdirectories in source are 
        created under target.
    '''
    


    for item in os.listdir(source):
        if os.path.isfile(os.path.join(source, item)):
            #sys.stdout.write("\rTransfering " + os.path.join(source, item) + " to %s/%s" % (target, item))
            sftp.put(os.path.join(source, item), '%s/%s' % (target, item))
            progress+=1
            printProgress(progress, numFiles, "Progress: ", "Complete", 1, 50)
        else:
            
            #sys.stdout.write("\rCreating directory %s/%s\n" % (target, item))
            remote_dir = ('%s/%s' % (target, item))
            try:
                sftp.mkdir(remote_dir)
            except IOError:
                sys.stdout.write( '%s already exists.' % remote_dir)
            progress = put_dir(sftp, os.path.join(source, item), '%s/%s' % (target, item), numFiles, progress)
    return progress


# uploads localPath via sftp to remotePath using username/password/ip/hostname
# If remote directory doesn't exist, it will be created.
def upload_sftp(u,p,ipHostname,localPath,remotePath):
    print("Creating SFTP Connection... \nConnection logs are written to /tmp/sftpConnection.log\nEstablishing connection to server...")
    transport = paramiko.Transport((ipHostname, 22))
    transport.connect(username = u, password = p)
    sftp = paramiko.SFTPClient.from_transport(transport)
    try:
        sftp.chdir(remotePath)  # Test if remote_path exists
    except IOError:
        sftp.mkdir(remotePath)  # Create remote_path
        ("Remote path created: " + remotePath)
        sftp.chdir(remotePath)
    print("Connected to " + ipHostname + "@" + remotePath)
   
    numFiles = sum([len(files) for r, d, files in os.walk(localPath)])
    put_dir(sftp, localPath, '.', numFiles)    # At this point, you are in remote_path in either case
    transport.close()

# if __name__ == "__main__":
#     
#     upload_sftp('root', '$G7nd7lf7$', '172.16.42.1', "/Users/dylan/Documents/workspace/PortalBuilder/Portal49815/", "/www/")
#     print("\n################################## \nSFTP deploy completed!")
    
