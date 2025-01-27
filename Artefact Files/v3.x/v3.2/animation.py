#Imports the relevant parts of the external modules
from matplotlib import pyplot as plt
from celluloid import Camera
from main import projectileInfo, tickRate

fig = plt.figure()
camera = Camera(fig)

for tick in projectileInfo:
    plt.plot([tick[1]], [tick[0]], color = '000000', marker = '.')
    plt.axis('off')
    camera.snap()

ani = camera.animate(interval = 1000*tickRate, repeat = False)
plt.show()