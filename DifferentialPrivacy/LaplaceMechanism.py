import numpy as np
import math
class LaplaceMechanism:
    def __init__(self,  epsilon,delta,n_value):
        
        self.epsilon = epsilon
        self.delta = delta
        self.n_value = n_value
        self.global_sensitivity = (self.n_value**(2/3))*np.log(n_value)
        self.Z= 0


    def expectedValuePadLength(self):
        Z= self.zSampleLaplace(self.global_sensitivity,self.epsilon)
        k = self.k(global_sensitivity=self.global_sensitivity,epsilon=self.epsilon,delta=self.delta)
        p = math.ceil(self.p(Z,k))
        expected_value = self.expectedValue(k,self.epsilon,self.delta,self.n_value)
        
        
        return expected_value
    
    

    def expectedValue(self,k,epsilon,delta,n):
        return (k+((np.exp(-epsilon))*delta*(1-k)))/n
    def zSampleLaplace(self, global_sensitivity, epsilon):
        return np.random.laplace(0, self.global_sensitivity / self.epsilon)
    
    def k(self,global_sensitivity, epsilon,delta):
        return (global_sensitivity / epsilon) * np.log(0.5* 1/delta)+ global_sensitivity +1
    
    def p(self,Z,k):
        return max(1,(Z+k))
    
