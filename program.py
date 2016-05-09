#!/usr/bin/env python

from numpad import Numpad
from keypad import Keypad
from main import *
from sett_conf import *
from tree import Tree
from table_graph import Table_Graph 

import pickle
import subprocess, os, time
from datetime import *


from gi.repository import Gtk, GObject
password="newworld"

counter=("","","")
process_counter=("","","")


class main_GUI(Keypad,Numpad,Sett_GUI,Tree,Table_Graph):

	global counter
	global process_counter

  
	numst=""
	time_counter=0
	admin_resp=""
	def __init__(self):
		global time_sett
		self.sett_init()
		self.tree_init()
		self.table_graph_init()
		system_riv_time=datetime.strptime("01-01-2012 00:00:00","%d-%m-%Y %H:%M:%S")
		system_op_time=datetime.strptime("01-01-2012 00:00:00","%d-%m-%Y %H:%M:%S")

		self.recall_time()

		self.flag=0



#Windows###############################################
    	
		self.main_screen = self.builder2.get_object("main_screen")
		self.Mode_sel = self.builder2.get_object("Mode_sel")
		self.S_mode = self.builder2.get_object("S_mode")
		self.S1_setup = self.builder2.get_object("S1_setup")
		self.S1_conf = self.builder2.get_object("S1_conf")
		self.S1_cycle = self.builder2.get_object("S1_cycle")
		self.T_mode = self.builder2.get_object("T_mode")
		self.T1_cycle = self.builder2.get_object("T1_cycle")
		self.T1_conf = self.builder2.get_object("T1_conf")
		self.T1_setup = self.builder2.get_object("T1_setup")
		self.F_mode = self.builder2.get_object("F_mode")
		self.F1_setup = self.builder2.get_object("F1_setup")
		self.F1_conf = self.builder2.get_object("F1_conf")
		self.F1_cycle = self.builder2.get_object("F1_cycle")
		self.E_mode = self.builder2.get_object("E_mode")
		self.E1_setup = self.builder2.get_object("E1_setup")
		self.E1_conf = self.builder2.get_object("E1_conf")
		self.E1_cycle = self.builder2.get_object("E1_cycle")
		self.N_mode = self.builder2.get_object("N_mode")
		self.N1_setup = self.builder2.get_object("N1_setup")
		self.N1_conf = self.builder2.get_object("N1_conf")
		self.N1_cycle = self.builder2.get_object("N1_cycle")
		self.H_mode = self.builder2.get_object("H_mode")
		self.H1_setup = self.builder2.get_object("H1_setup")
		self.H1_conf = self.builder2.get_object("H1_conf")
		self.H1_cycle = self.builder2.get_object("H1_cycle") 

		"""
		self.main_screen.fullscreen()
		self.Mode_sel.fullscreen()
		self.S_mode.fullscreen()
		self.S1_setup.fullscreen()
		self.S1_conf.fullscreen()	
		self.S1_cycle.fullscreen()
		self.T_mode.fullscreen()
		self.T1_cycle.fullscreen()
		self.T1_conf.fullscreen()
		self.T1_setup.fullscreen()
		self.F_mode.fullscreen()
		self.F1_setup.fullscreen()
		self.F1_conf.fullscreen()
		self.F1_cycle.fullscreen()
		self.E_mode.fullscreen()
		self.E1_setup.fullscreen()
		self.E1_conf.fullscreen()
		self.E1_cycle.fullscreen()
		self.N_mode.fullscreen()
		self.N1_setup.fullscreen()
		self.N1_conf.fullscreen()
		self.N1_cycle.fullscreen()
		self.H_mode.fullscreen()
		self.H1_setup.fullscreen()
		self.H1_conf.fullscreen()
		self.H1_cycle.fullscreen()"""

#Dummy Objects#########################################################

		self.curr_window = self.builder2.get_object("main_screen") 
		self.curr_cycle = self.builder2.get_object("S1_cycle") 
		self.curr_prog=""
		self.curr_entry = self.builder2.get_object("S1_setup_NA_toll")
		self.curr_mode1 = self.builder2.get_object("S1_setup")
		self.curr_mode2 = self.builder2.get_object("S1_conf")
		self.curr_mode3 = self.builder2.get_object("S1_cycle")  
  
		self.numpad = self.builder2.get_object("numpad")
		self.keypad = self.builder2.get_object("keypad")
		self.aboutdialog = self.builder2.get_object("aboutdialog1")
		self.result2 = self.builder2.get_object("num_disp")
		self.result1 = self.builder2.get_object("keypad_disp")
		
		self.numpad.fullscreen()
		self.keypad.fullscreen()
		self.aboutdialog.fullscreen()
		self.result2 = self.builder2.get_object("num_disp")
		self.result1 = self.builder2.get_object("keypad_disp")

#Entry##############################################################

		self.F1_setup_E_toll = self.builder2.get_object("F1_setup_E_toll")	
		self.F1_setup_T_toll = self.builder2.get_object("F1_setup_T_toll")	

		self.F1_conf_E_toll= self.builder2.get_object("F1_conf_E_toll")	
		self.F1_conf_E = self.builder2.get_object("F1_conf_E")	
		self.F1_conf_T_toll= self.builder2.get_object("F1_conf_T_toll")	
		self.F1_conf_F= self.builder2.get_object("F1_conf_F")	
		self.F1_conf_T = self.builder2.get_object("F1_conf_T")	
		self.E1_setup_T_toll= self.builder2.get_object("E1_setup_T_toll")	
		self.E1_setup_F_toll= self.builder2.get_object("E1_setup_F_toll")	

		self.E1_conf_T= self.builder2.get_object("E1_conf_T")	
		self.E1_conf_F= self.builder2.get_object("E1_conf_F")	
		self.E1_conf_E= self.builder2.get_object("E1_conf_E")	
		self.E1_conf_T_toll= self.builder2.get_object("E1_conf_T_toll")	
		self.E1_conf_F_toll= self.builder2.get_object("E1_conf_F_toll")	

		self.N1_setup_T_toll= self.builder2.get_object("N1_setup_T_toll")	

		self.N1_conf_T_toll= self.builder2.get_object("N1_conf_T_toll")	
		self.N1_conf_T= self.builder2.get_object("N1_conf_T")	

		self.H1_setup_T_toll= self.builder2.get_object("H1_setup_T_toll")	
		self.H1_setup_F_toll= self.builder2.get_object("H1_setup_F_toll")	

		self.H1_conf_T= self.builder2.get_object("H1_conf_T")	
		self.H1_conf_F= self.builder2.get_object("H1_conf_F")	
		self.H1_conf_H= self.builder2.get_object("H1_conf_H")	
		self.H1_conf_T_toll= self.builder2.get_object("H1_conf_T_toll")	
		self.H1_conf_F_toll= self.builder2.get_object("H1_conf_F_toll")	

		self.S1_setup_NA_toll= self.builder2.get_object("S1_setup_NA_toll")	
		self.S1_setup_T_toll= self.builder2.get_object("S1_setup_T_toll")	
		self.S1_setup_F_toll= self.builder2.get_object("S1_setup_F_toll")	

		self.S1_conf_NA= self.builder2.get_object("S1_conf_NA")
		self.S1_conf_S= self.builder2.get_object("S1_conf_S")
		self.S1_conf_T= self.builder2.get_object("S1_conf_T")
		self.S1_conf_F= self.builder2.get_object("S1_conf_F")
		self.S1_conf_NA_toll= self.builder2.get_object("S1_conf_NA_toll")
		self.S1_conf_T_toll= self.builder2.get_object("S1_conf_T_toll")
		self.S1_conf_F_toll= self.builder2.get_object("S1_conf_F_toll")
	
        
		self.T1_conf_T = self.builder2.get_object("T1_conf_T")	

		self.T1_cycle_T = self.builder2.get_object("T1_cycle_T")	

