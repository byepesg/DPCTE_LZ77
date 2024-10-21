import numpy as np
import math
from scipy.stats import bootstrap
class LaplaceMechanism:
    def __init__(self,  epsilon,delta,n_value):
        
        self.epsilon = epsilon
        self.delta = delta
        self.n_value = n_value

    def globalSensitivity(self,n):
        return n**(2/3)*np.log(n)

    def k(self,global_sensitivity, epsilon,delta):
        return (global_sensitivity / epsilon) * np.log(0.5* 1/delta)+ global_sensitivity +1
    
    def p(self):
        #p = math.ceil(self.p(Z,k))
        return max(1,(self.zSampleLaplace(self.globalSensitivity(self.n_value),self.epsilon)+self.k(global_sensitivity=self.globalSensitivity(self.n_value),epsilon=self.epsilon,delta=self.delta)))

    def expectedValuePadLength(self):
        k = self.k(global_sensitivity=self.globalSensitivity(self.n_value),epsilon=self.epsilon,delta=self.delta)
        expected_value = self.expectedValue(k,self.epsilon,self.delta,self.n_value)    
        # if(self.n_value==100):
        #     print("k====",k)
        return expected_value
    def expectedValue(self,k,epsilon,delta,n):
        #return (k+((np.exp(-epsilon))*delta*(1-k)))/n
        #return (k+((np.exp(-epsilon))*delta*self.globalSensitivity(self.n_value)/epsilon))/n
        return (k+((self.globalSensitivity(self.n_value)/epsilon)*(np.exp(-epsilon))*delta  ))
        
    
    def zSampleLaplace(self, global_sensitivity, epsilon):
        return np.random.laplace(0, (global_sensitivity / epsilon))
    
    def zSamplesLaplaceInterval():
        # Parameters
        mu = 0      # Location parameter
        b = 1       # Scale parameter
        n_samples = 1000  # Number of samples

        # Generate samples
        samples = np.random.laplace(mu, b, n_samples)
        # Sample statistics
        sample_mean = np.mean(samples)
        sample_std = np.std(samples, ddof=1)
        n = len(samples)
        confidence_level = 0.95
        alpha = 1 - confidence_level
        # Z-score for the desired confidence level
        z = norm.ppf(1 - alpha/2)

        # Margin of error
        margin_error = z * (sample_std / np.sqrt(n))

        # Confidence interval
        ci_lower = sample_mean - margin_error
        ci_upper = sample_mean + margin_error

        print(f"95% Confidence Interval for the Mean: ({ci_lower}, {ci_upper})")
