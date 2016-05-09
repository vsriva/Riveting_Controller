#!/usr/bin/env python
import subprocess, os, time, pickle

from gi.repository import Gtk
from keypad import Keypad
from main import *
from recall import *

from datetime import datetime


conf=("","","","","","","")
alarm=("","","","")
log=("","","","")
time_sett=("","","","","","","","","")
adv_sett=["settings/adv_sett"]

#conf[3]="any" Admin password
#conf[2]="new" Superuser password



class Sett_GUI (Keypad):
  	filename="plot/foo.png"
	no=0 
	day=0
	superuser_pass_change_curr_resp=""
	superuser_pass_change_new_resp=""
	superuser_pass_change_ren_new_resp=""
	def sett_init(self):
		self.setfile = "per_screen.glade"
		self.builder = Gtk.Builder()
		self.builder.add_from_file(self.setfile)
		self.builder.connect_signals(self)
		self.mainfile = "dialog_try.glade"
		self.builder2 = Gtk.Builder()
		self.builder2.add_from_file(self.mainfile)
		self.builder2.connect_signals(self)
		self.keypad = self.builder2.get_object("keypad")
		self.result1 = self.builder2.get_object("keypad_disp")

		self.main_screen=self.builder2.get_object("main_screen")
		self.admin_pass=self.builder.get_object("admin_pass")
		self.advanced_settings=self.builder.get_object("advanced_settings")
		self.alarm=self.builder.get_object("alarm")
		self.configuration_settings=self.builder.get_object("configuration_settings")
		self.advanced_settings=self.builder.get_object("advanced_settings")
		self.superuser_pass=self.builder.get_object("superuser_pass")
		self.superuser_pass_change=self.builder.get_object("superuser_pass_change")
		self.time_settings=self.builder.get_object("time_settings")
		self.tools=self.builder.get_object("tools")
		self.graph_win=self.builder.get_object("graph_win")
		self.graph_fullscreen=self.builder.get_object("graph_fullscreen")
		self.table=self.builder.get_object("table")

		
#admin_pass##################################################################		
		self.admin_disp= self.builder.get_object("admin_pass_disp")    
		self.admin_ok=self.builder.get_object("admin_pass_ok")
		self.admin_can=self.builder.get_object("admin_pass_can")

#advanced_settings############################################################# 
		self.advanced_settings_def_toll_NA=self.builder.get_object("advanced_settings_def_toll_NA")
		self.advanced_settings_def_toll_S=self.builder.get_object("advanced_settings_def_toll_S")
		self.advanced_settings_def_toll_T=self.builder.get_object("advanced_settings_def_toll_T")
		self.advanced_settings_def_toll_F=self.builder.get_object("advanced_settings_def_toll_F")
		self.advanced_settings_def_toll_E=self.builder.get_object("advanced_settings_def_toll_E")
		self.advanced_settings_def_toll_H=self.builder.get_object("advanced_settings_def_toll_H")
		self.advanced_settings_max_riv_time=self.builder.get_object("advanced_settings_max_riv_time")
		self.advanced_settings_mot_off_delay=self.builder.get_object("advanced_settings_mot_off_delay")
		self.advanced_settings_auto_pause=self.builder.get_object("advanced_settings_auto_pause")
		self.advanced_settings_cal_path=self.builder.get_object("advanced_settings_cal_path")
		self.advanced_settings_Enc_path=self.builder.get_object("advanced_settings_Enc_path")

		self.advanced_settings_form_fac=self.builder.get_object("advanced_settings_form_fac")
		self.advanced_settings_orb_riv=self.builder.get_object("advanced_settings_orb_riv")
		self.advanced_settings_delta_T=self.builder.get_object("advanced_settings_delta_T")
		self.advanced_settings_delta_F=self.builder.get_object("advanced_settings_delta_F")
		self.advanced_settings_min_path_touch=self.builder.get_object("advanced_settings_min_path_touch")
		self.advanced_settings_plus_toll_S=self.builder.get_object("advanced_settings_plus_toll_S")
		self.advanced_settings_plus_toll_T=self.builder.get_object("advanced_settings_plus_toll_T")
		self.advanced_settings_plus_toll_F=self.builder.get_object("advanced_settings_plus_toll_F")
		self.advanced_settings_plus_toll_E=self.builder.get_object("advanced_settings_plus_toll_E")
		self.advanced_settings_plus_toll_H=self.builder.get_object("advanced_settings_plus_toll_H")
		self.advanced_settings_curve_int=self.builder.get_object("advanced_settings_curve_int")

		self.advanced_settings_min_force=self.builder.get_object("advanced_settings_min_force")
		self.advanced_settings_force_zoom=self.builder.get_object("advanced_settings_force_zoom")
		self.advanced_settings_log_drive=self.builder.get_object("advanced_settings_log_drive")
		self.advanced_settings_speed=self.builder.get_object("advanced_settings_speed")
		self.advanced_settings_func_x14=self.builder.get_object("advanced_settings_func_x14")
		self.advanced_settings_auto_com=self.builder.get_object("advanced_settings_auto_com")
		self.advanced_settings_error_emg=self.builder.get_object("advanced_settings_error_emg")
		self.advanced_settings_mot_off_delay=self.builder.get_object("advanced_settings_reset_time")
		self.advanced_settings_PLC_act=self.builder.get_object("advanced_settings_PLC_act")
		self.advanced_settings_touch_probe=self.builder.get_object("advanced_settings_touch_probe")
		self.adadvanced_settings_prog_diag=self.builder.get_object("advanced_settings_prog_diag")

		self.advanced_settings_off_ext_NA=self.builder.get_object("advanced_settings_off_ext_NA")
		self.advanced_settings_path_meas_H=self.builder.get_object("advanced_settings_path_meas_H")
		self.advanced_settings_min_path_H=self.builder.get_object("advanced_settings_min_path_H")
		self.advanced_settings_minus_path=self.builder.get_object("advanced_settings_minus_path")
		self.advanced_settings_off_path_toll=self.builder.get_object("advanced_settings_off_path_toll")
		self.advanced_settings_min_path_NA=self.builder.get_object("advanced_settings_min_path_NA")
		self.advanced_settings_time_NA=self.builder.get_object("advanced_settings_time_NA")
		self.advanced_settings_cal_press_force=self.builder.get_object("advanced_settings_cal_press_force")
		self.advanced_settings_upp_pis=self.builder.get_object("advanced_settings_upp_pis")
		self.advanced_settings_low_pis=self.builder.get_object("advanced_settings_low_pis")
		self.advanced_settings_man_trigg=self.builder.get_object("advanced_settings_man_trigg")


		self.advanced_settings_up_data_cycle=self.builder.get_object("advanced_settings_up_data_cycle")
		self.advanced_settings_cal_path=self.builder.get_object("advanced_settings_cal_path")


		self.advanced_settings_exit=self.builder.get_object("advanced_settings_exit")
		self.advanced_settings_save=self.builder.get_object("advanced_settings_save")
		self.advanced_settings_reset=self.builder.get_object("advanced_settings_reset")
		self.advanced_settings_GUI_exit=self.builder.get_object("advanced_settings_GUI_exit")

		self.advanced_settings_date_and_time=self.builder.get_object("advanced_settings_date_and_time")