#Display Labels############################################

		self.F1_cycle_E_toll= self.builder2.get_object("F1_cycle_E_toll")	
		self.F1_cycle_E = self.builder2.get_object("F1_cycle_E")	
		self.F1_cycle_T_toll= self.builder2.get_object("F1_cycle_T_toll")	
		self.F1_cycle_F= self.builder2.get_object("F1_cycle_F")	
		self.F1_cycle_T = self.builder2.get_object("F1_cycle_T")	

		self.F1_setup_E = self.builder2.get_object("F1_setup_E")	
		self.F1_setup_F= self.builder2.get_object("F1_setup_F")	
		self.F1_setup_T = self.builder2.get_object("F1_setup_T")	

		self.E1_cycle_T= self.builder2.get_object("E1_cycle_T")	
		self.E1_cycle_F= self.builder2.get_object("E1_cycle_F")	
		self.E1_cycle_E= self.builder2.get_object("E1_cycle_E")	
		self.E1_cycle_T_toll= self.builder2.get_object("E1_cycle_T_toll")	
		self.E1_cycle_F_toll= self.builder2.get_object("E1_cycle_F_toll")

		self.E1_setup_T= self.builder2.get_object("E1_setup_T")	
		self.E1_setup_F= self.builder2.get_object("E1_setup_F")	
		self.E1_setup_E= self.builder2.get_object("E1_setup_E")	

		self.H1_cycle_T= self.builder2.get_object("H1_cycle_T")	
		self.H1_cycle_F= self.builder2.get_object("H1_cycle_F")	
		self.H1_cycle_H= self.builder2.get_object("H1_cycle_H")	
		self.H1_cycle_T_toll= self.builder2.get_object("H1_cycle_T_toll")	
		self.H1_cycle_F_toll= self.builder2.get_object("H1_cycle_F_toll")	

		self.H1_setup_T= self.builder2.get_object("H1_setup_T")	
		self.H1_setup_F= self.builder2.get_object("H1_setup_F")	
		self.H1_setup_H= self.builder2.get_object("H1_setup_H")	


		self.N1_cycle_T_toll= self.builder2.get_object("N1_cycle_T_toll")	
		self.N1_cycle_T= self.builder2.get_object("N1_cycle_T")	

		self.N1_setup_T= self.builder2.get_object("N1_setup_T")	

		self.S1_cycle_NA= self.builder2.get_object("S1_cycle_NA")
		self.S1_cycle_S= self.builder2.get_object("S1_cycle_S")
		self.S1_cycle_T= self.builder2.get_object("S1_cycle_T")
		self.S1_cycle_F= self.builder2.get_object("S1_cycle_F")
		self.S1_cycle_E= self.builder2.get_object("S1_cycle_E")

		self.S1_cycle_NA_toll= self.builder2.get_object("S1_cycle_NA_toll")
		self.S1_cycle_S_toll= self.builder2.get_object("S1_cycle_S_toll")
		self.S1_cycle_T_toll= self.builder2.get_object("S1_cycle_T_toll")
		self.S1_cycle_F_toll= self.builder2.get_object("S1_cycle_F_toll")
		self.S1_cycle_E_toll= self.builder2.get_object("S1_cycle_E_toll")

		self.S1_setup_NA= self.builder2.get_object("S1_setup_NA")
		self.S1_setup_S= self.builder2.get_object("S1_setup_S")
		self.S1_setup_T= self.builder2.get_object("S1_setup_T")
		self.S1_setup_F= self.builder2.get_object("S1_setup_F")
		self.S1_setup_E= self.builder2.get_object("S1_setup_E")


		self.T1_cycle_T = self.builder2.get_object("T1_cycle_T")	

		self.T1_setup_T = self.builder2.get_object("T1_setup_T")
	
#General labels############################################

		self.F1_cycle_OK = self.builder2.get_object("F1_cycle_OK")	
		self.F1_cycle_NOK = self.builder2.get_object("F1_cycle_NOK")	
		self.F1_cycle_A = self.builder2.get_object("F1_cycle_A")	
		self.F1_cycle_B = self.builder2.get_object("F1_cycle_B")	

		self.F1_conf_OK = self.builder2.get_object("F1_conf_OK")	
		self.F1_conf_NOK = self.builder2.get_object("F1_conf_NOK")	
		self.F1_conf_A = self.builder2.get_object("F1_conf_A")	
		self.F1_conf_B = self.builder2.get_object("F1_conf_B")	


		self.F1_setup_OK = self.builder2.get_object("F1_setup_OK")	
		self.F1_setup_NOK = self.builder2.get_object("F1_setup_NOK")	
		self.F1_setup_A = self.builder2.get_object("F1_setup_A")	
		self.F1_setup_B = self.builder2.get_object("F1_setup_B")	


		self.E1_cycle_OK = self.builder2.get_object("E1_cycle_OK")	
		self.E1_cycle_NOK = self.builder2.get_object("E1_cycle_NOK")	
		self.E1_cycle_A = self.builder2.get_object("E1_cycle_A")	
		self.E1_cycle_B = self.builder2.get_object("E1_cycle_B")	

		self.E1_conf_OK = self.builder2.get_object("E1_conf_OK")	
		self.E1_conf_NOK = self.builder2.get_object("E1_conf_NOK")	
		self.E1_conf_A = self.builder2.get_object("E1_conf_A")	
		self.E1_conf_B = self.builder2.get_object("E1_conf_B")	

		self.E1_setup_OK = self.builder2.get_object("E1_setup_OK")	
		self.E1_setup_NOK = self.builder2.get_object("E1_setup_NOK")	
		self.E1_setup_A = self.builder2.get_object("E1_setup_A")	
		self.E1_setup_B = self.builder2.get_object("E1_setup_B")	
	

		self.H1_cycle_OK = self.builder2.get_object("H1_cycle_OK")	
		self.H1_cycle_NOK = self.builder2.get_object("H1_cycle_NOK")	
		self.H1_cycle_A = self.builder2.get_object("H1_cycle_A")	
		self.H1_cycle_B = self.builder2.get_object("H1_cycle_B")	

		self.H1_conf_OK = self.builder2.get_object("H1_conf_OK")	
		self.H1_conf_NOK = self.builder2.get_object("H1_conf_NOK")	
		self.H1_conf_A = self.builder2.get_object("H1_conf_A")	
		self.H1_conf_B = self.builder2.get_object("H1_conf_B")	


		self.H1_setup_OK = self.builder2.get_object("H1_setup_OK")	
		self.H1_setup_NOK = self.builder2.get_object("H1_setup_NOK")	
		self.H1_setup_A = self.builder2.get_object("H1_setup_A")	
		self.H1_setup_B = self.builder2.get_object("H1_setup_B")	



		self.S1_cycle_OK = self.builder2.get_object("S1_cycle_OK")	
		self.S1_cycle_NOK = self.builder2.get_object("S1_cycle_NOK")	
		self.S1_cycle_A = self.builder2.get_object("S1_cycle_A")	
		self.S1_cycle_B = self.builder2.get_object("S1_cycle_B")	

		self.S1_conf_OK = self.builder2.get_object("S1_conf_OK")	
		self.S1_conf_NOK = self.builder2.get_object("S1_conf_NOK")	
		self.S1_conf_A = self.builder2.get_object("S1_conf_A")	
		self.S1_conf_B = self.builder2.get_object("S1_conf_B")	


		self.S1_setup_OK = self.builder2.get_object("S1_setup_OK")	
		self.S1_setup_NOK = self.builder2.get_object("S1_setup_NOK")	
		self.S1_setup_A = self.builder2.get_object("S1_setup_A")	
		self.S1_setup_B = self.builder2.get_object("S1_setup_B")	


		self.T1_cycle_OK = self.builder2.get_object("T1_cycle_OK")	
		self.T1_cycle_NOK = self.builder2.get_object("T1_cycle_NOK")	
		self.T1_cycle_A = self.builder2.get_object("T1_cycle_A")	
		self.T1_cycle_B = self.builder2.get_object("T1_cycle_B")	

		self.T1_conf_OK = self.builder2.get_object("T1_conf_OK")	
		self.T1_conf_NOK = self.builder2.get_object("T1_conf_NOK")	
		self.T1_conf_A = self.builder2.get_object("T1_conf_A")	
		self.T1_conf_B = self.builder2.get_object("T1_conf_B")	

		self.T1_setup_OK = self.builder2.get_object("T1_setup_OK")	
		self.T1_setup_NOK = self.builder2.get_object("T1_setup_NOK")	
		self.T1_setup_A = self.builder2.get_object("T1_setup_A")	
		self.T1_setup_B = self.builder2.get_object("T1_setup_B")	

		self.N1_cycle_OK = self.builder2.get_object("N1_cycle_OK")	
		self.N1_cycle_NOK = self.builder2.get_object("N1_cycle_NOK")	
		self.N1_cycle_A = self.builder2.get_object("N1_cycle_A")	
		self.N1_cycle_B = self.builder2.get_object("N1_cycle_B")	

		self.N1_conf_OK = self.builder2.get_object("N1_conf_OK")	
		self.N1_conf_NOK = self.builder2.get_object("N1_conf_NOK")	
		self.N1_conf_A = self.builder2.get_object("N1_conf_A")	
		self.N1_conf_B = self.builder2.get_object("N1_conf_B")	


		self.N1_setup_OK = self.builder2.get_object("N1_setup_OK")	
		self.N1_setup_NOK = self.builder2.get_object("N1_setup_NOK")	
		self.N1_setup_A = self.builder2.get_object("N1_setup_A")	
		self.N1_setup_B = self.builder2.get_object("N1_setup_B")	

		self.main_screen_date_and_time = self.builder2.get_object("main_screen_date_and_time")	

#Headings##################################################
   
		self.S1_setup_head = self.builder2.get_object("S1_setup_head")	
		self.S1_conf_head = self.builder2.get_object("S1_conf_head")	
		self.S1_cycle_head = self.builder2.get_object("S1_cycle_head")	
		self.T1_cycle_head = self.builder2.get_object("T1_cycle_head")	
		self.T1_conf_head = self.builder2.get_object("T1_conf_head")	
		self.T1_setup_head = self.builder2.get_object("T1_setup_head")	
		self.F1_setup_head = self.builder2.get_object("F1_setup_head")	
		self.F1_conf_head = self.builder2.get_object("F1_conf_head")	
		self.F1_cycle_head = self.builder2.get_object("F1_cycle_head")	
		self.E1_setup_head = self.builder2.get_object("E1_setup_head")	
		self.E1_conf_head = self.builder2.get_object("E1_conf_head")	
		self.E1_cycle_head = self.builder2.get_object("E1_cycle_head")	
		self.N1_setup_head = self.builder2.get_object("N1_setup_head")	
		self.N1_conf_head = self.builder2.get_object("N1_conf_head")	
		self.N1_cycle_head = self.builder2.get_object("N1_cycle_head")	
		self.H1_setup_head = self.builder2.get_object("H1_setup_head")	
		self.H1_conf_head = self.builder2.get_object("H1_conf_head")	
		self.H1_cycle_head = self.builder2.get_object("H1_cycle_head")	


