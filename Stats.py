'''
A program analysing the process of random walks and the interesting analytical
characteristics that come with them
'''
############################## Analytical section #############################
######################### Importing necessary modules #########################
from RW import Generate_walk
from numpy import empty, sum, unique, round
import matplotlib.pyplot as plt
from scipy.stats import norm, rayleigh
from tqdm import tqdm
########################### Statistical calculations ##########################
def fs_distance(steps, dims, fixed_step):
    '''
    Evaluates the distance between all pairs of points at a fixed number
    of steps apart, fixed_step, along the walk for dimensions, dims, up to 3
    '''
    if fixed_step > steps:
        print('Error: fixed_step must be smaller than the number of points')
        return None
    else:
        data = Generate_walk(steps, dims)
        try:
            if dims == 1:
                distances = empty((dims, 1+steps-fixed_step))
                for i in range(1+steps - fixed_step):
                    distances[0, i] = data[0, i+fixed_step] - data[0, i]
            if dims == 2:
                distances = empty((dims+1, 1+steps-fixed_step))
                for i in range(1+steps - fixed_step):
                    distances[1, i] = int(data[0, i+fixed_step] - data[0, i])
                    distances[2, i] = int(data[1, i+fixed_step] - data[1, i])
                    distances[0, i] = (distances[1, i]**2 + distances[2, i]**2)**(1/2)
            if dims == 3:
                distances = empty((dims+1, 1+steps-fixed_step))
                for i in range(1+steps - fixed_step):
                    distances[1, i] = int(data[0, i+fixed_step] - data[0, i])
                    distances[2, i] = int(data[1, i+fixed_step] - data[1, i])
                    distances[3, i] = int(data[2, i+fixed_step] - data[2, i])
                    distances[0, i] = (distances[1, i]**2 + distances[2, i]**2 + distances[3, i]**2)**(1/2)
        except IndexError:
            print('fixed_step too large to index, try a smaller value')
        return distances
def Stats(steps, dims):
    '''
    Finds the mean and variance value for the distances found at each fixed
    step from the function `fs_distance` and is used to plot against a
    Gaussian distribution in `Plot_gauss`
    '''
#finding the mean and variance of the distances from the origin for each step 
#size
    if dims == 1:
        means = empty((dims, steps))
#        means_sq = empty((dims, steps))
        variances = empty((dims, steps))
        step_size = empty((1, steps))
#        var = empty((dims, steps))
        for i in tqdm(range(1, steps+1), desc='Calculating distribution of distances travelled in walk'):
            distances = fs_distance(steps, dims, i)
#calculating the mean of the distances found between each fixed_step distance
            means[0, i-1] = sum(distances)/len(distances[0])
#            means_sq[0, i-1] = sum(distances**2)/len(distances[0])
#            var[0, i-1] = means_sq[0, i-1] - means[0, i-1]**2
#calculating variance corresponding to the first random variable
            if i == 1:
                variances[0, i-1] = sum((distances-means[0, i-1])**2)/(len(distances[0]))
#calculating variance for all other following random variables
            else:
                variances[0, i-1] = variances[0, i-2] + sum((distances-means[0, i-1])**2)/(len(distances[0]))
            step_size[0, i-1] = i
#calculating the mean of the mean of the distances
        mom = sum(means[0])/len(means[0])
#calculating the variance correspong to the mom
        var_mom = sum((means[0]-mom)**2)/(len(means[0]))
#calulating the standard deviation of the mom
        std_mom = var_mom**(1/2)
#creating gaussian fit of means
        gauss = norm.pdf(means[0], mom, std_mom)
#counting how many walks were of each distance away from the origin
        distance, counts = unique(round(means), return_counts=True)
#normalising count to be consistent with normal distribution
        norm_counts = counts/sum(counts)
        return gauss, norm_counts, distance, means, variances, mom, var_mom, step_size
    if dims == 2:
        means = empty((dims+1, steps))
#        means_sq = empty((dims, steps))
        variances = empty((dims+1, steps))
        step_size = empty((1, steps))
#        var = empty((dims, steps))
        for i in tqdm(range(1, steps+1), desc='Calculating distribution of distances travelled in walk'):
            distances = fs_distance(steps, dims, i)
#calculating the mean of the distances found between each fixed_step distance
            means[0, i-1] = sum(distances[1])/len(distances[1])
            means[1, i-1] = sum(distances[2])/len(distances[2])
            means[2, i-1] = sum(distances[0])/len(distances[0])
#calculating variance corresponding to the first random variable
            if i == 1:
                variances[0, i-1] = sum((distances[1]-means[0, i-1])**2)/len(distances[1])
                variances[1, i-1] = sum((distances[2]-means[1, i-1])**2)/len(distances[2])
                variances[2, i-1] = sum((distances[0]-means[2, i-1])**2)/len(distances[0])
#calculating variance for all other following random variables
            else:
                variances[0, i-1] = variances[0, i-2] + sum((distances[1]-means[0, i-1])**2)/len(distances[1])
                variances[1, i-1] = variances[1, i-2] + sum((distances[2]-means[1, i-1])**2)/len(distances[2])
                variances[2, i-1] = variances[2, i-2] + sum((distances[0]-means[2, i-1])**2)/len(distances[0])
            step_size[0, i-1] = i
