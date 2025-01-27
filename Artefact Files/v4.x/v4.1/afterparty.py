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
    'Horizontal drag force'
    ]

menu = tk.Tk()
menu.title('Simulation results')

#This creates the play button
frm_play = tk.Frame(master = menu)

btn_play = tk.Button(
    master = frm_play, 
    text = 'Play simulation', 
    #command = partial(animate, projectileInfo, tickRate),
    )

btn_play.pack()
frm_play.pack()

#This creates the graph selection part

axislist = ['x', 'y']

frm_graphs = tk.Frame(master = menu)
frm_graphs.rowconfigure(0)
frm_graphs.rowconfigure(1)

for i in range(2):
    frm_axis = tk.Frame(master = frm_graphs)
    for j in range(2):
        frm_axis.columnconfigure(j)
    
    lbl_axis = tk.Label(master = frm_axis, text = axislist[i])
    lbl_axis.grid(row = 0, column = 0)

    frm_selector = tk.Frame(master = frm_axis)
    for j in range(3):
        frm_selector.columnconfigure(j)
    
    btn_back = tk.Button(master = frm_selector, text = '<-' ) #Must add command
    btn_back.grid(row = 0, column = 0)

    lbl_currentselection = tk.Label(master = frm_selector, text = 'foo')
    lbl_currentselection.grid(row = 0, column = 1)

    btn_for = tk.Button(master = frm_selector, text = '->') #Must add command
    btn_for.grid(row = 0, column = 2)

    frm_selector.grid(row = 0, column = 1)

    frm_axis.grid(row = i, column = 0)

frm_graphs.pack()

menu.mainloop()