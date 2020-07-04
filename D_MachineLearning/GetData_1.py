'''
This function is copied from 
/Users/Peidong/0_Python_Code/Dissertation_HFNF_PSZ/C_SlipZoneArea/Func_c_SlipZoneArea.py
'''
import timeit
start_time = timeit.default_timer()

import numpy as np
import random
# import matplotlib.pyplot as plt                             # for plotting
import pandas as pd                                         # DataFrames
np.warnings.filterwarnings('ignore')

class FractureStress(object):
    def __init__(self,half_length,S1,S2,P_net,beta,miu,P_pore,delta,x_wide,y_wide):
        self.S1 = S1; self.S2 = S2; 
        self.P_net = P_net; self.a = half_length; 
        self.delta = delta; 
        self.L_x = x_wide; self.L_y = y_wide;
        self.beta  = beta*(np.pi/180) # w.r.t HF, counterclockwise, ranging 0 to 180
        self.miu   = miu              # friction coefficient
        self.P_pore=P_pore  
        
        self.CFF()
        
    def grid_block(self):
        self.center_line_num = self.L_y/self.delta+1
        self.num_dx = int(2*self.L_x/self.delta+1)
        self.num_dy = int(2*self.L_y/self.delta+1)
        self.xrange = np.linspace(self.a-self.L_x, self.a+self.L_x, self.num_dx)
        # self.xrange = np.linspace(0, self.a+self.L_x, self.num_dx) 
        self.yrange = np.linspace(-self.L_y, self.L_y, self.num_dy)
        self.x, self.y = np.meshgrid(self.xrange,self.yrange)
        
    def myatan(self,x,y):
        value = np.arctan2(y,x)
        value[value<0] += 2*np.pi
        return value  
        
    def parameter(self):
        r  = np.sqrt(self.x**2+self.y**2)
        r1 = np.sqrt((self.x-self.a)**2+self.y**2)
        r2 = np.sqrt((self.x+self.a)**2+self.y**2)
        th = self.myatan(self.x,self.y)
        th1= self.myatan(self.x-self.a,self.y)
        th2= self.myatan(self.x+self.a,self.y)
        self.c  = np.nan_to_num( self.P_net*r/np.sqrt(r1*r2) )
        self.c1 = np.cos(th-0.5*(th1+th2)) 
        self.c2 = np.nan_to_num( self.a**2/(r1*r2)*np.sin(th)*np.sin(1.5*(th1+th2)) )
        self.c3 = np.nan_to_num( self.a**2/(r1*r2)*np.sin(th)*np.cos(1.5*(th1+th2)) )
        
    def stresses(self):
        self.grid_block()
        self.parameter()
        self.sig11 = self.c*(self.c1-self.c2)-self.P_net-self.S1
        self.sig22 = self.c*(self.c1+self.c2)-self.P_net-self.S2
        self.sig12 = self.c*self.c3

    def CFF(self):  
        self.stresses()
        s11_plus_s22 = self.sig11+self.sig22
        s11_min_s22  = self.sig11-self.sig22
        s22_min_s11  = self.sig22-self.sig11
        TwoBeta = 2*self.beta     
        # normal stress acting on the plane
        self.sigma = 0.5*(s11_plus_s22)-0.5*(s11_min_s22)*np.cos(TwoBeta)-self.sig12*np.sin(TwoBeta) 
        # maximum principal stress
        self.P1 = 0.5*(s11_plus_s22)+((0.5*(s11_min_s22))**2+self.sig12**2)**0.5
        # self.eff_sigma = np.absolute(self.sigma+self.P_pore) 
        self.eff_sigma = -(self.sigma+self.P_pore)
        self.tau   = np.absolute(0.5*(s22_min_s11)*np.sin(TwoBeta)+self.sig12*np.cos(TwoBeta))
        
        # Criterion 1: If new Frac initiate at the other end, Gu and Weng (2010)
        self.Fail_1 = self.P1+self.P_pore
        self.Fail_1[self.Fail_1 >= 0] = 1 # Meaning New HF initiate
        self.Fail_1[self.Fail_1 <  0] = 0 
        
        # Criterion 2: If NF open      
        self.Fail_2 = self.sigma+self.P_pore
        self.Fail_2[self.Fail_2 >= 0] = 1 # Meaning NF open
        self.Fail_2[self.Fail_2 <  0] = 0
        
        # Criterion 3: If NF slip 
        self.Fail_3 = self.tau - self.eff_sigma*self.miu 
        
        self.Fail_3[self.Fail_3 >= 0] = 1 # Meaning NF slip
        self.Fail_3[self.Fail_3 <  0] = 0 # Meaning ok
        self.Fail_3[self.Fail_2 == 1] = 0 # IF effective stress is tensile, 
        
        # Final: Potential Slip: if C3 meets while C1,C2 not meet           
        self.Fail_PSZ = np.full_like(self.Fail_3, 0)
        self.Fail_PSZ[self.Fail_3 == 1] = 1
        self.Fail_PSZ[self.Fail_1 == 1] = 0
                    
        self.area = np.count_nonzero(self.Fail_PSZ)*self.delta**2
#########################################################################################################
##########################################################################################################

def get_random(min_val,max_val,nums_of_points):
    np.random.seed([88990])
    rand_numbers = np.random.uniform(size=nums_of_points)
    rand_numbers = rand_numbers*(max_val-min_val)+min_val
    return rand_numbers

# plt.plot(get_random(3500,3550,100));

# a = get_random(5500,5550,10)
# b = get_random(300,250,10)
# c = get_random(30,39,10)
# dataset = pd.DataFrame({'A': a, 'B': b,'C': c})
# dataset.head(10)

#########################################################################################################
##########################################################################################################


num_cases = 10000

FG        = get_random(0.014,0.022,num_cases)
k         = get_random(0.88,1,num_cases)
beta      = get_random(0,90,num_cases)
TVD       = get_random(2900,3300,num_cases)
OverPress = get_random(1.4,1.8,num_cases)
miu       = get_random(0.4,0.8,num_cases)
P_net     = get_random(1,5,num_cases)
 

S2 = TVD*FG;     S1 = S2/k# KPa/m
P_pore = TVD*0.0098*OverPress # KPa/m

half_length = 10;      
y_wide = 5             
x_wide = 3
delta = 0.01;  

area = np.empty_like(beta)
for i in range(num_cases):
    RE = FractureStress(half_length,S1[i],S2[i],beta[i],P_net[i],miu[i],P_pore[i],delta,x_wide,y_wide)
    area[i] = RE.area

HFNF_PSZ_area = pd.DataFrame({'FG':FG,'K':k,'beta':beta,'TVD':TVD,'OverPress':OverPress,'miu':miu,'P_net':P_net,'Area':area})

HFNF_PSZ_area.to_csv(path_or_buf='HFNF_PSZ_area_RESULTS_1.csv')

print('Computing Time = %.2f sec'%(timeit.default_timer() - start_time))