import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy.linalg as lin
import numpy as np

molecs=int(input('Ingrese un número de moléculas: '))

fig, axis = plt.subplots()
x=[0 for i in range(molecs)]
y=[0 for j in range(molecs)]

axis.set(xlim=(-40, 40), xticks=np.arange(-40, 41, 10),
       ylim=(-40, 40), yticks=np.arange(-40, 41, 10))

def step(particles_x, particles_y, n):
      for i in range(n):
          step_x=np.random.normal(0,1)
          step_y=np.random.normal(0,1)
          POS=np.array([step_x,step_y])
          try:
              POS=POS/lin.norm(POS,2)
          except ZeroDivisionError:
              continue
          particles_x[i]=particles_x[i]+POS[0]
          particles_y[i]=particles_y[i]+POS[1]

def actualizar(i):
    fig.clear()
    step(x,y,molecs)
    axis=fig.add_subplot()
    axis.set(xlim=(-40, 40), xticks=np.arange(-40, 41, 10),
           ylim=(-40, 40), yticks=np.arange(-40, 41, 10))
    scat=axis.scatter(x, y, marker='.',s=5,color='green')
    return scat

ani=animation.FuncAnimation(fig, actualizar, frames=range(200), interval=5)
plt.show()
