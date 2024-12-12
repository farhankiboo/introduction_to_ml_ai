import numpy as np
import pandas as pd

# Library visualisasi
import matplotlib.pyplot as plt
import seaborn as sns
import ipywidgets as widgets
from ipywidgets import interact

def hitung_probabilitas(number_of_sample, number_of_event):
    """
    Fungsi untuk menghitung probabilitas kejadian
    
    args:
        number_of_sample : jumlah keseluruhan sample
        number_of_event : jumlah event yang ingin dihitung probabilitasnya terhadap sample
    
    return:
        probability : probabilitas dari event
    """
    
    probability = number_of_event / number_of_sample 
    return round(probability,2)

def hitung_total_probabilitas(*args):
    p_even = [args[i] for i in range(len(args)) if i%2==0]
    p_likelihood = [args[i] for i in range(len(args)) if i%2!=0]
    
    prob_result = []
    
    for i in range(len(p_even)):
        probability = p_even[i] * p_likelihood[i]
        prob_result.append(probability)
        
    return sum(prob_result)

def hitung_probabilitas_posterior(prior, likelihood, marginal_likelihood):
    posterior = prior*likelihood / marginal_likelihood
    return posterior

def plot_range_probabilitas_posterior(start, stop, step, prior=0, sensitivity=0, specificity=0, by="default"):
    if by == "prior":
        prior_range = np.arange(start, stop, step)
        p_terdeteksi = hitung_total_probabilitas(sensitivity, prior_range,
                                               (1-specificity), (1-prior_range))
        posterior_values = hitung_probabilitas_posterior(prior_range, sensitivity, p_terdeteksi).round(3)

        plt.plot(prior_range, posterior_values)
        plt.xlabel('p(spam)', fontsize=16)
        plt.axis([0, 1, 0, 1])
        _ = plt.ylabel('p(spam|terdeteksi)', fontsize=16)
        plt.yticks(fontsize=16)
        plt.xticks(fontsize=16)
        
    elif by == "sensitivity":
        sensitivity_range = np.arange(start, stop, step)
        posterior_values = []
        for i in range(len(sensitivity_range)):
            p_terdeteksi = hitung_total_probabilitas(sensitivity_range[i], prior,
                                               (1-specificity), (1-prior))
            posterior_values.append(hitung_probabilitas_posterior(prior, sensitivity_range[i], p_terdeteksi))
        
        plt.plot(sensitivity_range, posterior_values)
        plt.xlabel('sensitivity', fontsize=16)
        plt.axis([0, 1, 0, 1])
        _ = plt.ylabel('posterior', fontsize=16)
        plt.yticks(fontsize=16)
        plt.xticks(fontsize=16)

    elif by == "specificity":
        specificity_range = np.arange(start, stop, step)
        posterior_values = []
        for i in range(len(specificity_range)):
            p_terdeteksi = hitung_total_probabilitas(sensitivity, prior,
                                               (1-specificity_range[i]), (1-prior))
            posterior_values.append(hitung_probabilitas_posterior(prior, sensitivity, p_terdeteksi))
        
        plt.plot(specificity_range, posterior_values)
        plt.xlabel('specificity', fontsize=16)
        plt.axis([0, 1, 0, 1])
        _ = plt.ylabel('posterior', fontsize=16)
        plt.yticks(fontsize=16)
        plt.xticks(fontsize=16)
        
def hitung_jumlah_kejadian(number_of_ss, prob_events):
    number_of_events = round(number_of_ss*prob_events)
    return number_of_events

def summary_data(data_file_name):
    """
    Fungsi untuk merangkum data
    """
    # Import Library Print Hasil
    from tabulate import tabulate

    # Membaca data
    data_operasi = pd.read_csv(data_file_name)

    # Jumlah kejadian
    n_mampang_pipa = len(data_operasi[(data_operasi["toko_cabang"]=="mampang") 
                                       & (data_operasi["kategori_produk"]=="Pipa")])
    n_mampang_semen = len(data_operasi[(data_operasi["toko_cabang"]=="mampang") 
                                       & (data_operasi["kategori_produk"]=="Semen")])
    n_citayem_pipa = len(data_operasi[(data_operasi["toko_cabang"]=="citayem") 
                                      & (data_operasi["kategori_produk"]=="Pipa")])
    n_citayem_semen = len(data_operasi[(data_operasi["toko_cabang"]=="citayem") 
                                      & (data_operasi["kategori_produk"]=="Semen")])
    
    # Print hasil
    headers = ["Hasil Data Operasi", "Pipa", "Semen"]
    data = [["Mampang", n_mampang_pipa, n_mampang_semen],
            ["Citayem", n_citayem_pipa, n_citayem_semen]]

    print(tabulate(data, headers=headers))


