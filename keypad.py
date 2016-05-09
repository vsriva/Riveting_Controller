#!/usr/bin/env python
from gi.repository import Gtk

class Keypad:
  
  numst=""
  keypad_final=""
  shift_flag=0
  caps_flag=0
  def __init__(self):
    self.gladefile = "dialog.glade"
    self.builder = Gtk.Builder()
    self.builder.add_from_file(self.gladefile)
    self.builder.connect_signals(self)
    self.keypad = self.builder.get_object("keypad")
    self.result1 = self.builder.get_object("keypad_disp")
    self.keypad.show()
    
  def on_keypad_destroy(self, object, data=None):
    print "quit with cancel"
    Gtk.main_quit()

  def on_key_1_clicked(self, button, data=None):
   self.numst = self.numst + '1'
   self.result1.set_text(self.numst)

  def on_key_2_clicked(self, button, data=None):
   self.numst = self.numst + '2'
   self.result1.set_text(self.numst)
   
  def on_key_3_clicked(self, button, data=None):
   self.numst = self.numst + '3'
   self.result1.set_text(self.numst)
   
  def on_key_4_clicked(self, button, data=None):
   self.numst = self.numst + '4'
   self.result1.set_text(self.numst)
   
  def on_key_5_clicked(self, button, data=None):
   self.numst = self.numst + '5'
   self.result1.set_text(self.numst)
   
  def on_key_6_clicked(self, button, data=None):
   self.numst = self.numst + '6'
   self.result1.set_text(self.numst)
   
  def on_key_7_clicked(self, button, data=None):
   self.numst = self.numst + '7'
   self.result1.set_text(self.numst)
   
  def on_key_8_clicked(self, button, data=None):
   self.numst = self.numst + '8'
   self.result1.set_text(self.numst)
   
  def on_key_9_clicked(self, button, data=None):
   self.numst = self.numst + '9'
   self.result1.set_text(self.numst)

  def on_key_0_clicked(self, button, data=None):
   self.numst = self.numst + '0'
   self.result1.set_text(self.numst)
   
   
  def on_key_q_clicked(self, button, data=None):

   if ((self.shift_flag == 1)|(self.caps_flag == 1)):
     self.numst = self.numst + 'Q'
     self.shift_flag=0
   else:
     self.numst = self.numst + 'q'  

   self.result1.set_text(self.numst)

  def on_key_w_clicked(self, button, data=None):

   if ((self.shift_flag == 1)|(self.caps_flag == 1)):
     self.numst = self.numst + 'W'
     self.shift_flag=0
   else:
     self.numst = self.numst + 'w'  

   self.result1.set_text(self.numst)

  def on_key_e_clicked(self, button, data=None):

   if ((self.shift_flag == 1)|(self.caps_flag == 1)):
     self.numst = self.numst + 'E'
     self.shift_flag=0
   else:
     self.numst = self.numst + 'e'  

   self.result1.set_text(self.numst)

  def on_key_r_clicked(self, button, data=None):

   if ((self.shift_flag == 1)|(self.caps_flag == 1)):
     self.numst = self.numst + 'R'
     self.shift_flag=0
   else:
     self.numst = self.numst + 'r'  

   self.result1.set_text(self.numst)

  def on_key_t_clicked(self, button, data=None):

   if ((self.shift_flag == 1)|(self.caps_flag == 1)):
     self.numst = self.numst + 'T'
     self.shift_flag=0
   else:
     self.numst = self.numst + 't'  

   self.result1.set_text(self.numst)

  def on_key_y_clicked(self, button, data=None):

   if ((self.shift_flag == 1)|(self.caps_flag == 1)):
     self.numst = self.numst + 'Y'
     self.shift_flag=0
   else:
     self.numst = self.numst + 'y'  

   self.result1.set_text(self.numst)

  def on_key_u_clicked(self, button, data=None):

   if ((self.shift_flag == 1)|(self.caps_flag == 1)):
     self.numst = self.numst + 'U'
     self.shift_flag=0
   else:
     self.numst = self.numst + 'u'  

   self.result1.set_text(self.numst)

  def on_key_i_clicked(self, button, data=None):

   if ((self.shift_flag == 1)|(self.caps_flag == 1)):
     self.numst = self.numst + 'I'
     self.shift_flag=0
   else:
     self.numst = self.numst + 'i'  

   self.result1.set_text(self.numst)

  def on_key_o_clicked(self, button, data=None):

   if ((self.shift_flag == 1)|(self.caps_flag == 1)):
     self.numst = self.numst + 'O'
     self.shift_flag=0
   else:
     self.numst = self.numst + 'o'  

   self.result1.set_text(self.numst)

  def on_key_p_clicked(self, button, data=None):

   if ((self.shift_flag == 1)|(self.caps_flag == 1)):
     self.numst = self.numst + 'P'
     self.shift_flag=0
   else:
     self.numst = self.numst + 'p'  

   self.result1.set_text(self.numst)

  def on_key_a_clicked(self, button, data=None):

   if ((self.shift_flag == 1)|(self.caps_flag == 1)):
     self.numst = self.numst + 'A'
     self.shift_flag=0
   else:
     self.numst = self.numst + 'a'  

   self.result1.set_text(self.numst)

  def on_key_s_clicked(self, button, data=None):

   if ((self.shift_flag == 1)|(self.caps_flag == 1)):
     self.numst = self.numst + 'S'
     self.shift_flag=0
   else:
     self.numst = self.numst + 's'  

   self.result1.set_text(self.numst)

  def on_key_d_clicked(self, button, data=None):

   if ((self.shift_flag == 1)|(self.caps_flag == 1)):
     self.numst = self.numst + 'D'
     self.shift_flag=0
   else:
     self.numst = self.numst + 'd'  

   self.result1.set_text(self.numst)

  def on_key_f_clicked(self, button, data=None):

   if ((self.shift_flag == 1)|(self.caps_flag == 1)):
     self.numst = self.numst + 'F'
     self.shift_flag=0
   else:
     self.numst = self.numst + 'f'  

   self.result1.set_text(self.numst)

  def on_key_g_clicked(self, button, data=None):

   if ((self.shift_flag == 1)|(self.caps_flag == 1)):
     self.numst = self.numst + 'G'
     self.shift_flag=0
   else:
     self.numst = self.numst + 'g'  

   self.result1.set_text(self.numst)

  def on_key_h_clicked(self, button, data=None):

   if ((self.shift_flag == 1)|(self.caps_flag == 1)):
     self.numst = self.numst + 'H'
     self.shift_flag=0
   else:
     self.numst = self.numst + 'h'  

   self.result1.set_text(self.numst)

  def on_key_j_clicked(self, button, data=None):

   if ((self.shift_flag == 1)|(self.caps_flag == 1)):
     self.numst = self.numst + 'J'
     self.shift_flag=0
   else:
     self.numst = self.numst + 'j'  

   self.result1.set_text(self.numst)

  def on_key_k_clicked(self, button, data=None):

   if ((self.shift_flag == 1)|(self.caps_flag == 1)):
     self.numst = self.numst + 'K'
     self.shift_flag=0
   else:
     self.numst = self.numst + 'k'  

   self.result1.set_text(self.numst)

  def on_key_l_clicked(self, button, data=None):

   if ((self.shift_flag == 1)|(self.caps_flag == 1)):
     self.numst = self.numst + 'L'
     self.shift_flag=0
   else:
     self.numst = self.numst + 'l'  

   self.result1.set_text(self.numst)


  def on_key_z_clicked(self, button, data=None):

   if ((self.shift_flag == 1)|(self.caps_flag == 1)):
     self.numst = self.numst + 'Z'
     self.shift_flag=0
   else:
     self.numst = self.numst + 'z'  

   self.result1.set_text(self.numst)

  def on_key_x_clicked(self, button, data=None):

   if ((self.shift_flag == 1)|(self.caps_flag == 1)):
     self.numst = self.numst + 'X'
     self.shift_flag=0
   else:
     self.numst = self.numst + 'x'  

   self.result1.set_text(self.numst)

  def on_key_c_clicked(self, button, data=None):

   if ((self.shift_flag == 1)|(self.caps_flag == 1)):
     self.numst = self.numst + 'C'
     self.shift_flag=0
   else:
     self.numst = self.numst + 'c'  

   self.result1.set_text(self.numst)

  def on_key_v_clicked(self, button, data=None):

   if ((self.shift_flag == 1)|(self.caps_flag == 1)):
     self.numst = self.numst + 'V'
     self.shift_flag=0
   else:
     self.numst = self.numst + 'v'  

   self.result1.set_text(self.numst)

  def on_key_b_clicked(self, button, data=None):

   if ((self.shift_flag == 1)|(self.caps_flag == 1)):
     self.numst = self.numst + 'B'
     self.shift_flag=0
   else:
     self.numst = self.numst + 'b'  

   self.result1.set_text(self.numst)

  def on_key_n_clicked(self, button, data=None):

   if ((self.shift_flag == 1)|(self.caps_flag == 1)):
     self.numst = self.numst + 'N'
     self.shift_flag=0
   else:
     self.numst = self.numst + 'n'  

   self.result1.set_text(self.numst)

  def on_key_m_clicked(self, button, data=None):

   if ((self.shift_flag == 1)|(self.caps_flag == 1)):
     self.numst = self.numst + 'M'
     self.shift_flag=0
   else:
     self.numst = self.numst + 'm'  

   self.result1.set_text(self.numst)


  def on_key_space_clicked(self, button, data=None):
   self.numst = self.numst + ' '
   print self.numst
   self.result1.set_text(self.numst)

  def on_key_under_clicked(self, button, data=None):
    self.numst = self.numst + '_'
    self.result1.set_text(self.numst)  

  def on_key_col_clicked(self, button, data=None):
    self.numst = self.numst + ':'
    self.result1.set_text(self.numst)
  

  def on_key_comma_clicked(self, button, data=None):
   self.numst = self.numst + ','
   self.result1.set_text(self.numst)
   

  def on_key_back_arrow_clicked(self, button, data=None):
   self.numst = self.numst + ''
   self.result1.set_text(self.numst)
   

  def on_key_forward_arrow_clicked(self, button, data=None):
   self.numst = self.numst + ''
   self.result1.set_text(self.numst)
   

  def on_key_alt_clicked(self, button, data=None):
   self.numst = self.numst + ''
   self.result1.set_text(self.numst)
   

  def on_key_at_rate_clicked(self, button, data=None):
   self.numst = self.numst + '@'
   self.result1.set_text(self.numst)
  
 

  def on_key_dot_clicked(self, button, data=None):
   self.numst = self.numst + '.'
   self.result1.set_text(self.numst)
   

  def on_key_back_clicked(self, button, data=None):
   self.numst = self.numst[:-1]
   self.result1.set_text(self.numst)
   
  def on_key_caps_toggled(self, button, data=None):
   self.caps_flag ^= 1
   
  def on_key_shift_pressed(self, button, data=None):
   self.shift_flag ^= 1
   

  def on_key_go_clicked(self, button, data=None):
   self.result1.set_text(self.numst)
   self.keypad_final = self.numst
   self.numst=""
   self.result1.set_text(self.numst)
   print self.keypad_final
   self.keypad.hide()
   self.curr_mode1.set_text(self.keypad_final)
   self.curr_mode2.set_text(self.keypad_final)
   self.curr_mode3.set_text(self.keypad_final)

   self.curr_window.show()  ##derived class variable
   

if __name__ == "__main__":
  main = Keypad()
  Gtk.main()
  
