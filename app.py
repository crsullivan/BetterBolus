import tkinter as tk
from tkinter import filedialog, Text

root=tk.Tk() 
root.title("Better Bolus V2.0")
root.iconbitmap("./favicon.ico")
  
# setting the windows size  
root.geometry("600x400") 
   
# declaring string variable 
# for storing name and password 
bg_var=tk.StringVar() 
bolus_var=tk.StringVar() 
bolusTime_var=tk.StringVar()
   
# defining a function that will 
# get the name and password and  
# print them on the screen 
def submit(): 
  
    bg=bg_var.get() 
    bolus=bolus_var.get() 
    bolusTime=bolusTime_var.get()
      
    print("bg is : " + bg) 
    print("bolus amount is : " + bolus) 
    print("bolus time is : " + bolusTime) 
      
    bg_var.set("") 
    bolus_var.set("") 
    bolusTime_var.set("")
      
      
# creating a label for  
# bg using widget Label 
bg_label = tk.Label(root, text = 'Blood Glucose', 
                      font=('calibre', 
                            10, 'bold')) 
   
# creating a entry for input 
# bg using widget Entry 
bg_entry = tk.Entry(root, 
                      textvariable = bg_var,
                      font=('calibre',10,'normal')) 
   
# creating a label for bolus 
bolus_label = tk.Label(root, 
                       text = 'Bolus Amount', 
                       font = ('calibre',10,'bold')) 
   
# creating a entry for bolus 
bolus_entry=tk.Entry(root, 
                     textvariable = bolus_var, 
                     font = ('calibre',10,'normal')) 

# creating a label for bolus time
bolusTime_label = tk.Label(root, 
                       text = 'Bolus Time', 
                       font = ('calibre',10,'bold')) 
   
# creating a entry for bolus time
bolusTime_entry=tk.Entry(root, 
                     textvariable = bolusTime_var, 
                     font = ('calibre',10,'normal')) 
   
# creating a button using the widget  
# Button that will call the submit function  
sub_btn=tk.Button(root,text = 'Submit', 
                  command = submit) 
   
# placing the label and entry in 
# the required position using grid 
# method 
bg_label.grid(row=0,column=0) 
bg_entry.grid(row=0,column=1) 
bolus_label.grid(row=1,column=0) 
bolus_entry.grid(row=1,column=1) 
bolusTime_label.grid(row=2,column=0)
bolusTime_entry.grid(row=2,column=1)
sub_btn.grid(row=3,column=1) 
   
# performing an infinite loop  
# for the window to display 
root.mainloop() 