#		self.main_screen.fullscreen()
		GObject.timeout_add(1000,self.time_display)
  
		self.main_screen.show()
#		self.tools.show()



# MAIN_SCREEN HANDLERS #########################################################3

	def on_main_screen_destroy(self, object, data=None):
		print "quit with cancel"
		Gtk.main_quit()

	def on_main_screen_info_clicked(self, object, data=None):
		print "main_screen_info about selected"
		self.response = self.aboutdialog.run()
		self.aboutdialog.hide()

	def on_main_screen_setup_clicked(self, object, data=None):
		print "main_screen_setup selected"
		self.Mode_sel.show()
		self.main_screen.hide()

	def on_main_screen_cycle_clicked(self, object, data=None):
		print "main_screen_cycle selected"
		self.curr_cycle.show()
		self.main_screen.hide()
    
	def on_main_screen_shutdown_clicked(self, object, data=None):
		dialog_win=self.main_screen
		ans=self.warn_box(dialog_win,"System Shutting Down","Do you want to shutdown ?")
		if ans==1:
#			os.system("echo fastrack | sudo -S shutdown -h now")
			self.time_save()
			Gtk.main_quit()

# MODE_SEL HANDLER ##############################################################


	def on_main_screen_setup_clicked(self, object, data=None):
		print "main_screen_setup selected"
		self.Mode_sel.show()
		self.main_screen.hide()

	def on_Mode_sel_exit_clicked(self, object, data=None):
		print "Mode_sel_exit selected"
		self.main_screen.show()
		self.Mode_sel.hide()


	def on_S_mode_back_clicked(self, object, data=None):
		print "S_mode_back selected"
		self.Mode_sel.show()
		self.S_mode.hide()

	def on_Mode_sel_E_sel_clicked(self, object, data=None):
		print "Mode_sel_E_sel selected"
		self.E_mode.show()
		self.Mode_sel.hide()

	def on_Mode_sel_T_sel_clicked(self, object, data=None):
		print "Mode_sel_T_sel selected"
		self.T_mode.show()
		self.Mode_sel.hide()

	def on_Mode_sel_F_sel_clicked(self, object, data=None):
		print "Mode_sel_F_sel selected"
		self.F_mode.show()
		self.Mode_sel.hide()
  
	def on_Mode_sel_N_sel_clicked(self, object, data=None):
		print "Mode_sel_N_sel selected"
		self.N_mode.show()
		self.Mode_sel.hide()

	def on_Mode_sel_H_sel_clicked(self, object, data=None):
		print "Mode_sel_H_sel selected"
		self.H_mode.show()
		self.Mode_sel.hide()

	def on_Mode_sel_S_sel_clicked(self, object, data=None):
		print "Mode_sel_S_sel selected"
		self.S_mode.show()
		self.Mode_sel.hide()

# S_MODE HANDLER ##############################################################

	def on_S_mode_back_clicked(self, object, data=None):
		print "S_mode_back selected"
		self.Mode_sel.show()
		self.S_mode.hide()
    
	def on_S_mode_S1_sel_clicked(self, object, data=None):
		print "S_mode_S1_sel selected"
		self.S1_setup.show()
		self.S_mode.hide()

# T_MODE HANDLER ##############################################################

	def on_T_mode_T1_sel_clicked(self, object, data=None):
		print "T_mode_T1_sel selected"
		self.T1_setup.show()
		self.T_mode.hide()

	def on_T_mode_back_clicked(self, object, data=None):
		print "T1_cycle_back selected"
		self.Mode_sel.show()
		self.T_mode.hide()

# F_MODE HANDLER ##############################################################


	def on_F_mode_F1_sel_clicked(self, object, data=None):
		print "F_mode_F1_sel selected"
		self.F1_setup.show()
		self.F_mode.hide()

	def on_F_mode_back_clicked(self, object, data=None):
		print "F1_cycle_back selected"
		self.Mode_sel.show()
		self.F_mode.hide()

# E_MODE HANDLER ##############################################################

	def on_E_mode_E1_sel_clicked(self, object, data=None):
		print "E_mode_E1_sel selected"
		self.E1_setup.show()
		self.E_mode.hide()

	def on_E_mode_back_clicked(self, object, data=None):
		print "E1_cycle_back selected"
		self.Mode_sel.show()
		self.E_mode.hide()

# N_MODE HANDLER ##############################################################

	def on_N_mode_N1_sel_clicked(self, object, data=None):
		print "N_mode_N1_sel selected"
		self.N1_setup.show()
		self.N_mode.hide()

	def on_N_mode_back_clicked(self, object, data=None):
		print "N1_cycle_back selected"
		self.Mode_sel.show()
		self.N_mode.hide()

# H_MODE HANDLER ##############################################################

	def on_H_mode_H1_sel_clicked(self, object, data=None):
		print "H_mode_H1_sel selected"
		self.H1_setup.show()
		self.H_mode.hide()

	def on_H_mode_back_clicked(self, object, data=None):
		print "H1_cycle_back selected"
		self.Mode_sel.show()
		self.H_mode.hide()

# S1_MODE HANDLER ##############################################################

# S1_SETUP HANDLER ##############################################################

	def on_S1_setup_back_clicked(self, object, data=None):
		print "S1_setup_back selected"
		self.S_mode.show()
		self.S1_setup.hide()

	def on_S1_setup_conf_clicked(self, object, data=None):
		print "S1_setup_conf selected"
		self.S1_conf.show()
		self.S1_setup.hide()

	def on_S1_setup_prog_id_clicked(self, object, data=None):
		print "S1_setup_prog_id selected"
		self.keypad.show()
		self.curr_window=self.S1_setup
		self.curr_mode1=self.S1_setup_head
		self.curr_mode2=self.S1_conf_head
		self.curr_mode3=self.S1_cycle_head

#		self.S1_setup.hide()

	def on_S1_setup_info_clicked(self, object, data=None):
		print "S1_setup_info selected"
		dialog_win=self.S1_setup
		self.info_box(dialog_win,"S1 Mode","S1 Setup")
    
	def on_S1_setup_NA_toll_button_press_event(self, object, data=None):
		print "S1_setup_NA_toll selected"
		self.numpad.show()
		self.curr_window=self.S1_setup
		self.curr_entry=self.S1_setup_NA_toll
#		self.S1_setup.hide()
    
	def on_S1_setup_F_toll_button_press_event(self, object, data=None):
		print "S1_setup_F_toll selected"
		self.numpad.show()
		self.curr_window=self.S1_setup
		self.curr_entry=self.S1_setup_F_toll
#		self.S1_setup.hide()
    
	def on_S1_setup_T_toll_button_press_event(self, object, data=None):
		print "S1_setup_T_toll selected"
		self.numpad.show()
		self.curr_window=self.S1_setup
		self.curr_entry=self.S1_setup_T_toll
#		self.S1_setup.hide()
    
# S1_CONF HANDLER ##############################################################

	def on_S1_conf_exit_clicked(self, object, data=None):
		print "S1_conf_exit selected"
		self.main_screen.show()
		self.S1_conf.hide()
    

	def on_S1_conf_cycle_clicked(self, object, data=None):
		print "S1_conf_cycle selected"
		self.S1_cycle.show()
		self.curr_cycle=self.S1_cycle
		self.S1_conf.hide()

	def on_S1_conf_prog_id_clicked(self, object, data=None):
		print "keypad selected"
		self.keypad.show()
		self.curr_window=self.S1_conf
		self.curr_mode1=self.S1_setup_head
		self.curr_mode2=self.S1_conf_head
		self.curr_mode3=self.S1_cycle_head

#		self.S1_conf.hide()


	def on_S1_conf_info_clicked(self, object, data=None):
		print "S1_conf_info selected"
		dialog_win=self.S1_conf

		self.info_box(dialog_win,"S1 Mode","S1 Conf")

	def on_S1_conf_save_clicked(self, object, data=None):
		print "S1_conf_save selected"
		Title=self.S1_cycle_head.get_text()
		filename="S1_"+Title
		self.curr_prog=filename
		self.curr_mode=self.curr_prog[0:2]
		Mode="S1"
		Time=""
		NA=self.S1_conf_NA.get_text()
		S=self.S1_conf_S.get_text()
		T=self.S1_conf_T.get_text()
		F=self.S1_conf_F.get_text()
		E="N/A"
		H="N/A"
		NA_toll=self.S1_conf_NA_toll.get_text()
		S_toll="N/A"
		T_toll=self.S1_conf_T_toll.get_text()
		F_toll=self.S1_conf_F_toll.get_text()
		E_toll="N/A"
		H_toll="N/A"
		A=self.S1_conf_A.get_text()
		B=self.S1_conf_B.get_text()
		save_file(("programs/"+filename,Mode,Title,Time,NA,S,T,F,E,H,NA_toll,S_toll,T_toll,F_toll,E_toll,H_toll,A,B))  

	def on_S1_conf_F_toll_button_press_event(self, object, data=None):
		print "entry13 selected"
		self.numpad.show()
		self.curr_window=self.S1_conf
		self.curr_entry=self.S1_conf_F_toll
