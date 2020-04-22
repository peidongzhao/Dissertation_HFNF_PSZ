#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validated on Mar 17 2020
@author: Peidong
"""

import timeit
import os
import numpy as np
import matplotlib.pyplot as plt
from b_SlipZoneFunc_1 import *

save_plots_to = '/Users/Peidong/0_Python_Code/Slip_SumAll/Plots/'
fig_name = 'c_04_OverPressureIndex_2.png'

start_time = timeit.default_timer()
##############################################################################
########################       Relative Angle       ##########################
##############################################################################
plt.figure(figsize=(7, 5))  

half_length = 10;      
y_wide = 5             
x_wide = 5
delta = 0.02;      

# Stress Inputs
P_net = 4

TVD = 3300
FG = 0.022;     S2 = TVD*FG; # KPa/m
PG =0.0098;     OverPress = 1.8;      P_pore = TVD*PG*OverPress # KPa/m

miu    = 0.4
K1 =P_net*(np.pi*half_length)**0.5

fig = plt.figure(figsize=(7.5, 5),facecolor='white')
ax = fig.add_subplot(1,1,1)

beta   = np.arange(0.,91., 1.)
k   =  np.linspace(0.88, 1, 5)

num_S_diff = 0
Saving_Area = np.empty([k.size, beta.size])

for j in k:
    
    S1 = S2/j   # MPa
    num_beta = 0 
    area = np.empty_like(beta)
    
    for i in beta:  
        
        RE = FractureStress(half_length,S1,S2,P_net,i,miu,P_pore,delta,x_wide,y_wide)
        area[num_beta] = RE.area
        num_beta += 1 
               
    Saving_Area[num_S_diff,:] = area
    DC = 'C'+str(num_S_diff)
    plt.plot(beta,area,color=DC,label='S$_{2}$/S$_{1}$ = %0.2f'%j)
    xmax = beta[np.argmax(area)]
    ymax = area.max()
    plt.plot(xmax,ymax,'ro')
    num_S_diff += 1
    print(xmax)

text = ('\
F.G = %.0f kPa/m\n\
H.G = %.1f kPa/m\n\
P.G  = %.1f*H.G\n\
S$_{2}$ = %d MPa\n\
P$_{p}$ = %d MPa\n\
a = %.0f m\n\
P$_{net}$ = %.0f MPa\n\
K$_{1}$ = %.1f MPa$\sqrt{m}$\n\
$\\mu$ = %.1f'\
        %(FG*1000,PG*1000,OverPress,S2,P_pore,half_length,P_net,K1,miu))
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

plt.savefig( save_plots_to+'c_01_RelAngle_stressDiff_1.png', dpi=300)

##############################################################################
########################     Depth, Confine Stress  ##########################
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

beta   = np.arange(0.,91., 1.)
k   =  0.88

TVD = np.linspace(2800, 3300, 6)
FG = 0.022;     
PG =0.0098;     OverPress = 1.8;      
P_pore = 0; S2 = 0; S1 = 0
num_S_diff = 0
for j in TVD:
    
    S2 = j*FG;
    S1 = S2/k
    P_pore = j*PG*OverPress 
    
    num_beta = 0 
    area = np.empty_like(beta)
    
    for i in beta:  
        
        RE = FractureStress(half_length,S1,S2,P_net,i,miu,P_pore,delta,x_wide,y_wide)
        area[num_beta] = RE.area
        num_beta += 1 
               
    DC = 'C'+str(num_S_diff)
    plt.plot(beta,area,color=DC,label='S$_{2}$ = %.0f MPa @ %.0f m'%(S2,j))
    xmax = beta[np.argmax(area)]
    ymax = area.max()
    plt.plot(xmax,ymax,'ro')
    num_S_diff += 1
    print(xmax)

text = ('\
F.G = %.0f kPa/m\n\
H.G = %.1f kPa/m\n\
P.G  = %.1f*H.G\n\
S$_{2}$/S$_{1}$ = %.2F\n\
a = %.0f m\n\
P$_{net}$ = %.0f MPa\n\
K$_{1}$ = %.1f MPa$\sqrt{m}$\n\
$\\mu$ = %.1f'\
        %(FG*1000,PG*1000,OverPress,k,half_length,P_net,K1,miu))
props = dict(boxstyle='round', facecolor='whitesmoke', alpha=0.9, edgecolor='none')     
fig.text(0.72, 0.33, text,bbox=props,fontsize=10)

plt.title("Area of Potential Slip Zone",fontsize=14,fontweight='bold')
plt.ylabel('Area (m$^2$)',rotation=90, fontsize=12)
plt.xlabel('Relative Angle ('+chr(176)+')' , fontsize=12)
ax.set_facecolor('cornsilk')

plt.xticks(np.linspace(0,90,7))
plt.xlim(0,90)
plt.ylim(0,12)
plt.grid(which='major', linestyle='-')
plt.grid(which='minor', linestyle=':') 
plt.legend(loc='upper right',shadow=True, fontsize=10)

plt.savefig( save_plots_to+'c_02_ConfStress_Depth_1.png', dpi=300)

# for low stress differential conditon, 
# the relative angle does not have a major influence

##############################################################################
########################         Net Pressure       ##########################
##############################################################################
plt.figure(figsize=(7, 5))  

half_length = 10;      
y_wide = 5             
x_wide = 5
delta = 0.02;      

# Stress Inputs
P_net = np.linspace(2, 10, 5)
miu    = 0.4

fig = plt.figure(figsize=(7.5, 5),facecolor='white')
ax = fig.add_subplot(1,1,1)

beta   = np.arange(0.,91., 1.)
k   =  0.88
TVD = 3300
FG = 0.022;     
PG =0.0098;     OverPress = 1.8;   

S2 = TVD*FG;    S1 = S2/k
P_pore = TVD*PG*OverPress 
##############################################################################
num_S_diff = 0
for j in P_net:
    
    K1 = j*(np.pi*half_length)**0.5
    num_beta = 0 
    area = np.empty_like(beta)
    
    for i in beta:  
        
        RE = FractureStress(half_length,S1,S2,j,i,miu,P_pore,delta,x_wide,y_wide)
        area[num_beta] = RE.area
        num_beta += 1 
               
    DC = 'C'+str(num_S_diff)
    plt.plot(beta,area,color=DC,label='P$_{net}$ = %.0f MPa, K$_{1}$ = %.0f MPa$\sqrt{m}$'%(j,K1))
    xmax = beta[np.argmax(area)]
    ymax = area.max()
    plt.plot(xmax,ymax,'ro')
    num_S_diff += 1
    print(xmax)

text = ('\
F.G = %.0f kPa/m\n\
H.G = %.1f kPa/m\n\
P.G  = %.1f*H.G\n\
S$_{2}$ = %d MPa\n\
S$_{2}$/S$_{1}$ = %.2F\n\
a = %.0f m\n\
$\\mu$ = %.1f'\
        %(FG*1000,PG*1000,OverPress,S2,k,half_length,miu))
props = dict(boxstyle='round', facecolor='whitesmoke', alpha=0.9, edgecolor='none')     
fig.text(0.72, 0.33, text,bbox=props,fontsize=10)

plt.title("Area of Potential Slip Zone",fontsize=14,fontweight='bold')
plt.ylabel('Area (m$^2$)',rotation=90, fontsize=12)
plt.xlabel('Relative Angle ('+chr(176)+')' , fontsize=12)
ax.set_facecolor('cornsilk')

plt.xticks(np.linspace(0,90,7))
plt.xlim(0,90)
# plt.ylim(0,8)
plt.grid(which='major', linestyle='-')
plt.grid(which='minor', linestyle=':') 
plt.legend(loc='upper right',shadow=True, fontsize=10)

plt.savefig( save_plots_to+'c_03_P_net_1.png', dpi=300)

##############################################################################
########################         Over-Pressure      ##########################
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

beta   = np.arange(0.,91., 1.)
k   =  0.88
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
    plt.plot(xmax,ymax,'ro')
    print(xmax)
    
    num_S_diff += 1
    


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

plt.savefig( save_plots_to+fig_name, dpi=300)


print(timeit.default_timer() - start_time)