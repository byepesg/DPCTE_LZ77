import numpy as np
import math
class LaplaceMechanism:
    def __init__(self,  epsilon,delta,n_value):
        
        self.epsilon = epsilon
        self.delta = delta
        self.n_value = n_value


    def expectedValuePadLength(self):
        k = self.k(global_sensitivity=self.globalSensitivity(self.n_value),epsilon=self.epsilon,delta=self.delta)
        expected_value = self.expectedValue(k,self.epsilon,self.delta,self.n_value)    
        if(self.n_value==100):
            print("k====",k)
        return expected_value

    def globalSensitivity(self,n):
        return n**(2/3)*np.log(n)
    def expectedValue(self,k,epsilon,delta,n):
        return (k+((np.exp(-epsilon))*delta*(1-k)))/n
    def zSampleLaplace(self, global_sensitivity, epsilon):
        return np.random.laplace(0, global_sensitivity / epsilon)
    def k(self,global_sensitivity, epsilon,delta):
        return (global_sensitivity / epsilon) * np.log(0.5* 1/delta)+ global_sensitivity +1
    
    def p(self):
        #p = math.ceil(self.p(Z,k))
        return max(1,(self.zSampleLaplace(self.globalSensitivity(self.n_value),self.epsilon)+self.k(global_sensitivity=self.globalSensitivity(self.n_value),epsilon=self.epsilon,delta=self.delta)))
    
