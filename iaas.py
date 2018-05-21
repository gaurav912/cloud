#!/usr/bin/env python
import cgi
import cgitb
ctigb.enable()
import commands

print 'Content-type:text/html'
print ''

web_data=cgi.FieldStorage()

# extracting input names from webpage

os_name=web_data.getFieldStorage('os')
os_ram=web_data.getFieldStorage('or')
os_cpu=web_data.getFieldStorage('oc')
os_hdd=web_data.getFieldStorage('oh')

os_launch='sudo virt-install --CDROM /tails-i386-2.10.iso  --ram '+os_ram+'  --vcpu '+os_cpu+' --nodisk  --name '+os_name

print commands.getoutput(os_launch)
