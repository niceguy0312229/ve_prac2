from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
x = np.linspace(0, 2*np.pi, 100)
line, = ax.plot(x, np.sin(x))



def update(frame):
    # Update y-data at each frame
    line.set_ydata(np.sin(x + frame / 20))    
    return line,

anim = FuncAnimation(fig, update, frames=100, interval=50)

plt.show()

