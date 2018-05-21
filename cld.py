#!/usr/bin/env python
import time
import getpass
import subprocess


print '#############################################'
print '#                                           #'
print '#            Welcome to the CloudX          #'
print '#                                           #'
print '#############################################'

time.sleep(2)
print '\nPlease select one of the Services : \n'

option= '''
	1.Software as a Servvice(Saas)
	2.Storage as a Service(Staas)
	3.Platform as a Service(Paas)
	4.Infrastructure as a Service(Iaas)

	'''
print option

ch=raw_input()
subprocess.call('clear')

if ch=='4':
	print '\nLoading.....\n'
	time.sleep(2)
	subprocess.call('clear')
	print '\n                     Infrastructure as a Service(Iaas)\n\n\n              '
	usrn=raw_input('Enter username : ')
	pswd=getpass.getpass('Enter password : ')
	
	if usrn=='root' and pswd=='toor123' :
		subprocess.call('clear')
		print 'Welcome '+ usrn.upper() +' You have successfully logged in...\n'
	else:
		subprocess.call('clear')		
		print '\nWrong credentials...\n'

















