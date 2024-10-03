import matplotlib.pyplot as plt
import numpy as np
from DifferentialPrivacy.LaplaceMechanism import LaplaceMechanism

def plot(n_values,expected_values, x_label, y_label,label1,title,store_values):
    condition = expected_values < n_values/4
    first_index = np.where(condition)[0][0]
    plt.scatter(n_values[first_index], expected_values[first_index], color='red', zorder=5)
    plt.plot(n_values, expected_values, label=label1)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.legend()
    plt.grid(True)
    
     
    
    
