#!/usr/bin/env python

from gi.repository import Gtk
from pylab import *
import random
import matplotlib.pyplot as plt
import timeit
import csv

from main import find_usbdrive
from log import Excel_edit

class Table_Graph(Excel_edit):

 
	def table_graph_init(self):
		self.gladefile = "table_graph.glade"
		self.builder3 = Gtk.Builder()
		self.builder3.add_from_file(self.gladefile)
		self.builder3.connect_signals(self)
		self.graph_win = self.builder3.get_object("graph_win")
		self.table=self.builder3.get_object("table")
		self.table_table= self.builder3.get_object("table_table") 
		self.table_label= self.builder3.get_object("table_label") 
		

	
#table##################################################################
		self.table_exit= self.builder3.get_object("table_exit") 
		self.table_log= self.builder3.get_object("table_log") 
		self.table_xls= self.builder3.get_object("table_xls") 
		self.table_table= self.builder3.get_object("table_table")
		self.table_title=  self.builder3.get_object("table_title")

#graph_win##############################################################
		self.graph_win_disp= self.builder3.get_object("graph_win_disp") 
   
		self.graph_win_exit= self.builder3.get_object("graph_win_exit")    
		self.graph_win_prev= self.builder3.get_object("graph_win_prev")    
		self.graph_win_next= self.builder3.get_object("graph_win_next")
		self.graph_win_full_screen= self.builder3.get_object("graph_win_full_screen")    
		self.graph_win_save= self.builder3.get_object("graph_win_save")  	
		self.graph_win_title=self.builder3.get_object("graph_win_title")		

#fullscreen_graph##############################################################

		self.fullscreen_graph= self.builder3.get_object("fullscreen_graph")
    		self.fullscreen_img= self.builder3.get_object("fullscreen_graph_img")

		self.value_feed()

		
#		self.table.show_all()
		

#		self.graph_win_show()

	def value_feed(self):
	  	self.S_No=[]
	  	self.NA=[]
	  	self.S=[]
	  	self.T=[]
	  	self.F=[]
	  	self.E=[]
	  	self.H=[]

		for i in range(0,100):
			self.S_No.append(i)
			self.NA.append(random.randint(1,20))
			self.S.append(random.randint(30,40))
			self.T.append(i)
			self.F.append(random.randint(40,60))
			self.E.append(random.randint(60,80))
			self.H.append(random.randint(80,90))

		self.graph_filename="Trial"
		self.table_filename="Trial"
		self.plot_graph()
		self.table_new()	

	def plot_graph(self):
		self.graph_f_name=[]
		self.plot_y=[]
		self.y_label=[]
		self.graph_index_no=0
		fig=plt.gcf()
		fig.set_size_inches(9.2,3.5)

		self.plot_y.append(self.S)
		self.plot_x=self.T
		plt.plot(self.T,self.S)
		plt.grid(b=None, which='major',axis='both')

		self.x_label='Time (msec)'
		self.y_label.append('S (mm)')

		plt.ylabel(self.y_label[0])
		plt.xlabel(self.x_label)
		graph_name=self.graph_filename+"_S.png"
		self.graph_f_name.append(graph_name)
		savefig("plot/"+graph_name,bbox_inches='tight')
		
		plt.clf()
		self.plot_y.append(self.F)
		plt.plot(self.T,self.F)
		plt.grid(b=None, which='major',axis='both')

		self.y_label.append('F (kN)')

		plt.ylabel(self.y_label[1])
		plt.xlabel(self.x_label)
		graph_name=self.graph_filename+"_F.png"
		self.graph_f_name.append(graph_name)
		savefig("plot/"+graph_name,bbox_inches='tight')

		plt.clf()
		self.plot_y.append(self.E)
		plt.plot(self.T,self.E)
		plt.grid(b=None, which='major',axis='both')
		plt.ylabel('E (mm)')
		plt.xlabel('Time (msec)')

		self.y_label.append('E (mm)')

		plt.ylabel(self.y_label[2])
		plt.xlabel(self.x_label)
		graph_name=self.graph_filename+"_E.png"
		self.graph_f_name.append(graph_name)
		savefig("plot/"+graph_name,bbox_inches='tight')

		plt.clf()
		self.plot_y.append(self.NA)
		plt.plot(self.T,self.NA)
		plt.grid(b=None, which='major',axis='both')
		plt.ylabel('NA (mm)')
		plt.xlabel('Time (msec)')

		self.y_label.append('NA (mm)')

		plt.ylabel(self.y_label[3])
		plt.xlabel(self.x_label)
		graph_name=self.graph_filename+"_NA.png"
		self.graph_f_name.append(graph_name)
		savefig("plot/"+graph_name,bbox_inches='tight')
		
	def graph_win_show(self):
		self.graph_filename=self.graph_f_name[0]		
		self.graph_win_title.set_text("Graph: "+self.graph_filename.rpartition('.')[0])		
		self.graph_win_disp.set_from_file("plot/"+self.graph_filename)
		self.graph_win.show_all()

	def graph_fullscreen_show(self):
		print "fullscreen_img"
		plt.clf()
		fig=plt.gcf()
		fig.set_size_inches(10.67,6.4)
		plt.plot(self.plot_x,self.plot_y[self.graph_index_no])
		plt.grid(b=None, which='major',axis='both')
		plt.ylabel(self.y_label[self.graph_index_no])
		plt.xlabel(self.x_label)

		graph_full=self.graph_f_name[self.graph_index_no]
		savefig("plot/FUll"+graph_full,bbox_inches='tight')
		self.fullscreen_img.set_from_file("plot/FUll"+graph_full)
		self.fullscreen_graph.show()
		self.fullscreen_graph.fullscreen()
		
