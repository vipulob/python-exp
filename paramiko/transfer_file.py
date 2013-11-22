
# Tested on Python 2.7(Ubuntu)

import paramiko


ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect("192.168.60.1", username="username", password="password")

sftp = ssh.open_sftp()

# Transfer localfile to remote machine with name as remotefile
sftp.put("localfile","remotefile")

ssh.close()
