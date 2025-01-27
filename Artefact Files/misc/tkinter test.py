import tkinter as tk

global inputs
inputs = []
def submit():
    inputs.append(ent_name.get())
    inputs.append(str(ent_age.get()))
    print (inputs)
    menu.destroy()

#This initialises and sets up the styling for the window
menu = tk.Tk()
menu.title('Information')
menu.minsize(270, 100)
menu.maxsize(270, 100)


#This creates a section for the inputs
frm_info = tk.Frame(master = menu)
for i in range(2):
    frm_info.columnconfigure(i, weight = 1)
for i in range(1):
    frm_info.rowconfigure(i, weight = 1)
frm_info.pack()

#This handles the name entry portion of the input
frm_name = tk.Frame(master = frm_info, relief = tk.RAISED, borderwidth = 1)
frm_name.grid(row = 0, column = 0, padx = 5, pady = 5)

lbl_name = tk.Label(master = frm_name, text = 'Please input your name')
ent_name = tk.Entry(master = frm_name,fg = 'red')

lbl_name.pack()
ent_name.pack()

#This handles the age entry
frm_age = tk.Frame(master = frm_info, relief = tk.RAISED, borderwidth = 1)
frm_age.grid(row = 0, column = 1, padx = 5, pady = 5)

lbl_age = tk.Label(master = frm_age, text = 'Please input your age')
ent_age = tk.Entry(master = frm_age, fg = 'red')

lbl_age.pack()
ent_age.pack()

#This creates the 'submit' button

frm_submit = tk.Frame(master = menu)
frm_submit.pack(fill = tk.X)

btn_submit = tk.Button(master = frm_submit, text = 'Submit', command = submit)
btn_submit.pack(side = tk.RIGHT, padx = 5, pady = 5)

menu.mainloop()