#		self.S1_conf.hide()
    
    
	def on_S1_conf_T_toll_button_press_event(self, object, data=None):
		print "entry12 selected"
		self.numpad.show()
		self.curr_window=self.S1_conf
		self.curr_entry=self.S1_conf_T_toll
#		self.S1_conf.hide()
    
    
	def on_S1_conf_NA_toll_button_press_event(self, object, data=None):
		print "S1_conf_NA_toll selected"
		self.numpad.show()
		self.curr_window=self.S1_conf
		self.curr_entry=self.S1_conf_NA_toll
#		self.S1_conf.hide()
    
    
	def on_S1_conf_F_button_press_event(self, object, data=None):
		print "entry10 selected"
		self.numpad.show()
		self.curr_window=self.S1_conf
		self.curr_entry=self.S1_conf_F
#		self.S1_conf.hide()
    
    
	def on_S1_conf_T_button_press_event(self, object, data=None):
		print "S1_conf_T selected"
		self.numpad.show()
		self.curr_window=self.S1_conf
		self.curr_entry=self.S1_conf_T
#		self.S1_conf.hide()
    
    
	def on_S1_conf_S_button_press_event(self, object, data=None):
		print "S1_conf_S selected"
		self.numpad.show()
		self.curr_window=self.S1_conf
		self.curr_entry=self.S1_conf_S
#		self.S1_conf.hide()
    
    
	def on_S1_conf_NA_button_press_event(self, object, data=None):
		print "S1_conf_NA selected"
		self.numpad.show()
		self.curr_window=self.S1_conf
		self.curr_entry=self.S1_conf_NA
#		self.S1_conf.hide()

# S1_CYCLE HANDLER ##############################################################


	def on_S1_cycle_exit_clicked(self, object, data=None):
		print "S1_cycle_exit selected"
		self.S1_cycle.hide()
		self.main_screen.show()

	def on_S1_cycle_conf_clicked(self, object, data=None):
		print "S1_cycle_conf selected"
		self.S1_conf.show()
		self.S1_cycle.hide()

	def on_S1_cycle_prog_clicked(self, object, data=None):
		print "S1_cycle_conf selected"
		self.read_list("S1")
		self.file_select.show()

	def on_S1_cycle_graph_clicked(self, object, data=None):
		print "S1_cycle_graph selected"

		self.graph_win_show()
		self.S1_cycle.hide()

	def on_S1_cycle_table_clicked(self, object, data=None):
		print "S1_cycle_table selected"
		self.table.show_all()
		self.S1_cycle.hide()


	def on_S1_cycle_info_clicked(self, object, data=None):
		print "S1_cycle_info selected"
		dialog_win=self.S1_cycle

		self.info_box(dialog_win,"S1 Mode","S1 Cycle")

# T1_MODE HANDLER ##############################################################

# T1_SETUP HANDLER ##############################################################

	def on_T1_setup_back_clicked(self, object, data=None):
		print "T1_setup_back selected"
		self.T_mode.show()
		self.T1_setup.hide()

	def on_T1_setup_conf_clicked(self, object, data=None):
		print "T1_setup_conf selected"
		self.T1_conf.show()
		self.T1_setup.hide()

	def on_T1_setup_prog_id_clicked(self, object, data=None):
		print "T1_setup_prog_id selected" #under dev
		self.curr_window=self.T1_setup
		self.curr_mode1=self.T1_cycle_head
		self.curr_mode2=self.T1_conf_head
		self.curr_mode3=self.T1_setup_head
		self.keypad.show()
#		self.T1_setup.hide()



	def on_T1_setup_info_clicked(self, object, data=None):
		print "T1_setup_info selected"
		dialog_win=self.T1_setup

		self.info_box(dialog_win,"T1 Mode","T1 Setup")


# T1_CONF HANDLER ##############################################################

	def on_T1_conf_prog_id_clicked(self, object, data=None):
		print "keypad selected"
		self.keypad.show()
		self.curr_window=self.T1_conf
		self.curr_mode1=self.T1_setup_head
		self.curr_mode2=self.T1_conf_head
		self.curr_mode3=self.T1_cycle_head

#		self.T1_conf.hide()

	def on_T1_conf_exit_clicked(self, object, data=None):
		print "T1_conf_exit selected"
		self.main_screen.show()
		self.T1_conf.hide()

	def on_T1_conf_cycle_clicked(self, object, data=None):
		print "T1_cycle_exit selected"
		self.T1_cycle.show()
		self.curr_cycle=self.T1_cycle
		self.T1_conf.hide()

	def on_T1_conf_save_clicked(self, object, data=None):
		print "T1_conf_save selected"
		Title=self.T1_cycle_head.get_text()
		filename="T1_"+Title
		self.curr_prog=filename
		self.curr_mode=self.curr_prog[0:2]
		Mode="T1"
		Time=""
		NA="N/A"
		S="N/A"
		T=self.T1_conf_T.get_text()
		F="N/A"
		E="N/A"
		H="N/A"
		NA_toll="N/A"
		S_toll="N/A"
		T_toll="N/A"
		F_toll="N/A"
		E_toll="N/A"
		H_toll="N/A"
		A=self.T1_conf_A.get_text()
		B=self.T1_conf_B.get_text()
		save_file(("programs/"+filename,Mode,Title,Time,NA,S,T,F,E,H,NA_toll,S_toll,T_toll,F_toll,E_toll,H_toll,A,B))  
   

	def on_T1_conf_prog_id_clicked(self, object, data=None):
		print "T1_conf_prog_id selected" #under dev
		self.keypad.show()
		self.curr_window=self.T1_conf
		self.curr_mode1=self.T1_cycle_head
		self.curr_mode2=self.T1_conf_head
		self.curr_mode3=self.T1_setup_head

#		self.T1_conf.hide()


	def on_T1_conf_info_clicked(self, object, data=None):
		print "T1_conf_info selected"
		dialog_win=self.T1_conf

		self.info_box(dialog_win,"S1 Mode","S1 Conf")

	def on_T1_conf_T_button_press_event(self, object, data=None):
		print "T1_conf_T selected"
		self.numpad.show()
		self.curr_window=self.T1_conf
		self.curr_entry=self.T1_conf_T
#		self.T1_conf.hide()

# T1_CYCLE HANDLER ##############################################################

	def on_T1_cycle_exit_clicked(self, object, data=None):
		print "T_mode_back selected"
		self.main_screen.show()
		self.T1_cycle.hide()

	def on_T1_cycle_conf_clicked(self, object, data=None):
		print "T_mode_T1_sel selected"
		self.T1_conf.show()
		self.T1_cycle.hide()

	def on_T1_cycle_prog_clicked(self, object, data=None):
		print "T1_cycle_conf selected"
		self.read_list("T1")
		self.file_select.show()

	def on_T1_cycle_graph_clicked(self, object, data=None):
		print "T1_cycle_graph selected"
		self.graph_win_show()
		self.T1_cycle.hide()

	def on_T1_cycle_table_clicked(self, object, data=None):
		print "T1_cycle_table selected"
		self.table.show_all()
		self.T1_cycle.hide()


	def on_T1_cycle_info_clicked(self, object, data=None):
		print "T1_cycle_info selected"
		dialog_win=self.T1_cycle

		self.info_box(dialog_win,"S1 Mode","S1 Cycle")

# F1_MODE HANDLER ##############################################################

# F1_SETUP HANDLER ##############################################################

	def on_F1_setup_back_clicked(self, object, data=None):
		print "F1_setup_back selected"
		self.F_mode.show()
		self.F1_setup.hide()

	def on_F1_setup_conf_clicked(self, object, data=None):
		print "F1_setup_conf selected"
		self.F1_conf.show()
		self.F1_setup.hide()

	def on_F1_setup_prog_id_clicked(self, object, data=None):
		print "button54 selected" #under dev
		self.keypad.show()
		self.curr_window=self.F1_setup
		self.curr_mode1=self.F1_setup_head
		self.curr_mode2=self.F1_conf_head
		self.curr_mode3=self.F1_cycle_head

#		self.F1_setup.hide()


	def on_F1_setup_info_clicked(self, object, data=None):
		print "F1_setup_info selected"
		dialog_win=self.F1_setup

		self.info_box(dialog_win,"F1 Mode","F1 Setup")

	def on_F1_setup_E_toll_button_press_event(self, object, data=None):
		print "F1_setup_E_toll selected"
		self.numpad.show()
		self.curr_window=self.F1_setup
		self.curr_entry=self.F1_setup_E_toll
#		self.F1_setup.hide()

	def on_F1_setup_T_toll_button_press_event(self, object, data=None):
		print "F1_setup_T_toll selected"
		self.numpad.show()
		self.curr_window=self.F1_setup
		self.curr_entry=self.F1_setup_T_toll
#		self.F1_setup.hide()

