#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 15:20:37 2020

@author: Peidong
"""

import numpy as np
import matplotlib.pyplot as plt
from Func_c_SlipZoneArea import *
import timeit

start_time = timeit.default_timer()

import os
save_plots_to = str(os.getcwd()) + '/Plots/'

fig_name = 'c_06_Half_length.png'

##############################################################################
##############################################################################
TVD = 3300
FG = 0.022;     S2 = TVD*FG;     k = 0.88;   S1 = S2/k# KPa/m
PG =0.0098;     OverPress = 1.8;      P_pore = TVD*PG*OverPress # KPa/m

miu  = 0.4;

K1 = 4*(np.pi*10)**0.5

half_length = np.arange(10,160,5)


##############################################################################
##############################################################################
fig, (ax1,ax2,ax3) = plt.subplots(3, 1,figsize=(7, 8),\
                                                    constrained_layout=True)
##############################################################################
beta = 0;  

y_wide = 2            
x_wide = 1
delta = 0.005;  
num_case = 0;
tp = ax1
for j in half_length:
    
    P_net = K1/(np.pi*j)**0.5
    RE_01 = FractureStress(j,S1,S2,P_net,beta,miu,P_pore,delta,x_wide,y_wide)
    
    DC = 'C'+str(num_case)
    tp.plot(-1000,1000,color=DC,label='$\mu$ = '+str(miu)) # For coloring of the legend line
    tp.contour(RE_01.x, RE_01.y, RE_01.Fail_PSZ,[0.9, 1],linewidth=0.01,colors=DC)
    tp.contourf(RE_01.x, RE_01.y, RE_01.Fail_PSZ, [0.5, 1], colors=DC)
    num_case += 1

tp.set_title('$\\beta$ = %.0f$^\circ$'%beta, fontsize=12,color='C3')
tp.set_ylabel('y (m)',rotation=90, fontsize=10)
tp.plot([0,max(half_length)],[0,0],'k-',linewidth=1)
tp.set_ylim(-y_wide,y_wide)
tp.set_xlim(0,160)
##############################################################################
beta = 30;  

y_wide = 7            
x_wide = 4
delta = 0.02;  
num_case = 0;
tp = ax2
for j in half_length:
    
    P_net = K1/(np.pi*j)**0.5
    RE_01 = FractureStress(j,S1,S2,P_net,beta,miu,P_pore,delta,x_wide,y_wide)
    
    DC = 'C'+str(num_case)
    tp.plot(-1000,1000,color=DC,label='$\mu$ = '+str(miu)) # For coloring of the legend line
    tp.contour(RE_01.x, RE_01.y, RE_01.Fail_PSZ,[0.9, 1],linewidth=0.01,colors=DC)
    tp.contourf(RE_01.x, RE_01.y, RE_01.Fail_PSZ, [0.5, 1], colors=DC)
    num_case += 1

tp.set_title('$\\beta$ = %.0f$^\circ$'%beta, fontsize=12,color='C4')
tp.set_ylabel('y (m)',rotation=90, fontsize=10)
tp.plot([0,max(half_length)],[0,0],'k-',linewidth=1)
tp.set_ylim(-y_wide,y_wide)
tp.set_xlim(0,160)
##############################################################################
beta = 60;  

y_wide = 2.5             
x_wide = 1.5
delta = 0.02;   
num_case = 0;
tp = ax3
for j in half_length:
    
    P_net = K1/(np.pi*j)**0.5
    RE_01 = FractureStress(j,S1,S2,P_net,beta,miu,P_pore,delta,x_wide,y_wide)
    
    DC = 'C'+str(num_case)
    tp.plot(-1000,1000,color=DC,label='$\mu$ = '+str(miu)) # For coloring of the legend line
    tp.contour(RE_01.x, RE_01.y, RE_01.Fail_PSZ,[0.9, 1],linewidth=0.01,colors=DC)
    tp.contourf(RE_01.x, RE_01.y, RE_01.Fail_PSZ, [0.5, 1], colors=DC)
    num_case += 1
    
tp.set_title('$\\beta$ = %.0f$^\circ$'%beta, fontsize=12,color='C1')
tp.set_ylabel('y (m)',rotation=90, fontsize=10)
tp.plot([0,max(half_length)],[0,0],'k-',linewidth=1)
tp.set_ylim(-y_wide,y_wide)
tp.set_xlim(0,160)
tp.set_xlabel('x (m)', fontsize=10)
##############################################################################
ax1.xaxis.set_ticklabels([])
ax2.xaxis.set_ticklabels([])

ax1.grid(which='major', linestyle=':')
ax2.grid(which='major', linestyle=':')
ax3.grid(which='major', linestyle=':')

text = ('\
FG  = %.0f kPa/m\n\
HG  = %.1f kPa/m\n\
PG  = %.1f*HG\n\
TVD = 3300 m\n\
S$_{2}$ = %d MPa\n\
S$_{2}$/S$_{1}$ = %.2F\n\
P$_{p}$ = %.0f MPa\n\
$\\mu$ = %.1f\n\
K$_{1}$ = %.d MPa$\sqrt{m}$'\
        %(FG*1000,PG*1000,OverPress,S2,k,P_pore,miu,K1))
    
props = dict(boxstyle='round', facecolor='whitesmoke', alpha=0.9, edgecolor='none')     
fig.text(1, 0.25, text,bbox=props,fontsize=10)


im = plt.imread('Rel_Angl.png')
phyl_ax=fig.add_axes([1, 0.63, 0.2, 0.2])
#  list of [left, bottom, width, height] values in 0-1 relative figure coordinates:
phyl_ax.get_xaxis().set_visible(False)
phyl_ax.get_yaxis().set_visible(False)
phyl_ax.spines['bottom'].set_color('none')
phyl_ax.spines['top'].set_color('none')
phyl_ax.spines['left'].set_color('none')
phyl_ax.spines['right'].set_color('none')
phyl_ax.set_facecolor('none')
phyl_ax.imshow(im,interpolation='nearest')

fig.suptitle('Potential Slip Zone',fontsize=14)
plt.subplots_adjust(left=0.0, bottom=0.0, right=0.98, top=0.91, wspace=0, hspace=0.25)

plt.savefig( save_plots_to+fig_name, dpi=300, bbox_inches="tight")
print('Computing Time = %.2f sec'%(timeit.default_timer() - start_time))
