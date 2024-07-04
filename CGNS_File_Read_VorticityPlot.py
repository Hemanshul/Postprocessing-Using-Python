# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 15:00:17 2018

@author: HemanshulGarg
"""

import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)
from scipy import interpolate



plt.close('all')
plt.ion()
fonts = 10

majorLocator = MultipleLocator(2)
majorFormatter = FormatStrFormatter('%d')
minorLocator = MultipleLocator(0.4)

majorLocator1 = MultipleLocator(2)
majorFormatter1 = FormatStrFormatter('%d')
minorLocator1 = MultipleLocator(0.4)


folder_path = 'https://github.com/Hemanshul/Postprocessing-Using-Python/edit/main/'

result = 'post'

def figsize_mm(figSWmm=65, figAR=0.618, nRows=1, nCols=1):
    figW = nCols * figSWmm / 25.4
    figH = nRows * figSWmm * figAR / 25.4
    return figW, figH


def margins_adjust(fig, figW, figH,
                   left=10, right=2.5, bottom=10, top=2.5,
                   wspace=15, hspace=2):
    fig.subplots_adjust(left=left / (figW * 25.4),
                        right=1 - right / (figW * 25.4),
                        bottom=bottom / (figH * 25.4),
                        top=1 - top / (figH * 25.4),
                        wspace=wspace / 25.4,
                        hspace=hspace / 25.4)


rowNum = 1  # num of rows of the subplots
colNum = 3  # num of colums of the subplots
## figure size
figW, figH = figsize_mm(figSWmm=80, figAR=1,
                              nRows=rowNum, nCols=colNum)


fig, axs = plt.subplots(figsize=(figW, figH),
                        nrows=rowNum, ncols=colNum,
                        sharex=False,squeeze=False)  # sharing the x-label
margins_adjust(fig, figW, figH, left=10, right=2, top=5, bottom=10,
                    wspace=4,hspace=4)



#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    
for i in range(0,rowNum):
   for j in range(colNum):
       plt.sca(axs[i,j])
       plt.cla()

file =os.path.join(folder_path,'Output.dat') 
 
with open(file, 'r') as f:
       data = np.loadtxt(f)  


# *****************************************************************************

ax = axs[0,0]      

X,Y = np.meshgrid(data[:,0],data[:,1])
ax.tricontourf(data[:,0],data[:,1],data[:,3],21,cmap='RdBu_r')

# *****************************************************************************

ax = axs[0,1]      

X,Y = np.meshgrid(data[:,0],data[:,1])
ax.tricontourf(data[:,0],data[:,1],data[:,4],21,cmap='RdBu_r')

# *****************************************************************************

ax = axs[0,2]

x_min = np.min(data[:,0])
x_max = np.max(data[:,0])
y_min = np.min(data[:,1])
y_max = np.max(data[:,1])


xi = np.linspace(x_min, x_max, 100)
yi = np.linspace(y_min, y_max, 100)

X1, Y1 = np.meshgrid(xi, yi)

xvel = data[:,3]
yvel = data[:,4]


xc = data[:,0]
yc = data[:,1]

U = interpolate.griddata((xc, yc), xvel, (X1, Y1), method='cubic')
V = interpolate.griddata((xc, yc), yvel, (X1, Y1), method='cubic')

c = np.sqrt(U**2+V**2)

ax.streamplot(X1, Y1, U, V, density = [3, 3], color = '#000000', arrowstyle='-',linewidth=0.5)
  
Q =ax.pcolormesh(X1,Y1,c,shading='gouraud',alpha=0.8,cmap=mpl.cm.Blues);

Q.set_clim(vmin=c.min(), vmax=c.max());

    
directory = os.path.join(folder_path,result)
figName = ('Vorticity_Velocity_Streamlines.png')
    
    
if not os.path.exists(directory):
        os.makedirs(directory)
        
fig.savefig(figName, dpi=200)
