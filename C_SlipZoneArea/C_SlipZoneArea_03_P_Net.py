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

fig_name = 'c_03_P_net.png'

##############################################################################
########################         Net Pressure       ##########################
##############################################################################
half_length = 10;      
y_wide = 5             
x_wide = 3
delta = 0.01;    

# Stress Inputs
P_net = np.linspace(5, 1, 5)
miu    = 0.4

fig = plt.figure(figsize=(6, 4),facecolor='white',constrained_layout=True)
ax = fig.add_subplot(1,1,1)

beta   = np.arange(0.,91., 1.)
k   =  0.88
TVD = 3300
FG = 0.022;     
PG =0.0098;     OverPress = 1.8;   

S2 = TVD*FG;    S1 = S2/k
P_pore = TVD*PG*OverPress 
##############################################################################
num_S_diff = 0
for j in P_net:
    
    K1 = j*(np.pi*half_length)**0.5
    num_beta = 0 
    area = np.empty_like(beta)
    
    for i in beta:  
        
        RE = FractureStress(half_length,S1,S2,j,i,miu,P_pore,delta,x_wide,y_wide)
        area[num_beta] = RE.area
        num_beta += 1 
               
    DC = 'C'+str(num_S_diff)
    plt.plot(beta,area,color=DC,label='P$_{net}$ = %.0f MPa, K$_{1}$ = %.0f MPa$\sqrt{m}$'%(j,K1))
    xmax = beta[np.argmax(area)]
    ymax = area.max()
    plt.plot(xmax,ymax,'ro')
    num_S_diff += 1
    # print(xmax)

text = ('\
FG  = %.0f kPa/m\n\
HG  = %.1f kPa/m\n\
PG  = %.1f*H.G\n\
TVD = 3300 m\n\
S$_{2}$ = %d MPa\n\
S$_{2}$/S$_{1}$ = %.2F\n\
P$_{p}$ = %.1f MPa\n\
a = %.0f m\n\
$\\mu$ = %.1f'\
        %(FG*1000,PG*1000,OverPress,S2,k,P_pore,half_length,miu))

props = dict(boxstyle='round', facecolor='whitesmoke', alpha=0.9, edgecolor='none')     
fig.text(0.75, 0.2, text,bbox=props,fontsize=10)

plt.title("Area of Potential Slip Zone",fontsize=14)
plt.ylabel('Area (m$^2$)',rotation=90, fontsize=12)
plt.xlabel('Relative Angle ('+chr(176)+')' , fontsize=12)
ax.set_facecolor('cornsilk')

ax.set_xticks(np.linspace(0,90,7),minor=False)
ax.set_xticks(np.linspace(0,90,91),minor=True)
plt.xlim(0,90)
plt.ylim(0,20)
ax.set_yticks(np.linspace(0,20,5),minor=False)
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

plt.savefig( save_plots_to+fig_name, dpi=300)

# for low stress differential conditon, 
# the relative angle does not have a major influence

print('Computing Time = %.2f sec'%(timeit.default_timer() - start_time))