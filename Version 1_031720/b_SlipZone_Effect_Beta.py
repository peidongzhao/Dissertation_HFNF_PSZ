#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validated on Mar 17 2020
@author: Peidong
"""

save_plots_to = '/Users/Peidong/0_Python_Code/Slip_SumAll/Plots/'

import numpy as np
import matplotlib.pyplot as plt
from b_SlipZoneFunc import *
# from b_SlipZoneFunc_v2 import *

##############################################################################
#                       Effect of Relative Angle, Beta
##############################################################################

delta = 0.0005;       y_wide = 0.3;           x_wide = 0.3
half_length = 10;    
S1 = 60;             S2 = 55;              P_net = 2
miu  = 0.4;          P_pore = 35
K1 =P_net*(np.pi*half_length)**0.5


####################################################################################
####################################################################################

fig, ((ax1,ax2),(ax3,ax4),(ax5,ax6)) = plt.subplots(3, 2,figsize=(7, 8),\
                                                    constrained_layout=True)
fig.suptitle('Potential Slip Zone',fontsize=14,fontweight='bold')

##############  0.0 degree ##############
beta = 0;
RE_01 = FractureStress(half_length,S1,S2,P_net,beta,miu,P_pore,delta,x_wide,y_wide)
DC = 'C3'
ax1.plot(10,0,color=DC,label='Rel. Angle = '+str(beta)+chr(176)) # For coloring of the legend line
ax1.contour(RE_01.x, RE_01.y, RE_01.Fail_PSZ,levels=[1],colors=DC,linewidth=0.1)
ax1.contourf(RE_01.x, RE_01.y, RE_01.Fail_PSZ,levels=[0.8,1], cmap=plt.cm.Reds)
# Plot label =======================================================
tp = ax1
tp.set_title('$\\beta$ = %.0f$^\circ$'%beta, fontsize=14,color=DC)
tp.set_ylabel('y (m)',rotation=90, fontsize=12)
# tp.set_xlabel('x (m)', fontsize=12)
tp.plot([0,half_length],[0,0],'k-',linewidth=1)
tp.set_ylim(-y_wide,y_wide)
tp.set_xlim(half_length-x_wide,half_length+x_wide)
tp.set_xticks(np.linspace(half_length-x_wide,half_length+x_wide,5))
tp.set_yticks(np.linspace(-y_wide,y_wide,5))
tp.grid(which='major', linestyle=':')
tp.set_facecolor('cornsilk')

##############  90 degree ##############
beta = 90;
RE_01 = FractureStress(half_length,S1,S2,P_net,beta,miu,P_pore,delta,x_wide,y_wide)
DC = 'C0'
ax2.plot(-1000,1000,color=DC,label='Rel. Angle = '+str(beta)+chr(176)) # For coloring of the legend line
ax2.contour(RE_01.x, RE_01.y, RE_01.Fail_PSZ,[0.5, 1],colors=DC,linewidth=0.1)
ax2.contourf(RE_01.x, RE_01.y, RE_01.Fail_PSZ, [0.5, 1], cmap=plt.cm.Blues)
# Plot label =======================================================
tp = ax2
tp.set_title('$\\beta$ = %.0f$^\circ$'%beta, fontsize=14,color=DC)
# tp.set_ylabel('y (m)',rotation=90, fontsize=12)
# tp.set_xlabel('x (m)', fontsize=12)
tp.plot([0,half_length],[0,0],'k-',linewidth=1)
tp.set_ylim(-y_wide,y_wide)
tp.set_xlim(half_length-x_wide,half_length+x_wide)
tp.set_xticks(np.linspace(half_length-x_wide,half_length+x_wide,5))
tp.set_yticks(np.linspace(-y_wide,y_wide,5))
tp.grid(which='major', linestyle=':')
tp.set_facecolor('cornsilk')

##############  30 degree ##############
beta = 30;
RE_01 = FractureStress(half_length,S1,S2,P_net,beta,miu,P_pore,delta,x_wide,y_wide)
DC = 'C1'
ax3.plot(-1000,1000,color=DC,label='Rel. Angle = '+str(beta)+chr(176)) # For coloring of the legend line
ax3.contour(RE_01.x, RE_01.y, RE_01.Fail_PSZ,[0.5, 1],colors=DC,linewidth=0.1)
ax3.contourf(RE_01.x, RE_01.y, RE_01.Fail_PSZ, [0.5, 1], cmap=plt.cm.Oranges)
# Plot label =======================================================
tp = ax3
tp.set_title('$\\beta$ = %.0f$^\circ$'%beta, fontsize=14,color=DC)
tp.set_ylabel('y (m)',rotation=90, fontsize=12)
# tp.set_xlabel('x (m)', fontsize=12)
tp.plot([0,half_length],[0,0],'k-',linewidth=1)
tp.set_ylim(-y_wide,y_wide)
tp.set_xlim(half_length-x_wide,half_length+x_wide)
tp.set_xticks(np.linspace(half_length-x_wide,half_length+x_wide,5))
tp.set_yticks(np.linspace(-y_wide,y_wide,5))
tp.grid(which='major', linestyle=':')
tp.set_facecolor('cornsilk')

##############  60 degree ##############
beta = 60;
RE_01 = FractureStress(half_length,S1,S2,P_net,beta,miu,P_pore,delta,x_wide,y_wide)
DC = 'C4'
ax4.plot(-1000,1000,color=DC,label='Rel. Angle = '+str(beta)+chr(176)) # For coloring of the legend line
ax4.contour(RE_01.x, RE_01.y, RE_01.Fail_PSZ,[0.5, 1],colors=DC,linewidth=0.1)
ax4.contourf(RE_01.x, RE_01.y, RE_01.Fail_PSZ, [0.5, 1], cmap=plt.cm.Purples)
# Plot label =======================================================
tp = ax4
tp.set_title('$\\beta$ = %.0f$^\circ$'%beta, fontsize=14,color=DC)
# tp.set_ylabel('y (m)',rotation=90, fontsize=12)
# tp.set_xlabel('x (m)', fontsize=12)
tp.plot([0,half_length],[0,0],'k-',linewidth=1)
tp.set_ylim(-y_wide,y_wide)
tp.set_xlim(half_length-x_wide,half_length+x_wide)
tp.set_xticks(np.linspace(half_length-x_wide,half_length+x_wide,5))
tp.set_yticks(np.linspace(-y_wide,y_wide,5))
tp.grid(which='major', linestyle=':')
tp.set_facecolor('cornsilk')

##############  45 degree ##############
beta = 45;
RE_01 = FractureStress(half_length,S1,S2,P_net,beta,miu,P_pore,delta,x_wide,y_wide)
DC = 'C7'
ax5.plot(-1000,1000,color=DC,label='Rel. Angle = '+str(beta)+chr(176)) # For coloring of the legend line
ax5.contour(RE_01.x, RE_01.y, RE_01.Fail_PSZ,[0.5, 1],colors=DC,linewidth=0.1)
ax5.contourf(RE_01.x, RE_01.y, RE_01.Fail_PSZ, [0.5, 1], cmap=plt.cm.Greys)
# Plot label =======================================================
tp = ax5
tp.set_title('$\\beta$ = %.0f$^\circ$'%beta, fontsize=14,color=DC)
tp.set_ylabel('y (m)',rotation=90, fontsize=12)
tp.set_xlabel('x (m)', fontsize=12)
tp.plot([0,half_length],[0,0],'k-',linewidth=1)
tp.set_ylim(-y_wide,y_wide)
tp.set_xlim(half_length-x_wide,half_length+x_wide)
tp.set_xticks(np.linspace(half_length-x_wide,half_length+x_wide,5))
tp.set_yticks(np.linspace(-y_wide,y_wide,5))
tp.grid(which='major', linestyle=':')
tp.set_facecolor('cornsilk')

##############  -45 degree ##############
beta = -45;
RE_01 = FractureStress(half_length,S1,S2,P_net,beta,miu,P_pore,delta,x_wide,y_wide)
DC = 'C2'
ax6.plot(-1000,1000,color=DC,label='Rel. Angle = '+str(beta)+chr(176)) # For coloring of the legend line
ax6.contour(RE_01.x, RE_01.y, RE_01.Fail_PSZ,[0.5, 1],colors=DC,linewidth=0.1)
ax6.contourf(RE_01.x, RE_01.y, RE_01.Fail_PSZ, [0.5, 1], cmap=plt.cm.Greens)
# Plot label =======================================================
tp = ax6
tp.set_title('$\\beta$ = %.0f$^\circ$'%beta, fontsize=14,color=DC)
# tp.set_ylabel('y (m)',rotation=90, fontsize=12)
tp.set_xlabel('x (m)', fontsize=12)
tp.plot([0,half_length],[0,0],'k-',linewidth=1)
tp.set_ylim(-y_wide,y_wide)
tp.set_xlim(half_length-x_wide,half_length+x_wide)
tp.set_xticks(np.linspace(half_length-x_wide,half_length+x_wide,5))
tp.set_yticks(np.linspace(-y_wide,y_wide,5))
tp.grid(which='major', linestyle=':')
tp.set_facecolor('cornsilk')

ax1.xaxis.set_ticklabels([])
ax2.xaxis.set_ticklabels([])
ax3.xaxis.set_ticklabels([])
ax4.xaxis.set_ticklabels([])

ax2.yaxis.set_ticklabels([])
ax4.yaxis.set_ticklabels([])
ax6.yaxis.set_ticklabels([])

####################################################################################
####################################################################################

# text = ('L$_{h}$ = %.0f m\nP$_{net}$ = %.1f MPa\nS$_{1}$ = %d MPa\
# \nS$_{2}$ = %d MPa\nP$_{pore}$ = %d MPa\
# \n$\\mu$ = %.1f\nK$_{1}$ = %.1f MPa$\sqrt{m}$'\
#         %(half_length,P_net,S1,S2,P_pore,miu,K1))

text = ('\
a  = %.0f m\n\
S$_{1}$ = %d MPa\n\
S$_{2}$ = %d MPa\n\
P$_{p}$ = %d MPa\n\
P$_{n}$ = %.1f MPa\n\
K$_{1}$ = %.1f MPa$\sqrt{m}$\n\
$\\mu$  = %.1f'\
        %(half_length,S1,S2,P_pore,P_net,K1,miu))
props = dict(boxstyle='round', facecolor='whitesmoke', alpha=0.9, edgecolor='none')     
fig.text(0.43, 0.55, text, bbox=props,fontsize=12)


props = dict(boxstyle='round', facecolor='whitesmoke', alpha=0.1, edgecolor='none')     
fig.text(0.13, 0.89, '(A)', bbox=props,fontsize=12)
fig.text(0.92, 0.89, '(B)', bbox=props,fontsize=12)

fig.text(0.13, 0.585, '(C)', bbox=props,fontsize=12)
fig.text(0.92, 0.585, '(D)', bbox=props,fontsize=12)

fig.text(0.13, 0.285, '(E)', bbox=props,fontsize=12)
fig.text(0.92, 0.285, '(F)', bbox=props,fontsize=12)
####################################################################################
####################################################################################
# x-off, y-off relative figure coordinates
im = plt.imread('Rel_Angl.png')
phyl_ax=fig.add_axes([0.76, 0.63, 0.2, 0.2])
#  list of [left, bottom, width, height] values in 0-1 relative figure coordinates:
phyl_ax.get_xaxis().set_visible(False)
phyl_ax.get_yaxis().set_visible(False)
phyl_ax.spines['bottom'].set_color('none')
phyl_ax.spines['top'].set_color('none')
phyl_ax.spines['left'].set_color('none')
phyl_ax.spines['right'].set_color('none')
phyl_ax.set_facecolor('none')
phyl_ax.imshow(im,interpolation='nearest')

# fig, ax = plt.subplots(4, 4, sharex=True, sharey=True)
# 'C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9'
# blue,orange,green,red,purple,brown,pink,gray,olive,cyan



plt.savefig( save_plots_to+'b_03_Effect_Beta.png', dpi=300)