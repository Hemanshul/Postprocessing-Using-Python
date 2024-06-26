# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 00:47:42 2024

@author: hemanshul
"""


import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)
import matplotlib.ticker as ticker


plt.close('all')
plt.ion()
fonts = 12

majorLocator = MultipleLocator(2)
majorFormatter = FormatStrFormatter('%d')
minorLocator = MultipleLocator(0.4)

majorLocator1 = MultipleLocator(1)
majorFormatter1 = FormatStrFormatter('%d')
minorLocator1 = MultipleLocator(0.2)


folder_path = 'https://github.com/Hemanshul/Postprocessing-Using-Python/edit/main/'

# folder_path = 'D:/Desktop/Python/273/1C'

result = 'post'
# start = 30000
# step = 200
# plot_marker = 1

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


rowNum = 3  # num of rows of the subplots
colNum = 4  # num of colums of the subplots
## figure size
figW, figH = figsize_mm(figSWmm=55, figAR=1.5,
                              nRows=rowNum, nCols=colNum)


fig, axs = plt.subplots(figsize=(figW, figH),
                        nrows=rowNum, ncols=colNum,
                        sharex=False,squeeze=False)  # sharing the x-label
margins_adjust(fig, figW, figH, left=10, right=7, top=2, bottom=3,
                    wspace=6,hspace=4)



#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    
for i in range(0,rowNum):
   for j in range(colNum):
       plt.sca(axs[i,j])
       plt.cla()
      
   
filename = os.path.join(folder_path,'0000001000.za')

  
data1 = np.loadtxt(filename,skiprows = 6)


xc = data1[0:40,0]

yc = np.zeros([40,1])        

for i in range(0,40):
            yc[i,0] = data1[0+i*40,1]



X,Y = np.meshgrid(xc,yc)

arr = data1[:,16]

Z = np.array_split(arr, 40)

arr1 = data1[:,8]

Z1 = np.array_split(arr1, 40)

arr2 = data1[:,9]

Z2 = np.array_split(arr2, 40)

arr3 = data1[:,17]

Z3 = np.array_split(arr3, 40)

def myfmt(x, pos):
    return '{0:.003f}'.format(x)

def myfmt1(x, pos):
    return '{0:.002e}'.format(x)

ax0 = axs[0,0].contourf(X,Y,Z,21,cmap=plt.cm.jet)

Zmin = min(data1[:,16])
Zmax = max(data1[:,16])

print(Zmin,Zmax)

# fig.subplots_adjust(top = 0.85)
cbar_ax = fig.add_axes([0.06, 0.93, 0.16, 0.01])
fig.colorbar(ax0, cax = cbar_ax,ticks=[Zmin, 0.5*(Zmin+Zmax), Zmax],format=ticker.FuncFormatter(myfmt), orientation='horizontal', label='')

ax1 = axs[0,1].contourf(X,Y,Z1,21,cmap=plt.cm.PuBuGn)


Zmin = min(data1[:,8])
Zmax = max(data1[:,8])

print(Zmin,Zmax)

# fig.subplots_adjust(top = 0.85)
cbar_ax = fig.add_axes([0.296, 0.93, 0.18, 0.01])
fig.colorbar(ax1, cax = cbar_ax, ticks=[Zmin, 0.5*(Zmin+Zmax), Zmax],format=ticker.FuncFormatter(myfmt),orientation='horizontal', label='')

ax2 = axs[0,2].contourf(X,Y,Z2,21,cmap=plt.cm.RdBu)

Zmin = min(data1[:,9])
Zmax = max(data1[:,9])

print(Zmin,Zmax)

# fig.subplots_adjust(top = 0.85)
cbar_ax = fig.add_axes([0.54, 0.93, 0.17, 0.01])
fig.colorbar(ax2, cax = cbar_ax,ticks=[0.0],format=ticker.FuncFormatter(myfmt),orientation='horizontal', label='')


ax3 = axs[0,3].contourf(X,Y,Z3,21,cmap=plt.cm.OrRd)

Zmin = min(data1[:,17])
Zmax = max(data1[:,17])

print(Zmin,Zmax)



fig.subplots_adjust(top = 0.9)
cbar_ax = fig.add_axes([0.785, 0.93, 0.18, 0.01])
fig.colorbar(ax3, cax = cbar_ax,ticks=[Zmin, 0.5*(Zmin+Zmax), Zmax],format=ticker.FuncFormatter(myfmt1),  orientation='horizontal', label='')




axs[0,3].text(0.8, 1.25, 'Variable4',
        verticalalignment='top', horizontalalignment='right',
        transform=axs[0,3].transAxes,
        color='black', fontsize=fonts)

axs[0,2].text(0.8, 1.25, 'Variable3',
        verticalalignment='top', horizontalalignment='right',
        transform=axs[0,2].transAxes,
        color='black', fontsize=fonts)

axs[0,1].text(0.8, 1.25, 'Variable2',
        verticalalignment='top', horizontalalignment='right',
        transform=axs[0,1].transAxes,
        color='black', fontsize=fonts)

axs[0,0].text(0.8, 1.25, 'Variable1',
        verticalalignment='top', horizontalalignment='right',
        transform=axs[0,0].transAxes,
        color='black', fontsize=fonts)


filename = os.path.join(folder_path,'0000053000.za')
    
data1 = np.loadtxt(filename,skiprows = 6)


arr = data1[:,16]

Z = np.array_split(arr, 40)

arr1 = data1[:,8]

Z1 = np.array_split(arr1, 40)

arr2 = data1[:,9]

Z2 = np.array_split(arr2, 40)

arr3 = data1[:,17]

Z3 = np.array_split(arr3, 40)



ax0 = axs[1,0].contourf(X,Y,Z,21,cmap=plt.cm.jet)

Zmin = min(data1[:,16])
Zmax = max(data1[:,16])


# fig.subplots_adjust(top = 0.85)
cbar_ax = fig.add_axes([0.06, 0.615, 0.16, 0.01])
fig.colorbar(ax0, cax = cbar_ax,ticks=[Zmin, 0.5*(Zmin+Zmax), Zmax],format=ticker.FuncFormatter(myfmt), orientation='horizontal', label='')


ax1 = axs[1,1].contourf(X,Y,Z1,21,cmap=plt.cm.PuBuGn)

Zmin = min(data1[:,8])
Zmax = max(data1[:,8])


cbar_ax = fig.add_axes([0.3, 0.615, 0.19, 0.01])
fig.colorbar(ax1, cax = cbar_ax, ticks=[Zmin, 0.5*(Zmin+Zmax), Zmax],format=ticker.FuncFormatter(myfmt),orientation='horizontal', label='')


ax2 = axs[1,2].contourf(X,Y,Z2,21,cmap=plt.cm.RdBu)

Zmin = min(data1[:,9])
Zmax = max(data1[:,9])

cbar_ax = fig.add_axes([0.54, 0.615, 0.17, 0.01])
fig.colorbar(ax2, cax = cbar_ax,ticks=[Zmin, 0.5*(Zmin+Zmax), Zmax],format=ticker.FuncFormatter(myfmt),orientation='horizontal', label='')


ax3 = axs[1,3].contourf(X,Y,Z3,21,cmap=plt.cm.OrRd)

Zmin = min(data1[:,17])
Zmax = max(data1[:,17])

cbar_ax = fig.add_axes([0.785, 0.615, 0.18, 0.01])
fig.colorbar(ax3, cax = cbar_ax,ticks=[Zmin, 0.5*(Zmin+Zmax), Zmax],format=ticker.FuncFormatter(myfmt1),  orientation='horizontal', label='')



axs[0,0].text(-0.05, 1, '(a)',
        verticalalignment='top', horizontalalignment='right',
        transform=axs[0,0].transAxes,
        color='black', fontsize=fonts)

axs[1,0].text(-0.05, 1, '(b)',
        verticalalignment='top', horizontalalignment='right',
        transform=axs[1,0].transAxes,
        color='black', fontsize=fonts)

axs[2,0].text(-0.05, 1, '(c)',
        verticalalignment='top', horizontalalignment='right',
        transform=axs[2,0].transAxes,
        color='black', fontsize=fonts)



filename = os.path.join(folder_path,'0000106635.za')  #283 3C
    
data1 = np.loadtxt(filename,skiprows = 6)


arr = data1[:,16]

Z = np.array_split(arr, 40)

arr1 = data1[:,8]

Z1 = np.array_split(arr1, 40)

arr2 = data1[:,9]

Z2 = np.array_split(arr2, 40)

arr3 = data1[:,17]

Z3 = np.array_split(arr3, 40)


ax0 = axs[2,0].contourf(X,Y,Z,21,cmap=plt.cm.jet)


Zmin = min(data1[:,16])
Zmax = max(data1[:,16])


cbar_ax = fig.add_axes([0.06, 0.305, 0.16, 0.01])
fig.colorbar(ax0, cax = cbar_ax,ticks=[Zmin, 0.5*(Zmin+Zmax), Zmax],format=ticker.FuncFormatter(myfmt), orientation='horizontal', label='')



ax1 = axs[2,1].contourf(X,Y,Z1,21,cmap=plt.cm.PuBuGn)

Zmin = min(data1[:,8])
Zmax = max(data1[:,8])


cbar_ax = fig.add_axes([0.3, 0.305, 0.19, 0.01])
fig.colorbar(ax1, cax = cbar_ax, ticks=[Zmin, 0.5*(Zmin+Zmax), Zmax],format=ticker.FuncFormatter(myfmt),orientation='horizontal', label='')


ax2 = axs[2,2].contourf(X,Y,Z2,21,cmap=plt.cm.RdBu)

Zmin = min(data1[:,9])
Zmax = max(data1[:,9])

cbar_ax = fig.add_axes([0.54, 0.305, 0.17, 0.01])
fig.colorbar(ax2, cax = cbar_ax,ticks=[Zmin, 0.5*(Zmin+Zmax), Zmax],format=ticker.FuncFormatter(myfmt),orientation='horizontal', label='')



ax3 = axs[2,3].contourf(X,Y,Z3,21,cmap=plt.cm.OrRd)

Zmin = min(data1[:,17])
Zmax = max(data1[:,17])

cbar_ax = fig.add_axes([0.785, 0.305, 0.18, 0.01])
fig.colorbar(ax3, cax = cbar_ax,ticks=[Zmin, 0.5*(Zmin+Zmax), Zmax],format=ticker.FuncFormatter(myfmt1),  orientation='horizontal', label='')




for i in range(0,rowNum):
   for j in range(colNum):
       axs[i,j].tick_params(which='both',left=0, top=0, right=0,
                    bottom=0, labelleft=0, labeltop=0,
                  labelright=0, labelbottom=0, width=0.5, direction="in") 



    

    
directory = os.path.join(folder_path,result)
figName = (directory+'Multiple_contours'+'.png')
    
    
if not os.path.exists(directory):
        os.makedirs(directory)
        
fig.savefig(figName, dpi=200)


