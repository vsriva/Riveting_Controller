
import pickle
from pylab import *
import matplotlib.pyplot as plt
import time
import datetime
import logging

sample_NA=[]
sample_S=[]
sample_T=[]
sample_F=[]
sample_E=[]
sample_H=[]

def save_file(program) :
	
	print "Writing"

	prog_file = open(program[0]+".pkl","wb")
	pickle.dump(program,prog_file)
	prog_file.close()
	print "Writing Complete"


def load_file(filename):

	prog_file= open(filename+".pkl","rb")
	data=pickle.load(prog_file)
	print data
	prog_file.close()
	print "Loading "+filename+" Complete"
	return data



def graph_plot(filename,series1,series2):
	
	plt.plot([1,2,3,4])
	plt.ylabel('Series')
	plt.xlabel('Time')
	savefig(filename+'.png')

 
def alarm_punch(message):
	prog_file = open("alarm.pkl","a")
	alarm=(datetime.datetime.now().strftime("%d-%m-%y"),datetime.datetime.now().strftime("%H:%M"),message)
	print alarm
	pickle.dump(alarm,prog_file)
	prog_file.close()
	logging.basicConfig(filename='alarm.log',format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

	logging.warning(message)

def log_punch(program):
	prog_file = open("log.pkl","a")
	log=(datetime.datetime.now().strftime("%d-%m-%y"),datetime.datetime.now().strftime("%H:%M"),program)
	print log
	pickle.dump(log,prog_file)
	prog_file.close()
	
	logging.basicConfig(filename='program.log',format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

	logging.warning(program)




def find_usbdrive():

	disk_file=open ("/etc/mtab","rb")
	lines=disk_file.readlines()
	disk_file.close()	
	for line in lines:
		mtpt="".join(line.split()[1:2])
		found = mtpt.find("media")

	if found==1:
		print mtpt
		return mtpt
	else:
		print "Not Found"	
		return 0
 


#def sampling(frequency)

#requirement of logic engine for graph and table coding

#alarm_punch("Message")


	
