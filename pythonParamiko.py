import paramiko
import os
import sys

print sys.version, sys.version_info
print "hello world"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect('10.20.187.117',22,'root','password')
stdin, stdout,stderr = ssh.exec_command('ls')

for testNumber in stdout.readlines():
    #print testNumber
    if testNumber.startswith('iptable'):
        print testNumber
        aa = 'cat %s' % testNumber
        stdin, stdout,stderr = ssh.exec_command('cat %s' % testNumber)
        print stdout.read()

#print stdout.readlines()
ssh.close()