#Time_settings#######################################################################
		self.Time_settings_day=self.builder.get_object("Time_settings_day")
		self.Time_settings_month=self.builder.get_object("Time_settings_month")
		self.Time_settings_year=self.builder.get_object("Time_settings_year")
		self.Time_settings_hours=self.builder.get_object("Time_settings_hours")
		self.Time_settings_min=self.builder.get_object("Time_settings_min")
		self.Time_settings_sec=self.builder.get_object("Time_settings_sec")
		self.Time_settings_time_riv=self.builder.get_object("Time_settings_time_riv")
		self.Time_settings_time_op=self.builder.get_object("Time_settings_time_op")

		self.Time_settings_exit=self.builder.get_object("Time_settings_exit")
		self.Time_settings_save=self.builder.get_object("Time_settings_save")
		self.Time_settings_reset=self.builder.get_object("Time_settings_reset")

#configuration_settings###########################################################
		self.configuration_settings_user_pass=self.builder.get_object("configuration_settings_user_pass")
		self.configuration_settings_adm_pass=self.builder.get_object("configuration_settings_adm_pass")
		self.configuration_settings_su_pass=self.builder.get_object("configuration_settings_su_pass")
		self.configuration_settings_serial=self.builder.get_object("configuration_settings_serial")
		self.configuration_settings_ip_add=self.builder.get_object("configuration_settings_ip_add")
		self.configuration_settings_ip_sub=self.builder.get_object("configuration_settings_ip_sub")

		self.configuration_settings_exit=self.builder.get_object("configuration_settings_exit")
		self.configuration_settings_save=self.builder.get_object("configuration_settings_save")
		self.configuration_settings_reset=self.builder.get_object("configuration_settings_reset")

		self.configuration_settings_date_and_time=self.builder.get_object("configuration_settings_date_and_time")

#alarm################################################################################
		self.alarm1_date=self.builder.get_object("alarm1_date")
		self.alarm1_time=self.builder.get_object("alarm1_time")
		self.alarm1_mess=self.builder.get_object("alarm1_mess")
		
		self.alarm2_date=self.builder.get_object("alarm2_date")
		self.alarm2_time=self.builder.get_object("alarm2_time")
		self.alarm2_mess=self.builder.get_object("alarm2_mess")
		
		self.alarm3_date=self.builder.get_object("alarm3_date")
		self.alarm3_time=self.builder.get_object("alarm3_time")
		self.alarm3_mess=self.builder.get_object("alarm3_mess")
		
		self.alarm4_date=self.builder.get_object("alarm4_date")
		self.alarm4_time=self.builder.get_object("alarm4_time")
		self.alarm4_mess=self.builder.get_object("alarm4_mess")
		
		self.alarm5_date=self.builder.get_object("alarm5_date")
		self.alarm5_time=self.builder.get_object("alarm5_time")
		self.alarm5_mess=self.builder.get_object("alarm5_mess")
		
		self.alarm6_date=self.builder.get_object("alarm6_date")
		self.alarm6_time=self.builder.get_object("alarm6_time")
		self.alarm6_mess=self.builder.get_object("alarm6_mess")
		
		self.alarm7_date=self.builder.get_object("alarm7_date")
		self.alarm7_time=self.builder.get_object("alarm7_time")
		self.alarm7_mess=self.builder.get_object("alarm7_mess")
		
		self.alarm8_date=self.builder.get_object("alarm8_date")
		self.alarm8_time=self.builder.get_object("alarm8_time")
		self.alarm8_mess=self.builder.get_object("alarm8_mess")
		
		self.alarm9_date=self.builder.get_object("alarm9_date")
		self.alarm9_time=self.builder.get_object("alarm9_time")
		self.alarm9_mess=self.builder.get_object("alarm9_mess")
		
		self.alarm10_date=self.builder.get_object("alarm10_date")
		self.alarm10_time=self.builder.get_object("alarm10_time")
		self.alarm10_mess=self.builder.get_object("alarm10_mess")

		self.alarm11_date=self.builder.get_object("alarm11_date")
		self.alarm11_time=self.builder.get_object("alarm11_time")
		self.alarm11_mess=self.builder.get_object("alarm11_mess")
		
		self.alarm_table=self.builder.get_object("alarm_table")

		self.alarm_exit=self.builder.get_object("alarm_exit")

#tools######################################################################
		self.tools_conf_set=self.builder.get_object("tools_conf_set")
		self.tools_alarm_his=self.builder.get_object("tools_alarm_his")
		self.tools_exp_prog=self.builder.get_object("tools_exp_prog")
		self.tools_load_set=self.builder.get_object("tools_load_set")
		self.tools_load_prog=self.builder.get_object("tools_load_prog")
		self.tools_log_data=self.builder.get_object("tools_log_data")
		self.tools_time_det=self.builder.get_object("tools_time_det")
		self.tools_pass=self.builder.get_object("tools_pass")
		self.tools_ok_reset=self.builder.get_object("tools_ok_reset")
		self.tools_nok_reset=self.builder.get_object("tools_nok_reset")
		self.tools_fac_set=self.builder.get_object("tools_fac_set")
		self.tools_exit=self.builder.get_object("tools_exit")
		
	
#superuser_pass##############################################################
		self.superuser_pass_disp= self.builder.get_object("superuser_pass_disp")    

		self.superuser_pass_ok=self.builder.get_object("superuser_pass_ok")
		self.superuser_pass_can=self.builder.get_object("superuser_pass_can")

#superuser_pass_change##############################################################
		self.superuser_pass_change_curr_pass= self.builder.get_object("superuser_pass_change_curr_pass")    
		self.superuser_pass_change_new_pass= self.builder.get_object("superuser_pass_change_new_pass")    
		self.superuser_pass_change_ren_new_pass= self.builder.get_object("superuser_pass_change_ren_new_pass")    
		self.superuser_pass_change_ok=self.builder.get_object("superuser_pass_change_ok")
		self.superuser_pass_change_can=self.builder.get_object("superuser_pass_change_can")


#logger_data################################################################
		self.logger_data_date1=self.builder.get_object("logger_data_date1")
		self.logger_data_time1=self.builder.get_object("logger_data_time1")
		self.logger_data_mess1=self.builder.get_object("logger_data_mess1")
		
		self.logger_data_date2=self.builder.get_object("logger_data_date2")
		self.logger_data_time2=self.builder.get_object("logger_data_time2")
		self.logger_data_mess2=self.builder.get_object("logger_data_mess2")
		
		self.logger_data_date3=self.builder.get_object("logger_data_date3")
		self.logger_data_time3=self.builder.get_object("logger_data_time3")
		self.logger_data_mess3=self.builder.get_object("logger_data_mess3")
		
		self.logger_data_date4=self.builder.get_object("logger_data_date4")
		self.logger_data_time4=self.builder.get_object("logger_data_time4")
		self.logger_data_mess4=self.builder.get_object("logger_data_mess4")
		
		self.logger_data_date5=self.builder.get_object("logger_data_date5")
		self.logger_data_time5=self.builder.get_object("logger_data_time5")
		self.logger_data_mess5=self.builder.get_object("logger_data_mess5")
	
		self.logger_data_date6=self.builder.get_object("logger_data_date6")
		self.logger_data_time6=self.builder.get_object("logger_data_time6")
		self.logger_data_mess6=self.builder.get_object("logger_data_mess6")
		
		self.logger_data_date7=self.builder.get_object("logger_data_date7")
		self.logger_data_time7=self.builder.get_object("logger_data_time7")
		self.logger_data_mess7=self.builder.get_object("logger_data_mess7")
		
		self.logger_data_date8=self.builder.get_object("logger_data_date8")
		self.logger_data_time8=self.builder.get_object("logger_data_time8")
		self.logger_data_mess8=self.builder.get_object("logger_data_mess8")
		
		self.logger_data_date9=self.builder.get_object("logger_data_date9")
		self.logger_data_time9=self.builder.get_object("logger_data_time9")
		self.logger_data_mess9=self.builder.get_object("logger_data_mess9")
		
		self.logger_data_date10=self.builder.get_object("logger_data_date10")
		self.logger_data_time10=self.builder.get_object("logger_data_time10")
		self.logger_data_mess10=self.builder.get_object("logger_data_mess10")

		self.logger_data_exit=self.builder.get_object("logger_data_exit")

  
    
