#!/usr/bin/env python
import cgi
import cgitb
cgitb.enable()
import os

print 'content-type:text/html'
print ''

webdata=cgi.FieldStorage()

# Get filename here.
fileitem=webdata['filename']
#fileitem=webdata.getvalue('filename')

# Test if the file was uploaded
if fileitem.filename:
	# strip leading path from file name to avoid 
    # directory traversal attacks
	fn=os.path.basename(fileitem.filename.replace("\\","/"))
	#open("/tmp/"+fn,'wb').write(fileitem.file.read())
	open("/var/www/html/storages/"+st_name+"/"+fn,'wb').write(fileitem.file.read())
	print 'the file "'+fn+'" was uploaded successfully'
	#message="the file '"+fn+"' was uploaded successfully"
else:
	print 'No files were uploaded...'
	#message='No files were uploaded...'
