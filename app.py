import tkinter as tk
from tkinter import filedialog, Text
import main as main

def raise_frame(frame):
    frame.tkraise()

root=tk.Tk() 
root.title("Better Bolus V2.0")
root.iconbitmap("./favicon.ico")

f1 = tk.Frame(root)
f2 = tk.Frame(root)
f3 = tk.Frame(root)
f4 = tk.Frame(root)

for frame in (f1, f2, f3, f4):
    frame.grid(row=0, column=0, sticky='news')
  
# setting the windows size  
root.geometry("600x400") 
   
# declaring string variables 
bg_var = tk.StringVar() 
trending_var = tk.StringVar()
bolus_var = tk.StringVar() 
bolusTime_var = tk.StringVar()

   
# defining a function that will 
# get and store data
def submit_f1(): 
  
    bg = int(bg_var.get()) 
    trending = trending_var.get()
      
    print(f"bg is : {bg}") 
    print("trending: " + trending) 
      
    bg_var.set("") 
    trending_var.set("")   

    main.initial_bg(bg)
    main.unadjusted_graph(trending)
    main.show_unadjusted_graph()

      
# creating a label for  
# bg using widget Label 
bg_label = tk.Label(f1, text = 'Blood Glucose', 
                      font=('calibre', 
                            10, 'bold')) 
   
# creating a entry for input 
# bg using widget Entry 
bg_entry = tk.Entry(f1, 
                      textvariable = bg_var,
                      font=('calibre',10,'normal')) 

choices = { 'Stable','Rising','Dropping','Rising Fast','Dropping Fast', 'Unknown'}
trending_var.set('Unknown') # set the default option

trending_profile = tk.OptionMenu(f1, trending_var, *choices,)
trending_label = tk.Label(f1, text="Choose a Trending Option")
trending_profile.grid(row = 2, column =1)

# on change dropdown value
def change_dropdown(*args):
    print( trending_var.get() )

# link function to change dropdown
trending_var.trace('w', change_dropdown)

# # creating a label for trending 
# trending_label = tk.Label(root, 
#                        text = 'Trending', 
#                        font = ('calibre',10,'bold')) 
   
# # creating a entry for trending 
# trending_entry=tk.Entry(root, 
#                      textvariable = trending_var, 
#                      font = ('calibre',10,'normal')) 
   
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
sub_btn=tk.Button(f1,text = 'Submit', 
                  command = submit_f1) 
   
# placing the label and entry in 
# the required position using grid 
# method 
bg_label.grid(row=0,column=0) 
bg_entry.grid(row=0,column=1) 
trending_label.grid(row=1,column=0)
trending_profile.grid(row=1,column=1)
# bolus_label.grid(row=1,column=0) 
# bolus_entry.grid(row=1,column=1) 
# bolusTime_label.grid(row=2,column=0)
# bolusTime_entry.grid(row=2,column=1)
sub_btn.grid(row=2,column=1) 
   
# performing an infinite loop  
# for the window to display 
# root.mainloop() 

# bg_label.grid(row=0,column=0) 
# bg_entry.grid(row=0,column=1) 
# bolus_label.grid(row=1,column=0) 
# bolus_entry.grid(row=1,column=1)

raise_frame(f1)
root.mainloop()