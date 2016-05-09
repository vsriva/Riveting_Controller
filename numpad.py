#!/usr/bin/env python

from gi.repository import Gtk

class Numpad:
  
  numpad_final=""
  def __init__(self):
    self.gladefile = "dialog.glade"
    self.builder = Gtk.Builder()
    self.builder.add_from_file(self.gladefile)
    self.builder.connect_signals(self)
    self.numpad = self.builder.get_object("numpad")
    self.result2 = self.builder.get_object("num_disp")
    self.numpad.show()
    
  def on_numpad_destroy(self, object, data=None):
    print "quit with cancel"
    Gtk.main_quit()

  def on_num1_clicked(self, button, data=None):
   self.numst = self.numst + '1'
   self.result2.set_text(self.numst)

  def on_num2_clicked(self, button, data=None):
   self.numst = self.numst + '2'
   self.result2.set_text(self.numst)
   
  def on_num3_clicked(self, button, data=None):
   self.numst = self.numst + '3'
   self.result2.set_text(self.numst)
   
  def on_num4_clicked(self, button, data=None):
   self.numst = self.numst + '4'
   self.result2.set_text(self.numst)
   
  def on_num5_clicked(self, button, data=None):
   self.numst = self.numst + '5'
   self.result2.set_text(self.numst)
   
  def on_num6_clicked(self, button, data=None):
   self.numst = self.numst + '6'
   self.result2.set_text(self.numst)
   
  def on_num7_clicked(self, button, data=None):
   self.numst = self.numst + '7'
   self.result2.set_text(self.numst)
   
  def on_num8_clicked(self, button, data=None):
   self.numst = self.numst + '8'
   self.result2.set_text(self.numst)
   
  def on_num9_clicked(self, button, data=None):
   self.numst = self.numst + '9'
   self.result2.set_text(self.numst)
   
  def on_num0_clicked(self, button, data=None):
   self.numst = self.numst + '0'
   self.result2.set_text(self.numst)

  def on_num_dec_clicked(self, button, data=None):
   self.numst = self.numst + '.'
   self.result2.set_text(self.numst)
   
  def on_num_all_clear_clicked(self, button, data=None):
   self.numst = ""
   self.result2.set_text(self.numst)
   
  def on_num_back_clicked(self, button, data=None):
   self.numst = self.numst[:-1]
   self.result2.set_text(self.numst)
   
  def on_num_ok_clicked(self, button, data=None):
   self.result2.set_text(self.numst)
   self.numpad_final = self.numst
   self.numst=""
   self.result2.set_text(self.numst)
   self.numpad.hide()
   self.curr_entry.set_text(self.numpad_final)
   self.curr_window.show()

if __name__ == "__main__":
  main = Numpad()
  Gtk.main()

  
