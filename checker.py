from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
def numcheck(num):
	if num:
		try:
			int(num)
		except :
			return False
		else:
			return True
	else:
		return False
def string(text):
	if text:
		if any(x.isdigit for x in text):
			return False
		elif not any(x.isdigit for x in text):
			return True
	else:
		return False
def ownerid(id):
	if id:
		try:
			int(id)
		except:
			return False
		else:
			if len(id) == 10:
				return True
			else:
				return False 
	else:
		return False
def sqlsearchquery(mode,text):
	er = None
	import sqlite3 as db
	conn = db.connect(r'data\db1.db')
	cur = conn.cursor()
	if mode == 1:
		er = 2
		if numcheck(text):
			cur.execute('select arch_num||"---"||name, arch_num from arch where arch_num like ?',('%'+text+'%',))
		else:
			return False , er ,0
	elif mode == 2:
		er = 3
		if numcheck(text):
			cur.execute('select arch_num||"---"||name ,arch_num from arch where piece_num like ?',('%'+text+'%',))
		else:
			return False , er , 0
	elif mode == 3:
		er = 4
		if string(text):
			cur.execute('select arch_num||"---"||name ,arch_num from arch where name like ? ',('%'+text+'%',))
		else:
			return False ,er ,0
	elif mode == 4:
		er = 1
		if numcheck(text):
			cur.execute('select arch_num||"---"||name, arch_num from arch where id_num like ?',('%'+text+'%',))
		else:
			return False , er, 0
	row = cur.fetchall()
	try:
		row[0]
	except:
		return False , er , 0
	else:
		lis = ['']
		idlis = ['']
		for i in row:
			lis.append(i[0])
			idlis.append(i[1]) 

		return True , lis , idlis
def e_sqlsearchquery(mode,text):
	er = None
	import sqlite3 as db
	conn = db.connect(r'data\db1.db')
	cur = conn.cursor()
	if mode == 1:
		er = 4
		if numcheck(text):
			cur.execute('select arch_num||"---"||name, arch_num from arch where arch_num like ?',('%'+text+'%',))
		else:
			return False , er ,0
	elif mode == 2:
		er = 6
		if numcheck(text):
			cur.execute('select arch_num||"---"||name ,arch_num from arch where piece_num like ?',('%'+text+'%',))
		else:
			return False , er , 0
	elif mode == 3:
		er = 2
		if string(text):
			cur.execute('select arch_num||"---"||name ,arch_num from arch where name like ? ',('%'+text+'%',))
		else:
			return False ,er ,0
	elif mode == 4:
		er = 5
		if numcheck(text):
			cur.execute('select arch_num||"---"||name, arch_num from arch where id_num like ?',('%'+text+'%',))
		else:
			return False , er, 0
	row = cur.fetchall()
	try:
		row[0]
	except:
		return False , er , 0
	else:
		lis = ['']
		idlis = ['']
		for i in row:
			lis.append(i[0])
			idlis.append(i[1]) 

		return True , lis , idlis
def d_sqlsearchquery(mode,text):
	er = None
	import sqlite3 as db
	conn = db.connect(r'data\db1.db')
	cur = conn.cursor()
	if mode == 1:
		er = 4
		if numcheck(text):
			cur.execute('select arch_num||"---"||name, arch_num from arch where arch_num like ?',('%'+text+'%',))
		else:
			return False , er ,0
	elif mode == 2:
		er = 6
		if numcheck(text):
			cur.execute('select arch_num||"---"||name ,arch_num from arch where piece_num like ?',('%'+text+'%',))
		else:
			return False , er , 0
	elif mode == 3:
		er = 2
		if string(text):
			cur.execute('select arch_num||"---"||name ,arch_num from arch where name like ? ',('%'+text+'%',))
		else:
			return False ,er ,0
	elif mode == 4:
		er = 5
		if numcheck(text):
			cur.execute('select arch_num||"---"||name, arch_num from arch where id_num like ?',('%'+text+'%',))
		else:
			return False , er, 0
	row = cur.fetchall()
	try:
		row[0]
	except:
		return False , er , 0
	else:
		lis = ['']
		idlis = ['']
		for i in row:
			lis.append(i[0])
			idlis.append(i[1]) 

		return True , lis , idlis
def sqlarchsearch(archid):
	import sqlite3
	conn = sqlite3.connect(r'data\db1.db')
	archcur = conn.cursor()
	flawcur = conn.cursor()
	imgcur =  conn.cursor()
	archcur.execute('select arch_num , piece_num , name , id_num ,location , id from arch where arch_num=?',(archid,))
	archrow =  archcur.fetchall()
	archlis = list(archrow[0])
	flawcur.execute('select flaw_name from flaws where arch_id=  (select id from arch where arch_num = ? and piece_num = ? and id_num = ?)',(archlis[0],archlis[1],archlis[3],))
	imgcur.execute('select img_directory from img where arch_id= (select id from arch where arch_num = ? and piece_num = ? and id_num = ?)',(archlis[0],archlis[1],archlis[3],))
	flawrow = flawcur.fetchall()
	imgrow = imgcur.fetchall()
	flawlis = []
	imglis = []
	for i in flawrow:
		flawlis.append(i[0])
	for i in imgrow:
		imglis.append(i[0])
	return archlis , flawlis , imglis