# --- interaktif belum
def plot_interaktif_probabilitas_posterior(start, stop, step, prior=None, sensitivity=None, specificity=None, by=None):
    if by=="prior":
        prior_values = np.arange(start, stop, step)
        posterior_values = []

        for prior in prior_values:
            p_terdeteksi = hitung_total_probabilitas(sensitivity, prior,
                                                   (1-specificity), (1-prior))
            posterior = hitung_probabilitas_posterior(prior, sensitivity, p_terdeteksi).round(3)
            posterior_values.append(posterior)

        data = pd.DataFrame({"prior":prior_values, "posterior":posterior_values})

        prior_w = widgets.FloatSlider(min=0, max=1, step=0.001, description="prior")

        ui = widgets.HBox([prior_w])

        def draw_scatter_plot(prior):
            plt.scatter(data[data["prior"]==prior]["prior"], data[data["prior"]==prior]["posterior"], s=100)
            plt.plot(data["prior"], data["posterior"])
            plt.xlim(0-0.05, 1.05)
            plt.ylim(0, 1.05)
            plt.xlabel("Nilai Prior")
            plt.ylabel("Nilai Posterior")
            post = data[data["prior"]==prior]["posterior"].values
            plt.title(f"Saat prior = {prior}, nilai posterior = {post}")
            plt.show()

        out = widgets.interactive_output(draw_scatter_plot, {"prior":prior_w})
        display(ui, out)
        
    elif by=="sensitivity":
        sensitivity_range = np.arange(start, stop, step)
        posterior_values = []

        for sensitivity in sensitivity_range:
            p_terdeteksi = hitung_total_probabilitas(sensitivity, prior,
                                                   (1-specificity), (1-prior))
            posterior = hitung_probabilitas_posterior(prior, sensitivity, p_terdeteksi).round(3)
            posterior_values.append(posterior)
         

        data = pd.DataFrame({"sensitivity":sensitivity_range, "posterior":posterior_values})

        sens_w = widgets.FloatSlider(min=0, max=1, step=0.001, description="sensitivity")

        ui = widgets.HBox([sens_w])

        def draw_scatter_plot(sensitivity):
            plt.scatter(data[data["sensitivity"]==sensitivity]["sensitivity"], data[data["sensitivity"]==sensitivity]["posterior"], s=100)
            plt.plot(data["sensitivity"], data["posterior"])
            plt.xlim(0-0.05, 1.05)
            plt.ylim(0, 1.05)
            plt.xlabel("Nilai sensitivity")
            plt.ylabel("Nilai Posterior")
            post = data[data["sensitivity"]==sensitivity]["posterior"].values
            plt.title(f"Saat sensitivity = {sensitivity}, nilai posterior = {post}")
            plt.show()

        out = widgets.interactive_output(draw_scatter_plot, {"sensitivity":sens_w})
        display(ui, out)

    
    elif by=="specificity":
        specificity_range = np.arange(start, stop, step)
        posterior_values = []

        for specificity in specificity_range:
            p_terdeteksi = hitung_total_probabilitas(sensitivity, prior,
                                                   (1-specificity), (1-prior))
            posterior = hitung_probabilitas_posterior(prior, sensitivity, p_terdeteksi).round(3)
            posterior_values.append(posterior)
         

        data = pd.DataFrame({"specificity":specificity_range, "posterior":posterior_values})

        spec_w = widgets.FloatSlider(min=0, max=1, step=0.001, description="specificity")

        ui = widgets.HBox([spec_w])

        def draw_scatter_plot(specificity):
            plt.scatter(data[data["specificity"]==specificity]["specificity"], data[data["specificity"]==specificity]["posterior"], s=100)
            plt.plot(data["specificity"], data["posterior"])
            plt.xlim(0-0.05, 1.05)
            plt.ylim(0, 1.05)
            plt.xlabel("Nilai specificity")
            plt.ylabel("Nilai Posterior")
            post = data[data["specificity"]==specificity]["posterior"].values
            plt.title(f"Saat specificity = {specificity}, nilai posterior = {post}")
            plt.show()

        out = widgets.interactive_output(draw_scatter_plot, {"specificity":spec_w})
        display(ui, out)
        
    if by=="all":
        prior_w = widgets.FloatSlider(min=start, max=stop, step=step, description="prior")
        sensitivity_w = widgets.FloatSlider(min=start, max=stop, step=step, description="sensitivity")
        specitivity_w = widgets.FloatSlider(min=start, max=stop, step=step, description="specificity")

        ui = widgets.HBox([prior_w, sensitivity_w, specitivity_w])
        
        def hitung_posterior(prior, sensitivity, specificity):
            marginal_likelihood = hitung_total_probabilitas(sensitivity, prior, (1-specificity), (1-prior))
            posterior = hitung_probabilitas_posterior(prior, sensitivity, marginal_likelihood)
            print(f"""
                Jika nilai prior = {prior}
                nilai sensitivity = {sensitivity} 
                nilai specificity = {specificity}

                Maka nilai probabilitas posteriornya adalah {posterior:.3f}
            """)

        out = out = widgets.interactive_output(hitung_posterior, {'prior': prior_w, 'sensitivity': sensitivity_w, 'specificity': specitivity_w})
        display(ui, out)
    