#graph_fullscreen##############################################################
		
		self.graph_fullscreen_disp= self.builder.get_object("graph_fullscreen_disp") 

		self.recall_conf()


		

#MAIN_SCREEN
###################################################################

	def on_main_screen_tools_clicked(self, object, data=None):
		self.admin_pass.show()

#MESSAGE_BOX
###################################################################

	def info_box(self, win,prime_message,sec_message):
		dialog = Gtk.MessageDialog(win, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, prime_message)
		dialog.format_secondary_text(sec_message)
		dialog.run()
		print "INFO dialog closed"
		dialog.destroy()

	def error_box(self,prime_message,sec_message):
		dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.ERROR, Gtk.ButtonsType.CANCEL, prime_message)
		dialog.format_secondary_text(sec_message)
		dialog.run()
		print "ERROR dialog closed"
		dialog.destroy()

	def warn_box(self,win,prime_message,sec_message):
		flag=0
		dialog = Gtk.MessageDialog(win,0, Gtk.MessageType.WARNING, Gtk.ButtonsType.OK_CANCEL, prime_message)
		dialog.format_secondary_text(sec_message)
		response = dialog.run()
		if response == Gtk.ResponseType.OK:
			print "WARN dialog closed by clicking OK button"
			flag=1
		elif response == Gtk.ResponseType.CANCEL:
			print "WARN dialog closed by clicking CANCEL button"
			flag=0

		dialog.destroy()
		return flag

	def question_box(self, prime_message,sec_message):
		flag=0
		dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.QUESTION, Gtk.ButtonsType.YES_NO, prime_message)
		dialog.format_secondary_text(sec_message)
		response = dialog.run()
		if response == Gtk.ResponseType.YES:
			print "QUESTION dialog closed by clicking YES button"
			flag=1
		elif response == Gtk.ResponseType.NO:
			print "QUESTION dialog closed by clicking NO button"
			flag=0
		dialog.destroy()
		return flag




#ADMIN_PASS
###################################################################

	def on_admin_disp_button_press_event(self, object, data=None):
		self.keypad.show()
		self.admin_pass.hide()
		self.curr_window=self.admin_pass
		self.curr_mode1=self.admin_disp
		self.curr_mode2=self.admin_disp
		self.curr_mode3=self.admin_disp

	def on_admin_ok_clicked(self, object, data=None):
		self.admin_resp=str(self.admin_disp.get_text())
		print self.admin_resp, len(self.admin_resp)
		if (self.admin_resp == conf[2])|(self.admin_resp == conf[3]):
			self.tools.show()
			self.main_screen.hide()
			self.admin_disp.set_text("")
			self.admin_pass.hide()
			
		else:
			self.admin_pass.hide()
			self.admin_disp.set_text("")
			self.admin_pass.show()

	def on_admin_can_clicked(self, object, data="None"):
		self.main_screen.show()
		self.admin_disp.set_text("")
		self.admin_pass.hide()	



#TOOLS
################################################################
 
	def on_tools_conf_set_clicked(self, object, data="None"):
		print "tools_conf_set_clicked"
		self.tools.hide()
		self.configuration_settings.show() 
 
	def on_tools_alarm_his_clicked(self, object, data="None"):
		print "tools_alarm_his_clicked"
		self.tools.hide()
		self.recall_alarm()
		self.alarm.show()
 
	def on_tools_exp_prog_clicked(self, object, data="None"):
		print "tools_exp_prog_clicked"
		self.exp_path=find_usbdrive()
		print self.exp_path
		self.path="mkdir "+self.exp_path+"/programs"
		os.system(self.path)
		os.system("cp -r programs "+self.exp_path)
		os.system("cp -r settings "+self.exp_path)
		
	def on_tools_load_set_clicked(self, object, data="None"):
		print "tools_load_set_clicked"
		self.exp_path=find_usbdrive()
		print self.exp_path
		os.system("cp -r "+self.exp_path+"/settings ./")
		
	def on_tools_load_prog_clicked(self, object, data="None"):
		print "tools_load_prog_clicked"
		self.exp_path=find_usbdrive()
		print self.exp_path
		os.system("cp -r "+self.exp_path+"/programs ./")
		print "done"
                          
	def on_tools_log_data_clicked(self, object, data="None"):
		print "tools_log_data_clicked"
		self.tools.hide()
		self.recall_log()
		self.logger_data.show()
 
	def on_tools_time_det_clicked(self, object, data="None"):
		print "tools_time_det_clicked"
		self.tools.hide()
		#self.recall_time()
		self.time_settings.show()
		self.feed_time()

 
	def on_tools_pass_clicked(self, object, data="None"):
		print "tools_pass_clicked"
		self.superuser_pass.show()
 
	def on_tools_ok_reset_clicked(self, object, data="None"):
		print "tools_ok_reset_clicked"
		self.OK_counter_reset()
 
	def on_tools_nok_reset_clicked(self, object, data="None"):
		print "tools_nok_reset_clicked"
		self.NOK_counter_reset()
 
	def on_tools_fac_set_clicked(self, object, data="None"):
		print "tools_fac_set_clicked"
		os.system("cp -r reset/* ./programs ")
		
 
	def on_tools_exit_clicked(self, object, data="None"):
		print "tools_exit_clicked"
		self.tools.hide()
		self.main_screen.show()

