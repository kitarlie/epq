import tkinter as tk

#Having a separate list for the raw values reduces the amount of rewriting I have to do for the main code
global inputs
inputs = []

#These variables keeps track of which preset is currently shown
global currentprojectile
currentprojectile = 0

global currentplanet
currentplanet = 0

#This list makes the generation of input boxes much easier, as it can be looped instead of written explicitly
values = [
    'Mass', 
    'Initial velocity', 
    'Initial height', 
    'Angle of projection', 
    'Cross-sectional area', 
    'Drag coefficient', 
    'Acceleration due to gravity', 
    'Fluid density',
    ]

#The following lists contain the preset values
projectilepresets = [
    ['Custom','','','','','','','-','-'],
    ['Football', '0.45', '-', '-', '-', '0.38', '0.5', '-', '-'],
    ['Basketball', '0.6', '-', '-', '-', '0.44', '0.5', '-', '-'],
    ['Golf ball', '0.046', '', '-', '-', '0.0014', '0.5', '-', '-'],
]

planetpresets = [
    ['Custom','-','','','','-','-','',''],
    ['Earth','-','-','-','-','-','-','9.81','1.225'],
    ['Venus','-','-','-','-','-','-','8.87','65'],
    ['Mars','-','-','-','-','-','-','3.71','0.020'],
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

def prevprojectile():
    pass

def nextprojectile():
    pass

#This makes the initial window
menu = tk.Tk()
menu.title('Parameter input')
#menu.minsize(285,220)
#menu.maxsize(285,220)

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

#This makes the section with the presets
frm_presets = tk.Frame(master = menu)
for i in range(2):
    frm_presets.rowconfigure(i)
frm_presets.pack()

#This creates the section for the projectile presets
frm_projectilepresets = tk.Frame(master = frm_presets)
frm_projectilepresets.grid(row = 0)

#These are the buttons that scroll through the projectile presets
btn_prevprojectile = tk.Button(master = frm_projectilepresets, text = '<-', command = prevprojectile)
btn_nextprojectile = tk.Button(master = frm_projectilepresets, text = '->', command = nextprojectile)

#This displays the current projectile preset
lbl_projectilepreset = tk.Label(master = frm_projectilepresets, text = 'Custom')

#This adds them to the frame
btn_prevprojectile.grid(column = 0, row = 0)
lbl_projectilepreset.grid(column = 1, row = 0)
btn_nextprojectile.grid(column = 2, row = 0)

#This makes the section with the submit/clear buttons
frm_buttons = tk.Frame(master = menu)
frm_buttons.pack(side = tk.RIGHT)

#This adds each button to the frame
btn_submit = tk.Button(master = frm_buttons, text = 'Submit', command = submit, width = 7)
btn_submit.pack(side = tk.RIGHT, padx = 5, pady = 5)

btn_clear = tk.Button(master = frm_buttons, text = 'Clear', command = clear, width = 7)
btn_clear.pack(side = tk.RIGHT, padx = 5, pady = 5)

menu.mainloop()