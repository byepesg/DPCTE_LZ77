import matplotlib.pyplot as plt

from DifferentialPrivacy.LaplaceMechanism import LaplaceMechanism

def plot(n_values,pad_length_per_n,pad_length_per_n_p, x_label, y_label,label1,label2,title,store_values):

    plt.plot(n_values, pad_length_per_n, label=label1)
    plt.plot(n_values, pad_length_per_n_p, label=label2)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()
    
