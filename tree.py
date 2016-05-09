#!/usr/bin/env python
from gi.repository import Gtk, GObject
import os
from main import load_file



class Tree:
	name=[]
	date=[]
	time=[]


	def tree_init(self):
		self.gladefile = "tree.glade"
		self.builder3 = Gtk.Builder()
		self.builder3.add_from_file(self.gladefile)
		self.builder3.connect_signals(self)
		self.file_select = self.builder3.get_object("file_select")
		self.liststore = self.builder3.get_object("liststore")

		
		self.tree = self.builder3.get_object("treeview")
		

	def on_file_select_OK_clicked(self, object, data=None):
		print "OK Clicked"
		sel = self.tree.get_selection()
		(model,rows)=sel.get_selected()
		self.filename="programs/"+model[rows][1]
		self.load_prog(load_file(self.filename))
		self.liststore.clear()
		self.name[:]=[]
		self.date[:]=[]
		self.time[:]=[]

		self.file_select.hide()

	def on_file_select_Cancel_clicked(self, object, data=None):
		print "Cancel Clicked"
		self.liststore.clear()
		self.name[:]=[]
		self.date[:]=[]
		self.time[:]=[]

		self.file_select.hide()


	def read_list (self,mode):
		os.system("ls -l programs| grep \""+mode+"_\" | awk '{print $8}'>f_time.txt")
		os.system("ls -l --full-time programs| grep \""+mode+"_\" | awk '{print $6}' >f_date.txt")
		os.system("ls -l programs| grep \""+mode+"_\" | awk '{print $9}' >f_name.txt")
		
	  
		prog_file1= open("f_name.txt","rb")
		prog_file2= open("f_date.txt","rb")
		prog_file3= open("f_time.txt","rb")
		i=0
		for line in prog_file1:
			self.name.append(line)
			

		for line in prog_file2:
			self.date.append(line)

		for line in prog_file3:
			i=i+1
			self.time.append(line)
			self.liststore.append([str(i),self.name[i-1].rstrip('.pkl\n'),self.date[i-1].rstrip('\n'),self.time[i-1].rstrip('\n')])
			print self.liststore,self.name[i-1]
		
		prog_file1.close()
		prog_file2.close()
		prog_file3.close()
		print "Loading Complete"

    


if __name__ == "__main__":
  main = Tree()
  Gtk.main()
