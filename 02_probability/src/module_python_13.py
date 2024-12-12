import pandas as pd
import numpy as np
from numpy import cov
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.patches import Ellipse
import matplotlib.transforms as transforms

import ipywidgets as widgets
from ipywidgets import interact



def confidence_ellipse(x, y, ax, n_std=3.0, facecolor='none', **kwargs):
    """
    Create a plot of the covariance confidence ellipse of *x* and *y*.

    Parameters
    ----------
    x, y : array-like, shape (n, )
        Input data.

    ax : matplotlib.axes.Axes
        The axes object to draw the ellipse into.

    n_std : float
        The number of standard deviations to determine the ellipse's radiuses.

    **kwargs
        Forwarded to `~matplotlib.patches.Ellipse`

    Returns
    -------
    matplotlib.patches.Ellipse
    """
    if x.size != y.size:
        raise ValueError("x and y must be the same size")

    cov = np.cov(x, y)
    pearson = cov[0, 1]/np.sqrt(cov[0, 0] * cov[1, 1])
    # Using a special case to obtain the eigenvalues of this
    # two-dimensionl dataset.
    ell_radius_x = np.sqrt(1 + pearson)
    ell_radius_y = np.sqrt(1 - pearson)
    ellipse = Ellipse((0, 0), width=ell_radius_x * 2, height=ell_radius_y * 2,
                      facecolor=facecolor, **kwargs)

    # Calculating the stdandard deviation of x from
    # the squareroot of the variance and multiplying
    # with the given number of standard deviations.
    scale_x = np.sqrt(cov[0, 0]) * n_std
    mean_x = np.mean(x)

    # calculating the stdandard deviation of y ...
    scale_y = np.sqrt(cov[1, 1]) * n_std
    mean_y = np.mean(y)

    transf = transforms.Affine2D() \
        .rotate_deg(45) \
        .scale(scale_x, scale_y) \
        .translate(mean_x, mean_y)

    ellipse.set_transform(transf + ax.transData)
    return ax.add_patch(ellipse)

def plotter_corr(val):
    np.random.seed(42)
    if val < 0:
        coeff = -1
    else:
        coeff = 1

    x = np.linspace(0,10,101)
    noise = np.random.normal(0,np.abs(val),101)
    y = coeff * 2 * x + 1.5 + noise

    fig, axs = plt.subplots(1, 1, figsize=(8, 8))
    axs.scatter(x,y)
    confidence_ellipse(x,y,axs,edgecolor='red')
    plt.show()

    print(f"Correlation coefficient: {np.corrcoef(x,y)[0][1]}")
    print(f"Covariance X and Y: {cov(x,y)[0][1]}")
    
    
def playground_corr():
    pelemparan_slider = widgets.SelectionSlider(
        options=[-100, -50, -20, -10, -5, -1, -0.5, -0.2, -0.1, 
                 0 , 0.1, 0.2, 0.5, 1, 5, 10, 20, 50, 100],
        value=0,
        description='randomness:',
        disabled=False,
        continuous_update=False,
        orientation='horizontal',
        readout=True
    )

    print("Masukkan 'Randomness':")
    interact(plotter_corr, val=pelemparan_slider);
    
    
def plot_randomness():
    randomness=[-100, -75,-50, -20, -10, -5, -1, -0.5, -0.2, -0.1, 
            0 , 0.1, 0.2, 0.5, 1, 5, 10, 20, 50, 75, 100]
    corr_val = []
    cov_val = []
    np.random.seed(42)
    for ra in randomness:
        if ra < 0:
            coeff = -1
        else:
            coeff = 1

        x = np.linspace(0,10,101)
        noise = np.random.normal(0,np.abs(ra),101)
        y = coeff * 2 * x + 1.5 + noise
        corr_val.append(np.corrcoef(x,y)[0][1])
        cov_val.append(cov(x,y)[0][1])

    fig,axs = plt.subplots(1,2, figsize=(12,5))
    axs[0].plot(randomness,corr_val)
    axs[0].set_title("Correlation Values")
    axs[0].set_xlabel("Randomness")
    axs[1].plot(randomness,cov_val)
    axs[1].set_title("Covariance Values")
    axs[1].set_xlabel("Randomness")
    
    
def heatmap_correlation(corr):
    fig, ax = plt.subplots(figsize=(10,8))
    sns.heatmap(corr, cmap='coolwarm', annot=True, fmt=".2f")
    plt.xticks(range(len(corr.columns)), corr.columns);
    plt.yticks(range(len(corr.columns)), corr.columns)
    plt.show()
    
    
def stripplot_boxplot(df):
    g = sns.stripplot(data = df.melt(), 
                      x = 'variable', 
                      y = 'value', 
                      color = 'red')
    sns.boxplot(data = df.melt(),
                x = 'variable', 
                y = 'value', 
                color = 'yellow')