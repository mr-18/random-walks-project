############################# Random walk project #############################
'''
A program analysing the process of random walks and the interesting analytical
characteristics that come with them
'''
############################# Random walk section #############################
######################### Importing necessary modules #########################
import random
from numpy import empty, linspace
import matplotlib.pyplot as plt
# this import registers the 3d projection, but is otherwise unused
from mpl_toolkits.mplot3d import Axes3D
############################## Parameter setting ##############################
steps = 100000
dims = 2
########################### Creating the random walk ##########################
def Generate_walk(steps, dims):
    '''
    Computing a simple square lattice random walk for the number of steps,
    'steps', in dimensions, 'dims'. Bound is defined if user wants to
    keep random walk inside a specified boundary.
    '''
    N = 1
    data = empty((dims, steps+1))
# setting start position
    for i in range(dims):
        data[i, 0] = 0
# generating line data
    while N <= steps:
        i = random.randint(0, dims-1)
        data[:, N] = data[:, N-1]
        data[i, N] = data[i, N-1] + random.choice([-1, 1])
        N += 1
    return data
def Plot_walk(steps, dims):
    '''
    Plots the random walk calculated from the number of steps given in the
    number of dimensions specified
    '''
    fig = plt.figure(figsize=(10, 10))
    data = Generate_walk(steps, dims)
    if dims == 1:
        t = linspace(0, steps, steps+1)
        plt.plot(t, data[0, :], marker='x', markersize=3)
        plt.plot(t[0], data[0, 0], marker='.', markersize=12, color='g', label='Start position')
        plt.plot(t[-1], data[0, -1], marker='.', markersize=12, color='r', label='End position')
        plt.xlabel('time')
        plt.ylabel('X')
        plt.title('1D Random walk of length {} steps'.format(steps))
        plt.legend(loc='upper right')
        plt.show()
    elif dims == 2:
        plt.plot(data[0, :], data[1, :], marker='x', markersize=3)
        plt.plot(data[0, 0], data[1, 0], marker='.', markersize=12, color='g', label='Start position')
        plt.plot(data[0, -1], data[1, -1], marker='.', markersize=12, color='r', label='End position')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('2D Random walk of length {} steps'.format(steps))
        plt.legend(loc='upper right')
        plt.show()
    elif dims == 3:
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(data[0, :], data[1, :], data[2, :], marker='x', markersize=3)
        ax.plot(data[0, 0:1], data[1, 0:1], data[2, 0:1], marker='.',
                 markersize=12, color='limegreen', label='Start position')
        ax.plot(data[0, -1:], data[1, -1:], data[2, -1:], marker='.',
                 markersize=12, color='r', label='End position')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title('3D Random Walk of length {} steps'.format(steps))
        ax.legend(loc='upper right')
        plt.show()
# fourth dimension = colour ; if time permits
#    elif dims == 4:
#        ax = fig.add_subplot(111, projection='3d')
#        ax.plot(data[0, :], data[1, :], data[2, :], color=w[1], marker='x',
#                markersize=3)
#        ax.plot(data[0, 0:1], data[1, 0:1], data[2, 0:1], marker='.',
#                 markersize=12, color='g')
#        ax.plot(data[0, -1:], data[1, -1:], data[2, -1:], marker='.',
#                 markersize=12, color='r')
#        ax.set_xlabel('X')
#        ax.set_ylabel('Y')
#        ax.set_zlabel('Z')
#        ax.set_title('4D Random Walk')
#        plt.show()

    else:
        print('Dimensions too high to represent graphically; try 4 or lower for visual path')
    return None
if __name__=='__main__':
    random_walk = Plot_walk(steps, dims)
