import tkinter as tk
from graphics import animate, graphs #This will become the command for the 'play simulation' button
from functools import partial #This is needed to pass arguments to the command functions.
from main import projectileInfo, tickRate

#A list of the plottable values and their list index within the tickInfo sublist.
values = [
    'Vertical displacement',
    'Horizontal displacement',
    'Vertical velocity',
    'Horizontal velocity',
    'Vertical acceleration',
    'Horizontal acceleration',
    'Vertical drag force',
    'Horizontal drag force',
    'Time',
    ]

def nextvertaxis():
    global currentVerticalAxis
    if currentVerticalAxis == 8:
        currentVerticalAxis = 0
        textBoxes[0].config(text = values[currentVerticalAxis])
    if currentVerticalAxis != 8:
        currentVerticalAxis += 1
        textBoxes[0].config(text = values[currentVerticalAxis])
    

def prevvertaxis():
    global currentVerticalAxis
    if currentVerticalAxis == 0:
        currentVerticalAxis = 8
        textBoxes[0].config(text = values[currentVerticalAxis])
    if currentVerticalAxis != 0:
        currentVerticalAxis -= 1
        textBoxes[0].config(text = values[currentVerticalAxis])

def nexthoriaxis():
    global currentHorizontalAxis
    if currentHorizontalAxis == 8:
        currentVerticalAxis = 0
        textBoxes[0].config(text = values[currentVerticalAxis])
    if currentHorizontalAxis != 8:
        currentHorizontalAxis += 1
        textBoxes[1].config(text = values[currentHorizontalAxis])

def prevhoriaxis():
    global currentHorizontalAxis
    if currentHorizontalAxis == 0:
        currentVerticalAxis = 8
        textBoxes[0].config(text = values[currentVerticalAxis])
    if currentHorizontalAxis != 0:
        currentHorizontalAxis -= 1
        textBoxes[1].config(text = values[currentHorizontalAxis])

#Keep track of which axis value is currently selected.
currentVerticalAxis = 0
currentHorizontalAxis = 0


#Makes the text update process easier

textBoxes = []

menu = tk.Tk()
menu.title('Simulation results')

#Creates the play button
frm_play = tk.Frame(master = menu)

btn_play = tk.Button(
    master = frm_play, 
    text = 'Play simulation', 
    command = partial(animate, projectileInfo, tickRate),
    width = 37
    )

btn_play.pack()
frm_play.pack()

#Spaces out the two sections

frm_spacer = tk.Frame(
    height = 10, 
    master = menu
    )
frm_spacer.pack()

#Creates the graph selection part

frm_graphs = tk.Frame(master = menu)
frm_graphs.rowconfigure(0)
frm_graphs.rowconfigure(1)
frm_graphs.rowconfigure(2)

#Button
lbl_plot = tk.Button(
    master = frm_graphs, 
    text = 'Plot a graph',
    width = 37,
    command = graphs
    )
lbl_plot.grid(row = 0, column = 0)

#The frame for the axis selectors

frm_axis = tk.Frame(master = frm_graphs)

#Creates the selector for the vertical axis

frm_selectorv = tk.Frame(master = frm_axis)
for j in range(4):
    frm_selectorv.columnconfigure(j)

lbl_axis = tk.Label(
    master = frm_selectorv, 
    text = 'Vertical',
    anchor = 'nw',
    width = 10
    )
lbl_axis.grid(row = 0, column = 0)

#Back button
btn_back = tk.Button(
    master = frm_selectorv, 
    text = '<-', 
    command = prevvertaxis
    )
btn_back.grid(row = 0, column = 1)

#Displays currently selected variable
lbl_currentselection = tk.Label(
    master = frm_selectorv, 
    text = values[currentVerticalAxis], 
    width = 20
    )
lbl_currentselection.grid(row = 0, column = 2)
textBoxes.append(lbl_currentselection)

#Forward button
btn_for = tk.Button(
    master = frm_selectorv, 
    text = '->', 
    command = nextvertaxis
    )
btn_for.grid(row = 0, column = 3)

frm_selectorv.grid(row = 1, column = 0)



#This creates the selector for the horizontal axis

frm_selectorh = tk.Frame(master = frm_axis)
for j in range(4):
    frm_selectorh.columnconfigure(j)

lbl_axis = tk.Label(
    master = frm_selectorh, 
    text = 'Horizontal',
    width = 10,
    anchor = 'nw'
    )
lbl_axis.grid(row = 0, column = 0)

#Back button
btn_back = tk.Button(
    master = frm_selectorh, 
    text = '<-', 
    command = prevhoriaxis
    ) 
btn_back.grid(row = 0, column = 1)

#Displays currently selected variable
lbl_currentselection = tk.Label(master = frm_selectorh, 
    text = values[currentHorizontalAxis], 
    width = 20)
lbl_currentselection.grid(row = 0, column = 2)
textBoxes.append(lbl_currentselection)

#Forward button
btn_for = tk.Button(
    master = frm_selectorh, 
    text = '->', 
    command = nexthoriaxis
    )

btn_for.grid(row = 0, column = 3)

frm_selectorh.grid(row = 2, column = 0)

#######################################################################################################

frm_axis.grid(row = 1, column = 0)

frm_graphs.pack()

menu.mainloop()