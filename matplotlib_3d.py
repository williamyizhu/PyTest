import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D


import pandas as pd
import numpy as np


df = pd.DataFrame(np.random.randn(5, 4), columns=['A', 'B', 'C', 'D'])
print(df)

   A         B         C         D
0  0.791692 -0.945571  0.183304  2.039369
1 -0.474666  1.117902 -0.483240  0.137620
2  1.448765  0.228217  0.294523  0.728543
3 -0.196164  0.898117 -1.770550  1.259608
4  0.646730 -0.366295 -0.893671 -0.745815

import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# x = df.columns
x = np.arange(len(df.columns))
y = df.index
X,Y = np.meshgrid(x,y)
Z = df
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z)



df = pd.DataFrame(np.random.randn(5, 4))

import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = df.columns
y = df.index
X,Y = np.meshgrid(x,y)
Z = df
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z)



## Matplotlib Sample Code using 2D arrays via meshgrid
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X ** 2 + Y ** 2)
Z = np.sin(R)
fig = plt.figure()
ax = Axes3D(fig)
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
ax.set_zlim(-1.01, 1.01)

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf, shrink=0.5, aspect=5)
plt.title('Original Code')
plt.show()



cmap = plt.cm.get_cmap('gnuplot', len(gg.index)+1)

xx = ivc.iv2['c']
df = xx.groupby('weekly')
gg = df.mean()

x = np.arange(len(gg.columns))
y = np.arange(len(gg.index))

X,Y = np.meshgrid(x,y)
Z = gg
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, color='white', linewidth=12.0)

ax.axes.set_xticklabels(gg.columns)
ax.axes.set_yticklabels(gg.index)

for i in range(0, len(gg)):

    ax.plot(x, np.ones(16)*i, gg.iloc[i], color=cmap(i), marker='.')



ax.plot(x, np.ones(16), gg.loc['2017-16'], color=cmap(1))



from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm

fig = plt.figure()
ax = fig.gca(projection='3d')
X, Y, Z = axes3d.get_test_data(0.05)
ax.plot_surface(X, Y, Z, rstride=8, cstride=8, alpha=0.3)
cset = ax.contour(X, Y, Z, zdir='z', offset=-100, cmap=cm.coolwarm)
cset = ax.contour(X, Y, Z, zdir='x', offset=-40, cmap=cm.coolwarm)
cset = ax.contour(X, Y, Z, zdir='y', offset=40, cmap=cm.coolwarm)

ax.set_xlabel('X')
ax.set_xlim(-40, 40)
ax.set_ylabel('Y')
ax.set_ylim(-40, 40)
ax.set_zlabel('Z')
ax.set_zlim(-100, 100)

plt.show()


from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm

fig = plt.figure()
ax = fig.gca(projection='3d')
X, Y, Z = axes3d.get_test_data(0.05)
cset = ax.contour(X, Y, Z, extend3d=True, cmap=cm.coolwarm)
ax.clabel(cset, fontsize=9, inline=1)

plt.show()