#GRAPH_WIN
###################################################################
	def on_graph_win_exit_clicked(self, object, data="None"):
		print "graph_back_exit_clicked"
		self.main_screen.show()
		self.graph_win.hide()

	def on_graph_win_prev_clicked(self, object, data="None"):
		print "graph_win_prev_clicked"
		if self.graph_index_no==0:
			self.graph_index_no=4
		self.graph_index_no=self.graph_index_no - 1		
		self.graph_filename=self.graph_f_name[self.graph_index_no]
		self.graph_win_title.set_text("Graph: "+self.graph_filename.rpartition('.')[0])		
		self.graph_win_disp.set_from_file("plot/"+self.graph_filename)

	def on_graph_win_next_clicked(self, object, data="None"):
		print "graph_win_next_clicked"
		if self.graph_index_no==3:
			self.graph_index_no=-1

		self.graph_index_no=self.graph_index_no + 1
		self.graph_filename=self.graph_f_name[self.graph_index_no]		
		self.graph_win_title.set_text("Graph: "+self.graph_filename.rpartition('.')[0])		
		self.graph_win_disp.set_from_file("plot/"+self.graph_filename)

	def on_graph_win_full_screen_clicked(self, object, data="None"):
		print "graph_win_full_screen_clicked"
		self.graph_win.hide()
		self.graph_fullscreen_show()
		
	def on_graph_win_save_clicked(self, object, data="None"): #pendrive save
		print "graph_win_save_clicked"
		self.exp_path=find_usbdrive()
		if self.exp_path==0:
			print "USB Drive Not found"
		else:
			self.path="mkdir "+self.exp_path+"/plots"
			os.system(self.path)
			os.system("cp -r plots/"+self.graph_filename+"* "+self.exp_path+"/plots")
		
		

#GRAPH_FULLSCREEN
###################################################################

	def on_fullscreen_graph_img_button_press_event(self, object, data="None"):
		print "Graph fullscreen clicked"
		self.fullscreen_graph.hide()
		self.graph_win.show()		

	def on_fullscreen_graph_event_button_press_event(self, object, data="None"):
		print "fullscreen_graph_event clicked"
		self.fullscreen_graph.hide()
		self.graph_win.show()		

#TABLE
###################################################################

	def on_table_exit_clicked(self, object, data="None"):
		print "table_exit_clicked"
		self.main_screen.show()
		self.table.hide()


	def on_table_export_clicked(self, object, data="None"):
		print "table_save_clicked"
		self.exp_path=find_usbdrive()
		if self.exp_path==0:
			print "USB Drive Not found"
		else:

			self.path="mkdir "+self.exp_path+"/table"
			os.system(self.path)
			os.system("cp -r table/"+self.table_xls_filename+".xls "+self.exp_path+"/table")

	def on_table_xls_clicked(self, object, data="None"):
		print "table_xls_clicked"
		print self.table_filename
		
		self.table_xls_filename=self.table_filename
		self.excel_init()
		self.add_entry ()

		
###################################################################
	def table_new(self):
		self.table_table.resize(100,7)
		self.table_title.set_text("Table: "+self.table_filename.rpartition('.')[0])		

		for i in range(0,100):
#			print "Row "+str(i)

			part1="label_h"+str(i)+"_0 = Gtk.Label(label=\""+str(self.S_No[i]+1)+"\")"
			exec(part1)
			part="self.table_table.attach(label_h"+str(i)+"_0, 0, 1, "+str(i)+", "+str(i+1)+")"
			exec(part) 

			part1="label_h"+str(i)+"_1 = Gtk.Label(label=\""+str(self.NA[i])+"\")"
			exec(part1)
			part="self.table_table.attach(label_h"+str(i)+"_1, 1, 2, "+str(i)+", "+str(i+1)+")"
			exec(part) 

			part1="label_h"+str(i)+"_2 = Gtk.Label(label=\""+str(self.S[i])+"\")"
			exec(part1)
			part="self.table_table.attach(label_h"+str(i)+"_2, 2, 3, "+str(i)+", "+str(i+1)+")"
			exec(part) 

			part1="label_h"+str(i)+"_3 = Gtk.Label(label=\""+str(self.T[i])+"\")"
			exec(part1)
			part="self.table_table.attach(label_h"+str(i)+"_3, 3, 4, "+str(i)+", "+str(i+1)+")"
			exec(part) 

			part1="label_h"+str(i)+"_4 = Gtk.Label(label=\""+str(self.F[i])+"\")"
			exec(part1)
			part="self.table_table.attach(label_h"+str(i)+"_4, 4, 5, "+str(i)+", "+str(i+1)+")"
			exec(part) 

			part1="label_h"+str(i)+"_5 = Gtk.Label(label=\""+str(self.E[i])+"\")"
			exec(part1)
			part="self.table_table.attach(label_h"+str(i)+"_5, 5, 6, "+str(i)+", "+str(i+1)+")"
			exec(part) 

			part1="label_h"+str(i)+"_6 = Gtk.Label(label=\""+str(self.H[i])+"\")"
			exec(part1)
			part="self.table_table.attach(label_h"+str(i)+"_6, 6, 7, "+str(i)+", "+str(i+1)+")"
			exec(part) 

			


    

if __name__ == "__main__":
	main = Table_Graph()
	Gtk.main()

  
