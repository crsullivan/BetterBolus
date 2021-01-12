from tkinter import *


def raise_frame(frame):
    frame.tkraise()

root = Tk()
root.geometry("400x200") 

f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)
f4 = Frame(root)

for frame in (f1, f2, f3, f4):
    frame.grid(row=0, column=0, sticky='news')

Label(f1, text='Please enter a Blood Glucose value between 120-499.').pack()
Button(f1, text='Go to frame 2', command=lambda:raise_frame(f2)).pack()

# Create a Tkinter variable
tkvar = StringVar(root)

choices = { 'Unknown','Stable','Dropping','Rising','Dropping Fast','Rising Fast'}
tkvar.set('Unknown') # set the default option

popupMenu = OptionMenu(f1, tkvar, *choices)
Label(f1, text="Select a Trending Option").pack()
popupMenu.pack()

# on change dropdown value
def change_dropdown(*args):
    print( tkvar.get() )

# link function to change dropdown
tkvar.trace('w', change_dropdown)

Label(f2, text='FRAME 2').pack()
Button(f2, text='Go to frame 3', command=lambda:raise_frame(f3)).pack()

Label(f3, text='FRAME 3').pack()
Button(f3, text='Go to frame 4', command=lambda:raise_frame(f4)).pack()

Label(f4, text='FRAME 4').pack()
Button(f4, text='Goto to frame 1', command=lambda:raise_frame(f1)).pack()

raise_frame(f1)
root.mainloop()