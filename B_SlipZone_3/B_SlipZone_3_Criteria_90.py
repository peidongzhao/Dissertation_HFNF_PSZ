'''
         UPDATED ON March 19th 2020
         UPDATED ON April 13th 2020
'''

import numpy as np
import matplotlib.pyplot as plt
from Func_b_SlipZone import *
import timeit

start_time = timeit.default_timer()

import os
save_plots_to = str(os.getcwd()) + '/Plots/'
##############################################################################
#                  Changing beta, the angle between HF and NF
##############################################################################
beta = 90;
y_wide = 0.1;           x_wide = 0.1

delta = 0.0001;    
half_length = 10;    
S1 = 60;             S2 = 55;              P_net = 2
P_pore = 35
K1 =P_net*(np.pi*half_length)**0.5
##############################################################################
#                         PLOTTING INDIVIDUAL CRITERION 
##############################################################################
miu  = 0.4;
RE_01 = FractureStress(half_length,S1,S2,P_net,beta,miu,P_pore,delta,x_wide,y_wide)

fig, (ax1,ax2,ax3) = plt.subplots(1, 3,figsize=(12*0.8, 4*0.8),constrained_layout=True)

#               Criterion 1: If new Frac initiate at the other end
DC = 'C1'   # For coloring 
ax1.contour(RE_01.x, RE_01.y, RE_01.Fail_1,[0.5, 1],colors=DC,linewidth=0.1)
ax1.contourf(RE_01.x, RE_01.y, RE_01.Fail_1, [0.5, 1], cmap=plt.cm.Oranges)
ax1.set_title('Criterion 1: New HF Initiation',fontsize=12) 
ax1.set_ylabel('y (m)',rotation=90, fontsize=12)
ax1.set_xlabel('x (m)', fontsize=12)
ax1.plot([0,half_length],[0,0],'k-',linewidth=1)
ax1.set_ylim(-y_wide,y_wide)
ax1.set_xlim(half_length-x_wide,half_length+x_wide)
ax1.set_xticks(np.linspace(half_length-x_wide,half_length+x_wide,5))
ax1.set_yticks(np.linspace(-y_wide,y_wide,5))
ax1.grid(which='major', linestyle=':')
ax1.set_facecolor('cornsilk')

#                         Criterion 2: If NF open
DC = 'C2'   # For coloring 
ax2.plot(-1000,1000,color=DC,label='$\mu$ = '+str(miu)) 
ax2.contour(RE_01.x, RE_01.y, RE_01.Fail_2,[0.5, 1],colors=DC,linewidth=0.1)
ax2.contourf(RE_01.x, RE_01.y, RE_01.Fail_2, [0.5, 1], cmap=plt.cm.Greens)
ax2.set_title('Criterion 2: NF Reopen',fontsize=12) 
# ax2.set_ylabel('y (m)',rotation=90, fontsize=12)
ax2.set_xlabel('x (m)', fontsize=12)
ax2.plot([0,half_length],[0,0],'k-',linewidth=1)
ax2.set_ylim(-y_wide,y_wide)
ax2.set_xlim(half_length-x_wide,half_length+x_wide)
ax2.set_xticks(np.linspace(half_length-x_wide,half_length+x_wide,5))
ax2.set_yticks(np.linspace(-y_wide,y_wide,5))
ax2.grid(which='major', linestyle=':')
ax2.set_facecolor('cornsilk')


#                         Criterion 3: If NF slip 
DC = 'C0'   # For coloring 
ax3.plot(-1000,1000,color=DC,label='$\mu$ = '+str(miu)) 
ax3.contour(RE_01.x, RE_01.y, RE_01.Fail_3,[0.5, 1],colors=DC,linewidth=0.1)
ax3.contourf(RE_01.x, RE_01.y, RE_01.Fail_3, [0.5, 1], cmap=plt.cm.Blues)
ax3.set_title('Criterion 3: NF Slip',fontsize=12) 
# ax3.set_ylabel('y (m)',rotation=90, fontsize=12)
ax3.set_xlabel('x (m)', fontsize=12)
ax3.plot([0,half_length],[0,0],'k-',linewidth=1)
ax3.set_ylim(-y_wide,y_wide)
ax3.set_xlim(half_length-x_wide,half_length+x_wide)
ax3.set_xticks(np.linspace(half_length-x_wide,half_length+x_wide,5))
ax3.set_yticks(np.linspace(-y_wide,y_wide,5))
ax3.grid(which='major', linestyle=':')
ax3.set_facecolor('cornsilk')

