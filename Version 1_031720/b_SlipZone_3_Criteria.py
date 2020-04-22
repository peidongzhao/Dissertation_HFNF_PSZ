'''
         UPDATED ON March 19th 2020
'''

import numpy as np
import matplotlib.pyplot as plt
# from Func_b_SlipZone import *
from b_SlipZoneFunc_v1 import *
import timeit

start_time = timeit.default_timer()
save_plots_to = '/Users/Peidong/0_Python_Code/Slip_SumAll/Plots/'
##############################################################################
#                  Changing beta, the angle between HF and NF
##############################################################################
beta = 90;
y_wide = 0.1;           x_wide = 0.1

delta = 0.000001;       
half_length = 10;    
S1 = 60;             S2 = 55;              P_net = 2
P_pore = 35
K1 =P_net*(np.pi*half_length)**0.5
##############################################################################
#                         PLOTTING INDIVIDUAL CRITERION 
##############################################################################
miu  = 0.4;
RE_01 = FractureStress(half_length,S1,S2,P_net,beta,miu,P_pore,delta,x_wide,y_wide)


fig = plt.figure(figsize=(5/0.8, 5),facecolor='white')
ax = fig.add_subplot(1,1,1)
DC = 'C0'   # For coloring 
ax.plot(-1000,1000,color=DC,label='$\mu$ = '+str(miu)) 

#               Criterion 1: If new Frac initiate at the other end
ax.contour(RE_01.x, RE_01.y, RE_01.Fail_1,[0.5, 1],colors=DC,linewidth=0.1)
ax.contourf(RE_01.x, RE_01.y, RE_01.Fail_1, [0.5, 1], cmap=plt.cm.Blues)
ax.set_title('#1: New HF Initiation Zone',fontsize=14,fontweight='bold') 
ax.set_ylabel('y (m)',rotation=90, fontsize=12)
ax.set_xlabel('x (m)', fontsize=12)
ax.plot([0,half_length],[0,0],'k-',linewidth=1)
ax.set_ylim(-y_wide,y_wide)
ax.set_xlim(half_length-x_wide,half_length+x_wide)
ax.set_xticks(np.linspace(half_length-x_wide,half_length+x_wide,5))
ax.set_yticks(np.linspace(-y_wide,y_wide,5))
ax.grid(which='major', linestyle=':')
ax.set_facecolor('cornsilk')

#                         Criterion 2: If NF open
fig = plt.figure(figsize=(5/0.8, 5),facecolor='white')
ax = fig.add_subplot(1,1,1)
DC = 'C1'   # For coloring 
ax.plot(-1000,1000,color=DC,label='$\mu$ = '+str(miu)) 
ax.contour(RE_01.x, RE_01.y, RE_01.Fail_2,[0.5, 1],colors=DC,linewidth=0.1)
ax.contourf(RE_01.x, RE_01.y, RE_01.Fail_2, [0.5, 1], cmap=plt.cm.Oranges)
ax.set_title('#2: NF Re-opening Zone',fontsize=14,fontweight='bold') 
ax.set_ylabel('y (m)',rotation=90, fontsize=12)
ax.set_xlabel('x (m)', fontsize=12)
ax.plot([0,half_length],[0,0],'k-',linewidth=1)
ax.set_ylim(-y_wide,y_wide)
ax.set_xlim(half_length-x_wide,half_length+x_wide)
ax.set_xticks(np.linspace(half_length-x_wide,half_length+x_wide,5))
ax.set_yticks(np.linspace(-y_wide,y_wide,5))
ax.grid(which='major', linestyle=':')
ax.set_facecolor('cornsilk')

#                         Criterion 3: If NF slip 
fig = plt.figure(figsize=(5/0.8, 5),facecolor='white')
ax = fig.add_subplot(1,1,1)
DC = 'C2'   # For coloring 
ax.plot(-1000,1000,color=DC,label='$\mu$ = '+str(miu)) 
ax.contour(RE_01.x, RE_01.y, RE_01.Fail_3,[0.5, 1],colors=DC,linewidth=0.1)
ax.contourf(RE_01.x, RE_01.y, RE_01.Fail_3, [0.5, 1], cmap=plt.cm.Greens)
ax.set_title('#3: NF Slip Zone',fontsize=14,fontweight='bold') 
ax.set_ylabel('y (m)',rotation=90, fontsize=12)
ax.set_xlabel('x (m)', fontsize=12)
ax.plot([0,half_length],[0,0],'k-',linewidth=1)
ax.set_ylim(-y_wide,y_wide)
ax.set_xlim(half_length-x_wide,half_length+x_wide)
ax.set_xticks(np.linspace(half_length-x_wide,half_length+x_wide,5))
ax.set_yticks(np.linspace(-y_wide,y_wide,5))
ax.grid(which='major', linestyle=':')
ax.set_facecolor('cornsilk')


