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
steps = 1000
dims = 1
############################ Gaussian distribution ############################
def Plot_gauss(steps, dims):
    '''
    Plots the distribution of the mean of the distances at each fixed step
    against the corresponding Gaussian distribution; for 1 dimensional
    distribution from 1 and 2 dimensional walks
    '''
    fig = plt.figure(figsize=(10, 10))
    if dims == 1:
        gauss, counts, distance, means, variances, mom, var_mom, step_size = Stats(steps, dims)
        plt.title('Distribution with mean = {} and \nvariance = {}'.format(round(mom, 3), round(var_mom, 3)))
        plt.scatter(distance, counts, label='normalised count of x component')
        plt.vlines(mom, ymin=0, ymax=max(counts), linestyles='dashed', label='mean')
        plt.scatter(means[0], gauss, color='r', label='Gaussian distribution')
        plt.xlabel('Distance (steps)')
        plt.ylabel('Probability')
        plt.legend()
        plt.show()
        return None
    if dims == 2:
        g_x, g_y, ray, nc_x, nc_y, nc_r, d_x, d_y, d_r, means, variances, mom_x, mom_y, mom_r, var_mom_x, var_mom_y, var_mom_r, step_size = Stats(steps, dims)
        plt.title('Double Distribution of x values with mean = {} and variance = {}\n and y values with mean = {} and variance = {}'.format(round(mom_x, 3), round(var_mom_x, 3), round(mom_y, 3), round(var_mom_y, 3)))
        plt.scatter(d_x, nc_x, label='normalised count for x component')
        plt.scatter(d_y, nc_y, label='normalised count for y component')
        plt.vlines(mom_x, ymin=0, ymax=max(nc_x), linestyles='dashed', label='mean value of x', color='b')
        plt.vlines(mom_y, ymin=0, ymax=max(nc_y), linestyles='dashed', label='mean value of y', color='orange')
        plt.scatter(means[0], g_x, color='r', label='Gaussian distribution of x values', alpha=0.1)
        plt.scatter(means[1], g_y, color='purple', label='Gaussian distribution of y values', alpha=0.1)
        plt.xlabel('Distance (steps)')
        plt.ylabel('Probability')
        plt.legend()
        plt.show()
        return None
    if dims == 3:
        g_x, g_y, g_z, ray, nc_x, nc_y, nc_z, nc_r, d_x, d_y, d_z, d_r, means, variances, mom_x, mom_y, mom_z, mom_r, var_mom_x, var_mom_y, var_mom_z, var_mom_r, step_size = Stats(steps, dims)
        plt.title('Triple Distribution of x values with mean = {} and variance = {};\n y values with mean = {} and variance = {}\n and z values with mean = {} and variance = {}'.format(round(mom_x, 3), round(var_mom_x, 3), round(mom_y, 3), round(var_mom_y, 3), round(mom_z, 3), round(var_mom_z, 3)))
        plt.scatter(d_x, nc_x, label='normalised count for x component')
        plt.scatter(d_y, nc_y, label='normalised count for y component')
        plt.scatter(d_z, nc_z, label='normalised count for z component')
        plt.vlines(mom_x, ymin=0, ymax=max(nc_x), linestyles='dashed', label='mean value of x', color='b')
        plt.vlines(mom_y, ymin=0, ymax=max(nc_y), linestyles='dashed', label='mean value of y', color='orange')
        plt.vlines(mom_z, ymin=0, ymax=max(nc_z), linestyles='dashed', label='mean value of z', color='green')
        plt.scatter(means[0], g_x, color='r', label='Gaussian distribution of x values', alpha=0.1)
        plt.scatter(means[1], g_y, color='purple', label='Gaussian distribution of y values', alpha=0.1)
        plt.scatter(means[2], g_z, color='pink', label='Gaussian distribution of z values', alpha=0.1)
        plt.xlabel('Distance (steps)')
        plt.ylabel('Probability')
        plt.legend()
        plt.show()
        return None
    else:
        print('To see distribution for more than 1D distributions try `Rayleigh.py`')
        return None
if __name__=='__main__':
    Gaussian_distribution = Plot_gauss(steps, dims)
