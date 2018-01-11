import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
from pylab import *
import pylab
import datetime as dt
os.chdir('Z:\williamyizhu On My Mac\Documents\workspace\PyTest')
import Stats

# -------------------------------------------------------------------------------------------------------------------
datadir = 'C:\\quandl_data_cn_futures\\eod'

gg = Stats.Stats(datadir)
gg.get_contract('DCE', 'M', 2013, 2017, ['09'])

gg.get_data(fill_datetime_index=True)
gg.get_contract_log_return_data(fill_datetime_index=True, ndiff=10, remove_nan=True)

fig, ax = plt.figure()

gg.plot(fig, 'SETTLE')



gg.hist(fig, 'SETTLE', 0.5, False)


fig, ax = plt.subplots()

mm = gg.data.groupby('contract')

cmap = plt.cm.get_cmap('gnuplot', len(mm)+1)
c = cycler('color', cmap(range(0,len(mm)+1)))
plt.rcParams["axes.prop_cycle"] = c

# mm.apply(lambda x: ax.plot(range(0,len(x)), x['SETTLE']))

mm.apply(lambda x: ax.plot(x['SETTLE']))

ax.legend(mm.groups.keys())
plt.show()





mm.apply(lambda x: print(x['contract']))

mm.plot(y=['SETTLE','CLOSE'])


mm.plot()


mm = gg.data.groupby('contract')
for i in mm:    
    
    print(type(i))
    
    
    
    print(i.index_of(mm))


datadir = 'C:\\quandl_data_cn_futures\\eod'
gg = Stats.Stats(datadir)
gg.get_contract('SHFE', 'CU', 2016, 2016, ['01'])
gg.get_contract_log_return_data(fill_datetime_index=True, ndiff=10, remove_nan=False)
fig, ax = plt.subplots()
gg.hist(ax, 'SETTLE', 'gnuplot', False)




mm = gg.get_dataset('\\'.join([gg.datadir, 'SHFE.CU1601.csv']), ',', True)
plt.plot(mm['SETTLE'])
nn = gg.log_return(mm, ndiff=10, remove_nan=False)


mm = gg.get_dataset('\\'.join([gg.datadir, 'DCE.M1701.csv']), ',', True)
plt.plot(mm['SETTLE'])
nn = gg.log_return(mm, ndiff=10, remove_nan=False)




to_percentage = lambda y: str(round( ( y / float(len(cg['SETTLE'])) ) * 100.0, 2)) + '%'
plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percentage))

plt.show()

np.histogram(np.array(cg['SETTLE']))


bb = get_dataset('C:\\quandl_data_cn_futures\\eod\\DCE.I1705.csv')

cj=log_return(aa)

date_index = pd.date_range(start=aa.index[0], end=aa.index[-1], freq='D')

aa.set_index(pd.DatetimeIndex(date_index))
             
             , inplace=True)
dc=aa.resample('D').pad()

dc['abc'] = dc.index
dc.diff(3, axis=0)
dc.div(3, axis=0)


plt.hist(cj['OPEN'], 100)
plt.hist(cj['CLOSE'], 100, alpha=0.5)
plt.hist(cj['SETTLE'], 100, alpha=0.5)


match(cj['OPEN'], min(cj['OPEN']))

qq=np.where( abs(cj['OPEN']) >= 0.06)

tempdata.apply(lambda x:np.diff(x), axis=0, reduce=True)

tempdata.apply(lambda x:np.log(x), axis=1)

tempdata.T.apply(lambda x:np.diff(x), axis=0)


aa['DATETIME'].drop(0)

x=pd.Series()

np.log(tempdata)

type(tempdata.iloc[:,1])

df=aa

np.diff(np.log(aa['OI']))




cols.remove('DATETIME')

.remove('DATETIME')
df[xx.drop('DATETIME')]


xx.columns.delete(['DATETIME'])

idx = [~np.isnan(value['DATETIME']) for idx, value in xx.iterrows()]

gg = xx.iloc[idx]

ss = np.array(np.log(gg['SETTLE']))



# -------------------------------------------------------------------------------------------------------------------
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

fig, ax = plt.subplots()

# The required parameters
num_steps = 10
max_percentage = 0.1
num_bins = 40

# Calculating the maximum value on the y axis and the yticks
max_val = max_percentage * len(data)
step_size = max_val / num_steps
yticks = [ x * step_size for x in range(0, num_steps+1) ]
ax.set_yticks( yticks )
plt.ylim(0, max_val)

# Running the histogram method
n, bins, patches = plt.hist(data, num_bins)

# To plot correct percentages in the y axis     
to_percentage = lambda y, pos: str(round( ( y / float(len(data)) ) * 100.0, 2)) + '%'
plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percentage))

plt.show()

# -------------------------------------------------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
np.random.seed(19680801)

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, normed=True, facecolor='g', alpha=0.75)

# add a 'best fit' line
y = mlab.normpdf(bins, mu, sigma)
plt.plot(bins, y, 'r--')
plt.xlabel('Smarts')
plt.ylabel('Probability')

# Tweak spacing to prevent clipping of ylabel
plt.subplots_adjust(left=0.15)

