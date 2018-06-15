#!/usr/bin/env python
import cgi
import cgitb
import os,commands
cgitb.enable()
import mysql.connector as sql


#defining fieldarea to accept values
webdata=cgi.FieldStorage()
print '<div class="welcome_header">'
print '<h1 align="center">CloudMix</h1>'
#displaying username
print 'Welcome    '+uname
print '</div>'
print '\n\n\n'
#creating database connection
conn=sql.connect(user='root',password='ok',database='cloudmix',host='localhost')
#creating cursor object
cur=conn.cursor()

if signupbtn:
	print '<br><br><br>'
	print '<p align="center">Upload ur data in cloud storage<p>'
	print '<div class="upload_file" align="center">'
	print '<form action="http://127.0.0.1/cgi-bin/upload.py" enctype="multipart/form-data" method="post">'
	print '<input type="file" name="filename"><br><br>'
	print '<input type="submit" name="upload" value="Upload">'
	print '</form>'
	print '</div><br><br><br><br><br><br>'

	print '<p align="center">View ur cloud data<p>'
	print '<div class="view_file" align="center">'
	print '<form action="http://127.0.0.1/storages/'+st_name+'" method="post">'
	print '<input type="submit" name="viewdata" value="View Datas">'
	print '</form>'
	print '</div>'



elif loginbtn:
	cur.execute('select storage_name from userinfo where username=%s',(uname))
	out=cur.fetchall()
	print out



conn.close()