# F1_CONF HANDLER ##############################################################

	def on_F1_conf_exit_clicked(self, object, data=None):
		print "F1_conf_exit selected" #under dev
		self.main_screen.show()
		self.F1_conf.hide()

	def on_F1_conf_cycle_clicked(self, object, data=None):
		print "F1_conf_cycle selected" 
		self.F1_cycle.show()
		self.curr_cycle=self.F1_cycle
		self.F1_conf.hide()

	def on_F1_conf_save_clicked(self, object, data=None):
		print "F1_conf_save selected" 
		Title=self.F1_cycle_head.get_text()
		filename="F1_"+Title
		self.curr_prog=filename
		self.curr_mode=self.curr_prog[0:2]
		Mode="F1"
		Time=""
		NA="N/A"
		S="N/A"
		T=self.F1_conf_T.get_text()
		F=self.F1_conf_F.get_text()
		E=self.F1_conf_E.get_text()
		H="N/A"
		NA_toll="N/A"
		S_toll="N/A"
		T_toll=self.F1_conf_T_toll.get_text()
		F_toll="N/A"
		E_toll=self.F1_conf_E_toll.get_text()
		H_toll="N/A"
		A=self.F1_conf_A.get_text()
		B=self.F1_conf_B.get_text()
		save_file(("programs/"+filename,Mode,Title,Time,NA,S,T,F,E,H,NA_toll,S_toll,T_toll,F_toll,E_toll,H_toll,A,B))  


	def on_F1_conf_prog_id_clicked(self, object, data=None):
		print "F1_conf_prog_id selected"
#		self.F1_conf.hide() 
		self.curr_window=self.F1_conf
		self.curr_mode1=self.F1_setup_head
		self.curr_mode2=self.F1_conf_head
		self.curr_mode3=self.F1_cycle_head
		self.keypad.show()

	def on_F1_conf_info_clicked(self, object, data=None):
		print "F1_conf_info selected"
		dialog_win=self.F1_conf
		self.info_box(dialog_win,"F1 Mode","F1 Conf")

	def on_F1_conf_E_toll_button_press_event(self, object, data=None):
		print "F1_conf_E_toll selected"
		self.numpad.show()
		self.curr_window=self.F1_conf
		self.curr_entry=self.F1_conf_E_toll
#		self.F1_conf.hide()

	def on_F1_conf_E_button_press_event(self, object, data=None):
		print "F1_conf_E selected"
		self.numpad.show()
		self.curr_window=self.F1_conf
		self.curr_entry=self.F1_conf_E
#		self.F1_conf.hide()

	def on_F1_conf_T_toll_button_press_event(self, object, data=None):
		print "F1_conf_T_toll selected"
		self.numpad.show()
		self.curr_window=self.F1_conf
		self.curr_entry=self.F1_conf_T_toll
#		self.F1_conf.hide()

	def on_F1_conf_F_button_press_event(self, object, data=None):
		print "F1_conf_F selected"
		self.numpad.show()
		self.curr_window=self.F1_conf
		self.curr_entry=self.F1_conf_F
#		self.F1_conf.hide()

	def on_F1_conf_T_button_press_event(self, object, data=None):
		print "F1_conf_T selected"
		self.numpad.show()
		self.curr_window=self.F1_conf
		self.curr_entry=self.F1_conf_T
#		self.F1_conf.hide()

# F1_CYCLE HANDLER ##############################################################

	def on_F1_cycle_exit_clicked(self, object, data=None):
		print "F1_cycle_exit selected"
		self.main_screen.show()
		self.F1_cycle.hide()

	def on_F1_cycle_conf_clicked(self, object, data=None):
		print "F1_cycle_conf selected" 
		self.F1_conf.show()
		self.F1_cycle.hide()

	def on_F1_cycle_prog_clicked(self, object, data=None):
		print "F1_cycle_conf selected"
		self.read_list("F1")
		self.file_select.show()

	def on_F1_cycle_graph_clicked(self, object, data=None):
		print "F1_cycle_graph selected"
		self.graph_win.show()
		self.F1_cycle.hide()

	def on_F1_cycle_table_clicked(self, object, data=None):
		print "F1_cycle_table selected"
		self.table.show_all()
		self.F1_cycle.hide()


	def on_F1_cycle_info_clicked(self, object, data=None):
		print "F1_cycle_info selected"
		dialog_win=self.F1_cycle

		self.info_box(dialog_win,"F1 Mode","F1 Cycle")

# E1_MODE HANDLER ##############################################################

# E1_SETUP HANDLER ##############################################################

	def on_E1_setup_back_clicked(self, object, data=None):
		print "E1_setup_back selected"
		self.E_mode.show()
		self.E1_setup.hide()

	def on_E1_setup_conf_clicked(self, object, data=None):
		print "E1_setup_conf selected"
		self.E1_conf.show()
		self.E1_setup.hide()

	def on_E1_setup_prog_id_clicked(self, object, data=None):
		print "E1_setup_prog_id selected" #under dev
		self.keypad.show()
		self.curr_window=self.E1_setup
		self.curr_mode1=self.E1_setup_head
		self.curr_mode2=self.E1_conf_head
		self.curr_mode3=self.E1_cycle_head

#		self.E1_setup.hide()


	def on_E1_setup_info_clicked(self, object, data=None):
		print "E1_setup_info selected"
		dialog_win=self.E1_setup

		self.info_box(dialog_win,"E1 Mode","E1 Setup")

	def on_E1_setup_F_toll_button_press_event(self, object, data=None):
		print "E1_setup_F_toll selected"
		self.numpad.show()
		self.curr_window=self.E1_setup
		self.curr_entry=self.E1_setup_F_toll
#		self.E1_setup.hide()

	def on_E1_setup_T_toll_button_press_event(self, object, data=None):
		print "E1_setup_T_toll selected"
		self.numpad.show()
		self.curr_window=self.E1_setup
		self.curr_entry=self.E1_setup_T_toll
#		self.E1_setup.hide()

# E1_CONF HANDLER ##############################################################

	def on_E1_conf_exit_clicked(self, object, data=None):
		print "E1_conf_exit selected"
		self.main_screen.show()
		self.E1_conf.hide()

	def on_E1_conf_cycle_clicked(self, object, data=None):
		print "E1_conf_cycle selected"
		self.E1_cycle.show()
		self.curr_cycle=self.E1_cycle
		self.E1_conf.hide()

	def on_E1_conf_save_clicked(self, object, data=None):
		print "E1_conf_save selected"
		Title=self.E1_cycle_head.get_text()
		filename="E1_"+Title
		self.curr_prog=filename
		self.curr_mode=self.curr_prog[0:2]
		Mode="E1"
		Time=""
		NA="N/A"
		S="N/A"
		T=self.E1_conf_T.get_text()
		F=self.E1_conf_F.get_text()
		E=self.E1_conf_E.get_text()
		H="N/A"
		NA_toll="N/A"
		S_toll="N/A"
		T_toll=self.E1_conf_T_toll.get_text()
		F_toll=self.E1_conf_F_toll.get_text()
		E_toll="N/A"
		H_toll="N/A"
		A=self.E1_conf_A.get_text()
		B=self.E1_conf_B.get_text()
		save_file(("programs/"+filename,Mode,Title,Time,NA,S,T,F,E,H,NA_toll,S_toll,T_toll,F_toll,E_toll,H_toll,A,B))  


	def on_E1_conf_prog_id_clicked(self, object, data=None):
		print "E1_conf_prog_id selected" #under dev
		self.keypad.show()
		self.curr_window=self.E1_conf
		self.curr_mode1=self.E1_setup_head
		self.curr_mode2=self.E1_conf_head
		self.curr_mode3=self.E1_cycle_head
#		self.E1_conf.hide()

	def on_E1_conf_info_clicked(self, object, data=None):
		print "E1_conf_info selected"
		dialog_win=self.E1_conf

		self.info_box(dialog_win,"E1 Mode","E1 Conf")


	def on_E1_conf_E_button_press_event(self, object, data=None):
		print "E1_conf_E selected"
		self.numpad.show()
		self.curr_window=self.E1_conf
		self.curr_entry=self.E1_conf_E
#		self.E1_conf.hide()

	def on_E1_conf_T_toll_button_press_event(self, object, data=None):
		print "F1_conf_T_toll selected"
		self.numpad.show()
		self.curr_window=self.E1_conf
		self.curr_entry=self.E1_conf_T_toll
#		self.E1_conf.hide()

	def on_E1_conf_F_button_press_event(self, object, data=None):
		print "E1_conf_F selected"
		self.numpad.show()
		self.curr_window=self.E1_conf
		self.curr_entry=self.E1_conf_F
#		self.E1_conf.hide()

	def on_E1_conf_F_toll_button_press_event(self, object, data=None):
		print "E1_conf_F_toll selected"
		self.numpad.show()
		self.curr_window=self.E1_conf
		self.curr_entry=self.E1_conf_F_toll
#		self.E1_conf.hide()

	def on_E1_conf_T_button_press_event(self, object, data=None):
		print "E1_conf_T selected"
		self.numpad.show()
		self.curr_window=self.E1_conf
		self.curr_entry=self.E1_conf_T
#		self.E1_conf.hide()


