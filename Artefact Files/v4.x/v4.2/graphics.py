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