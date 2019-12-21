############################# Random walk project #############################
'''
A program analysing the process of random walks and the interesting analytical
characteristics that come with them
'''
############################## Analytical section #############################
######################### Importing necessary modules #########################
from Stats import Stats
import matplotlib.pyplot as plt
############################# Parameter choosing ##############################
steps = 1000
dims = 1
########################## Variance against step-size #########################
def Plot_variance(steps, dims):
    '''
    Plots the variance of the mean of the distances against the corresponding
    fixed step size
    '''
    fig = plt.figure(figsize=(10, 10))
    if dims == 1:
        gauss, counts, distance, means, variances, mom, var_mom, step_size = Stats(steps, dims)
        plt.title('Variance against step-size for a\n 1 dimensional walk')
        plt.scatter(step_size, variances[0])
        plt.xlabel('Variances')
        plt.ylabel('Step-size')
        plt.show()
    if dims == 2:
        g_x, g_y, ray, nc_x, nc_y, nc_r, d_x, d_y, d_r, means, variances, mom_x, mom_y, mom_r, var_mom_x, var_mom_y, var_mom_r, step_size = Stats(steps, dims)
        plt.title('Variance against step-size for a\n 2 dimensional walk')
        plt.scatter(step_size, variances[2])
        plt.xlabel('Variances')
        plt.ylabel('Step-size')
        plt.show()
    if dims == 3:
        g_x, g_y, g_z, ray, nc_x, nc_y, nc_z, nc_r, d_x, d_y, d_z, d_r, means, variances, mom_x, mom_y, mom_z, mom_r, var_mom_x, var_mom_y, var_mom_z, var_mom_r, step_size = Stats(steps, dims)
        plt.title('Variance against step-size for a\n 3 dimensional walk')
        plt.scatter(step_size, variances[3])
        plt.xlabel('Variances')
        plt.ylabel('Step-size')
        plt.show()
    return None
if __name__=='__main__':
    Variance_vs_stepsize = Plot_variance(steps, dims)