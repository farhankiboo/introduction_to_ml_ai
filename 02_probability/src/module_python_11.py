# Basic imports
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.stats import expon

def pdf_exponential(x, lambd):
    return lambd * np.exp(-lambd * x)

def simulasi_distribusi_eksponensial(lambd):
  x_axis = np.arange(0, 30, 0.01)
  y_axis = pdf_exponential(x_axis, lambd)
  plt.plot(x_axis, y_axis)
  plt.ylim(0,2.1)
  plt.xlabel("$x$")
  plt.title('PDF distribusi Eksponensial dengan lambda = '+str(lambd))
  plt.show()

import ipywidgets as widgets
from ipywidgets import interact

def playground_distribusi_eksponensial():
    slider_lambda = widgets.SelectionSlider(
        options=np.round(np.arange(0,2.1,0.1),2).tolist(),
        value=1.0,
        description='mean:',
        disabled=False,
        continuous_update=False,
        orientation='horizontal',
        readout=True
    )
    print("Masukkan Nilai Lambda:")
    interact(simulasi_distribusi_eksponensial, lambd = slider_lambda);
    
def pdf_normal(x, mu, var):
    return (1 / np.sqrt(2 * np.pi * var)) *\
        np.exp(-(1 / (2 * var)) * (x - mu) ** 2)

def simulasi_distribusi_normal(mean, var):
  x_axis = np.arange(-20, 20, 0.01)
  y_axis = pdf_normal(x_axis, mean, var)
  plt.plot(x_axis, y_axis)
  plt.ylim(0,0.6)
  plt.xlabel("$x$")
  plt.title('PDF distribusi normal dengan rata-rata = '+str(mean)+' dan varians = '+str(var)+'\n standar deviasi = ' + str(np.round(np.sqrt(var),3)))
  plt.show()

def playground_distribusi_normal():
    slider_mean = widgets.SelectionSlider(
        options=np.round(np.arange(-5,5,0.1),2).tolist(),
        value=-0.0,
        description='mean:',
        disabled=False,
        continuous_update=False,
        orientation='horizontal',
        readout=True
    )

    slider_var = widgets.SelectionSlider(
        options=np.arange(0.5,10,0.5).tolist(),
        value=1.0,
        description='var:',
        disabled=False,
        continuous_update=False,
        orientation='horizontal',
        readout=True
    )

    print("Masukkan Nilai Rata-rata dan Varians:")
    interact(simulasi_distribusi_normal, mean=slider_mean, var=slider_var);
    
    
import numpy as np
from scipy.stats import norm
import ipywidgets as widgets
from ipywidgets import interact

def CDF_distribusi_normal_standar(x):
  P = norm.cdf(x,0,1)
  P = np.round(P,4)
  return(print('peluang CDF kurang dari nilai',x,'adalah',P))

def tabel_distribusi_normal_standar():
    slider_x = widgets.SelectionSlider(
        options=np.round(np.arange(-4,4,0.01),2).tolist(),
        value=-0.0,
        description='x:',
        disabled=False,
        continuous_update=False,
        orientation='horizontal',
        readout=True
    )
    print("Masukkan Nilai x:")
    interact(CDF_distribusi_normal_standar, x = slider_x);
    
    
import numpy as np
from scipy.stats import norm
import ipywidgets as widgets
from ipywidgets import interact

def x_distribusi_normal_standar(P):
  x = norm.ppf(P,0,1)
  x = np.round(x,2)
  return(print('Peluang',P,'merupakan peluang nilai kurang dari',x))

def tabel_x_distribusi_normal_standar():
    slider_p = widgets.SelectionSlider(
        options=np.round(np.arange(0,1,0.0001),4).tolist(),
        value=0.5,
        description='CDF:',
        disabled=False,
        continuous_update=False,
        orientation='horizontal',
        readout=True
    )
    print("Masukkan Nilai Peluang CDF:")
    interact(x_distribusi_normal_standar, P=slider_p);