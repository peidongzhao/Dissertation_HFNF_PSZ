#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 16:21:07 2020

@author: Peidong
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validated on Mar 19 2020
@author: Peidong
"""
import numpy as np

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
        # self.xrange = np.linspace(self.a-self.L_x, self.a+self.L_x, self.num_dx) 
        self.xrange = np.linspace(0, self.a+self.L_x, self.num_dx) 
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
        self.sigma = 0.5*(s11_plus_s22)-0.5*(s11_min_s22)*np.cos(TwoBeta)-self.sig12*np.sin(TwoBeta)
        self.eff_sigma = np.absolute(self.sigma+self.P_pore)
        self.tau   = np.absolute(0.5*(s22_min_s11)*np.sin(TwoBeta)+self.sig12*np.cos(TwoBeta))
        
        # Criterion 1: If new Frac initiate at the other end
        self.Fail_1 = self.sig11+self.P_pore
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
        
        # Final: Potential Slip: if C3 meets while C1,C2 not meet         
        
        '''
        rows = self.Fail_1.shape[0]
        cols = self.Fail_1.shape[1]
        self.Fail_PSZ = self.Fail_3
        
        for i in np.arange(0,rows,1):
            for j in np.arange(0,cols,1):

                if self.Fail_3[i,j] == 1:
                    if self.Fail_1[i,j] != 1:
                        if self.Fail_2[i,j] != 1:

                            self.Fail_PSZ[i,j] = 1

                        else:
                            self.Fail_PSZ[i,j] = 0
                    else:
                        self.Fail_PSZ[i,j] = 0
                else:
                    self.Fail_PSZ[i,j] = 0
                    
        '''      
                
        self.Fail_PSZ = np.full_like(self.Fail_3, 0)
        self.Fail_PSZ[self.Fail_3 == 1] = 1
        self.Fail_PSZ[self.Fail_2 == 1] = 0
        self.Fail_PSZ[self.Fail_1 == 1] = 0
                    

        ####################################################################################
        #                      Previous Criterion without THREE CRITERIA
        ####################################################################################
        # self.CFF =  self.tau - self.eff_sigma*self.miu
        # # CFF; negative valued (shear is less than normal); zero if onset of slip
        # self.failure = self.CFF
        # self.failure[self.failure >= 0] = 1 # Meaning failure
        # self.failure[self.failure <  0] = 0 # Meaning ok
        ####################################################################################
        ####################################################################################
        # 
        self.area = np.count_nonzero(self.Fail_PSZ)*self.delta**2
        