# E1_CYCLE HANDLER ##############################################################

	def on_E1_cycle_exit_clicked(self, object, data=None):
		print "E1_cycle_exit selected" 
		self.main_screen.show()
		self.E1_cycle.hide()

	def on_E1_cycle_conf_clicked(self, object, data=None):
		print "E1_cycle_conf selected" 
		self.E1_conf.show() #under dev
		self.E1_cycle.hide()

	def on_E1_cycle_prog_clicked(self, object, data=None):
		print "E1_cycle_conf selected"
		self.read_list("E1")
		self.file_select.show()

	def on_E1_cycle_graph_clicked(self, object, data=None):
		print "E1_cycle_graph selected"
		self.graph_win.show()
		self.E1_cycle.hide()

	def on_E1_cycle_table_clicked(self, object, data=None):
		print "E1_cycle_table selected"
		self.table.show_all()
		self.E1_cycle.hide()

	def on_E1_cycle_info_clicked(self, object, data=None):
		print "E1_cycle_info selected"
		dialog_win=self.E1_cycle

		self.info_box(dialog_win,"E1 Mode","E1 Cycle")


# N1_MODE HANDLER ##############################################################

# N1_SETUP HANDLER ##############################################################

	def on_N1_setup_back_clicked(self, object, data=None):
		print "N1_setup_back selected"
		self.N_mode.show()
		self.N1_setup.hide()

	def on_N1_setup_conf_clicked(self, object, data=None):
		print "N1_setup_conf selected"
		self.N1_conf.show()
		self.N1_setup.hide()

	def on_N1_setup_prog_id_clicked(self, object, data=None):
		print "N1_setup_prog_id selected"
		self.keypad.show()
		self.curr_window=self.N1_setup
		self.curr_mode1=self.N1_setup_head
		self.curr_mode2=self.N1_conf_head
		self.curr_mode3=self.N1_cycle_head

#		self.N1_setup.hide()

	def on_N1_setup_info_clicked(self, object, data=None):
		print "N1_setup_info selected"
		dialog_win=self.S1_conf

		self.info_box(dialog_win,"N1 Mode","N1 Setup")

	def on_N1_setup_T_toll_button_press_event(self, object, data=None):
		print "N1_setup_T_toll selected"
		self.numpad.show()
		self.curr_window=self.N1_setup
		self.curr_entry=self.N1_setup_T_toll
#		self.N1_setup.hide()

# N1_CONF HANDLER ##############################################################

	def on_N1_conf_exit_clicked(self, object, data=None):
		print "N1_conf_exit selected"
		self.main_screen.show()
		self.N1_conf.hide()

	def on_N1_conf_cycle_clicked(self, object, data=None):
		print "N1_conf_cycle selected"
		self.N1_cycle.show()
		self.curr_cycle=self.N1_cycle
		self.N1_conf.hide()

	def on_N1_conf_save_clicked(self, object, data=None):
		print "N1_conf_save selected"
		Title=self.N1_cycle_head.get_text()
		filename="N1_"+Title
		self.curr_prog=filename
		self.curr_mode=self.curr_prog[0:2]
		Mode="N1"
		Time=""
		NA="N/A"
		S="N/A"
		T=self.N1_conf_T.get_text()
		F="N/A"
		E="N/A"
		H="N/A"
		NA_toll="N/A"
		S_toll="N/A"
		T_toll=self.N1_conf_T_toll.get_text()
		F_toll="N/A"
		E_toll="N/A"
		H_toll="N/A"
		A=self.N1_conf_A.get_text()
		B=self.N1_conf_B.get_text()
		save_file(("programs/"+filename,Mode,Title,Time,NA,S,T,F,E,H,NA_toll,S_toll,T_toll,F_toll,E_toll,H_toll,A,B))  

	def on_N1_conf_prog_id_clicked(self, object, data=None):
		print "N1_conf_prog_id selected" #under dev
		self.keypad.show()
		self.curr_window=self.N1_conf
		self.curr_mode1=self.N1_setup_head
		self.curr_mode2=self.N1_conf_head
		self.curr_mode3=self.N1_cycle_head
#		self.N1_conf.hide()

	def on_N1_conf_info_clicked(self, object, data=None):
		print "N1_conf_info selected"
		dialog_win=self.N1_conf
		self.info_box(dialog_win,"N1 Mode","N1 Conf")

	def on_N1_conf_T_toll_button_press_event(self, object, data=None):
		print "N1_conf_T_toll selected"
		self.curr_entry=self.N1_conf_T_toll
		self.numpad.show()
		self.curr_window=self.N1_conf
#		self.N1_conf.hide()

	def on_N1_conf_T_button_press_event(self, object, data=None):
		print "conf_T_button selected"
		self.numpad.show()
		self.curr_window=self.N1_conf
		self.curr_entry=self.N1_conf_T
#		self.N1_conf.hide()

# N1_CYCLE HANDLER ##############################################################

	def on_N1_cycle_exit_clicked(self, object, data=None):
		print "N1_cycle_exit selected"
		self.main_screen.show()
		self.N1_cycle.hide()

	def on_N1_cycle_conf_clicked(self, object, data=None):
		print "N1_cycle_conf selected" 
		self.N1_conf.show()
		self.N1_cycle.hide()

	def on_N1_cycle_prog_clicked(self, object, data=None):
		print "N1_cycle_conf selected"
		self.read_list("N1")
		self.file_select.show()

	def on_N1_cycle_graph_clicked(self, object, data=None):
		print "N1_cycle_graph selected"
		self.graph_win.show()
		self.N1_cycle.hide()

	def on_N1_cycle_table_clicked(self, object, data=None):
		print "N1_cycle_table selected"
		self.table.show_all()
		self.N1_cycle.hide()


	def on_N1_cycle_info_clicked(self, object, data=None):
		print "N1_cycle_info selected"
		dialog_win=self.N1_cycle

		self.info_box(dialog_win,"N1 Mode","N1 Cycle")


# H1_MODE HANDLER ##############################################################

# H1_SETUP HANDLER ##############################################################

	def on_H1_setup_back_clicked(self, object, data=None):
		print "H1_setup_back selected"
		self.H_mode.show()
		self.H1_setup.hide()

	def on_H1_setup_conf_clicked(self, object, data=None):
		print "H1_setup_conf selected"
		self.H1_conf.show()
		self.H1_setup.hide()

	def on_H1_setup_prog_id_clicked(self, object, data=None):
		print "H1_setup_prog_id selected"
		self.keypad.show()
		self.curr_window=self.H1_setup
		self.curr_mode1=self.H1_setup_head
		self.curr_mode2=self.H1_conf_head
		self.curr_mode3=self.H1_cycle_head
#		self.H1_setup.hide()

	def on_H1_setup_info_clicked(self, object, data=None):
		print "H1_setup_info selected"
		dialog_win=self.H1_setup

		self.info_box(dialog_win,"H1 Mode","H1 Setup")

	def on_H1_setup_info_clicked(self, object, data=None):
		print "button143 selected" #under dev
		self.Mode_sel.show()
		self.T_mode.hide()

	def on_H1_setup_F_toll_button_press_event(self, object, data=None):
		print "H1_setup_F_toll selected"
		self.numpad.show()
		self.curr_window=self.H1_setup
		self.curr_entry=self.H1_setup_F_toll
#		self.H1_setup.hide()

	def on_H1_setup_T_toll_button_press_event(self, object, data=None):
		print "H1_setup_T_toll selected"
		self.curr_entry=self.H1_setup_T_toll
		self.numpad.show()
		self.curr_window=self.H1_setup
#		self.H1_setup.hide()

# H1_CONF HANDLER ##############################################################

	def on_H1_conf_exit_clicked(self, object, data=None):
		print "H1_conf_exit selected" #under dev
		self.main_screen.show()
		self.H1_conf.hide()

	def on_H1_conf_cycle_clicked(self, object, data=None):
		print "H1_conf_cycle selected"
		self.H1_cycle.show()
		self.curr_cycle=self.H1_cycle
		self.H1_conf.hide()

	def on_H1_conf_save_clicked(self, object, data=None):
		print "H1_conf_save selected" 
		Title=self.H1_cycle_head.get_text()
		filename="H1_"+Title
		self.curr_prog=filename
		self.curr_mode=self.curr_prog[0:2]
		Mode="H1"
		Time=""
		NA="N/A"
		S="N/A"
		T=self.H1_conf_T.get_text()
		F=self.H1_conf_F.get_text()
		E="N/A"
		H=self.H1_conf_H.get_text()
		NA_toll="N/A"
		S_toll="N/A"
		T_toll=self.H1_conf_T_toll.get_text()
		F_toll=self.H1_conf_F_toll.get_text()
		E_toll="N/A"
		H_toll="N/A"
		A=self.H1_conf_A.get_text()
		B=self.H1_conf_B.get_text()
		save_file(("programs/"+filename,Mode,Title,Time,NA,S,T,F,E,H,NA_toll,S_toll,T_toll,F_toll,E_toll,H_toll,A,B))  

	def on_H1_conf_prog_id_clicked(self, object, data=None):
		print "H1_conf_prog_id selected" 
		self.keypad.show() #under dev
		self.curr_window=self.H1_conf
		self.curr_mode1=self.H1_setup_head
		self.curr_mode2=self.H1_conf_head
		self.curr_mode3=self.H1_cycle_head

#		self.H1_conf.hide()

	def on_H1_conf_info_clicked(self, object, data=None):
		print "H1_conf_info selected"
		dialog_win=self.H1_conf

		self.info_box(dialog_win,"H1 Mode","H1 Conf")

    
	def on_H1_conf_H_button_press_event(self, object, data=None):
		print "H1_conf_H selected"
		self.numpad.show()
		self.curr_window=self.H1_conf
		self.curr_entry=self.H1_conf_H
