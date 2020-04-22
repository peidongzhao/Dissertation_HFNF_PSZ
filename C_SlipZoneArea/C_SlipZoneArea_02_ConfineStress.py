'''
         UPDATED ON March 19th 2020
         UPDATED ON April 15th 2020
'''

import numpy as np
import matplotlib.pyplot as plt
from Func_c_SlipZoneArea import *
import timeit

start_time = timeit.default_timer()

import os
save_plots_to = str(os.getcwd()) + '/Plots/'

fig_name = 'c_02_ConfStress_Depth.png'

##############################################################################
########################     Depth, Confine Stress  ##########################
##############################################################################
half_length = 10;      
y_wide = 4             
x_wide = 2.5
delta = 0.01;  
  

# Stress Inputs
P_net = 4

miu    = 0.4
K1 =P_net*(np.pi*half_length)**0.5

fig = plt.figure(figsize=(6, 4),facecolor='white',constrained_layout=True)
ax = fig.add_subplot(1,1,1)

beta   = np.arange(0.,91., 1.)
k   =  0.88

TVD = np.linspace(2900, 3300, 5)
FG = 0.022;     
PG =0.0098;     OverPress = 1.8;      
P_pore = 0; S2 = 0; S1 = 0
num_S_diff = 0
for j in TVD:
    
    S2 = j*FG;
    S1 = S2/k
    P_pore = j*PG*OverPress 
    
    num_beta = 0 
    area = np.empty_like(beta)
    
    for i in beta:  
        
        RE = FractureStress(half_length,S1,S2,P_net,i,miu,P_pore,delta,x_wide,y_wide)
        area[num_beta] = RE.area
        num_beta += 1 
               
    DC = 'C'+str(num_S_diff)
    plt.plot(beta,area,color=DC,label='S$_{2}$ = %.0f MPa @ %.0f m'%(S2,j))
    xmax = beta[np.argmax(area)]
    ymax = area.max()
    plt.plot(xmax,ymax,'ro')
    num_S_diff += 1
    # print(xmax)

text = ('\
F.G = %.0f kPa/m\n\
H.G = %.1f kPa/m\n\
P.G  = %.1f*H.G\n\
S$_{2}$/S$_{1}$ = %.2F\n\
a = %.0f m\n\
P$_{net}$ = %.0f MPa\n\
K$_{1}$ = %.1f MPa$\sqrt{m}$\n\
$\\mu$ = %.1f'\
        %(FG*1000,PG*1000,OverPress,k,half_length,P_net,K1,miu))

props = dict(boxstyle='round', facecolor='whitesmoke', alpha=0.9, edgecolor='none')     
fig.text(0.75, 0.2, text,bbox=props,fontsize=10)

plt.title("Area of Potential Slip Zone",fontsize=14)
plt.ylabel('Area (m$^2$)',rotation=90, fontsize=12)
plt.xlabel('Relative Angle ('+chr(176)+')' , fontsize=12)
ax.set_facecolor('cornsilk')

ax.set_xticks(np.linspace(0,90,7),minor=False)
ax.set_xticks(np.linspace(0,90,91),minor=True)
plt.xlim(0,90)
plt.ylim(0,16)

ax.grid(which='major', linestyle='-')
ax.grid(which='minor',  linestyle=':') 
plt.legend(loc='upper right',shadow=True, fontsize=10)

# x-off, y-off relative figure coordinates
im = plt.imread('Rel_Angl.png')
phyl_ax=fig.add_axes([0.14, 0.7, 0.2, 0.2])
#  list of [left, bottom, width, height] values in 0-1 relative figure coordinates:
phyl_ax.get_xaxis().set_visible(False)
phyl_ax.get_yaxis().set_visible(False)
phyl_ax.spines['bottom'].set_color('none')
phyl_ax.spines['top'].set_color('none')
phyl_ax.spines['left'].set_color('none')
phyl_ax.spines['right'].set_color('none')
phyl_ax.set_facecolor('whitesmoke')
phyl_ax.imshow(im,interpolation='nearest')

# x-off, y-off relative figure coordinates
im = plt.imread('Rel_Angl.png')
phyl_ax=fig.add_axes([0.14, 0.7, 0.2, 0.2])
#  list of [left, bottom, width, height] values in 0-1 relative figure coordinates:
phyl_ax.get_xaxis().set_visible(False)
phyl_ax.get_yaxis().set_visible(False)
phyl_ax.spines['bottom'].set_color('none')
phyl_ax.spines['top'].set_color('none')
phyl_ax.spines['left'].set_color('none')
phyl_ax.spines['right'].set_color('none')
phyl_ax.set_facecolor('whitesmoke')
phyl_ax.imshow(im,interpolation='nearest')

plt.savefig( save_plots_to+fig_name, dpi=300)

# for low stress differential conditon, 
# the relative angle does not have a major influence

print('Computing Time = %.2f sec'%(timeit.default_timer() - start_time))