def openFileNameDialog():
    from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
    from PyQt5.QtGui import QIcon
    options = QFileDialog.Options()
    fileName, _ = QFileDialog.getOpenFileName("QFileDialog.getOpenFileName()", "","AllFiles(*)" ,options=options)
    if fileName:
       return fileName 
def createarch(archnum,piecenum,ownername,ownerid,userid,location='',flaws=[],imgs=[]):
	import shutil
	import os
	from datetime import datetime
	now = datetime.now()
	now2 = now
	now = now.strftime("%d/%m/%Y  %H:%M")
	import sqlite3 as db
	conn = db.connect(r'data\db1.db')
	conn.execute('insert into arch values ((select ifnull((max(id)+1),1) from arch),?,?,?,?,?,?,?)',(archnum,piecenum,ownername,ownerid,location,now,userid,))
	for i in flaws:
		conn.execute('insert into flaws values ((select max(id) from arch),?,?,?)',(i,now,userid,))
	for i,c in zip(imgs , range(len(imgs))):
		filename, file_extension = os.path.splitext(i)
		imgnewdir = r'img\%s'%(archnum+'_'+now2.strftime("%d_%m_%Y,%H_%M_%S")+str(c)+str(1)+str(file_extension))
		shutil.copy(i, imgnewdir)
		conn.execute('insert into img values ((select max(id) from arch),?,?,?)',(imgnewdir,now,userid,))
	conn.execute("insert into data_change values (?,?,3,?)",(userid,now,archnum,))
	conn.commit()
def digitonly(text):
	digit = ''
	for i in text:
		try:
			int(i)
		except:
			continue
		else:
			digit = digit + i
	return digit
def deletearch(userid,archid):
	if userid and archid:
		import sqlite3 as db
		import os
		from datetime import datetime
		now = datetime.now()
		now = now.strftime("%d/%m/%Y  %H:%M")
		conn = db.connect(r"data\db1.db")
		conn.execute("insert into data_change values (?,?,1,(select arch_num from arch where id =?))",(userid,now,archid,))
		conn.execute("delete from arch where id = ?",(archid,))
		conn.execute("delete from flaws where arch_id = ?",(archid,))
		delimgs = conn.cursor()
		delimgs.execute("select img_directory from img where arch_id = ?",(archid,))
		row = delimgs.fetchall()
		if row:
			imageslist = []
			for i in row:
				imageslist.append(i[0])
			for file in imageslist:
				try:
					os.remove(file)
				except:
					pass
		conn.execute("delete from img where arch_id = ?",(archid,))
		conn.commit()
def ma_changepasssql(oldpass,newpass,confirmpass,userid):
	import sqlite3 as db
	conn = db.connect(r"data\db1.db")
	row = conn.cursor()
	row.execute("select * from users where user_id = ? and user_pass=?",(userid,oldpass,))
	row = row.fetchall()
	if row and newpass == confirmpass:
		conn.execute("update users set user_pass = ? where user_id = ?",(newpass,userid,))
		conn.commit()
		return True
	else:
		return False
def m_addnewuser(username,userpass,userconfirmpass):
	if userpass == userconfirmpass:
		import sqlite3 as db
		from datetime import datetime
		now = datetime.now()
		now = now.strftime("%d/%m/%Y  %H:%M")
		conn = db.connect(r"data\db1.db")
		row = conn.cursor()
		row.execute("select * from users where users_name = ?",(username,))
		row = row.fetchall()
		if row :
			return False , 0
		else:
			conn.execute("insert into users values((select max(user_id)+1 from users),?,?,2,?)",(username,userpass,now))
			conn.commit()
			return True , 1
	else:
		return False , 1
def m_userstable():
	import sqlite3 as db
	conn = db.connect(r"data\db1.db")
	row = conn.cursor()
	row.execute("select users_name , user_pass , premname ,date from users , prem where user_prem = prem")
	row = row.fetchall()
	row2 = []
	for i in row:
		row2.append(list(i))
	return row2
def m_log():
	import sqlite3 as db
	conn = db.connect(r"data\db1.db")
	row = conn.cursor()
	row.execute("select users_name , time from users x , log y where x.user_id = y.user_id order by time DESC")
	row = row.fetchall()
	row2 = []
	for i in row:
		row2.append(list(i))
	return row2
def m_changedatalog():
	import sqlite3 as db
	conn = db.connect(r"data\db1.db")
	row = conn.cursor()
	row.execute("select users_name , cha , archid , y.date from users x , data_change y , changes z where x.user_id = y.user_id and z.num = y.changes order by y.date DESC")
	row = row.fetchall()
	row2 = []
	for i in row:
		row2.append(list(i))
	return row2
def blockusersql(userid):
	import sqlite3 as db
	conn = db.connect(r"data\db1.db")
	conn.execute("update users set user_prem = 3 where users_name = ?",(userid,))
	conn.commit()
def allowusersql(userid):
	import sqlite3 as db
	conn = db.connect(r"data\db1.db")
	conn.execute("update users set user_prem = 2 where users_name = ?",(userid,))
	conn.commit()
def m_mangeuserchange(username,newpass,confirmpass):
	import sqlite3 as db
	conn = db.connect(r"data\db1.db")
	row = conn.cursor()
	row.execute("select * from users where users_name=?",(username,))
	row = row.fetchall()
	if row and newpass == confirmpass:
		conn.execute("update users set user_pass = ? where users_name = ?",(newpass,username,))
		conn.commit()
		return True
	else:
		return False

