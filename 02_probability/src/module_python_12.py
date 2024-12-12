# load data
import pandas as pd
import numpy as np
import itertools
import random
from collections import Counter
import scipy.stats as st

# visualization
import seaborn as sns
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import matplotlib.pyplot as plt

def joint_plot_3d(x,y):
    # Define the borders
    deltaX = (max(x) - min(x))/10
    deltaY = (max(y) - min(y))/10
    xmin = min(x) - deltaX
    xmax = max(x) + deltaX
    ymin = min(y) - deltaY
    ymax = max(y) + deltaY
    print(xmin, xmax, ymin, ymax)
    # Create meshgrid
    xx, yy = np.mgrid[xmin:xmax:100j, ymin:ymax:100j]
    positions = np.vstack([xx.ravel(), yy.ravel()])
    values = np.vstack([x, y])
    kernel = st.gaussian_kde(values)
    f = np.reshape(kernel(positions).T, xx.shape)
    fig = plt.figure(figsize=(13, 7))
    ax = plt.axes(projection='3d')
    w = ax.plot_wireframe(xx, yy, f)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('PDF')
    ax.set_title('Joint PDF');
    
def joint_plot_cond_3d(x,y,x_cond, y_cond):
    # Define the borders
    deltaX = (max(x) - min(x))/10
    deltaY = (max(y) - min(y))/10
    xmin = min(x) - deltaX
    xmax = max(x) + deltaX
    ymin = min(y) - deltaY
    ymax = max(y) + deltaY
    print(xmin, xmax, ymin, ymax)
    # Create meshgrid
    xx, yy = np.mgrid[xmin:xmax:100j, ymin:ymax:100j]
    positions = np.vstack([xx.ravel(), yy.ravel()])
    values = np.vstack([x, y])
    kernel = st.gaussian_kde(values)
    f = np.reshape(kernel(positions).T, xx.shape)

    deltaX_cond = (max(x_cond) - min(x_cond))/10
    deltaY_cond = (max(y_cond) - min(y_cond))/10
    xmin_cond = min(x_cond) - deltaX_cond
    xmax_cond = max(x_cond) + deltaX_cond
    ymin_cond = min(y_cond) - deltaY_cond
    ymax_cond = max(y_cond) + deltaY_cond
    print(xmin_cond, xmax_cond, ymin_cond, ymax_cond)
    # Create meshgrid
    xx_cond, yy_cond = np.mgrid[xmin_cond:xmax_cond:100j, ymin_cond:ymax_cond:100j]
    positions_cond = np.vstack([xx_cond.ravel(), yy_cond.ravel()])
    values_cond = np.vstack([x_cond, y_cond])
    kernel_cond = st.gaussian_kde(values_cond)
    f_cond = np.reshape(kernel_cond(positions_cond).T, xx_cond.shape)

    fig = plt.figure(figsize=(13, 7))
    ax = plt.axes(projection='3d')
    ax.plot_wireframe(xx_cond, yy_cond, f_cond, color="orange",zorder = 0.3)
    ax.plot_wireframe(xx, yy, f, color="blue",zorder = 0.5)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('PDF')
    ax.set_title('Joint PDF');
    
    
