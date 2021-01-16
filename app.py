import tkinter as tk
from tkinter import filedialog, Text
import main as main
from sortedcontainers import SortedSet

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

# bolus profile values as an object of arrays, each with two values, 
# the first being the amount of insulin in units, 
# and the second being the amount of time in minutes between 
# now and when the bolus would be taken
bolusProfile = {}

insulinEffectUpdated = []
if len(insulinEffectUpdated) > 49:
    insulinEffectUpdated = insulinEffectUpdated[48:]
# declaring string variables 
bg_var = tk.StringVar() 
trending_var = tk.StringVar()
bolus_var = tk.StringVar() 
bolusTime_var = tk.StringVar()

   
# defining a function that will 
# generate original graph
def submit_f1(): 
  
    bg = int(bg_var.get()) 
    trending = trending_var.get()
      
    print(f"bg is : {bg}") 
    print("trending: " + trending) 
      
    bg_var.set("") 

    main.initial_bg(bg)
    main.unadjusted_graph(trending)
    main.show_unadjusted_graph()

# defining a function that will 
# generate graph with bolus profile applied
def submit_f2(): 
  
    bolus = int(bolus_var.get()) 
    trending = trending_var.get()
    time = bolusTime_var.get()
    print("time1:", time)
    if bolusTime_var.get() == "":
        time = '0.00'
        print("time2:", time)

    print(f"bolus is : {bolus}") 
    print("trending: " + trending) 

    bolusProfile.update({time: bolus})
    print(bolusProfile)

    bolus_var.set("") 
    trending_var.set("")

    insulinEffect = main.applyInitialBolus(bolusProfile)
    insulinEffectResistanceAdjusted = main.build_resistance_profile(trending, insulinEffect)
    main.show_adjusted_graph(insulinEffectResistanceAdjusted)

# defining a function that will 
# allow user to add more bolus info
def add_another_bolus(): 
  
    bolus = int(bolus_var.get()) 
    time = bolusTime_var.get()
    print("time1:", time)
    if bolusTime_var.get() == "":
        time = '0.00'
        print("time2:", time)

    print(f"bolus is : {bolus}") 
    print(f"time: {time}") 

    bolusProfile.update({time: bolus})

    bolus_var.set("") 
    bolusTime_var.set("")

    insulinEffect = main.applyInitialBolus(bolusProfile)
    insulinEffectUpdated.append(main.bolusStack(insulinEffect, bolusProfile))

def add_another_bolus2(): 
  
    bolus = int(bolus_var.get()) 
    time = bolusTime_var.get()
    print("time1:", time)
    if bolusTime_var.get() == "":
        time = '0.00'
        print("time2:", time)

    print(f"bolus is : {bolus}") 
    print(f"time: {time}") 

    bolusProfile.update({time: bolus})

    bolus_var.set("") 
    bolusTime_var.set("")
    print(insulinEffectUpdated[0])
    insulinEffectUpdated.append(main.bolusStack(insulinEffectUpdated[len(insulinEffectUpdated) - 1], bolusProfile))

def submit_f3(): 
  
    bolus = int(bolus_var.get()) 
    trending = trending_var.get()
    time = bolusTime_var.get()
    print("time1:", time)
    if bolusTime_var.get() == "":
        time = '0.00'
        print("time2:", time)

    print(f"bolus is : {bolus}") 
    print("trending: " + trending) 
    print(f"time: {time}")

    bolusProfile.update({time: bolus})
    print(bolusProfile)

    bolus_var.set("") 
    trending_var.set("")
    bolusTime_var.set("")

    insulinEffectUpdated.append(main.bolusStack(insulinEffectUpdated[len(insulinEffectUpdated) - 1], bolusProfile))
    insulinEffectResistanceAdjusted = main.build_resistance_profile(trending, insulinEffectUpdated[len(insulinEffectUpdated) - 1])
    # print(insulinEffectResistanceAdjusted)
    main.show_adjusted_graph(insulinEffectResistanceAdjusted)
# creating a label for  
# disclaimer 
disclaimer_label = tk.Label(f1, text = "THIS PROGRAM IS CURRENTLY FOR MODELING PURPOSES ONLY\nAND SHOULD NOT BE USED TO DETERMINE\nHOW TO MANAGE AN INDIVIDUAL'S BLOOD GLUCOSE.", 
                      font=('calibre', 
                            10, 'bold')) 