#		self.H1_conf.hide()

	def on_H1_conf_F_toll_button_press_event(self, object, data=None):
		print "H1_conf_F_toll selected"
		self.numpad.show()
		self.curr_window=self.H1_conf
		self.curr_entry=self.H1_conf_F_toll
#		self.H1_conf.hide()

	def on_H1_conf_T_toll_button_press_event(self, object, data=None):
		print "H1_conf_T_toll selected"
		self.numpad.show()
		self.curr_window=self.H1_conf
		self.curr_entry=self.H1_conf_T_toll
#		self.H1_conf.hide()

	def on_H1_conf_F_button_press_event(self, object, data=None):
		print "H1_conf_F selected"
		self.numpad.show()
		self.curr_window=self.H1_conf
		self.curr_entry=self.H1_conf_F
#		self.H1_conf.hide()

	def on_H1_conf_T_button_press_event(self, object, data=None):
		print "H1_conf_T selected"
		self.numpad.show()
		self.curr_window=self.H1_conf
		self.curr_entry=self.H1_conf_T
#		self.H1_conf.hide()

# H1_CYCLE HANDLER ##############################################################

	def on_H1_cycle_exit_clicked(self, object, data=None):
		print "H1_cycle_exit selected" 
		self.main_screen.show()
		self.H1_cycle.hide()

	def on_H1_cycle_conf_clicked(self, object, data=None):
		print "H1_cycle_conf selected"
		self.H1_conf.show()
		self.H1_cycle.hide()

	def on_H1_cycle_prog_clicked(self, object, data=None):
		print "H1_cycle_conf selected"
		self.read_list("H1")
		self.file_select.show()

	def on_H1_cycle_graph_clicked(self, object, data=None):
		print "H1_cycle_graph selected"
		self.graph_win.show()
		self.H1_cycle.hide()

	def on_H1_cycle_table_clicked(self, object, data=None):
		print "H1_cycle_table selected"
		self.table.show_all()
		self.H1_cycle.hide()

	def on_H1_cycle_info_clicked(self, object, data=None):
		print "H1_cycle_info selected"
		dialog_win=self.H1_cycle

		self.info_box(dialog_win,"H1 Mode","H1 Cycle")


#COUNTER########################################################

	def OK_NOK_counter_save(self): #use when exiting 
		OK=self.S1_conf_OK.get_text()
		NOK=self.S1_conf_NOK.get_text()
		save_file(("settings/counters",OK,NOK))

	def OK_counter_reset(self): #use when reset 
		counter=load_file("settings/counters")
		OK="0"
		NOK=counter[2]
		save_file(("settings/counters",OK,NOK))
	def NOK_counter_reset(self): #use when reset 
		counter=load_file("settings/counters")
		NOK="0"
		OK=counter[1]
		save_file(("settings/counters",OK,NOK))


	def OK_inc(self): #use for inc after each process
		counter[1]=counter[1] + 1

	def NOK_inc(self): #use for inc after each process
		counter[2]=counter[2] + 1

	def A_inc(self): #use for inc
		process_counter[1]=process_counter[1] + 1

	def B_inc(self): #use for inc
		process_counter[2]=process_counter[2] + 1

	def OK_NOK_counter_load(self): #use at starting
		counter=load_file("settings/counters")

	def A_B_counter_save(self): #use when exiting
		program=load_file(self.curr_prog)
		eval("program[16]=self."+self.curr_prog[0:2]+"_conf_A.get_text()")
		eval("program[17]=self."+self.curr_prog[0:2]+"_conf_B.get_text()")
		save_file(program)

	def A_B_counter_update(self): #use after each process and after loading prog
		eval(self.curr_mode+"_conf_A.set_text(process_counter[1])")
		eval(self.curr_mode+"_setup_A.set_text(process_counter[1])")
		eval(self.curr_mode+"_cycle_A.set_text(process_counter[1])")

		eval(self.curr_mode+"_conf_B.set_text(process_counter[2])")
		eval(self.curr_mode+"_setup_B.set_text(process_counter[2])")
		eval(self.curr_mode+"_cycle_B.set_text(process_counter[2])")


	def OK_NOK_update(self):  #use after each process an the starting
		self.S1_conf_OK.set_text(counter[1])
		self.S1_cycle_OK.set_text(counter[1])
		self.S1_setup_OK.set_text(counter[1])
    
		self.S1_conf_NOK.set_text(counter[2])
		self.S1_cycle_NOK.set_text(counter[2])
		self.S1_setup_NOK.set_text(counter[2])
	
		self.T1_conf_OK.set_text(counter[1])
		self.T1_cycle_OK.set_text(counter[1])
		self.T1_setup_OK.set_text(counter[1])
    
		self.T1_conf_NOK.set_text(counter[2])
		self.T1_cycle_NOK.set_text(counter[2])
		self.T1_setup_NOK.set_text(counter[2])
	
		self.F1_conf_OK.set_text(counter[1])
		self.F1_cycle_OK.set_text(counter[1])
		self.F1_setup_OK.set_text(counter[1])
    
		self.F1_conf_NOK.set_text(counter[2])
		self.F1_cycle_NOK.set_text(counter[2])
		self.F1_setup_NOK.set_text(counter[2])
	
		self.E1_conf_OK.set_text(counter[1])
		self.E1_cycle_OK.set_text(counter[1])
		self.E1_setup_OK.set_text(counter[1])
    
		self.E1_conf_NOK.set_text(counter[2])
		self.E1_cycle_NOK.set_text(counter[2])
		self.E1_setup_NOK.set_text(counter[2])
	
		self.N1_conf_OK.set_text(counter[1])
		self.N1_cycle_OK.set_text(counter[1])
		self.N1_setup_OK.set_text(counter[1])
    
		self.N1_conf_NOK.set_text(counter[2])
		self.N1_cycle_NOK.set_text(counter[2])
		self.N1_setup_NOK.set_text(counter[2])
	
		self.H1_conf_OK.set_text(counter[1])
		self.H1_cycle_OK.set_text(counter[1])
		self.H1_setup_OK.set_text(counter[1])
   
		self.H1_conf_NOK.set_text(counter[2])
		self.H1_cycle_NOK.set_text(counter[2])
		self.H1_setup_NOK.set_text(counter[2])

#TIME ###################################################################

	def time_display(self):
		time=str(datetime.now().time())
#		print time.rpartition(':')[0] 
#		print datetime.now().date()
		self.advanced_settings_date_and_time.set_text("Time:"+time.rpartition(':')[0]+"\nDate:"+str(datetime.now().date()))

		self.configuration_settings_date_and_time.set_text("Time:"+time.rpartition(':')[0]+"\nDate:"+str(datetime.now().date()))

		self.main_screen_date_and_time.set_text("Time:"+time.rpartition(':')[0]+"\nDate:"+str(datetime.now().date()))

		self.system_op_time=self.system_op_time + timedelta(seconds=1)
#		self.flag=int(raw_input("Enter the flag:"))

		if self.flag==1 :
			self.system_riv_time=self.system_riv_time + timedelta(seconds=1)

		self.Time_settings_time_riv.set_text(str(self.system_riv_time - datetime.strptime("01-01-2012 00:00:00","%d-%m-%Y %H:%M:%S")))

		self.Time_settings_time_op.set_text(str(self.system_op_time - datetime.strptime("01-01-2012 00:00:00","%d-%m-%Y %H:%M:%S")))

		self.main_screen_date_and_time.set_text("Time:"+time.rpartition(':')[0]+"\nDate:"+str(datetime.now().date()))

		return True



	def time_save(self): #use at end of the program
		date=str(datetime.now().date())
		day=date.rpartition('-')[2]
		month=(date.partition('-')[2]).partition('-')[0]
		year=date.partition('-')[0]
		time=str(datetime.now().time()).rpartition('.')[0]
		sec=time.rpartition(':')[2]
		minute=(time.partition(':')[2]).partition(':')[0]
		hour=time.partition(':')[0]
		self.str_op_time=self.system_op_time.strftime("%d-%m-%Y %H:%M:%S")
		self.str_riv_time=self.system_riv_time.strftime("%d-%m-%Y %H:%M:%S")
		time_obj=("settings/time_sett",day,month,year,hour,minute,sec,self.str_riv_time,self.str_op_time)
		save_file(time_obj)

