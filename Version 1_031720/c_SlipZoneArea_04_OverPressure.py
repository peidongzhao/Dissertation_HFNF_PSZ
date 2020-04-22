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
##############################################################################
##############################################################################
plt.figure(figsize=(7, 5))  

half_length = 10;      
y_wide = 5             
x_wide = 5
delta = 0.02;      

# Stress Inputs
P_net = 4

miu    = 0.4
K1 =P_net*(np.pi*half_length)**0.5

fig = plt.figure(figsize=(7.5, 5),facecolor='white')
ax = fig.add_subplot(1,1,1)

beta   = np.arange(0.,91., 15.)
k   =  0.88
##############################################################################
##############################################################################
TVD = 3300
FG = 0.022;     
PG =0.0098;
S2 = TVD*FG;
S1 = S2/k 
OverPress = np.linspace(1.4, 1.8, 5)  

num_S_diff = 0
for j in OverPress:

    P_pore = TVD*PG*j 
    
    num_beta = 0 
    area = np.empty_like(beta)
    
    for i in beta:  
        
        RE = FractureStress(half_length,S1,S2,P_net,i,miu,P_pore,delta,x_wide,y_wide)
        area[num_beta] = RE.area
        num_beta += 1 
               
    DC = 'C'+str(num_S_diff)
    plt.plot(beta,area,color=DC,label='P.G = %.1f*H.G'%j)
    xmax = beta[np.argmax(area)]
    ymax = area.max()
    plt.plot(xmax,ymax,'r*')
    num_S_diff += 1
    print(num_S_diff)

text = ('\
F.G = %.0f kPa/m\n\
H.G = %.1f kPa/m\n\
S$_{2}$ = %d MPa\n\
S$_{2}$/S$_{1}$ = %.2F\n\
a = %.0f m\n\
P$_{net}$ = %.0f MPa\n\
K$_{1}$ = %.1f MPa$\sqrt{m}$\n\
$\\mu$ = %.1f'\
        %(FG*1000,PG*1000,S2,k,half_length,P_net,K1,miu))
props = dict(boxstyle='round', facecolor='whitesmoke', alpha=0.9, edgecolor='none')     
fig.text(0.72, 0.33, text,bbox=props,fontsize=10)

plt.title("Area of Potential Slip Zone",fontsize=14,fontweight='bold')
plt.ylabel('Area (m$^2$)',rotation=90, fontsize=12)
plt.xlabel('Relative Angle ('+chr(176)+')' , fontsize=12)
ax.set_facecolor('cornsilk')

plt.xticks(np.linspace(0,90,7))
plt.xlim(0,90)
plt.ylim(0,8)
plt.grid(which='major', linestyle='-')
plt.grid(which='minor', linestyle=':') 
plt.legend(loc='upper right',shadow=True, fontsize=10)

plt.savefig( save_plots_to+'c_04_OverPressureIndex_1.png', dpi=300)

