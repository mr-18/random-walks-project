############################# Random walk project #############################
'''
A program analysing the process of random walks and the interesting analytical
characteristics that come with them
'''
############################## Analytical section #############################
######################### Importing necessary modules #########################
from Stats import Stats
from numpy import round
import matplotlib.pyplot as plt
############################# Parameter choosing ##############################
#choose either 2 or 3 dimensions
steps = 2000
dims = 2
############################ Rayleigh distribution ############################
def Plot_rayleigh(steps, dims):
    '''
    Plots the distribution of the mean of the radial distances at each fixed
    step against the correspong Rayleigh distribution; for 2 or 3 dimensional
    random walks
    '''
    fig = plt.figure(figsize=(10, 10))
    if dims == 2:
        g_x, g_y, ray, nc_x, nc_y, nc_r, d_x, d_y, d_r, means, variances, mom_x, mom_y, mom_r, var_mom_x, var_mom_y, var_mom_r, step_size = Stats(steps, dims)
        plt.title('Distribution of radial distances with mean = {} and variance = {}\n for a 2 dimensional walk'.format(round(mom_r, 3), round(var_mom_r, 3)))
        plt.scatter(d_r, nc_r, label='normalised count for radial distances')
        plt.vlines(mom_r, ymin=0, ymax=max(nc_r), linestyles='dashed', label='mean value of r', color='b')
        plt.scatter(means[2], ray, color='purple', label='Rayleigh distribution of radial distances', alpha=0.1)
        plt.xlabel('Distance (steps)')
        plt.ylabel('Probability')
        plt.legend()
        plt.show()
    if dims == 3:
        g_x, g_y, g_z, ray, nc_x, nc_y, nc_z, nc_r, d_x, d_y, d_z, d_r, means, variances, mom_x, mom_y, mom_z, mom_r, var_mom_x, var_mom_y, var_mom_z, var_mom_r, step_size = Stats(steps, dims)
        plt.title('Distribution of radial distances with mean = {} and variance = {}\n for a 3 dimensional walk'.format(round(mom_r, 3), round(var_mom_r, 3)))
        plt.scatter(d_r, nc_r, label='normalised count for radial distances')
        plt.vlines(mom_r, ymin=0, ymax=max(nc_r), linestyles='dashed', label='mean value of r', color='b')
        plt.scatter(means[3], ray, color='purple', label='Rayleigh distribution of radial distances', alpha=0.1)
        plt.xlabel('Distance (steps)')
        plt.ylabel('Probability')
        plt.legend()
        plt.show()
    else:
        print('To see distributions for 1 dimensional axes try `Gauss.py`')
    return None
if __name__=='__main__':
    Rayleigh_distribution = Plot_rayleigh(steps, dims)