#TIME_SETTINGS
###################################################################
	def on_Time_settings_time_exit_clicked(self, object, data=None):
		print "time_settings_exit_clicked"
		self.time_settings.hide()
		self.main_screen.show()

	def on_Time_settings_time_save_clicked(self, object, data=None):
		print "time_settings_save_clicked"
		self.day=str(self.Time_settings_day.get_text())
		self.month=str(self.Time_settings_month.get_text())
		self.year=str(self.Time_settings_year.get_text())

		self.hours=str(self.Time_settings_hours.get_text())
		self.min=str(self.Time_settings_min.get_text())
		self.sec=str(self.Time_settings_sec.get_text())

		os.system("echo fastrack | sudo date +%Y%m%d -s \""+self.year+self.month+self.day+"\"")
		os.system("echo fastrack | sudo date +%T -s \""+self.hours+":"+self.min+":"+self.sec+"\"")

		self.riv_time=str(self.Time_settings_time_riv.get_text())
		self.op_time=str(self.Time_settings_time_op.get_text())

		save_file(("settings/time_sett",self.day,self.month,self.year,self.hours,self.min,self.sec,self.riv_time,self.op_time))

	def on_Time_settings_time_reset_clicked(self, object, data=None):
		print "time_settings_reset_clicked"
		self.day=str(12)
		self.month=str(12)
		self.year=str(2012)

		self.hours=str(12)
		self.min=str(00)
		self.sec=str(00)

		self.riv_time=str("01-01-2012 00:00:00")
		self.op_time=str("01-01-2012 00:00:00")

		os.system("echo fastrack | sudo date -s \"01 JAN 2012 00:00:00\"") 

		self.Time_settings_day.set_text(self.day)
		self.Time_settings_month.set_text(self.month)
		self.Time_settings_year.set_text(self.year)

		self.Time_settings_hours.set_text(self.hours)
		self.Time_settings_min.set_text(self.min)
		self.Time_settings_sec.set_text(self.sec)


		print ("time_sett",self.day,self.month,self.year,self.hours,self.min,self.sec,self.riv_time,self.op_time)


		save_file(("settings/time_sett",self.day,self.month,self.year,self.hours,self.min,self.sec,self.riv_time,self.op_time))
		self.recall_time()

	def on_Time_settings_time_riv_button_press_event(self, object, data=None):
		self.keypad.show()
		self.time_settings.hide()
		self.curr_window=self.time_settings
		self.curr_mode1=self.Time_settings_time_riv
		self.curr_mode2=self.Time_settings_time_riv
		self.curr_mode3=self.Time_settings_time_riv

	def on_Time_settings_time_op_button_press_event(self, object, data=None):
		self.keypad.show()
		self.time_settings.hide()
		self.curr_window=self.time_settings
		self.curr_mode1=self.Time_settings_time_op
		self.curr_mode2=self.Time_settings_time_op
		self.curr_mode3=self.Time_settings_time_op

#SUPERUSER_PASS
###################################################################
	def on_superuser_pass_disp_button_press_event(self, object, data=None):
		self.keypad.show()
		self.superuser_pass.hide()
		self.curr_window=self.superuser_pass
		self.curr_mode1=self.superuser_pass_disp
		self.curr_mode2=self.superuser_pass_disp
		self.curr_mode3=self.superuser_pass_disp

	def on_superuser_pass_ok_clicked(self, object, data=None):
		self.superuser_pass_resp=str(self.superuser_pass_disp.get_text())
		print self.superuser_pass_resp, len(self.superuser_pass_resp)
		if (self.superuser_pass_resp == conf[3]):
			self.advanced_settings.show()
			self.tools.hide()
			self.superuser_pass_disp.set_text("")
			self.superuser_pass.hide()
			
		else:
			self.superuser_pass.hide()
			self.superuser_pass_disp.set_text("")
			self.superuser_pass.show()

	def on_superuser_pass_can_clicked(self, object, data="None"):
		self.tools.show()
		self.superuser_pass_disp.set_text("")
		self.superuser_pass.hide()	

#SUPERUSER_PASS_CHANGE
###################################################################
	def on_superuser_pass_change_curr_pass_button_press_event(self, object, data=None):
		self.keypad.show()
		self.superuser_pass_change.hide()
		self.curr_window=self.superuser_pass_change
		self.curr_mode1=self.superuser_pass_change_curr_pass
		self.curr_mode2=self.superuser_pass_change_curr_pass
		self.curr_mode3=self.superuser_pass_change_curr_pass
	def on_superuser_pass_change_new_pass_button_press_event(self, object, data=None):
		self.keypad.show()
		self.superuser_pass_change.hide()
		self.curr_window=self.superuser_pass_change
		self.curr_mode1=self.superuser_pass_change_new_pass
		self.curr_mode2=self.superuser_pass_change_new_pass
		self.curr_mode3=self.superuser_pass_change_new_pass
	def on_superuser_pass_change_ren_new_pass_button_press_event(self, object, data=None):
		self.keypad.show()
		self.superuser_pass_change.hide()
		self.curr_window=self.superuser_pass_change
		self.curr_mode1=self.superuser_pass_change_ren_new_pass
		self.curr_mode2=self.superuser_pass_change_ren_new_pass
		self.curr_mode3=self.superuser_pass_change_ren_new_pass

	def on_superuser_pass_change_ok_clicked(self, object, data=None):
		global conf
		self.superuser_pass_change_curr_resp=str(self.superuser_pass_change_curr_pass.get_text())
		self.superuser_pass_chatnge_new_resp=str(self.superuser_pass_change_new_pass.get_text())
		self.superuser_pass_change_ren_new_resp=str(self.superuser_pass_change_ren_new_pass.get_text())

		print self.superuser_pass_change_curr_resp, len(self.superuser_pass_change_curr_resp)
		print self.superuser_pass_change_new_resp, len(self.superuser_pass_change_new_resp)
		print self.superuser_pass_change_ren_new_resp, len(self.superuser_pass_change_ren_new_resp)

		if ((self.superuser_pass_change_curr_resp == conf[3])&(self.superuser_pass_change_new_resp == self.superuser_pass_change_ren_new_resp)):
			print "Password Changed"
			conf[3]=self.superuser_pass_change_new_resp	
			self.configuration_settings_su_pass.set_text(conf[3])		
			self.superuser_pass_change_curr_pass.set_text("")
			self.superuser_pass_change_new_pass.set_text("")
			self.superuser_pass_change_ren_new_pass.set_text("")
			self.superuser_pass_change.hide()
			self.configuration_settings.show()

			
		else:
			self.superuser_pass_change.hide()
			print "Wrong Password or mismatch"
			self.superuser_pass_change_curr_pass.set_text("")
			self.superuser_pass_change_new_pass.set_text("")
			self.superuser_pass_change_ren_new_pass.set_text("")
			self.superuser_pass_change.show()

	def on_superuser_pass_change_can_clicked(self, object, data="None"):
		self.configuration_settings.show()
		self.superuser_pass_change_curr_pass.set_text("")
		self.superuser_pass_change_new_pass.set_text("")
		self.superuser_pass_change_ren_new_pass.set_text("")
		self.superuser_pass_change.hide()	

#ALARM
###################################################################
	def on_alarm_exit_clicked(self, object, data="None"):
		print "alarm_exit_clicked"
		self.alarm.hide()
		self.main_screen.show()	



#LOGGER_DATA
###################################################################
	def on_logger_data_exit_clicked(self, object, data="None"):
		print "logger_data_exit_clicked"
		self.logger_data.hide()
		self.main_screen.show()	



