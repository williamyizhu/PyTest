# https://matplotlib.org/examples/color/colormaps_reference.html
# https://matplotlib.org/users/colormaps.html
# https://stackoverflow.com/questions/12236566/setting-different-color-for-each-series-in-scatter-plot-on-matplotlib
# https://stackoverflow.com/questions/4805048/how-to-get-different-colored-lines-for-different-plots-in-a-single-figure

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.colors as colors
import math
import numpy as np
import matplotlib as mpl


import matplotlib.pyplot as plt
import cycler
import numpy as np

# get colormap
# cmap=plt.cm.gist_rainbow
cmap = plt.cm.get_cmap('gnuplot', 2+1)

# build cycler with 5 equally spaced colors from that colormap
c = cycler.cycler('color', cmap([0,1]) )
# supply cycler to the rcParam
plt.rcParams["axes.prop_cycle"] = c


plt.plot(range(0,3), [1,2,3])
plt.plot(range(0,3), [3,6,4])
plt.plot(range(2,5), [7,8,3])



x = np.linspace(0,2*np.pi)
f = lambda x, phase:np.sin(x+phase)
 
for i in range(30):
    plt.plot(x,f(x,i/30.*np.pi) )

plt.show()


# ---------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.axes import Axes

rect = 0.1, 0.1, 0.8, 0.8

fig = plt.figure()
# ax1 = fig.add_axes(rect)
ax1 = fig.add_subplot(1,1,1)


t = np.arange(0.01, 10.0, 0.01)

ax1.plot(t, np.exp(t), 'b-') # Put your speed/power plot here
ax1.set_xlabel('Speed (mph)', color='b')
ax1.set_ylabel('Power', color='b')

ax11 = ax1.twinx()
ax11.plot(t, t*2)

ax2 = fig.add_axes(rect, frameon=False)
ax2.yaxis.tick_right()
ax2.yaxis.set_label_position('right')
ax2.xaxis.tick_top()
ax2.xaxis.set_label_position('top')

ax2.plot(t, np.sin(2*np.pi*t), 'r-') # Put your speed/rotation plot here
ax2.set_xlabel('Speed (kmph)', color='r')
ax2.set_ylabel('Rotations', color='r')

plt.show()

# ---------------------------------------------------------------------------
x = np.arange(10)
ys = [i+x+(i*x)**2 for i in range(10)]

colors = plt.cm.rainbow(np.linspace(0, 1, len(ys)))
for y, c in zip(ys, colors):
    plt.scatter(x, y, color=c)
    
# ---------------------------------------------------------------------------
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)

for i in range(1,15):
    ax1.plot(np.array([1,5])*i,label=i)

colormap = plt.cm.gist_ncar #nipy_spectral, Set1,Paired   
colors = [colormap(i) for i in np.linspace(0, 1,len(ax1.lines))]
for i,j in enumerate(ax1.lines):
    j.set_color(colors[i])


ax1.legend(loc=2)

# ---------------------------------------------------------------------------
# Illustrate the API for changing the cycle of colors used when plotting multiple lines on a single Axes.

yy = np.arange(24)
yy.shape = 6,4

mpl.rc('lines', linewidth=4)

fig = plt.figure()
mpl.rcParams['axes.color_cycle'] = ['r', 'g', 'b', 'c']
ax = fig.add_subplot(2,1,1)
ax.plot(yy)
ax.set_title('Changed default color cycle to rgbc')

ax = fig.add_subplot(2,1,2)
ax.set_color_cycle(['c', 'm', 'y', 'k'])
ax.plot(yy)
ax.set_title('This axes only, cycle is cmyk')

plt.show()

# ---------------------------------------------------------------------------
fig = plt.figure()
ax = fig.add_subplot(111)
 
ratio = 1.0 / 3.0
count = math.ceil(math.sqrt(len(colors.cnames)))
x_count = count * ratio
y_count = count / ratio
x = 0
y = 0
w = 1 / x_count
h = 1 / y_count
 
for c in colors.cnames:
    pos = (x / x_count, y / y_count)
    ax.add_patch(patches.Rectangle(pos, w, h, color=c))
    ax.annotate(c, xy=pos)
    if y >= y_count-1:
        x += 1
        y = 0
    else:
        y += 1
 
plt.show()