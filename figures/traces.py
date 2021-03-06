#!/usr/bin/env python

import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pylab

from matplotlib import rc
rc('font',**{'family':'serif','serif':['Times'],'size':'10'})
rc('text', usetex=True)

f = open(sys.argv[1], 'r')
tinytime = []
tinycurrent = []
androidtime = []
androidcurrent = []
for line in f:
    data = line.split(',')
    t = float(data[0])
    t = t - 4802360000.0
    tinytime.append(t)
    tinycurrent.append(float(data[1]))
f.close()

ff = open(sys.argv[2], 'r')
for line in ff:
    data = line.split(',')
    t = float(data[0])
    #t = t - 8185665000.0
    t = t - 8134965000.0
    #t = t*1000.0
    androidtime.append(t)
    androidcurrent.append(float(data[1]))

fig, ax = plt.subplots(2, sharex=True)

ax[0].set_ylabel(r'{\small \textbf{Current (mA)}}')
ax[0].plot(androidtime,androidcurrent, color='blue', linewidth=2,label=r'{\small \textbf{Sensor Android}}', rasterized=True)
ax[0].legend(loc='upper right')
ax[0].annotate('Idle draw 1.4 mA', xy=(75, 1),  xycoords='data',
        xytext=(50, 450), textcoords='data',
        arrowprops=dict(facecolor='black', width=1,shrink=0.05,headwidth=5),
        horizontalalignment='left', verticalalignment='top',
        )
ax[1].set_ylabel(r'{\small \textbf{Current (mA)}}')
ax[1].plot(tinytime,tinycurrent,color='green',label=r'{\small \textbf{Tiny Sensor Android}}', rasterized=True)
ax[1].set_xlabel(r'{\small \textbf{Time (Seconds)}}')
ax[1].legend(loc='upper right')
ax[1].annotate('Idle draw 8 mA', xy=(25,8),  xycoords='data',
        xytext=(50, 250), textcoords='data',
        arrowprops=dict(facecolor='black', width=1,shrink=0.05,headwidth=5),
        horizontalalignment='right', verticalalignment='top',
        )

fig.subplots_adjust(hspace=0.08, left=0.14, bottom=0.12,right=0.99, top=0.99)
fig.set_size_inches(3.5,3.0)
fig.savefig('traces.pdf')
