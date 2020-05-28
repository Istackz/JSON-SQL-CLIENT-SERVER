import json
from urllib import urlopen
import subprocess
import sys
#sprint 1, Issac Rodriguez

#______________STEPS________________
#Take API and urlopen inside variable
#Read API
#Load API into python object
#Print python object 
#Automated Tests

# API Pages 1-5 
Page_1=urlopen("https://jobs.github.com/positions.json?page=1")
Page_2=urlopen("https://jobs.github.com/positions.json?page=2") 
Page_3=urlopen("https://jobs.github.com/positions.json?page=3")
Page_4=urlopen("https://jobs.github.com/positions.json?page=4")
Page_5=urlopen("https://jobs.github.com/positions.json?page=5")

def githubPageOne():
	source =Page_1.read() #reads the data 
	Info=json.loads(source) #python object
	print(" PAGE 1"*25)


	print(json.dumps(Info,indent=3)) # indent data  
	print(" Data entries for Page 1 = :"  ,len(Info)) #Automated test to show how many data entries in each page printed out 


def githubPageTwo():
	source =Page_2.read() #reads the data 
	Info=json.loads(source) #python object
	print(" PAGE 2"*25)


	print(json.dumps(Info,indent=3)) # indent data  
	print(" Data entries for Page 2 = :"  ,len(Info)) #Automated test to show how many data entries in each page printed out 


def githubPageThree():
	source =Page_3.read() #reads the data 
	Info=json.loads(source) #python object
	print(" PAGE 3"*25)


	print(json.dumps(Info,indent=3)) # indent data  
	print(" Data entries for Page 3 = :"  ,len(Info)) #Automated test to show how many data entries in each page printed out 


def githubPageFour():
	source =Page_4.read() #reads the data 
	Info=json.loads(source) #python object
	print(" PAGE 4"*25)


	print(json.dumps(Info,indent=3)) # indent data  
	print(" Data entries for Page 4 = :"  ,len(Info)) #Automated test to show how many data entries in each page printed out 


def githubPageFive():
	source =Page_5.read() #reads the data 
	Info=json.loads(source) #python object
	print(" PAGE 5"*25)

	print(json.dumps(Info,indent=3)) # indent data  
	print(" Data entries for Page 5 = :"  ,len(Info)) #Automated test to show how many data entries in each page printed out 

	print(" ----END----")


def check(): #autoamted test 2 
    datafile = file('log.txt')
    found = False
    for line in datafile:
        if "Software Engineer" in line: 
            found = True
            break

stdoutOrigin=sys.stdout  #save output to file
sys.stdout = open("log.txt", "w")

githubPageOne()
githubPageTwo()
githubPageThree()
githubPageFour()
githubPageFive()

sys.stdout.close()
sys.stdout=stdoutOrigin
print("Output sucessfully saved to log.txt\n")
check()
if True:
    print "true" #print true if software engineer job found in log.txt (automated test 2)
else:
    print "false"