#CONFIGURATION_SETTINGS
###################################################################

	def on_configuration_settings_exit_clicked(self, object, data="None"):
		print "configuration_settings_exit"
		self.main_screen.show()
		self.configuration_settings.hide()

	def on_configuration_settings_save_clicked(self, object, data="None"):
		print "configuration_settings_save"
		self.user_pass=str(self.configuration_settings_user_pass.get_text())
		self.adm_pass=str(self.configuration_settings_adm_pass.get_text())
		self.su_pass=str(self.configuration_settings_su_pass.get_text())
		self.serial=str(self.configuration_settings_serial.get_text())
		self.ip_add=str(self.configuration_settings_ip_add.get_text())
		self.ip_sub=str(self.configuration_settings_ip_sub.get_text())

		save_file(("settings/conf_sett",self.user_pass,self.adm_pass,self.su_pass,self.serial,self.ip_add,self.ip_sub))


	def on_configuration_settings_reset_clicked(self, object, data="None"):
		print "configuration_settings_reset"
		self.user_pass=str(0)
		self.adm_pass=str(0)
		self.su_pass=str(0)
		self.serial=str(0)
		self.ip_add=str(0)
		self.ip_sub=str(0)

		self.configuration_settings_user_pass.set_text("")
		self.configuration_settings_adm_pass.set_text("")
		self.configuration_settings_su_pass.set_text("")
		self.configuration_settings_serial.set_text("")
		self.configuration_settings_ip_add.set_text("")
		self.configuration_settings_ip_sub.set_text("")

		save_file(("settings/conf_sett",self.user_pass,self.adm_pass,self.su_pass,self.serial,self.ip_add,self.ip_sub))

	def on_configuration_settings_clear_prog_clicked(self, object, data="None"):
		print "configuration_settings_clear_prog"
		dialog_win=self.main_screen
		ans=self.warn_box(dialog_win,"Remove All Programs","Do you want to remove all the programs ?")
    		if ans==1:
			os.system("rm -r programs/*")



	def on_configuration_settings_user_pass_button_press_event(self, object, data="None"):
		print "configuration_settings_user_pass"
		self.keypad.show()
		self.configuration_settings.hide()
		self.curr_window=self.configuration_settings
		self.curr_mode1=self.configuration_settings_user_pass
		self.curr_mode2=self.configuration_settings_user_pass
		self.curr_mode3=self.configuration_settings_user_pass

	def on_configuration_settings_adm_pass_button_press_event(self, object, data="None"):
		print "configuration_settings_adm_pass"
		self.keypad.show()
		self.configuration_settings.hide()
		self.curr_window=self.configuration_settings
		self.curr_mode1=self.configuration_settings_adm_pass
		self.curr_mode2=self.configuration_settings_adm_pass
		self.curr_mode3=self.configuration_settings_adm_pass

	def on_configuration_settings_su_pass_button_press_event(self, object, data="None"):
		print "configuration_settings_su_pass"
		self.superuser_pass_change.show()
		self.configuration_settings.hide()

	def on_configuration_settings_serial_button_press_event(self, object, data="None"):
		print "configuration_settings_serial"
		self.keypad.show()
		self.configuration_settings.hide()
		self.curr_window=self.configuration_settings
		self.curr_mode1=self.configuration_settings_serial
		self.curr_mode2=self.configuration_settings_serial
		self.curr_mode3=self.configuration_settings_serial


	def on_configuration_settings_ip_add_button_press_event(self, object, data="None"):
		print "configuration_settings_ip_add"
		self.keypad.show()
		self.configuration_settings.hide()
		self.curr_window=self.configuration_settings
		self.curr_mode1=self.configuration_settings_ip_add
		self.curr_mode2=self.configuration_settings_ip_add
		self.curr_mode3=self.configuration_settings_ip_add

	def on_configuration_settings_ip_sub_button_press_event(self, object, data="None"):
		print "configuration_settings_ip_sub"
		self.keypad.show()
		self.configuration_settings.hide()
		self.curr_window=self.configuration_settings
		self.curr_mode1=self.configuration_settings_ip_sub
		self.curr_mode2=self.configuration_settings_ip_sub
		self.curr_mode3=self.configuration_settings_ip_sub



