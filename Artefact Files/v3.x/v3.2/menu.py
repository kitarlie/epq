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
    'Atmospheric density',
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
        if entries[i].get() == '':
            return
        inputs.append(float(entries[i].get()))
    menu.destroy()
    exec(open("./main.py").read())

def clear():
    for i in values:
        entries[i].delete(0, tk.END)

#This is the button function for the 'previous projectile' button
def prevprojectile():
    global currentprojectile

    if currentprojectile > 0:
        currentprojectile -= 1

        lbl_projectilepreset['text'] = projectilepresets[currentprojectile][0]

    currententry = 0

    for i in entries:
        if projectilepresets[currentprojectile][currententry + 1] != '-':
            entries[values[currententry]].delete(0, tk.END)
            entries[values[currententry]].insert(0, str(projectilepresets[currentprojectile][currententry + 1]))
        currententry += 1

#This is the button function for the 'next projectile' button
def nextprojectile():
    global currentprojectile
    if currentprojectile < (len(projectilepresets) -1):
        currentprojectile += 1

    currententry = 0
    
    for i in entries:
        if projectilepresets[currentprojectile][currententry + 1] != '-':
            entries[values[currententry]].delete(0, tk.END)
            entries[values[currententry]].insert(0, str(projectilepresets[currentprojectile][currententry + 1]))
        currententry += 1        

    lbl_projectilepreset['text'] = projectilepresets[currentprojectile][0]

#This is the button function for the 'previous planet' button
def prevplanet():
    global currentplanet
    if currentplanet > 0:
        currentplanet -= 1

    currententry = 0
    
    for i in entries:
        if planetpresets[currentplanet][currententry + 1] != '-':
            entries[values[currententry]].delete(0, tk.END)
            entries[values[currententry]].insert(0, str(planetpresets[currentplanet][currententry + 1]))
        currententry += 1
        

    lbl_planetpreset['text'] = planetpresets[currentplanet][0]

#This is the button function for the 'next planet' button
def nextplanet():
    global currentplanet
    if currentplanet < (len(planetpresets) -1):
        currentplanet += 1

    currententry = 0
    
    for i in entries:
        if planetpresets[currentplanet][currententry + 1] != '-':
            entries[values[currententry]].delete(0, tk.END)
            entries[values[currententry]].insert(0, str(planetpresets[currentplanet][currententry + 1]))
        currententry += 1
        

    lbl_planetpreset['text'] = planetpresets[currentplanet][0]


########################################################################################################################################

#This makes the initial window
menu = tk.Tk()
menu.title('Parameter input')
menu.minsize(285,275)
menu.maxsize(285,275)

#This makes the section containing all of the inputs
frm_inputs = tk.Frame(master = menu)
for i in range(8):
    frm_inputs.rowconfigure(i, weight = 1)
frm_inputs.pack()

#This iterates through each grid co-ordinate, and creates a section for each specific value
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

########################################################################################################################################

#This makes the section with the presets
frm_presets = tk.Frame(master = menu)
for i in range(2):
    frm_presets.rowconfigure(i)
frm_presets.pack()

#This creates the section for the projectile presets
frm_projectilepresets = tk.Frame(master = frm_presets)
frm_projectilepresets.grid(row = 0)

#This is required to allow the nextprojectile and prevprojectile functions to access lbl_projectilepreset
global lbl_projectilepreset

#This displays the current projectile preset
lbl_projectilepreset = tk.Label(master = frm_projectilepresets, text = 'Custom', width = 10)

#These are the buttons that scroll through the projectile presets
btn_prevprojectile = tk.Button(master = frm_projectilepresets, text = '<-', command = prevprojectile)
btn_nextprojectile = tk.Button(master = frm_projectilepresets, text = '->', command = nextprojectile)

#This adds them to the frame
btn_prevprojectile.grid(column = 0, row = 0, pady = 2)
lbl_projectilepreset.grid(column = 1, row = 0, pady = 2)
btn_nextprojectile.grid(column = 2, row = 0, pady = 2)

#This creates the section for the planet presets
frm_planetpresets = tk.Frame(master = frm_presets)
frm_planetpresets.grid(row = 1)

#This is required to allow the nextplanet and prevplanet functions to access lbl_planetpreset
global lbl_planetpreset

#This displays the current planet preset
lbl_planetpreset = tk.Label(master = frm_planetpresets, text = 'Custom', width = 10)

#These are the buttons that scroll through the projectile presets
btn_prevplanet = tk.Button(master = frm_planetpresets, text = '<-', command = prevplanet)
btn_nextplanet = tk.Button(master = frm_planetpresets, text = '->', command = nextplanet)

#This adds them to the frame
btn_prevplanet.grid(column = 0, row = 0, pady = 2)
lbl_planetpreset.grid(column = 1, row = 0, pady = 2)
btn_nextplanet.grid(column = 2, row = 0, pady = 2)

########################################################################################################################################

#This makes the section with the submit/clear buttons
frm_buttons = tk.Frame(master = menu)
frm_buttons.pack(side = tk.RIGHT)

#This adds each button to the frame
btn_submit = tk.Button(master = frm_buttons, text = 'Submit', command = submit, width = 7)
btn_submit.pack(side = tk.RIGHT, padx = 5, pady = 2)

btn_clear = tk.Button(master = frm_buttons, text = 'Clear', command = clear, width = 7)
btn_clear.pack(side = tk.RIGHT, padx = 5, pady = 2)

menu.mainloop()