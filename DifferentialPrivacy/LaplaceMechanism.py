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
        return Z
    
    def k(global_sensitivity, epsilon,delta):
        return (global_sensitivity / epsilon) * np.log(0.5* delta)+ global_sensitivity +1
    
    def p(Z,k):
        return max(1,(Z+k))
    
    def padding():
        return "this would be the padding function"
    