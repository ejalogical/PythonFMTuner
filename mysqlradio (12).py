







import mysql.connector as mysql
from tkinter import *
import operator
import serial
import tkinter as tk


Window = tk.Tk()
Window.title('')
Window.geometry('500x300')
Window.configure(bg='cyan')
frequency = 87.9
r=0.0

db = mysql.Connect(host="localhost",user ="root",password ="",database="Radio")

command_handler = db.cursor()

def clear_text(self):
        self.entry.delete(0, 'end')
def storevalue():
   # Update a record
        
           

    
    # Commit changes
           db.commit()






def slider_Values(v):
   freqarray = list (range(109))
  
   frequency = 87.9
   freqcounter = 0
   while freqcounter < 101:

      freqarray = operator.add(frequency, .2)
      frequency = operator.add(frequency, .2)
      
      freqcounter = operator.add(freqcounter, 1)
      if freqcounter == int(v):         
      #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
          j.delete(0, END)

          j.insert(0,"%.1f" % frequency)

          sql = 'SELECT *  FROM stations WHERE Frequency ='"%.1f" % frequency
          command_handler.execute(sql)
          row = command_handler.fetchall()
          print(row)
                                                                                                                                             
                


          sqlA ='SELECT CallLetters FROM stations WHERE Frequency ='"%.1f" % frequency                                                                                                                                                                             
          command_handler.execute(sqlA)
          row = command_handler.fetchone()
          e.delete(0, END)
          e.insert(0,row)

          sqlA ='SELECT url FROM stations WHERE Frequency ='"%.1f" % frequency                                                                                                                                                                             
          command_handler.execute(sqlA)
          row = command_handler.fetchone()
          u.delete(0, END)
          u.insert(0,row)


          sqlA ='SELECT ContestName FROM stations WHERE Frequency ='"%.1f" % frequency                                                                                                                                                                             
          command_handler.execute(sqlA)
          row = command_handler.fetchone()
          c.delete(0, END)
          c.insert(0,row)



           
         
         
         
       #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
          Window.title(str(round(freqarray, 1))+ " FM")
          serialcom = serial.Serial('COM3', 9600)
          serialcom.write(bytes([int(v)]))
    
    
  
            
           
           

           


       

s = tk.Scale(Window, label='      Python FM Radio Tuner', from_=0, to=100, orient=tk.HORIZONTAL, length=200, showvalue=0, tickinterval=10, resolution=1, command=slider_Values)
s.pack()

selected = tk.StringVar()

Label(Window, text="Enter Frequency").pack()

   




j = Entry(Window,width =5)
j.pack()

j.focus_set()

Label(Window, text="Enter Call Letters").pack()



e = Entry(Window)
e.pack()

e.focus_set()
Label(Window, text="Enter URL").pack()
u = Entry(Window)
u.pack()

u.focus_set()
Label(Window, text="Enter contest name").pack()

c = Entry(Window)
c.pack()

c.focus_set()

def callback():
  # print (e.get()) # This is the text you may want to use latersql_bulk_update = "UPDATE table_name SET field1=%s, field2=%s, ..., field10=%s WHERE id=%s"
  print (e.get())
  print (j.get())
  print (u.get())
  print (c.get())
  
  sql = "UPDATE `stations` SET ContestName= %s, url= %s ,CallLetters=%s WHERE `Frequency`=%s"



  command_handler.execute(sql, (c.get(),u.get(),e.get(),float(j.get())))



  #command_handler.execute(sql, (e.get(),r))
  
    

b = Button(Window, text = "OK", width = 10, command = callback)
b.pack()







var = IntVar()
var.set(1)

btn = Button(Window, text = 'Save', bd = '5', command = storevalue)
                           
 
# Set the position of button on the top of window.   
btn.pack(side = 'bottom')


label = Label(Window)
label.pack()

mainloop()