#ADVANCED_SETTINGS
###################################################################

	def on_advanced_settings_exit_clicked(self, object, data="None"):
		print "advanced_settings_exit"
		self.main_screen.show()
		self.advanced_settings.hide()

	def on_advanced_settings_save_clicked(self, object, data="None"):
		print "advanced_settings_save"
		global adv_sett
		adv_sett.append(self.advanced_settings_def_toll_NA.get_text())
		adv_sett.append(self.advanced_settings_def_toll_S.get_text())
		adv_sett.append(self.advanced_settings_def_toll_T.get_text())
		adv_sett.append(self.advanced_settings_def_toll_F.get_text())
		adv_sett.append(self.advanced_settings_def_toll_E.get_text())
		adv_sett.append(self.advanced_settings_def_toll_H.get_text())
		adv_sett.append(self.advanced_settings_max_riv_time.get_text())
		adv_sett.append(self.advanced_settings_mot_off_delay.get_text())
		adv_sett.append(self.advanced_settings_auto_pause.get_text())
		adv_sett.append(self.advanced_settings_cal_path.get_text())
		adv_sett.append(self.advanced_settings_Enc_path.get_text())

		adv_sett.append(self.advanced_settings_form_fac.get_text())
		adv_sett.append(self.advanced_settings_orb_riv.get_text())
		adv_sett.append(self.advanced_settings_delta_T.get_text())
		adv_sett.append(self.advanced_settings_delta_F.get_text())
		adv_sett.append(self.advanced_settings_min_path_touch.get_text())
		adv_sett.append(self.advanced_settings_plus_toll_S.get_text())
		adv_sett.append(self.advanced_settings_plus_toll_T.get_text())
		adv_sett.append(self.advanced_settings_plus_toll_F.get_text())
		adv_sett.append(self.advanced_settings_plus_toll_E.get_text())
		adv_sett.append(self.advanced_settings_plus_toll_H.get_text())
		adv_sett.append(self.advanced_settings_curve_int.get_text())

		adv_sett.append(self.advanced_settings_min_force.get_text())
		adv_sett.append(self.advanced_settings_force_zoom.get_text())
		adv_sett.append(self.advanced_settings_log_drive.get_text())
		adv_sett.append(self.advanced_settings_speed.get_text())
		adv_sett.append(self.advanced_settings_func_x14.get_text())
		adv_sett.append(self.advanced_settings_auto_com.get_text())
		adv_sett.append(self.advanced_settings_error_emg.get_text())
		adv_sett.append(self.advanced_settings_mot_off_delay.get_text())
		adv_sett.append(self.advanced_settings_PLC_act.get_text())
		adv_sett.append(self.advanced_settings_touch_probe.get_text())
		adv_sett.append(self.adadvanced_settings_prog_diag.get_text())

		adv_sett.append(self.advanced_settings_off_ext_NA.get_text())
		adv_sett.append(self.advanced_settings_path_meas_H.get_text())
		adv_sett.append(self.advanced_settings_min_path_H.get_text())
		adv_sett.append(self.advanced_settings_minus_path.get_text())
		adv_sett.append(self.advanced_settings_off_path_toll.get_text())
		adv_sett.append(self.advanced_settings_min_path_NA.get_text())
		adv_sett.append(self.advanced_settings_time_NA.get_text())
		adv_sett.append(self.advanced_settings_cal_press_force.get_text())
		adv_sett.append(self.advanced_settings_upp_pis.get_text())
		adv_sett.append(self.advanced_settings_low_pis.get_text())
		adv_sett.append(self.advanced_settings_man_trigg.get_text())


		adv_sett.append(self.advanced_settings_up_data_cycle.get_text())
		adv_sett.append(self.advanced_settings_cal_path.get_text())


		save_file(adv_sett)


	def on_advanced_settings_reset_clicked(self, object, data="None"):
		print "configuration_settings_reset"
		global adv_sett
		self.advanced_settings_def_toll_NA.set_text("")
		self.advanced_settings_def_toll_S.set_text("")
		self.advanced_settings_def_toll_T.set_text("")
		self.advanced_settings_def_toll_F.set_text("")
		self.advanced_settings_def_toll_E.set_text("")
		self.advanced_settings_def_toll_H.set_text("")
		self.advanced_settings_max_riv_time.set_text("")
		self.advanced_settings_mot_off_delay.set_text("")
		self.advanced_settings_auto_pause.set_text("")
		self.advanced_settings_cal_path.set_text("")
		self.advanced_settings_Enc_path.set_text("")

		self.advanced_settings_form_fac.set_text("")
		self.advanced_settings_orb_riv.set_text("")
		self.advanced_settings_delta_T.set_text("")
		self.advanced_settings_delta_F.set_text("")
		self.advanced_settings_min_path_touch.set_text("")
		self.advanced_settings_plus_toll_S.set_text("")
		self.advanced_settings_plus_toll_T.set_text("")
		self.advanced_settings_plus_toll_F.set_text("")
		self.advanced_settings_plus_toll_E.set_text("")
		self.advanced_settings_plus_toll_H.set_text("")
		self.advanced_settings_curve_int.set_text("")

		self.advanced_settings_min_force.set_text("")
		self.advanced_settings_force_zoom.set_text("")
		self.advanced_settings_log_drive.set_text("")
		self.advanced_settings_speed.set_text("")
		self.advanced_settings_func_x14.set_text("")
		self.advanced_settings_auto_com.set_text("")
		self.advanced_settings_error_emg.set_text("")
		self.advanced_settings_mot_off_delay.set_text("")
		self.advanced_settings_PLC_act.set_text("")
		self.advanced_settings_touch_probe.set_text("")
		self.adadvanced_settings_prog_diag.set_text("")

		self.advanced_settings_off_ext_NA.set_text("")
		self.advanced_settings_path_meas_H.set_text("")
		self.advanced_settings_min_path_H.set_text("")
		self.advanced_settings_minus_path.set_text("")
		self.advanced_settings_off_path_toll.set_text("")
		self.advanced_settings_min_path_NA.set_text("")
		self.advanced_settings_time_NA.set_text("")
		self.advanced_settings_cal_press_force.set_text("")
		self.advanced_settings_upp_pis.set_text("")
		self.advanced_settings_low_pis.set_text("")
		self.advanced_settings_man_trigg.set_text("")


		self.advanced_settings_up_data_cycle.set_text("")
		self.advanced_settings_cal_path.set_text("")


		for i in range(0,46):
			adv_sett.append("")


		save_file(adv_sett)


	def on_advanced_settings_GUI_exit_clicked(self, object, data="None"):
		print "advanced_settings_GUI_exit"
		Gtk.main_quit()

	def on_advanced_settings_def_toll_NA_button_press_event(self, object, data=None):
		print "advanced_settings_def_toll_NA selected"
		self.numpad.show()
		self.curr_window=self.advanced_settings
		self.curr_entry=self.advanced_settings_def_toll_NA


	def on_advanced_settings_def_toll_S_button_press_event(self, object, data=None):
		print "advanced_settings_def_toll_S selected"
		self.numpad.show()
		self.curr_window=self.advanced_settings
		self.curr_entry=self.advanced_settings_def_toll_S

	def on_advanced_settings_def_toll_T_button_press_event(self, object, data=None):
		print "advanced_settings_def_toll_T selected"
		self.numpad.show()
		self.curr_window=self.advanced_settings
		self.curr_entry=self.advanced_settings_def_toll_T

	def on_advanced_settings_def_toll_F_button_press_event(self, object, data=None):
		print "advanced_settings_def_toll_F selected"
		self.numpad.show()
		self.curr_window=self.advanced_settings
		self.curr_entry=self.advanced_settings_def_toll_F

	def on_advanced_settings_def_toll_E_button_press_event(self, object, data=None):
		print "advanced_settings_def_toll_E selected"
		self.numpad.show()
		self.curr_window=self.advanced_settings
		self.curr_entry=self.advanced_settings_def_toll_E

	def on_advanced_settings_def_toll_H_button_press_event(self, object, data=None):
		print "advanced_settings_def_toll_H selected"
		self.numpad.show()
		self.curr_window=self.advanced_settings
		self.curr_entry=self.advanced_settings_def_toll_H

	def on_advanced_settings_max_riv_time_button_press_event(self, object, data=None):
		print "advanced_settings_max_riv_time selected"
		self.numpad.show()
		self.curr_window=self.advanced_settings
		self.curr_entry=self.advanced_settings_max_riv_time

	def on_advanced_settings_mot_off_delay_button_press_event(self, object, data=None):
		print "advanced_settings_mot_off_delay selected"
		self.numpad.show()
		self.curr_window=self.advanced_settings
		self.curr_entry=self.advanced_settings_mot_off_delay

	def on_advanced_settings_auto_pause_button_press_event(self, object, data=None):
		print "advanced_settings_auto_pause selected"
		self.numpad.show()
		self.curr_window=self.advanced_settings
		self.curr_entry=self.advanced_settings_auto_pause

	def on_advanced_settings_cal_path_button_press_event(self, object, data=None):
		print "advanced_settings_cal_path selected"
		self.numpad.show()
		self.curr_window=self.advanced_settings
		self.curr_entry=self.advanced_settings_cal_path

	def on_advanced_settings_Enc_path_button_press_event(self, object, data=None):
		print "advanced_settings_Enc_path selected"
		self.numpad.show()
		self.curr_window=self.advanced_settings
		self.curr_entry=self.advanced_settings_Enc_path

	def on_advanced_settings_form_fac_button_press_event(self, object, data=None):
		print "advanced_settings_form_fac selected"
		self.numpad.show()
		self.curr_window=self.advanced_settings
		self.curr_entry=self.advanced_settings_form_fac

	def on_advanced_settings_orb_riv_button_press_event(self, object, data=None):
		print "advanced_settings_orb_riv selected"
		self.numpad.show()
		self.curr_window=self.advanced_settings
		self.curr_entry=self.advanced_settings_orb_riv

	def on_advanced_settings_delta_T_button_press_event(self, object, data=None):
		print "advanced_settings_delta_T selected"
		self.numpad.show()
		self.curr_window=self.advanced_settings
		self.curr_entry=self.advanced_settings_delta_T

	def on_advanced_settings_delta_F_button_press_event(self, object, data=None):
		print "advanced_settings_delta_F selected"
		self.numpad.show()
		self.curr_window=self.advanced_settings
		self.curr_entry=self.advanced_settings_delta_F

	def on_advanced_settings_min_path_touch_button_press_event(self, object, data=None):
		print "advanced_settings_min_path_touch selected"
		self.numpad.show()
		self.curr_window=self.advanced_settings
		self.curr_entry=self.advanced_settings_min_path_touch

	def on_advanced_settings_plus_toll_S_button_press_event(self, object, data=None):
		print "advanced_settings_plus_toll_S selected"
		self.numpad.show()
		self.curr_window=self.advanced_settings
		self.curr_entry=self.advanced_settings_plus_toll_S

	def on_advanced_settings_plus_toll_T_button_press_event(self, object, data=None):
		print "advanced_settings_plus_toll_T selected"
		self.numpad.show()
		self.curr_window=self.advanced_settings
		self.curr_entry=self.advanced_settings_plus_toll_T

	def on_advanced_settings_plus_toll_F_button_press_event(self, object, data=None):
		print "advanced_settings_plus_toll_F selected"
		self.numpad.show()
		self.curr_window=self.advanced_settings
		self.curr_entry=self.advanced_settings_plus_toll_F

	def on_advanced_settings_plus_toll_E_button_press_event(self, object, data=None):
		print "advanced_settings_plus_toll_E selected"
		self.numpad.show()
		self.curr_window=self.advanced_settings
		self.curr_entry=self.advanced_settings_plus_toll_E

	def on_advanced_settings_plus_toll_H_button_press_event(self, object, data=None):
		print "advanced_settings_plus_toll_H selected"
		self.numpad.show()
		self.curr_window=self.advanced_settings
		self.curr_entry=self.advanced_settings_plus_toll_H

	def on_advanced_settings_curve_int_button_press_event(self, object, data=None):
		print "advanced_settings_curve_int selected"
		self.numpad.show()
		self.curr_window=self.advanced_settings
		self.curr_entry=self.advanced_settings_curve_int

	def on_advanced_settings_min_button_press_event(self, object, data=None):
		print "advanced_settings_min selected"
		self.numpad.show()
		self.curr_window=self.advanced_settings
		self.curr_entry=self.advanced_settings_min

	def on_advanced_settings_force_zoom_button_press_event(self, object, data=None):
		print "advanced_settings_force_zoom selected"
		self.numpad.show()
		self.curr_window=self.advanced_settings
		self.curr_entry=self.advanced_settings_force_zoom

	def on_advanced_settings_log_drive_button_press_event(self, object, data=None):
		print "advanced_settings_log_drive selected"
		self.numpad.show()
		self.curr_window=self.advanced_settings
		self.curr_entry=self.advanced_settings_log_drive

	def on_advanced_settings_speed_button_press_event(self, object, data=None):
		print "advanced_settings_speed selected"
		self.numpad.show()
		self.curr_window=self.advanced_settings
		self.curr_entry=self.advanced_settings_speed

	def on_advanced_settings_func_x14_button_press_event(self, object, data=None):
		print "advanced_settings_func_x14 selected"
		self.numpad.show()
		self.curr_window=self.advanced_settings
		self.curr_entry=self.advanced_settings_func_x14

	def on_advanced_settings_auto_com_button_press_event(self, object, data=None):
		print "advanced_settings_auto_com selected"
		self.numpad.show()
		self.curr_window=self.advanced_settings
		self.curr_entry=self.advanced_settings_auto_com

	def on_advanced_settings_error_emg_button_press_event(self, object, data=None):
		print "advanced_settings_error_emg selected"
		self.numpad.show()
		self.curr_window=self.advanced_settings
		self.curr_entry=self.advanced_settings_error_emg

	def on_advanced_settings_mot_off_delay_button_press_event(self, object, data=None):
		print "advanced_settings_mot_off_delay selected"
		self.numpad.show()
		self.curr_window=self.advanced_settings
		self.curr_entry=self.advanced_settings_mot_off_delay

	def on_advanced_settings_PLC_act_button_press_event(self, object, data=None):
		print "advanced_settings_PLC_act selected"
		self.numpad.show()
		self.curr_window=self.advanced_settings
		self.curr_entry=self.advanced_settings_PLC_act

	def on_advanced_settings_touch_probe_button_press_event(self, object, data=None):
		print "advanced_settings_touch_probe selected"
		self.numpad.show()
		self.curr_window=self.advanced_settings
		self.curr_entry=self.advanced_settings_touch_probe

	def on_advanced_settings_prog_diag_button_press_event(self, object, data=None):
		print "advanced_settings_prog_diag selected"
		self.numpad.show()
		self.curr_window=self.advanced_settings
		self.curr_entry=self.advanced_settings_prog_diag

	def on_advanced_settings_off_ext_NA_button_press_event(self, object, data=None):
		print "advanced_settings_off_ext_NA selected"
		self.numpad.show()
		self.curr_window=self.advanced_settings
		self.curr_entry=self.advanced_settings_off_ext_NA

	def on_advanced_settings_path_meas_H_button_press_event(self, object, data=None):
		print "advanced_settings_path_meas_H selected"
		self.numpad.show()
		self.curr_window=self.advanced_settings
		self.curr_entry=self.advanced_settings_path_meas_H

	def on_advanced_settings_minus_path_button_press_event(self, object, data=None):
		print "advanced_settings_minus_path selected"
		self.numpad.show()
		self.curr_window=self.advanced_settings
		self.curr_entry=self.advanced_settings_minus_path

	def on_advanced_settings_off_path_toll_button_press_event(self, object, data=None):
		print "advanced_settings_off_path_toll selected"
		self.numpad.show()
		self.curr_window=self.advanced_settings
		self.curr_entry=self.advanced_settings_off_path_toll

	def on_advanced_settings_min_path_NA_button_press_event(self, object, data=None):
		print "advanced_settings_min_path_NA selected"
		self.numpad.show()
		self.curr_window=self.advanced_settings
		self.curr_entry=self.advanced_settings_min_path_NA

	def on_advanced_settings_press_force_button_press_event(self, object, data=None):
		print "advanced_settings_time_NA selected"
		self.numpad.show()
		self.curr_window=self.advanced_settings
		self.curr_entry=self.advanced_settings_time_NA

	def on_advanced_settings_cal_press_force_button_press_event(self, object, data=None):
		print "advanced_settings_cal_press_force selected"
		self.numpad.show()
		self.curr_window=self.advanced_settings
		self.curr_entry=self.advanced_settings_cal_press_force

	def on_advanced_settings_upp_pis_button_press_event(self, object, data=None):
		print "advanced_settings_upp_pis selected"
		self.numpad.show()
		self.curr_window=self.advanced_settings
		self.curr_entry=self.advanced_settings_upp_pis

	def on_advanced_settings_low_pis_button_press_event(self, object, data=None):
		print "advanced_settings_low_pis selected"
		self.numpad.show()
		self.curr_window=self.advanced_settings
		self.curr_entry=self.advanced_settings_low_pis

	def on_advanced_settings_man_trigg_button_press_event(self, object, data=None):
		print "advanced_settings_man_trigg selected"
		self.numpad.show()
		self.curr_window=self.advanced_settings
		self.curr_entry=self.advanced_settings_man_trigg

	def on_advanced_settings_up_data_cycle_button_press_event(self, object, data=None):
		print "advanced_settings_up_data_cycle selected"
		self.numpad.show()
		self.curr_window=self.advanced_settings
		self.curr_entry=self.advanced_settings_up_data_cycle

	def on_advanced_settings_cal_path_button_press_event(self, object, data=None):
		print "advanced_settings_cal_path selected"
		self.numpad.show()
		self.curr_window=self.advanced_settings
		self.curr_entry=self.advanced_settings_cal_path

	def on_advanced_settings_UDP_comm_button_press_event(self, object, data=None):
		print "advanced_settings_UDP_comm selected"
		self.numpad.show()
		self.curr_window=self.advanced_settings
		self.curr_entry=self.advanced_settings_UDP_comm

	def on_advanced_settings_reset_time_button_press_event(self, object, data=None):
		print "advanced_settings_reset_time selected"
		self.numpad.show()
		self.curr_window=self.advanced_settings
		self.curr_entry=self.advanced_settings_reset_time

	def on_advanced_settings_min_force_button_press_event(self, object, data=None):
		print "advanced_settings_min_force selected"
		self.numpad.show()
		self.curr_window=self.advanced_settings
		self.curr_entry=self.advanced_settings_min_force

	def on_advanced_settings_low_pis_button_press_event(self, object, data=None):
		print "advanced_settings_low_pis selected"
		self.numpad.show()
		self.curr_window=self.advanced_settings
		self.curr_entry=self.advanced_settings_low_pis

	def on_advanced_settings_time_NA_button_press_event(self, object, data=None):
		print "advanced_settings_time_NA selected"
		self.numpad.show()
		self.curr_window=self.advanced_settings
		self.curr_entry=self.advanced_settings_time_NA

	def on_advanced_settings_min_path_H_button_press_event(self, object, data=None):
		print "advanced_settings_min_path_H selected"
		self.numpad.show()
		self.curr_window=self.advanced_settings
		self.curr_entry=self.advanced_settings_min_path_H


