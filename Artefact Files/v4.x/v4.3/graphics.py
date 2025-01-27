#Imports the relevant parts of the external modules
from matplotlib import pyplot as plt
from celluloid import Camera

def animate(projectileInfo, tickRate):
    x = []
    y = []

    fig = plt.figure()
    camera = Camera(fig)

    for tick in projectileInfo:
        x.append(tick[1])
        y.append(tick[0])
        plt.plot(x, y, color = '000000')
        camera.snap()

    ani = camera.animate(interval = 1000*tickRate, repeat = False)
    plt.show()

def graphs():
    #Imports the necessary variables for plotting
    from afterparty import currentVerticalAxis, currentHorizontalAxis, values
    from main import tickRate, projectileInfo

    #Sets up the data sets to be plotted
    y = []
    x = []

    #Handles values when time is selected on the y-axis
    if currentVerticalAxis == 8:
        currentTick = 0
        for i in projectileInfo:
            y.append(currentTick * tickRate)
            currentTick += 1
    
    #Handles values when time is selected on the x-axis
    elif currentHorizontalAxis == 8:
        currentTick = 0
        for i in projectileInfo:
            x.append(currentTick * tickRate)
            currentTick += 1
    
    #Adds the missing values to the lists
    if x == []:
        for j in projectileInfo:
             x.append(j[currentHorizontalAxis])

    if y == []:
        for j in projectileInfo:
            y.append(j[currentVerticalAxis])

    #Plots the graph
    plt.xlabel(values[currentHorizontalAxis])
    plt.ylabel(values[currentVerticalAxis])
    plt.plot(x, y, color = '000000')
    plt.show()
