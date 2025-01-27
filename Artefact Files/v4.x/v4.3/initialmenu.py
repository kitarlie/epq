import tkinter as tk

#Having a separate list for the raw values reduces the amount of rewriting I have to do 
#for the main code
global inputs
inputs = []

#Keeps track of which preset is currently shown
global currentProjectile
currentProjectile = 0

global currentPlanet
currentPlanet = 0

#This list makes the generation of input boxes much easier, 
#as it can be looped instead of written explicitly
values = [
    'Mass', 
    'Initial velocity', 
    'Initial height', 
    'Angle of projection', 
    'Cross-sectional area', 
    'Drag coefficient', 
    'Acceleration due to gravity', 
    'Atmospheric density',
    'Tick rate'
    ]

#Contain the preset values
projectilePresets = [
    ['Custom','','','','','','','-','-','-'],
    ['Football', '0.45', '-', '-', '-', '0.038', '0.5', '-', '-','-'],
    ['Basketball', '0.60', '-', '-', '-', '0.046', '0.5', '-', '-','-'],
    ['Golf ball', '0.046', '', '-', '-', '0.0015', '0.5', '-', '-','-'],
]

planetPresets = [
    ['Custom','-','','','','-','-','','','-'],
    ['Earth','-','-','-','-','-','-','9.81','1.225','-'],
    ['Venus','-','-','-','-','-','-','8.87','65','-'],
    ['Mars','-','-','-','-','-','-','3.71','0.020','-'],
]

#This dictionary allows each entry to be assigned a keyword, 
#which makes the submit() process easier
entries = {}


#Button functions
def submit():
    for i in values:
        if entries[i].get() == '':
            return
        inputs.append(float(entries[i].get()))
    menu.destroy()
    import main
    quit()

def clear():
    for i in values:
        entries[i].delete(0, tk.END)

def prevProjectile():
    global currentProjectile

    if currentProjectile > 0:
        currentProjectile -= 1

        lbl_projectilepreset['text'] = projectilePresets[currentProjectile][0]

    currentEntry = 0

    for i in entries:
        if projectilePresets[currentProjectile][currentEntry + 1] != '-':
            entries[values[currentEntry]].delete(0, tk.END)
            entries[values[currentEntry]].insert(0, str(projectilePresets[currentProjectile][currentEntry + 1]))
        currentEntry += 1

def nextProjectile():
    global currentProjectile
    if currentProjectile < (len(projectilePresets) -1):
        currentProjectile += 1

    currentEntry = 0
    
    for i in entries:
        if projectilePresets[currentProjectile][currentEntry + 1] != '-':
            entries[values[currentEntry]].delete(0, tk.END)
            entries[values[currentEntry]].insert(0, str(projectilePresets[currentProjectile][currentEntry + 1]))
        currentEntry += 1        

    lbl_projectilepreset['text'] = projectilePresets[currentProjectile][0]

def prevPlanet():
    global currentPlanet
    if currentPlanet > 0:
        currentPlanet -= 1

    currentEntry = 0
    
    for i in entries:
        if planetPresets[currentPlanet][currentEntry + 1] != '-':
            entries[values[currentEntry]].delete(0, tk.END)
            entries[values[currentEntry]].insert(0, str(planetPresets[currentPlanet][currentEntry + 1]))
        currentEntry += 1
        

    lbl_planetpreset['text'] = planetPresets[currentPlanet][0]

def nextPlanet():
    global currentPlanet
    if currentPlanet < (len(planetPresets) -1):
        currentPlanet += 1

    currentEntry = 0
    
    for i in entries:
        if planetPresets[currentPlanet][currentEntry + 1] != '-':
            entries[values[currentEntry]].delete(0, tk.END)
            entries[values[currentEntry]].insert(0, str(planetPresets[currentPlanet][currentEntry + 1]))
        currentEntry += 1
        

    lbl_planetpreset['text'] = planetPresets[currentPlanet][0]

#Spawns the menu window
menu = tk.Tk()
menu.title('Parameter input')
menu.minsize(285,300)
menu.maxsize(285,300)

########################################################################################################################################

#Frame containing all of the inputs
frm_inputs = tk.Frame(master = menu)
for i in range(9):
    frm_inputs.rowconfigure(i, weight = 1)
frm_inputs.pack()

#Iterates through each grid co-ordinate, and creates a section for each specific value
for i in range(9):
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

#Frame for the preset selection
frm_presets = tk.Frame(master = menu)
for i in range(2):
    frm_presets.rowconfigure(i)
frm_presets.pack()

#Frame for the projectile presets
frm_projectilePresets = tk.Frame(master = frm_presets)
frm_projectilePresets.grid(row = 0)

#Allows the nextProjectile and prevProjectile functions to access lbl_projectilepreset
global lbl_projectilepreset

#Displays the current projectile preset
lbl_projectilepreset = tk.Label(master = frm_projectilePresets, text = 'Custom', width = 10)

#Buttons for navigating projectile presets
btn_prevprojectile = tk.Button(master = frm_projectilePresets, text = '<-', command = prevProjectile)
btn_nextprojectile = tk.Button(master = frm_projectilePresets, text = '->', command = nextProjectile)

#Adds buttons/label to the frame
btn_prevprojectile.grid(column = 0, row = 0, pady = 2)
lbl_projectilepreset.grid(column = 1, row = 0, pady = 2)
btn_nextprojectile.grid(column = 2, row = 0, pady = 2)

#Frame for the planet presets
frm_planetPresets = tk.Frame(master = frm_presets)
frm_planetPresets.grid(row = 1)

#Allows the nextPlanet and prevPlanet functions to access lbl_planetpreset
global lbl_planetpreset

#Displays the current planet preset
lbl_planetpreset = tk.Label(master = frm_planetPresets, text = 'Custom', width = 10)

#Buttons for navigating the projectile presets
btn_prevplanet = tk.Button(master = frm_planetPresets, text = '<-', command = prevPlanet)
btn_nextplanet = tk.Button(master = frm_planetPresets, text = '->', command = nextPlanet)

#Adds buttons/label to the frame
btn_prevplanet.grid(column = 0, row = 0, pady = 2)
lbl_planetpreset.grid(column = 1, row = 0, pady = 2)
btn_nextplanet.grid(column = 2, row = 0, pady = 2)

########################################################################################################################################

#Frame for the submit/clear buttons
frm_buttons = tk.Frame(master = menu)
frm_buttons.pack(side = tk.RIGHT)

#Adds each button to the frame
btn_submit = tk.Button(master = frm_buttons, text = 'Submit', command = submit, width = 7)
btn_submit.pack(side = tk.RIGHT, padx = 5, pady = 2)

btn_clear = tk.Button(master = frm_buttons, text = 'Clear', command = clear, width = 7)
btn_clear.pack(side = tk.RIGHT, padx = 5, pady = 2)

menu.mainloop()