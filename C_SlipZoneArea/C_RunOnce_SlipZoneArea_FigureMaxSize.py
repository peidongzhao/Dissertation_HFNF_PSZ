#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validated on Mar 17 2020
@author: Peidong
"""
import numpy as np
import matplotlib.pyplot as plt
from Func_c_SlipZoneArea_xdx import *
import timeit

start_time = timeit.default_timer()

##############################################################################
############################################################################## 
y_wide = 0.5            
x_wide = 0.2
delta = 0.01;  
  
beta = 90;   


TVD = 3300
FG = 0.022;     S2 = TVD*FG;     k = 0.88;   S1 = S2/k# KPa/m
PG =0.0098;     OverPress = 1.8;      P_pore = TVD*PG*OverPress # KPa/m


K1 = 4*(np.pi*10)**0.5




fig = plt.figure(figsize=(5/0.8, 5),facecolor='white')
ax = fig.add_subplot(1,1,1)

half_length = 150
P_net = K1/(np.pi*half_length)**0.5


miu  = 0.4;
RE_01 = FractureStress(half_length,S1,S2,P_net,beta,miu,P_pore,delta,x_wide,y_wide)
DC = 'C1'
ax.plot(-1000,1000,color=DC,label='$\mu$ = '+str(miu)) # For coloring of the legend line
ax.contour(RE_01.x, RE_01.y, RE_01.Fail_PSZ,[0.9, 1],colors=DC,linewidth=0.1)
# ax.contourf(RE_01.x, RE_01.y, RE_01.Fail_PSZ, [0.5, 1], cmap=plt.cm.Oranges)

# Plot label =======================================================

ax.set_title('Potential Slip Zone',fontsize=14,fontweight='bold') #\nEffect of Frictional Coefficient 
ax.set_ylabel('y (m)',rotation=90, fontsize=12)
ax.set_xlabel('x (m)', fontsize=12)

ax.set_ylim(-y_wide,y_wide)
ax.set_xlim(half_length-x_wide,half_length+x_wide)

ax.grid(which='major', linestyle=':')
ax.set_facecolor('cornsilk')

text = ('\
a   = %.0f m\n\
S$_{1}$ = %d MPa\n\
S$_{2}$ = %d MPa\n\
P$_{p}$ = %d MPa\n\
P$_{n}$ = %.3f MPa\n\
K$_{1}$ = %.1f MPa$\sqrt{m}$\n\
$\\beta$  = %d$^\circ$'\
        %(half_length,S1,S2,P_pore,P_net,K1,beta))
props = dict(boxstyle='round', facecolor='whitesmoke', alpha=0.8, edgecolor='none')        
fig.text(0.14,0.15, text, size=12,bbox=props,fontsize=12)

print(RE_01.area)
print('Computing Time = %.2f sec'%(timeit.default_timer() - start_time))