'''
         UPDATED ON March 19th 2020
         UPDATED ON April 13th 2020
'''
import timeit
import numpy as np
import matplotlib.pyplot as plt
from Func_a_StressAroundCrack import *

start_time = timeit.default_timer()

import os
save_plots_to = str(os.getcwd()) +'/Plots/'
fig_name_1 = 'a_01_StressField_all.png'

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

fig,((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2,figsize=(10, 6),constrained_layout=True)

c1 = ax1.pcolor(RE.x, RE.y, RE.sig11,cmap='RdBu',vmin=int(sig11_lower_bound),
                vmax=int(sig11_lower_bound)+8)
ax1.plot([-4,4],[0,0],'k',linewidth=0.5)
cbar = fig.colorbar(c1,ax=ax1,shrink=0.9)
ax1.set_title('$\sigma_{xx}$',fontsize=16,y=1.01)
ax1.set_ylim(-RE.Length_y,RE.Length_y)
ax1.set_xlim(-RE.Length_x,RE.Length_x)
ax1.set_yticks(np.arange(-RE.Length_y, RE.Length_y+1, 5))
ax1.set_xticks(np.arange(-RE.Length_x, RE.Length_x+1, 5))
ax1.set_ylabel('y', rotation= 0,fontsize=10)
ax1.set_xlabel('x', fontsize=10)

C2 = ax2.pcolor(RE.x, RE.y, RE.sig22, cmap='RdBu',vmin=int(sig22_lower_bound), 
                vmax=int(sig22_lower_bound)+8)
ax2.plot([-4,4],[0,0],'k',linewidth=0.5)
cbar=fig.colorbar(C2,ax=ax2,shrink=0.9)
ax2.set_title('$\sigma_{yy}$',fontsize=16,y=1.01)
ax2.set_ylim(-RE.Length_y,RE.Length_y)
ax2.set_xlim(-RE.Length_x,RE.Length_x)
ax2.set_yticks(np.arange(-RE.Length_y, RE.Length_y+1, 5))
ax2.set_xticks(np.arange(-RE.Length_x, RE.Length_x+1, 5))
ax2.set_ylabel('y', rotation= 0,fontsize=10)
ax2.set_xlabel('x', fontsize=10)

c3 = ax3.pcolor(RE.x, RE.y, RE.sig12, cmap='RdBu', vmin=-1.5, vmax=1.5)
cbar=fig.colorbar(c3,ax=ax3,shrink=0.9)
ax3.plot([-4,4],[0,0],'k',linewidth=0.5)
ax3.set_title('$\sigma_{xy}$',fontsize=16,y=1.01)
ax3.set_ylim(-RE.Length_y,RE.Length_y)
ax3.set_xlim(-RE.Length_x,RE.Length_x)
ax3.set_yticks(np.arange(-RE.Length_y, RE.Length_y+1, 5))
ax3.set_xticks(np.arange(-RE.Length_x, RE.Length_x+1, 5))
ax3.set_ylabel('y',rotation=0, fontsize=10)
ax3.set_xlabel('x', fontsize=10)

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


ax4.plot(RE.xrange,RE.sig11[int(center-1),:],'red',
         label='$\sigma_{xx}$')
ax4.plot(RE.xrange,RE.sig22[int(center-1),:],'blue',
         label='$\sigma_{yy}$')
ax4.plot(RE.xrange,RE.sig12[int(center-1),:],'green',
         label='$\sigma_{xy}$')


ax4.set_title('Stresses Along Fracutre Strike',fontsize=14,y=1.01)
ax4.legend(loc="center right", shadow=True, fontsize='small')
ax4.set_ylabel('Stress (MPa)',rotation=90, fontsize=10)
ax4.set_xlabel('x (m)', fontsize=10)
ax4.grid(True)
ax4.minorticks_on()
ax4.grid(which='major', linestyle='-')
ax4.grid(which='minor', linestyle=':')
ax4.set_ylim(-35,5)
ax4.set_xlim(-20,20)



fig.suptitle('Asymptotic Stress Field Around a Hydraulic Fracture\nL$_{half}$ = 4m, S$_{hmax}$ = 30MPa, S$_{hmin}$ = 25MPa, P$_{net}$ = 3MPa',
              y=1.1, fontsize=16);


plt.savefig(save_plots_to+fig_name_1, dpi=300,bbox_inches='tight',fontweight='bold')
print(timeit.default_timer() - start_time)