#RECALL FUNCTIONS#############################################################
#CONF_SETT######################################################
	def recall_conf(self):
		global conf
		global adv_c

		print "Loading conf_sett"
		conf=load_file("settings/conf_sett")
		self.configuration_settings_user_pass.set_text(conf[1])
		self.configuration_settings_adm_pass.set_text(conf[2])
		self.configuration_settings_su_pass.set_text(conf[3])
		self.configuration_settings_serial.set_text(conf[4])
		self.configuration_settings_ip_add.set_text(conf[5])
		self.configuration_settings_ip_sub.set_text(conf[6])

		
		print "Loading adv_sett"
		adv_c=load_file("settings/adv_sett")

		self.advanced_settings_def_toll_NA.set_text(adv_c[1])
		self.advanced_settings_def_toll_S.set_text(adv_c[2])
		self.advanced_settings_def_toll_T.set_text(adv_c[3])
		self.advanced_settings_def_toll_F.set_text(adv_c[4])
		self.advanced_settings_def_toll_E.set_text(adv_c[5])
		self.advanced_settings_def_toll_H.set_text(adv_c[6])
		self.advanced_settings_max_riv_time.set_text(adv_c[7])
		self.advanced_settings_mot_off_delay.set_text(adv_c[8])
		self.advanced_settings_auto_pause.set_text(adv_c[9])
		self.advanced_settings_cal_path.set_text(adv_c[10])
		self.advanced_settings_Enc_path.set_text(adv_c[11])

		self.advanced_settings_form_fac.set_text(adv_c[12])
		self.advanced_settings_orb_riv.set_text(adv_c[13])
		self.advanced_settings_delta_T.set_text(adv_c[14])
		self.advanced_settings_delta_F.set_text(adv_c[15])
		self.advanced_settings_min_path_touch.set_text(adv_c[16])
		self.advanced_settings_plus_toll_S.set_text(adv_c[17])
		self.advanced_settings_plus_toll_T.set_text(adv_c[18])
		self.advanced_settings_plus_toll_F.set_text(adv_c[19])
		self.advanced_settings_plus_toll_E.set_text(adv_c[20])
		self.advanced_settings_plus_toll_H.set_text(adv_c[21])
		self.advanced_settings_curve_int.set_text(adv_c[22])

		self.advanced_settings_min_force.set_text(adv_c[23])
		self.advanced_settings_force_zoom.set_text(adv_c[24])
		self.advanced_settings_log_drive.set_text(adv_c[25])
		self.advanced_settings_speed.set_text(adv_c[26])
		self.advanced_settings_func_x14.set_text(adv_c[27])
		self.advanced_settings_auto_com.set_text(adv_c[28])
		self.advanced_settings_error_emg.set_text(adv_c[29])
		self.advanced_settings_mot_off_delay.set_text(adv_c[30])
		self.advanced_settings_PLC_act.set_text(adv_c[31])
		self.advanced_settings_touch_probe.set_text(adv_c[32])
		self.adadvanced_settings_prog_diag.set_text(adv_c[33])

		self.advanced_settings_off_ext_NA.set_text(adv_c[34])
		self.advanced_settings_path_meas_H.set_text(adv_c[35])
		self.advanced_settings_min_path_H.set_text(adv_c[36])
		self.advanced_settings_minus_path.set_text(adv_c[37])
		self.advanced_settings_off_path_toll.set_text(adv_c[38])
		self.advanced_settings_min_path_NA.set_text(adv_c[39])
		self.advanced_settings_time_NA.set_text(adv_c[40])
		self.advanced_settings_cal_press_force.set_text(adv_c[41])
		self.advanced_settings_upp_pis.set_text(adv_c[42])
		self.advanced_settings_low_pis.set_text(adv_c[43])
		self.advanced_settings_man_trigg.set_text(adv_c[44])

		self.advanced_settings_up_data_cycle.set_text(adv_c[45])
		self.advanced_settings_cal_path.set_text(adv_c[46])

		print "Loading settings completed" 


	
	def recall_alarm(self):
		global alarm
		print "Loading Alarm list"
		alarm=alarm_retrieve("settings/alarm")
		alarm.reverse()
		
		for i in range(1,len(alarm)+1):
			if i>=12:
				break
		
			temp=alarm[i-1]
						
			print temp
			eval("self.alarm"+str(i)+"_date.set_text(temp[0])")
			eval("self.alarm"+str(i)+"_time.set_text(temp[1])")
			eval("self.alarm"+str(i)+"_mess.set_text(temp[2])")
			
		
	def recall_log(self):
		global log
		print "Loading Log list"
		log=log_retrieve("settings/log")

		for i in range(1,len(log)+1):
			if i>=12:
				break
		
			temp=log[i-1]
			print temp
			
			eval("self.logger_data_date"+str(i)+".set_text(temp[0])")
			eval("self.logger_data_time"+str(i)+".set_text(temp[1])")
			eval("self.logger_data_mess"+str(i)+".set_text(temp[2])")

	def recall_table(self):
		global table
		print "Loading Table"
		table=table_retrieve("settings/table")
		for i in range(1,len(table)+1):
			if i>=12:
				break
		
			temp=table[i-1]
			print temp

			eval("self.table_sno"+str(i)+".set_text(temp[0])")
			eval("self.table_NA"+str(i)+".set_text(temp[1])")
			eval("self.table_S"+str(i)+".set_text(temp[2])")
			eval("self.table_T"+str(i)+".set_text(temp[3])")
			eval("self.table_F"+str(i)+".set_text(temp[4])")
			eval("self.table_E"+str(i)+".set_text(temp[5])")
			eval("self.table_H"+str(i)+".set_text(temp[6])")
			
	def recall_time(self):
		global time_sett
		print "Loading Time Settings"
		time_sett=load_file("settings/time_sett")
		self.system_riv_time=datetime.strptime(time_sett[7],"%d-%m-%Y %H:%M:%S")
		self.system_op_time=datetime.strptime(time_sett[8],"%d-%m-%Y %H:%M:%S") 
		
		

	def feed_time(self):
		print "feed"
		date=str(datetime.now().date())
		day=date.rpartition('-')[2]
		month=(date.partition('-')[2]).partition('-')[0]
		year=date.partition('-')[0]

		time=str(datetime.now().time()).rpartition('.')[0]
		sec=time.rpartition(':')[2]
		minute=(time.partition(':')[2]).partition(':')[0]
		hour=time.partition(':')[0]

		print "done"

		
		self.Time_settings_day.set_text(day)
		self.Time_settings_month.set_text(month)
		self.Time_settings_year.set_text(year)

		self.Time_settings_hours.set_text(hour)
		self.Time_settings_min.set_text(minute)
		self.Time_settings_sec.set_text(sec)
		
	def time_set(self):
		time_sett=self.recall_time()

	
	
############################################################################
#CLASS SETT_GUI ENDS

	

#Main Loop
###################################################################

		
	

if __name__ == "__main__":
	main = Sett_GUI()
	Gtk.main()

  
