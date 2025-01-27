import tkinter as tk
#from graphics import animate #This will become the command for the 'play simulation' button
from functools import partial #This is needed to pass arguments to the command functions.
#from main import projectileInfo
#from main import tickRate

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
    ]

def nextvertaxis():
    global currentverticalaxis
    if currentverticalaxis != 7:
        currentverticalaxis += 1
        textboxes[0].config(text = values[currentverticalaxis])

def prevvertaxis():
    global currentverticalaxis
    if currentverticalaxis != 0:
        currentverticalaxis -= 1
        textboxes[0].config(text = values[currentverticalaxis])

def nexthoriaxis():
    global currenthorizontalaxis
    if currenthorizontalaxis != 7:
        currenthorizontalaxis += 1
        textboxes[1].config(text = values[currenthorizontalaxis])

def prevhoriaxis():
    global currenthorizontalaxis
    if currenthorizontalaxis != 0:
        currenthorizontalaxis -= 1
        textboxes[1].config(text = values[currenthorizontalaxis])

#These keep track of which axis value is currently selected.
currentverticalaxis = 0
currenthorizontalaxis = 0

prevcommands = [prevvertaxis, prevhoriaxis]
nextcommands = [nextvertaxis, nexthoriaxis]
currentaxes = [currentverticalaxis, currenthorizontalaxis]

#This makes the text update process easier

textboxes = []



menu = tk.Tk()
menu.title('Simulation results')

#This creates the play button
frm_play = tk.Frame(master = menu)

btn_play = tk.Button(
    master = frm_play, 
    text = 'Play simulation', 
    #command = partial(animate, projectileInfo, tickRate),
    width = 37
    )

btn_play.pack()
frm_play.pack()

#This spaces out the two sections

frm_spacer = tk.Frame(
    height = 10, 
    master = menu
    )
frm_spacer.pack()

#This creates the graph selection part

frm_graphs = tk.Frame(master = menu)
frm_graphs.rowconfigure(0)
frm_graphs.rowconfigure(1)
frm_graphs.rowconfigure(2)

#Plot button
lbl_plot = tk.Button(
    master = frm_graphs, 
    text = 'Plot a graph',
    width = 37
    )
lbl_plot.grid(row = 0, column = 0)

#The frame for the axis selectors

frm_axis = tk.Frame(master = frm_graphs)

#This creates the selector for the vertical axis

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
    text = values[currentverticalaxis], 
    width = 20
    )
lbl_currentselection.grid(row = 0, column = 2)
textboxes.append(lbl_currentselection)

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
    text = values[currenthorizontalaxis], 
    width = 20)
lbl_currentselection.grid(row = 0, column = 2)
textboxes.append(lbl_currentselection)

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