from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
fig=plt.figure()
ax3=plt.axes(projection='3d')

xx=np.arange(-5.12,5.12,0.01)
yy=np.arange(-5.12,5.12,0.01)
x,y=np.meshgrid(xx,yy)
#z=20 + x**2 + y**2 - 10*(np.cos(2*np.pi*x)+np.cos(2*np.pi*y))
z=(3.0/(0.05+x**2+y**2))**2+(x**2+y**2)**2
ax3.plot_surface(x,y,z,cmap='rainbow')
plt.show()