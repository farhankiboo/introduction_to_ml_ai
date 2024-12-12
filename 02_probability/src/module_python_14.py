import pandas as pd
import numpy as np
import itertools
import random
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

def expectation_visualization(L, X_list):
    fig = sns.distplot(L, axlabel='length', kde=True)
    fig = sns.distplot(X_list, axlabel='length', kde=True)
    line1 = plt.axvline(L.mean(), color="k", linestyle="--", label = "rata-rata panjang semula")
    line2 = plt.axvline(np.mean(X_list), color="r", linestyle="--", label = "rata-rata X")
    first_legend = plt.legend(handles=[line1,line2], loc=1)
    plt.show()