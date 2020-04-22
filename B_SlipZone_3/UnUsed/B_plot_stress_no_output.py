#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 16:54:00 2020

@author: Peidong
"""

import numpy as np
import matplotlib.pyplot as plt
from Func_b_SlipZone import *
import timeit

##############################################################################
#                  Changing beta, the angle between HF and NF
##############################################################################
beta = 30;
y_wide = 5;           x_wide = 5

delta = 0.01;       
half_length = 10;    
S1 = 51;             S2 = 60*0.8;              P_net = 4
P_pore = 35
K1 =P_net*(np.pi*half_length)**0.5


#                             PLOTTING
miu  = 0.6;
RE_01 = FractureStress(half_length,S1,S2,P_net,beta,miu,P_pore,delta,x_wide,y_wide)


fig = plt.figure(figsize=(6.25, 5),facecolor='white')
ax1 = fig.add_subplot(1,1,1)


ax1.contour(RE_01.x, RE_01.y, RE_01.eff_sigma, levels=14, linewidths=0.5, colors='k')
cntr1 = ax1.contourf(RE_01.x, RE_01.y, RE_01.eff_sigma, levels=14, cmap="RdBu_r")

fig.colorbar(cntr1, ax=ax1)

fig, ((ax1)) = plt.subplots(1, 1,figsize=(7, 8))
    
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
