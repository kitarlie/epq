from matplotlib import pyplot as plt
from celluloid import Camera
from PIL import Image

x = []
y = []

fig = plt.figure()
camera = Camera(fig)
for i in range(1,50):
    #This creates each frame of the animation
    x.clear()
    y.clear()
    x.append(i)
    y.append(i**2)
    plt.xlabel('x')
    plt.ylabel('y')
    #plt.axis('off')
    plt.plot(x, y, color = '000000', marker = '.')
    camera.snap()

#This creates and displays the animation 
animation = camera.animate(interval = 200, repeat = False)
plt.show()