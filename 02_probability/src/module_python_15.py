
# Visualisasi
import numpy as np
import matplotlib.pyplot as plt


from scipy.stats import t
from scipy.stats import ttest_1samp
def critical_value_t_stats_less(t_crit,df):
    plt.style.use('seaborn')

    plt.fill_between(x=np.arange(-4,-t_crit,0.01),
                     y1= t.pdf(np.arange(-4,-t_crit,0.01), df=df) ,
                     facecolor='red',
                     alpha=0.35,
                     label= 'Area below t-crit'
                     )

    plt.fill_between(x=np.arange(-t_crit,4,0.01), 
                     y1= t.pdf(np.arange(-t_crit,4,0.01), df=df) ,
                     facecolor='blue',
                     alpha=0.35, 
                     label= 'Area above t_crit')
    plt.legend()
    plt.xlabel("critical value visualization in t-distribution")
    plt.title(f't-statistic = {round(t_crit,2)}');

def sample_and_population_mean(data):
    # Histogram
    plt.hist(data, bins=5) 

    # memberi judul pada histogram
    plt.title("Histogram Rata-Rata Kecepatan Sam Berlari")

    # memberi label pada koordinat x
    plt.xlabel("Rata-Rata Kecepatan Sam Berlari")

    # memberi label pada koordinat y
    plt.ylabel("Frequency")

    # membuat garis lurus untuk menandakan mean sample
    plt.axvline(np.mean(data), color='k', linestyle=':', linewidth=1,label= 'Mean sampel')

    # membuat garis lurus untuk menandakan mean populasi
    plt.axvline(8, color='k', linestyle='dashed', linewidth=1,label= 'Mean population')

    # menambahkan label pada histogram
    plt.legend(loc = 'upper left')
    plt.show()