#calculating the mean of the mean of the distances
        mom_x = sum(means[0])/len(means[0])
        mom_y = sum(means[1])/len(means[1])
        mom_r = sum(means[2])/len(means[2])
#calculating the variance correspong to the mom
        var_mom_x = sum((means[0]-mom_x)**2)/len(means[0])
        var_mom_y = sum((means[1]-mom_y)**2)/len(means[1])
        var_mom_r = sum((means[2]-mom_r)**2)/len(means[2])
#calulating the standard deviation of the mom
        std_mom_x = var_mom_x**(1/2)
        std_mom_y = var_mom_y**(1/2)
        std_mom_r = var_mom_r**(1/2)
#creating gaussian fit of means
        g_x = norm.pdf(means[0], mom_x, std_mom_x)
        g_y = norm.pdf(means[1], mom_y, std_mom_y)
#creating rayleigh fit of means
        ray = rayleigh.pdf(means[2], loc=0, scale=std_mom_r)
#counting how many walks were of each distance away from the origin
        d_x, c_x = unique(round(means[0]), return_counts=True)
        d_y, c_y = unique(round(means[1]), return_counts=True)
        d_r, c_r = unique(round(means[2]), return_counts=True)
#normalising count to be consistent with normal distribution
        nc_x = c_x/sum(c_x)
        nc_y = c_y/sum(c_y)
        nc_r = c_r/sum(c_r)
        return g_x, g_y, ray, nc_x, nc_y, nc_r, d_x, d_y, d_r, means, variances, mom_x, mom_y, mom_r, var_mom_x, var_mom_y, var_mom_r, step_size
    if dims == 3:
        means = empty((dims+1, steps))
#        means_sq = empty((dims, steps))
        variances = empty((dims+1, steps))
        step_size = empty((1, steps))
#        var = empty((dims, steps))
        for i in tqdm(range(1, steps+1), desc='Calculating distribution of distances travelled in walk'):
            distances = fs_distance(steps, dims, i)
#calculating the mean of the distances found between each fixed_step distance
            means[0, i-1] = sum(distances[1])/len(distances[1])
            means[1, i-1] = sum(distances[2])/len(distances[2])
            means[2, i-1] = sum(distances[3])/len(distances[3])
            means[3, i-1] = sum(distances[0])/len(distances[0])
#calculating variance corresponding to the first random variable
            if i == 1:
                variances[0, i-1] = sum((distances[1]-means[0, i-1])**2)/len(distances[1])
                variances[1, i-1] = sum((distances[2]-means[1, i-1])**2)/len(distances[2])
                variances[2, i-1] = sum((distances[3]-means[2, i-1])**2)/len(distances[3])
                variances[3, i-1] = sum((distances[0]-means[3, i-1])**2)/len(distances[0])
#calculating variance for all other following random variables
            else:
                variances[0, i-1] = variances[0, i-2] + sum((distances[1]-means[0, i-1])**2)/len(distances[1])
                variances[1, i-1] = variances[1, i-2] + sum((distances[2]-means[1, i-1])**2)/len(distances[2])
                variances[2, i-1] = variances[2, i-2] + sum((distances[3]-means[2, i-1])**2)/len(distances[3])
                variances[3, i-1] = variances[3, i-2] + sum((distances[0]-means[3, i-1])**2)/len(distances[0])
            step_size[0, i-1] = i
#calculating the mean of the mean of the distances
        mom_x = sum(means[0])/len(means[0])
        mom_y = sum(means[1])/len(means[1])
        mom_z = sum(means[2])/len(means[2])
        mom_r = sum(means[3])/len(means[3])
#calculating the variance correspong to the mom
        var_mom_x = sum((means[0]-mom_x)**2)/len(means[0])
        var_mom_y = sum((means[1]-mom_y)**2)/len(means[1])
        var_mom_z = sum((means[2]-mom_z)**2)/len(means[2])
        var_mom_r = sum((means[3]-mom_r)**2)/len(means[3])
#calulating the standard deviation of the mom
        std_mom_x = var_mom_x**(1/2)
        std_mom_y = var_mom_y**(1/2)
        std_mom_z = var_mom_z**(1/2)
        std_mom_r = var_mom_r**(1/2)
#creating gaussian fit of means
        g_x = norm.pdf(means[0], mom_x, std_mom_x)
        g_y = norm.pdf(means[1], mom_y, std_mom_y)
        g_z = norm.pdf(means[2], mom_z, std_mom_z)
#creating rayleigh fit of means
        ray = rayleigh.pdf(means[3], loc=0, scale=std_mom_r)
#counting how many walks were of each distance away from the origin
        d_x, c_x = unique(round(means[0]), return_counts=True)
        d_y, c_y = unique(round(means[1]), return_counts=True)
        d_z, c_z = unique(round(means[2]), return_counts=True)
        d_r, c_r = unique(round(means[3]), return_counts=True)
#normalising count to be consistent with normal distribution
        nc_x = c_x/sum(c_x)
        nc_y = c_y/sum(c_y)
        nc_z = c_z/sum(c_z)
        nc_r = c_r/sum(c_r)
        return g_x, g_y, g_z, ray, nc_x, nc_y, nc_z, nc_r, d_x, d_y, d_z, d_r, means, variances, mom_x, mom_y, mom_z, mom_r, var_mom_x, var_mom_y, var_mom_z, var_mom_r, step_size