# -------------------------------------------------------------------------------------------------------------------
data = [1.5]*7 + [2.5]*2 + [3.5]*8 + [4.5]*3 + [5.5]*1 + [6.5]*8
density = gaussian_kde(data)
xs = np.linspace(0,8,200)
density.covariance_factor = lambda : .25
density._compute_covariance()
plt.plot(xs,density(xs))
plt.show()

data = [1.5]*7 + [2.5]*2 + [3.5]*8 + [4.5]*3 + [5.5]*1 + [6.5]*8
df = pd.DataFrame(data)
df.plot(kind='density')

# -------------------------------------------------------------------------------------------------------------------
# http://www.milkbox.net/note/gaussian-kde-smoothed-histograms-with-matplotlib/
# bogus data
data = [1.5]*7 + [2.5]*2 + [3.5]*8 + [4.5]*3 + [5.5]*1 + [6.5]*8

# generated a density class
density = gaussian_kde(data)

# set the covariance_factor, lower means more detail
density.covariance_factor = lambda : 0.25
density._compute_covariance()

# generate a fake range of x values
xs = np.arange(0, 24, 0.1)

# fill y values using density class
ys = density(xs)

def ggaxes(fig=None):
    if fig is None: fig = plt.figure()
    ax = fig.add_subplot(111)
    rstyle(ax)
    return ax

# ggaxes is a wrapper around rstyle
ax = ggaxes(plt.figure(figsize=(10, 8)))

l = ax.plot(xs, ys, antialiased=True, linewidth=2, color="#A81450")
l = ax.fill_between(xs, ys, alpha=0.5, zorder=5, antialiased=True, color="#E01B6A")

pd.Series(data).hist(ax=ax, normed=1, bins=8, color='grey', antialiased=True)
ax.set_xlim(0,8)

plt.savefig("gaussian_kde_25.png")

# rstyle is the function to style matplotlib like ggplot2 
def rstyle(ax):
    """Styles an axes to appear like ggplot2
    Must be called after all plot and axis manipulation operations have been carried out (needs to know final tick spacing)
    """
    #set the style of the major and minor grid lines, filled blocks
    ax.grid(True, 'major', color='w', linestyle='-', linewidth=1.4)
    ax.grid(True, 'minor', color='0.92', linestyle='-', linewidth=0.7)
    ax.patch.set_facecolor('0.85')
    ax.set_axisbelow(True)

    #set minor tick spacing to 1/2 of the major ticks
    ax.xaxis.set_minor_locator(MultipleLocator( (plt.xticks()[0][1]-plt.xticks()[0][0]) / 2.0 ))
    ax.yaxis.set_minor_locator(MultipleLocator( (plt.yticks()[0][1]-plt.yticks()[0][0]) / 2.0 ))

    #remove axis border
    for child in ax.get_children():
        if isinstance(child, matplotlib.spines.Spine):
            child.set_alpha(0)

    #restyle the tick lines
    for line in ax.get_xticklines() + ax.get_yticklines():
        line.set_markersize(5)
        line.set_color("gray")
        line.set_markeredgewidth(1.4)

    #remove the minor tick lines
    for line in ax.xaxis.get_ticklines(minor=True) + ax.yaxis.get_ticklines(minor=True):
        line.set_markersize(0)

    #only show bottom left ticks, pointing out of axis
    rcParams['xtick.direction'] = 'out'
    rcParams['ytick.direction'] = 'out'
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    if ax.legend_ != None:
        lg = ax.legend_
        lg.get_frame().set_linewidth(0)
        lg.get_frame().set_alpha(0.5)

def rhist(ax, data, **keywords):
    """Creates a histogram with default style parameters to look like ggplot2
    Is equivalent to calling ax.hist and accepts the same keyword parameters.
    If style parameters are explicitly defined, they will not be overwritten
    """
    defaults = {
                'facecolor' : '0.3',
                'edgecolor' : '0.28',
                'linewidth' : '1',
                'bins' : 100
                }

    for k, v in defaults.items():
        if k not in keywords: keywords[k] = v

    return ax.hist(data, **keywords)


def rbox(ax, data, **keywords):
    """Creates a ggplot2 style boxplot, is eqivalent to calling ax.boxplot with the following additions:

    Keyword arguments:
    colors -- array-like collection of colours for box fills
    names -- array-like collection of box names which are passed on as tick labels

    """

    hasColors = 'colors' in keywords
    if hasColors:
        colors = keywords['colors']
        keywords.pop('colors')

    if 'names' in keywords:
        ax.tickNames = plt.setp(ax, xticklabels=keywords['names'] )
        keywords.pop('names')

    bp = ax.boxplot(data, **keywords)
    pylab.setp(bp['boxes'], color='black')
    pylab.setp(bp['whiskers'], color='black', linestyle = 'solid')
    pylab.setp(bp['fliers'], color='black', alpha = 0.9, marker= 'o', markersize = 3)
    pylab.setp(bp['medians'], color='black')

    numBoxes = len(data)
    for i in range(numBoxes):
        box = bp['boxes'][i]
        boxX = []
        boxY = []
        for j in range(5):
            boxX.append(box.get_xdata()[j])
            boxY.append(box.get_ydata()[j])
        boxCoords = zip(boxX,boxY)

        if hasColors:
            boxPolygon = Polygon(boxCoords, facecolor = colors[i % len(colors)])
        else:
            boxPolygon = Polygon(boxCoords, facecolor = '0.95')

        ax.add_patch(boxPolygon)
    return bp