# LOAD PROGRAMS #############################################################

	def load_prog(self,program):
		if (program[1]=="E1"):
			eval("self."+program[1]+"_cycle_head.set_text(program[2])") 
			eval("self."+program[1]+"_cycle_T.set_text(program[6])") 
			eval("self."+program[1]+"_cycle_F.set_text(program[7])")	
			eval("self."+program[1]+"_cycle_E.set_text(program[8])")
			eval("self."+program[1]+"_cycle_T_toll.set_text(program[12])") 
			eval("self."+program[1]+"_cycle_F_toll.set_text(program[13])") 
			eval("self."+program[1]+"_cycle_A.set_text(program[16])") 
			eval("self."+program[1]+"_cycle_B.set_text(program[17])") 

			eval("self."+program[1]+"_setup_head.set_text(program[2])") 
			eval("self."+program[1]+"_setup_T.set_text(program[6])") 
			eval("self."+program[1]+"_setup_F.set_text(program[7])")	
			eval("self."+program[1]+"_setup_E.set_text(program[8])")
			eval("self."+program[1]+"_setup_T_toll.set_text(program[12])") 
			eval("self."+program[1]+"_setup_F_toll.set_text(program[13])") 
			eval("self."+program[1]+"_setup_A.set_text(program[16])") 
			eval("self."+program[1]+"_setup_B.set_text(program[17])") 

			eval("self."+program[1]+"_conf_head.set_text(program[2])") 
			eval("self."+program[1]+"_conf_T.set_text(program[6])") 
			eval("self."+program[1]+"_conf_F.set_text(program[7])")	
			eval("self."+program[1]+"_conf_E.set_text(program[8])")
			eval("self."+program[1]+"_conf_T_toll.set_text(program[12])") 
			eval("self."+program[1]+"_conf_F_toll.set_text(program[13])") 
			eval("self."+program[1]+"_conf_A.set_text(program[16])") 
			eval("self."+program[1]+"_conf_B.set_text(program[17])") 

		elif (program[1]=="F1"):
			eval("self."+program[1]+"_cycle_head.set_text(program[2])") 
			eval("self."+program[1]+"_cycle_T.set_text(program[6])") 
			eval("self."+program[1]+"_cycle_F.set_text(program[7])")	
			eval("self."+program[1]+"_cycle_E.set_text(program[8])")
			eval("self."+program[1]+"_cycle_T_toll.set_text(program[12])") 
			eval("self."+program[1]+"_cycle_E_toll.set_text(program[14])") 
			eval("self."+program[1]+"_cycle_A.set_text(program[16])") 
			eval("self."+program[1]+"_cycle_B.set_text(program[17])") 

			eval("self."+program[1]+"_conf_head.set_text(program[2])") 
			eval("self."+program[1]+"_conf_T.set_text(program[6])") 
			eval("self."+program[1]+"_conf_F.set_text(program[7])")	
			eval("self."+program[1]+"_conf_E.set_text(program[8])")
			eval("self."+program[1]+"_conf_T_toll.set_text(program[12])") 
			eval("self."+program[1]+"_conf_E_toll.set_text(program[14])") 
			eval("self."+program[1]+"_conf_A.set_text(program[16])") 
			eval("self."+program[1]+"_conf_B.set_text(program[17])") 

			eval("self."+program[1]+"_setup_head.set_text(program[2])") 
			eval("self."+program[1]+"_setup_T.set_text(program[6])") 
			eval("self."+program[1]+"_setup_F.set_text(program[7])")	
			eval("self."+program[1]+"_setup_E.set_text(program[8])")
			eval("self."+program[1]+"_setup_T_toll.set_text(program[12])") 
			eval("self."+program[1]+"_setup_E_toll.set_text(program[14])") 
			eval("self."+program[1]+"_setup_A.set_text(program[16])") 
			eval("self."+program[1]+"_setup_B.set_text(program[17])") 

		elif (program[1]=="H1"):
			eval("self."+program[1]+"_cycle_head.set_text(program[2])") 
			eval("self."+program[1]+"_cycle_T.set_text(program[6])") 
			eval("self."+program[1]+"_cycle_F.set_text(program[7])")	
			eval("self."+program[1]+"_cycle_H.set_text(program[9])") 
			eval("self."+program[1]+"_cycle_T_toll.set_text(program[12])") 
			eval("self."+program[1]+"_cycle_F_toll.set_text(program[13])") 
			eval("self."+program[1]+"_cycle_A.set_text(program[16])") 
			eval("self."+program[1]+"_cycle_B.set_text(program[17])") 

			eval("self."+program[1]+"_conf_head.set_text(program[2])") 
			eval("self."+program[1]+"_conf_T.set_text(program[6])") 
			eval("self."+program[1]+"_conf_F.set_text(program[7])")	
			eval("self."+program[1]+"_conf_H.set_text(program[9])") 
			eval("self."+program[1]+"_conf_T_toll.set_text(program[12])") 
			eval("self."+program[1]+"_conf_F_toll.set_text(program[13])") 
			eval("self."+program[1]+"_conf_A.set_text(program[16])") 
			eval("self."+program[1]+"_conf_B.set_text(program[17])") 

			eval("self."+program[1]+"_setup_head.set_text(program[2])") 
			eval("self."+program[1]+"_setup_T.set_text(program[6])") 
			eval("self."+program[1]+"_setup_F.set_text(program[7])")	
			eval("self."+program[1]+"_setup_H.set_text(program[9])") 
			eval("self."+program[1]+"_setup_T_toll.set_text(program[12])") 
			eval("self."+program[1]+"_setup_F_toll.set_text(program[13])") 
			eval("self."+program[1]+"_setup_A.set_text(program[16])") 
			eval("self."+program[1]+"_setup_B.set_text(program[17])") 

		elif (program[1]=="N1"):
			eval("self."+program[1]+"_cycle_head.set_text(program[2])") 
			eval("self."+program[1]+"_cycle_T.set_text(program[6])") 
			eval("self."+program[1]+"_cycle_T_toll.set_text(program[12])") 
			eval("self."+program[1]+"_cycle_A.set_text(program[16])") 
			eval("self."+program[1]+"_cycle_B.set_text(program[17])") 

			eval("self."+program[1]+"_conf_head.set_text(program[2])") 
			eval("self."+program[1]+"_conf_T.set_text(program[6])") 
			eval("self."+program[1]+"_conf_T_toll.set_text(program[12])") 
			eval("self."+program[1]+"_conf_A.set_text(program[16])") 
			eval("self."+program[1]+"_conf_B.set_text(program[17])") 

			eval("self."+program[1]+"_setup_head.set_text(program[2])") 
			eval("self."+program[1]+"_setup_T.set_text(program[6])") 
			eval("self."+program[1]+"_setup_T_toll.set_text(program[12])") 
			eval("self."+program[1]+"_setup_A.set_text(program[16])") 
			eval("self."+program[1]+"_setup_B.set_text(program[17])") 

		elif (program[1]=="T1"):
			eval("self."+program[1]+"_cycle_head.set_text(program[2])") 
			eval("self."+program[1]+"_cycle_T.set_text(program[6])") 
			eval("self."+program[1]+"_cycle_A.set_text(program[16])") 
			eval("self."+program[1]+"_cycle_B.set_text(program[17])") 

			eval("self."+program[1]+"_conf_head.set_text(program[2])") 
			eval("self."+program[1]+"_conf_T.set_text(program[6])") 
			eval("self."+program[1]+"_conf_A.set_text(program[16])") 
			eval("self."+program[1]+"_conf_B.set_text(program[17])") 

			eval("self."+program[1]+"_setup_head.set_text(program[2])") 
			eval("self."+program[1]+"_setup_T.set_text(program[6])") 
			eval("self."+program[1]+"_setup_A.set_text(program[16])") 
			eval("self."+program[1]+"_setup_B.set_text(program[17])") 

		elif (program[1]=="S1"):
			eval("self."+program[1]+"_cycle_head.set_text(program[2])") 
			eval("self."+program[1]+"_cycle_NA.set_text(program[4])") 
			eval("self."+program[1]+"_cycle_S.set_text(program[5])") 
			eval("self."+program[1]+"_cycle_T.set_text(program[6])") 
			eval("self."+program[1]+"_cycle_F.set_text(program[7])")
			eval("self."+program[1]+"_cycle_NA_toll.set_text(program[10])") 
			eval("self."+program[1]+"_cycle_T_toll.set_text(program[12])") 
			eval("self."+program[1]+"_cycle_F_toll.set_text(program[13])") 
			eval("self."+program[1]+"_cycle_A.set_text(program[16])") 
			eval("self."+program[1]+"_cycle_B.set_text(program[17])") 
		
			eval("self."+program[1]+"_conf_head.set_text(program[2])") 
			eval("self."+program[1]+"_conf_NA.set_text(program[4])") 
			eval("self."+program[1]+"_conf_S.set_text(program[5])") 
			eval("self."+program[1]+"_conf_T.set_text(program[6])") 
			eval("self."+program[1]+"_conf_F.set_text(program[7])")
			eval("self."+program[1]+"_conf_NA_toll.set_text(program[10])") 
			eval("self."+program[1]+"_conf_T_toll.set_text(program[12])") 
			eval("self."+program[1]+"_conf_F_toll.set_text(program[13])") 
			eval("self."+program[1]+"_conf_A.set_text(program[16])") 
			eval("self."+program[1]+"_conf_B.set_text(program[17])") 
		
			eval("self."+program[1]+"_setup_head.set_text(program[2])") 
			eval("self."+program[1]+"_setup_NA.set_text(program[4])") 
			eval("self."+program[1]+"_setup_S.set_text(program[5])") 
			eval("self."+program[1]+"_setup_T.set_text(program[6])") 
			eval("self."+program[1]+"_setup_F.set_text(program[7])")
			eval("self."+program[1]+"_setup_NA_toll.set_text(program[10])") 
			eval("self."+program[1]+"_setup_T_toll.set_text(program[12])") 
			eval("self."+program[1]+"_setup_F_toll.set_text(program[13])") 
			eval("self."+program[1]+"_setup_A.set_text(program[16])") 
			eval("self."+program[1]+"_setup_B.set_text(program[17])") 
		

############################################################################
#CLASS MAIN_GUI ENDS




# MAIN LOOP 
#####################################################################3######
if __name__ == "__main__":
	main = main_GUI()
	Gtk.main()