ax2.yaxis.set_ticklabels([])
ax3.yaxis.set_ticklabels([])

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
props = dict(boxstyle='round', facecolor='whitesmoke', alpha=0.9, edgecolor='none')        
fig.text(0.33,0.3, text, size=14,bbox=props,fontsize=10)

im = plt.imread('Rel_Angl.png')
phyl_ax=fig.add_axes([0.46, 0.22, 0.25, 0.25])
#  list of [left, bottom, width, height] values in 0-1 relative figure coordinates:
phyl_ax.get_xaxis().set_visible(False)
phyl_ax.get_yaxis().set_visible(False)
phyl_ax.spines['bottom'].set_color('none')
phyl_ax.spines['top'].set_color('none')
phyl_ax.spines['left'].set_color('none')
phyl_ax.spines['right'].set_color('none')
phyl_ax.set_facecolor('none')
phyl_ax.imshow(im,interpolation='nearest')

plt.savefig(save_plots_to+'b_3Modes_sep_%.0f.png'%beta, dpi=300)


##############################################################################
#                   PLOTTING ALL THREE CRITERIA TOGETHER
##############################################################################

fig = plt.figure(figsize=(6.25, 5),facecolor='white',constrained_layout=True)
ax = fig.add_subplot(1,1,1)



#           Criterion 1: If new Frac initiate at the other end
DC = 'C1'   # For coloring 
ax.plot(-1000,1000,color=DC,label='HF Initiate') 
ax.contour(RE_01.x, RE_01.y, RE_01.Fail_1,[0.5, 1],colors=DC,linewidth=0.1)
ax.contourf(RE_01.x, RE_01.y, RE_01.Fail_1, [0.5, 1], cmap=plt.cm.Oranges)


#                         Criterion 2: If NF open
DC = 'C2'   # For coloring 
ax.plot(-1000,1000,color=DC,label='NF Reopen') 
ax.contour(RE_01.x, RE_01.y, RE_01.Fail_2,[0.5, 1],colors=DC,linewidth=0.1)
ax.contourf(RE_01.x, RE_01.y, RE_01.Fail_2, [0.5, 1], cmap=plt.cm.Greens)

#                         Criterion 3: If NF slip 
DC = 'C0'   # For coloring 
ax.plot(-1000,1000,color=DC,label='NF Slip') 
ax.contour(RE_01.x, RE_01.y, RE_01.Fail_3,[0.5, 1],colors=DC,linewidth=0.1)
ax.contourf(RE_01.x, RE_01.y, RE_01.Fail_3, [0.5, 1], cmap=plt.cm.Blues)

#                             PLOTTING
ax.set_title('Failure Modes Around Hydraulic Fracture',fontsize=14) 
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
phyl_ax=fig.add_axes([0.7, 0.1, 0.25, 0.25])
#  list of [left, bottom, width, height] values in 0-1 relative figure coordinates:
phyl_ax.get_xaxis().set_visible(False)
phyl_ax.get_yaxis().set_visible(False)
phyl_ax.spines['bottom'].set_color('none')
phyl_ax.spines['top'].set_color('none')
phyl_ax.spines['left'].set_color('none')
phyl_ax.spines['right'].set_color('none')
phyl_ax.set_facecolor('none')
phyl_ax.imshow(im,interpolation='nearest')


plt.savefig(save_plots_to+'b_3modes_all_%.0f.png'%beta, dpi=300)

print(timeit.default_timer() - start_time)