##############################################################################
#                   PLOTTING ALL THREE CRITERIA TOGETHER
##############################################################################

fig = plt.figure(figsize=(5/0.8, 5),facecolor='white')
ax = fig.add_subplot(1,1,1)

#                         Criterion 3: If NF slip 
DC = 'C0'   # For coloring 
ax.plot(-1000,1000,color=DC,label='NF Slip') 
ax.contour(RE_01.x, RE_01.y, RE_01.Fail_3,[0.5, 1],colors=DC,linewidth=0.1)
ax.contourf(RE_01.x, RE_01.y, RE_01.Fail_3, [0.5, 1], cmap=plt.cm.Blues)

#           Criterion 1: If new Frac initiate at the other end
DC = 'C1'   # For coloring 
ax.plot(-1000,1000,color=DC,label='HF Re-Initiate') 
ax.contour(RE_01.x, RE_01.y, RE_01.Fail_1,[0.5, 1],colors=DC,linewidth=0.1)
ax.contourf(RE_01.x, RE_01.y, RE_01.Fail_1, [0.5, 1], cmap=plt.cm.Oranges)

#                         Criterion 2: If NF open
DC = 'C2'   # For coloring 
ax.plot(-1000,1000,color=DC,label='NF Re-Open') 
ax.contour(RE_01.x, RE_01.y, RE_01.Fail_2,[0.5, 1],colors=DC,linewidth=0.1)
ax.contourf(RE_01.x, RE_01.y, RE_01.Fail_2, [0.5, 1], cmap=plt.cm.Greens)


#                             PLOTTING
ax.set_title('Failure Modes Around HF',fontsize=14,
             fontweight='bold') 
ax.set_ylabel('y (m)',rotation=90, fontsize=12)
ax.set_xlabel('x (m)', fontsize=12)
ax.plot([0,half_length],[0,0],'k-',linewidth=1)
ax.set_ylim(-y_wide,y_wide)
ax.set_xlim(half_length-x_wide,half_length+x_wide)
ax.set_xticks(np.linspace(half_length-x_wide,half_length+x_wide,5))
ax.set_yticks(np.linspace(-y_wide,y_wide,5))
ax.grid(which='major', linestyle=':')
ax.set_facecolor('cornsilk')
ax.legend(loc="2", fontsize='large',fancybox=True,\
          framealpha=0.95,edgecolor='none',facecolor='whitesmoke')
    
text = ('\
a   = %.0f m\n\
S$_{1}$ = %d MPa\n\
S$_{2}$ = %d MPa\n\
P$_{p}$ = %d MPa\n\
P$_{n}$ = %.1f MPa\n\
K$_{1}$ = %.1f MPa$\sqrt{m}$\n\
$\mu$   =  %.1f \n\
$\\beta$   = %d$^\circ$'\
        %(half_length,S1,S2,P_pore,P_net,K1,miu,beta))
ax.legend(loc='upper left', fontsize='large',fancybox=True,\
          framealpha=0.95,edgecolor='none',facecolor='whitesmoke')
props = dict(boxstyle='round', facecolor='whitesmoke', alpha=0.8, edgecolor='none')        
fig.text(0.14,0.15, text, size=12,bbox=props,fontsize=10)

im = plt.imread('Rel_Angl.png')
phyl_ax=fig.add_axes([0.7, 0.4, 0.18, 0.18])
#  list of [left, bottom, width, height] values in 0-1 relative figure coordinates:
phyl_ax.get_xaxis().set_visible(False)
phyl_ax.get_yaxis().set_visible(False)
phyl_ax.spines['bottom'].set_color('none')
phyl_ax.spines['top'].set_color('none')
phyl_ax.spines['left'].set_color('none')
phyl_ax.spines['right'].set_color('none')
phyl_ax.set_facecolor('none')
phyl_ax.imshow(im,interpolation='nearest')


plt.savefig(save_plots_to+'b_01_ThreeFailModes_%.0f.png'%beta, dpi=300)


print(timeit.default_timer() - start_time)