# creating a label for  
# disclaimer cont'd
disclaimer_label_cont = tk.Label(f1, text = "", 
                      font=('calibre', 
                            10, 'bold')) 

# creating a label for  
# disclaimer cont'd 2
disclaimer_label_cont2 = tk.Label(f1, text = "", 
                      font=('calibre', 
                            10, 'bold')) 
   
# creating a label for  
# bg using widget Label 
bg_label = tk.Label(f1, text = 'Blood Glucose', 
                      font=('calibre', 
                            10, 'bold')) 
   
# creating an entry for input 
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

# creating a button using the widget  
# Button that will call the submit function  
sub_btn=tk.Button(f1,text = 'Submit', 
                  command = lambda:[raise_frame(f2), submit_f1()]
                  )

# creating a label for f2 
f2_label = tk.Label(f2, text = "Please enter an initial bolus value", 
                      font=('calibre', 
                            10, 'bold'))  
   
# creating a label for bolus 
bolus_label = tk.Label(f2, 
                       text = 'Bolus Amount', 
                       font = ('calibre',10,'bold')) 
   
# creating an entry for bolus 
bolus_entry=tk.Entry(f2, 
                     textvariable = bolus_var, 
                     font = ('calibre',10,'normal')) 

# creating a button using the widget  
# Button that will call the submit function for f2  
sub2_btn=tk.Button(f2,text = 'Apply', 
                  command = submit_f2) 

# creating a button using the widget  
# Button that will call the submit function for f2
add_bolus_btn=tk.Button(f2,text = 'Add another bolus', 
                  command = lambda:[raise_frame(f3), add_another_bolus()]
                    )
# creating a label for f3
f3_label = tk.Label(f3, text = "Please enter another bolus value with a time to be applied", 
                      font=('calibre', 
                            10, 'bold'))  

# creating a label for f3
bolusprofile_label = tk.Label(f3, text = f"{bolusProfile}", 
                      font=('calibre', 
                            10, 'bold'))  

# creating a label for subsequent bolus 
bolus_label2 = tk.Label(f3, 
                       text = 'Bolus Amount', 
                       font = ('calibre',10,'bold')) 
   
# creating an entry for subsequent bolus 
bolus_entry2=tk.Entry(f3, 
                     textvariable = bolus_var, 
                     font = ('calibre',10,'normal')) 

times = SortedSet()

for el in main.insulinProfileList:
    times.add(el[0])
print(times)

bolus_time = tk.OptionMenu(f3, bolusTime_var, *times,)
time_label = tk.Label(f3, text="Choose a time to apply bolus\nin 5 minute increments from now")
bolus_time.grid(row = 2, column =1)

# on change dropdown value
def change_time_dropdown(*args):
    print( "time", bolusTime_var.get() )

# link function to change dropdown
bolusTime_var.trace('w', change_time_dropdown)
   
# creating a button using the widget  
# Button that will call the submit function for f2  
sub3_btn=tk.Button(f3,text = 'Apply', 
                  command = submit_f3)

# creating a button using the widget  
# Button that will call the submit function for f3
add_bolus_btn2=tk.Button(f3,text = 'Add another bolus', 
                  command = lambda:[raise_frame(f3), add_another_bolus2()] 
)

# placing the label and entry in 
# the required position using grid for f1
disclaimer_label.grid(row=0,column=0,columnspan=2)
bg_label.grid(row=1,column=0) 
bg_entry.grid(row=1,column=1) 
trending_label.grid(row=2,column=0)
trending_profile.grid(row=2,column=1)
sub_btn.grid(row=3,column=1) 

# placing the label and entry in 
# the required position using grid for f2
f2_label.grid(row=0,column=0,columnspan=2)
bolus_label.grid(row=1,column=0) 
bolus_entry.grid(row=1,column=1) 
sub2_btn.grid(row=3,column=1) 
add_bolus_btn.grid(row=3,column=2)

# placing the label and entry in 
# the required position using grid for f3
f3_label.grid(row=0,column=0,columnspan=2)
bolusprofile_label.grid(row=1,column=0,columnspan=2)
bolus_label2.grid(row=2,column=0) 
bolus_entry2.grid(row=2,column=1) 
time_label.grid(row=3,column=0)
bolus_time.grid(row=3,column=1)
sub3_btn.grid(row=4,column=1) 
add_bolus_btn2.grid(row=4,column=2)

# performing an infinite loop  
# for the window to display 
raise_frame(f1)
root.mainloop()