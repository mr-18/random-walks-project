#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 13:41:52 2019

@author: matt
"""
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3d
import matplotlib.animation as ani
import scipy

def Random_walk(points=1000, dimensions=2):
    '''
    '''
    #fixing random state for reproducible data
    np.random.seed(571)
    
    def Line_generation(points, dimensions):
        '''
        Create one line using a random walk algorithm
        ----------
        Parameters
        ----------
        points: Integer
            Number of lines to generate
        dimensions: Integer or Float
            Number of dimensions the line has
        -------
        Returns
        -------
        line_data: list, shape: (1, dimensions, points)
        '''
        line_data = np.empty((dimensions, points))
        line_data[:, 0] = np.random.rand(dimensions)
        moves = ([1, -1], [(0, 1), (1, 0), (0, -1), (-1, 0)],
                 [(0, 0, 1), (0, 1, 0), (1, 0, 0), (0, 0, -1), (0, -1, 0), (-1, 0, 0)])
        for i in range(1, points):
            choice = np.random.randint(0, dimensions*2)
            step = moves[dimensions-1][choice]
            line_data[:, i] = line_data[:, i-1] + step
        return line_data
    def update_lines(num, line_data, lines):
        '''
        '''
        for line, data in zip(lines, line_data):
            line.set_data(data[0:2, :num])
            line.set_3d_properties(data[2, :num])
        return lines
    #creating 3d axes
    fig = plt.figure()
    ax = p3d.Axes3D(fig)
    #creating data for line generation
    data = [Line_generation(points, dimensions)]
    #creating line objects
    lines = [ax.plot(dim[0, 0:1], dim[1, 0:1], dim[2, 0:1], marker='x',
                     markersize=3, color='darkviolet')[0] for dim in data]
    #setting axes bounds
    ax.set_xlim3d([np.float(np.min(data[0][0])), np.float(np.max(data[0][0]))])
    ax.set_xlabel('X')
    ax.set_ylim3d([np.float(np.min(data[0][1])), np.float(np.max(data[0][1]))])
    ax.set_ylabel('Y')
    ax.set_zlim3d([np.float(np.min(data[0][2])), np.float(np.max(data[0][2]))])
    ax.set_zlabel('Z')
    ax.set_title('3D test')
    #implementing animation of graphical data
    animation = ani.FuncAnimation(fig, update_lines, frames=points, fargs=(data, lines),
                                  interval=5, blit=False)
    #creating background plot of full path instantly
    ax.plot(data[0][0][:], data[0][1][:], data[0][2][:],alpha=0.1, marker='x',
            markersize=3, color='fuchsia')
    #creating start point marker
    ax.plot(data[0][0][0], data[0][1][0], data[0][2][0], marker='.',
            markersize=8, color='springgreen')
    #creating end point marker
    ax.plot(data[0][0][-1], data[0][1][-1], data[0][2][-1], marker='.',
            markersize=8, color='red')
    plt.show()
    return points, dimensions, data, animation
points, dimensions, data, animation = Random_walk(1000, 3)

def point_spacing(points, fixed_step):
    '''
    Evaluates the distance between all pairs of points at a fixed number
    of steps apart, fixed_step, along the walk
    '''
    if fixed_step > points:
        print('Error: fixed_step must be smaller than the number of points')
        return None
    else:
        distances = []
        for i in range(points-fixed_step):
            try:
                x_distance = data[0][0][i+fixed_step] - data[0][0][i]
                y_distance = data[0][1][i+fixed_step] - data[0][1][i]
                z_distance = data[0][2][i+fixed_step] - data[0][2][i]
                distance = (x_distance**2 + y_distance**2 + z_distance**2)**(1/2)
                distances.append(distance)
            except IndexError:
                print('point_gap too large to index, try a smaller value')
        return distances
def Gaussian_ladtribution(points, fs):
    '''
    '''
    for i in range(points):
        var = scipy.stats.var(point_spacing(i, fs))
    return None

    