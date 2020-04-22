'''
         UPDATED ON March 19th 2020
'''

import numpy as np
import matplotlib.pyplot as plt
from Func_b_SlipZone import *
import timeit

start_time = timeit.default_timer()
save_plots_to = '/Users/Peidong/0_Python_Code/Slip_SumAll/Plots/'

##############################################################################
#                       Effect of Frictional Coefficient
##############################################################################

delta = 0.0002;       y_wide = 0.3;           x_wide = 0.3
half_length = 10;    
S1 = 60;             S2 = 55;              P_net = 2
beta = 30.0;          P_pore = 35
K1 =P_net*(np.pi*half_length)**0.5
fig = plt.figure(figsize=(6.25, 5),facecolor='white',constrained_layout=True)
ax = fig.add_subplot(1,1,1)

miu  = 0.4;
RE_01 = FractureStress(half_length,S1,S2,P_net,beta,miu,P_pore,delta,x_wide,y_wide)
DC = 'C0'   # For coloring 
ax.plot(-1000,1000,color=DC,label='$\mu$ = '+str(miu)) 
ax.contour(RE_01.x, RE_01.y, RE_01.Fail_PSZ,[0.9,1],colors=DC,linewidth=0.1)
ax.contourf(RE_01.x, RE_01.y, RE_01.Fail_PSZ, [0.9, 1], cmap=plt.cm.Blues)

miu  = 0.6;
RE_01 = FractureStress(half_length,S1,S2,P_net,beta,miu,P_pore,delta,x_wide,y_wide)
DC = 'C1'
ax.plot(-1000,1000,color=DC,label='$\mu$ = '+str(miu)) # For coloring of the legend line
ax.contour(RE_01.x, RE_01.y, RE_01.Fail_PSZ,[0.9, 1],colors=DC,linewidth=0.1)
ax.contourf(RE_01.x, RE_01.y, RE_01.Fail_PSZ, [0.5, 1], cmap=plt.cm.Oranges)

miu  = 0.8;
RE_01 = FractureStress(half_length,S1,S2,P_net,beta,miu,P_pore,delta,x_wide,y_wide)
DC = 'C2'
ax.plot(-1000,1000,color=DC,label='$\mu$ = '+str(miu)) # For coloring of the legend line
ax.contour(RE_01.x, RE_01.y, RE_01.Fail_PSZ,[0.9, 1],colors=DC,linewidth=0.1)
ax.contourf(RE_01.x, RE_01.y, RE_01.Fail_PSZ, [0.5, 1], cmap=plt.cm.Greens)

# Plot label =======================================================

ax.set_title('Potential Slip Zone',fontsize=14,fontweight='bold') #\nEffect of Frictional Coefficient 
ax.set_ylabel('y (m)',rotation=90, fontsize=12)
ax.set_xlabel('x (m)', fontsize=12)
ax.plot([0,half_length],[0,0],'k-',linewidth=1)
ax.set_ylim(-y_wide,y_wide)
ax.set_xlim(half_length-x_wide,half_length+x_wide)
ax.set_xticks(np.linspace(half_length-x_wide,half_length+x_wide,5))
ax.set_yticks(np.linspace(-y_wide,y_wide,5))
ax.grid(which='major', linestyle=':')
ax.set_facecolor('cornsilk')

text = ('\
a   = %.0f m\n\
S$_{1}$ = %d MPa\n\
S$_{2}$ = %d MPa\n\
P$_{p}$ = %d MPa\n\
P$_{n}$ = %.1f MPa\n\
K$_{1}$ = %.1f MPa$\sqrt{m}$\n\
$\\beta$  = %d$^\circ$'\
        %(half_length,S1,S2,P_pore,P_net,K1,beta))
ax.legend(loc="2", fontsize='large',fancybox=True,\
          framealpha=0.95,edgecolor='none',facecolor='whitesmoke')
props = dict(boxstyle='round', facecolor='whitesmoke', alpha=0.8, edgecolor='none')        
fig.text(0.14,0.15, text, size=12,bbox=props,fontsize=12)

im = plt.imread('Rel_Angl.png')
phyl_ax=fig.add_axes([0.2, 0.6, 0.25, 0.25])
#  list of [left, bottom, width, height] values in 0-1 relative figure coordinates:
phyl_ax.get_xaxis().set_visible(False)
phyl_ax.get_yaxis().set_visible(False)
phyl_ax.spines['bottom'].set_color('none')
phyl_ax.spines['top'].set_color('none')
phyl_ax.spines['left'].set_color('none')
phyl_ax.spines['right'].set_color('none')
phyl_ax.set_facecolor('none')
phyl_ax.imshow(im,interpolation='nearest')

plt.savefig( save_plots_to+'b_02_Effect_Miu.png', dpi=300)

print(timeit.default_timer() - start_time)