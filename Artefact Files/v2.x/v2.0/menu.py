import tkinter as tk

#Having a separate list for the raw values reduces the amount of rewriting I have to do for the main code
global inputs
inputs = []

#This list makes the generation of input boxes much easier, as it can be looped instead of written explicitly
values = [
    'Mass', 
    'Initial velocity', 
    'Initial height', 
    'Angle of projection', 
    'Cross-sectional area', 
    'Drag coefficient', 
    'Acceleration due to gravity', 
    'Fluid density'
    ]

#This dictionary allows each entry to be assigned a keyword, which makes the submit() process easier
entries = {}


#These are the functions activated when pressing each button
def submit():
    for i in values:
        inputs.append(float(entries[i].get()))
    menu.destroy()
    import main

def clear():
    for i in values:
        entries[i].delete(0, tk.END)

#This makes the initial window
menu = tk.Tk()
menu.title('Parameter input')
menu.minsize(285,220)
menu.maxsize(285,220)

#This makes the section containing all of the inputs
frm_inputs = tk.Frame(master = menu)
for i in range(8):
    frm_inputs.rowconfigure(i, weight = 1)
frm_inputs.pack()

#This iterates through each necessary value, and creates a section for each specific value
for i in range(8):
    frm_input = tk.Frame(master = frm_inputs, relief = tk.RAISED, borderwidth = 1)
    for j in range(2):
        frm_input.columnconfigure(j, weight = 1)
    frm_input.grid(row = i, column = 0)

    lbl_input = tk.Label(master = frm_input, text = values[i], width = 30, anchor = 'w')
    lbl_input.grid(row = 0, column = 0)
    
    ent_input = tk.Entry(master = frm_input, width = 10)
    ent_input.grid(row = 0, column = 1)

    entries[values[i]] = ent_input

#This makes the section with the buttons
frm_buttons = tk.Frame(master = menu)
frm_buttons.pack(side = tk.RIGHT)

#This adds each button to the frame
btn_submit = tk.Button(master = frm_buttons, text = 'Submit', command = submit, width = 7)
btn_submit.pack(side = tk.RIGHT, padx = 5, pady = 5)

btn_clear = tk.Button(master = frm_buttons, text = 'Clear', command = clear, width = 7)
btn_clear.pack(side = tk.RIGHT, padx = 5, pady = 5)

menu.mainloop()