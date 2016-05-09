#!/usr/bin/env python
import subprocess, os, time, pickle

from gi.repository import Gtk
from keypad import Keypad
from main import save_file,load_file

alarm=[]
log=[]

def alarm_retrieve(filename):
	prog_file= open(filename+".pkl","rb")
	try:
		while True:
			alarm.append(pickle.load(prog_file))
	except EOFError:
		print "End of File"
	print alarm
	prog_file.close()
	print "Loading "+filename+" Complete"
	return alarm

def log_retrieve(filename):
	prog_file= open(filename+".pkl","rb")
	try:
		while True:
			log.append(pickle.load(prog_file))
	except EOFError:	
		print "End of File"

	print log
	prog_file.close()
	print "Loading "+filename+" Complete"
	return log


def table_retrieve(filename):
	prog_file= open(filename+".pkl","rb")
	try:
		while True:
			table.append(pickle.load(prog_file))
	except EOFError:	
		print "End of File"

	print table
	prog_file.close()
	print "Loading "+filename+" Complete"
	return table
