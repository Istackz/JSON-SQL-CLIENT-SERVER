import sqlite3 
import random
import time
import datetime
import matplotlib.pyplot as pyplot
import matplotlib.dates as mdates


conn=sqlite3.connect("Datatable.db")

c=conn.cursor()

def CreateTable():
	c.execute(""" CREATE TABLE IF NOT EXISTS DataTable(Name TEXT, timer REAL, TimerStamp REAL, age TEXT) """)
	conn.commit()
	print("DataTable Sucessfull")

def HardCodeTable():
	
	c.execute(""" INSERT INTO DataTable VALUES('Name','timer','TimerStamp','age') """)
	print("HardCode sucessfull")
	conn.commit()
	data=c.fetchall()
	for row in c.fetchall():
		print(row)


def DynamicData():
	Name="Issac"
	timer=time.time()
	TimerStamp=str(datetime.datetime.fromtimestamp(timer).strftime('%M:%d:%Y'))
	age=random.randrange(18,30)
	c.execute(""" INSERT INTO DataTable(Name,timer,TimerStamp,age) VALUES(?, ?, ?, ?) """, (Name,timer,TimerStamp,age))
	conn.commit()
	print("DynamicData Sucessfull ")

def ParseData():
	c.execute(""" SELECT Timerstamp,age FROM DataTable """)
	data=c.fetchall
	for row in data():
		print(row)

def GraphData():
	c.execute(""" SELECT timer,age FROM DataTable """)
	dates=[]
	age=[]
	for row in c.fetchall():

		dates.append(datetime.datetime.fromtimestamp(row[0]))
		timer.append(row[1])
		plt.plot_date(Timerstamp,age,'-')
		plt.show()
		conn.commit()

		dates.append(datetime.datetime.fromtimestamp(row[0]))
		value.append(row[1])
	plt.plot_date(dates,value,'-')
	print("GraphData Sucessfull")
	plt.show()





#CreateTable()
#HardCodeTable()
#DynamicData()
ParseData()
GraphData()
c.close()
conn.close()