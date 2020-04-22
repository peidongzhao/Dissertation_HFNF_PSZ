'''
         UPDATED ON March 19th 2020
'''
import timeit
import numpy as np
import matplotlib.pyplot as plt
from Func_a_StressAroundCrack import *

start_time = timeit.default_timer()

import os
save_plots_to = str(os.getcwd()) + '/Plots/'

fig_name_1 = 'a_02_StressField_3by1.png'
fig_name_2 = 'a_03_StressField_FEM_Validate.png'

##############################################################################
np.warnings.filterwarnings('ignore')

length = 4
Lx    = 15
Ly    = 15

resolution = 300
delta = Lx/resolution

# __init__(self, length, S1, S2, P_net, delta, Lx, Ly):
RE = SingleFractureStress(4,30,25,3,delta,Lx,Ly)

sig11_lower_bound=np.amin(RE.sig11)
sig22_lower_bound=np.amin(RE.sig22)
RE.Length_y

fig,((ax1,ax2,ax3)) = plt.subplots(3,1,figsize=(7, 9),constrained_layout=True)

c1 = ax1.pcolor(RE.x, RE.y, RE.sig11,cmap='RdBu',vmin=int(sig11_lower_bound),
                vmax=int(sig11_lower_bound)+8)
ax1.plot([-4,4],[0,0],'k',linewidth=0.5)
cbar = fig.colorbar(c1,ax=ax1)
cbar.ax.set_ylabel('MPa', rotation=270, fontsize=10)
cbar.ax.get_yaxis().labelpad = 15
ax1.set_title('$\sigma_{xx}$',fontsize=16,fontweight='bold',y=1.02)
ax1.set_ylim(-RE.Length_y,RE.Length_y)
ax1.set_xlim(-RE.Length_x,RE.Length_x)
ax1.set_yticks(np.arange(-RE.Length_y, RE.Length_y+1, 5))
ax1.set_xticks(np.arange(-RE.Length_x, RE.Length_x+1, 5))
ax1.set_ylabel('y', rotation= 0,fontsize=12)
ax1.set_xlabel('x', fontsize=12)

C2 = ax2.pcolor(RE.x, RE.y, RE.sig22, cmap='RdBu',vmin=int(sig22_lower_bound), 
                vmax=int(sig22_lower_bound)+8)
ax2.plot([-4,4],[0,0],'k',linewidth=0.5)
cbar=fig.colorbar(C2,ax=ax2)
cbar.ax.set_ylabel('MPa', rotation=270, fontsize=10)
cbar.ax.get_yaxis().labelpad = 15
ax2.set_title('$\sigma_{yy}$',fontsize=16,fontweight='bold',y=1.02)
ax2.set_ylim(-RE.Length_y,RE.Length_y)
ax2.set_xlim(-RE.Length_x,RE.Length_x)
ax2.set_yticks(np.arange(-RE.Length_y, RE.Length_y+1, 5))
ax2.set_xticks(np.arange(-RE.Length_x, RE.Length_x+1, 5))
ax2.set_ylabel('y', rotation= 0,fontsize=12)
ax2.set_xlabel('x', fontsize=12)

c3 = ax3.pcolor(RE.x, RE.y, RE.sig12, cmap='RdBu', vmin=-1.5, vmax=1.5)
cbar=fig.colorbar(c3,ax=ax3)
ax3.plot([-4,4],[0,0],'k',linewidth=0.5)
cbar.ax.set_ylabel('MPa', rotation=270, fontsize=10)
cbar.ax.get_yaxis().labelpad = 15
ax3.set_title('$\sigma_{xy}$',fontsize=16,fontweight='bold',y=1.02)
ax3.set_ylim(-RE.Length_y,RE.Length_y)
ax3.set_xlim(-RE.Length_x,RE.Length_x)
ax3.set_yticks(np.arange(-RE.Length_y, RE.Length_y+1, 5))
ax3.set_xticks(np.arange(-RE.Length_x, RE.Length_x+1, 5))
ax3.set_ylabel('y',rotation=0, fontsize=12)
ax3.set_xlabel('x', fontsize=12)

fig.suptitle('S$_{hmax}$ = 30 MPa, S$_{hmin}$ = 25 MPa, P$_{net}$ = 3 MPa',
             y=1.03, fontsize=16);
plt.savefig(save_plots_to+fig_name_1, dpi=resolution,bbox_inches='tight')

##############################################################################
# __init__(self, length, S1, S2, P_net, delta, Lx, Ly):
delta = 0.01 
RE = SingleFractureStress(4,30,25,3,delta,20,delta*2)
center=RE.center_line_num
# Assign inf stresses at the tips
def TipRemoval_2(value):
    value[value==0] = 'inf'
    return value
TipRemoval_2(RE.sig11)
TipRemoval_2(RE.sig22)

x = []
s11 = []
s22 = []
with open('StressAroundCrack_FEM.txt') as f:
    for line in f:
        data = line.split()
        x.append(float(data[0]))
        s11.append(float(data[1]))
        s22.append(float(data[2]))

plt.figure(figsize=(7, 5.5))

plt.plot(RE.xrange,RE.sig11[int(center-1),:],'red',
         label='$\sigma_{xx}$, Analytical')
plt.plot(RE.xrange,RE.sig22[int(center-1),:],'blue',
         label='$\sigma_{yy}$, Analytical')
plt.plot(RE.xrange,RE.sig12[int(center-1),:],'green',
         label='$\sigma_{xy}$, Analytical')

plt.plot(x,s11,'ro',label='$\sigma_{xx}$, FEM', markersize=5)
plt.plot(x,s22,'bo',label='$\sigma_{yy}$, FEM', markersize=5)

plt.title('Stresses Along the Hydraulic Fracture',fontsize=14,y=1.02,fontweight='bold')
plt.legend(loc="center right", shadow=True, fontsize='large')
plt.ylabel('Stress (MPa)',rotation=90, fontsize=12)
plt.xlabel('x (m)', fontsize=12)
plt.grid(True)
plt.minorticks_on()
plt.grid(which='major', linestyle='-')
plt.grid(which='minor', linestyle=':')
plt.ylim(-35,5)
plt.xlim(-20,20)
text = ('\
Half Length  =  %.0f m    \n\
S$_{hmax}$ = %d MPa\n\
S$_{hmin}$ = %d MPa\n\
P$_{net}$ =   %d MPa'
%(4,30,25,3))
props = dict(boxstyle='round', facecolor='whitesmoke', alpha=0.9, edgecolor='none')     
plt.text(-5.5, -8, text, bbox=props,horizontalalignment='right',
         verticalalignment='top',fontsize=12)

plt.savefig(save_plots_to+fig_name_2, dpi=resolution)

print(timeit.default_timer() - start_time)