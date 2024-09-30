import numpy as np
class LaplaceMechanism:
    def __init__(self, global_sensitivity, epsilon,delta,compression):
        self.global_sensitivity = global_sensitivity
        self.epsilon = epsilon
        self.delta = delta
        self.compression = compression
        self.Z= 0

    def add_noise(self, x):
        Z=x + np.random.laplace(0, self.global_sensitivity / self.epsilon)
        k = self.k(global_sensitivity=1,epsilon=1,delta=1)
        p = self.p(Z,k)
        padding = self.pad(self.compression,p)
        return padding


        return Z
    
    def k(self,global_sensitivity, epsilon,delta):
        return (global_sensitivity / epsilon) * np.log(0.5* delta)+ global_sensitivity +1
    
    def p(self,Z,k):
        return max(1,(Z+k))
    
    def pad(self,compression,p):
        return compression + p
    