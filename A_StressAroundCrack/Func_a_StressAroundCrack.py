import numpy as np

class SingleFractureStress(object):
    def __init__(self, length, S1, S2, P_net, delta, Lx, Ly):
        self.S1 = S1
        self.S2 = S2
        self.P_net = P_net
        self.a = length
        self.delta = delta
        self.Length_x = Lx
        self.Length_y = Ly
        self.grid_block()
        self.stresses()
        
    def grid_block(self):
        self.center_line_num = self.Length_y/self.delta+1
        num_dx = int(self.Length_x/self.delta*2+1)
        num_dy = int(self.Length_y/self.delta*2+1)
        self.xrange = np.linspace(-self.Length_x, self.Length_x, num_dx)
        self.yrange = np.linspace(-self.Length_y, self.Length_y, num_dy)
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
        self.c  = self.P_net*r/np.sqrt(r1*r2)
        self.c1 = np.cos(th-0.5*(th1+th2))
        self.c2 = self.a**2/(r1*r2)*np.sin(th)*np.sin(1.5*(th1+th2))
        self.c3 = self.a**2/(r1*r2)*np.sin(th)*np.cos(1.5*(th1+th2))
    
    def TipRemoval(self,value):
        value[value==float('inf')] = 0
        value[value==float('-inf')] = 0
        temp = np.argwhere(np.isnan(value))
        value[temp[0,0],temp[0,1]] = 0
        return value
    
    def stresses(self):
        self.parameter()
        self.sig11 = self.c*(self.c1-self.c2)-self.P_net-self.S1
        self.sig22 = self.c*(self.c1+self.c2)-self.P_net-self.S2
        self.sig12 = self.c*self.c3
        self.TipRemoval(self.sig11)
        self.TipRemoval(self.sig22)
        self.TipRemoval(self.sig12)
        
##############################################################################
