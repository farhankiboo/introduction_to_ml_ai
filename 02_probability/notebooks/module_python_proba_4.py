# Jalankan code berikut
# Library pengolahan data
import numpy as np
import pandas as pd

# Library visualisasi
import matplotlib.pyplot as plt
import seaborn as sns

import ipywidgets as widgets
from ipywidgets import interact


# Jalankan Code Berikut
# Untuk sementara dipakai dahulu
# Cara coding akan diajarkan pada course berikutnya

def simulasi_lempar_dua_dadu(jumlah_pelemparan):
    np.random.seed(1)

    """
    Simulasi melempar 2 dadu berkali-kali
    A adalah kejadian angka dadu pertama yang muncul
    B adalah kejadian angka dadu kedua yang muncul, diketahui A telah terjadi
    """
    # Buat simulasi lemparan secara random
    # pakai np.random.randint()
    simulasi_lemparan = np.random.randint(1, 7, size=(jumlah_pelemparan, 2))

    # Mapping lemparan dadu
    jumlah_lemparan = np.zeros((6, 6))
    peluang_lemparan = np.zeros((6, 6))
    for angka_dadu_1 in range(6):
        for angka_dadu_2 in range(6):
            # Mencari kejadian A
            kondisi_A = simulasi_lemparan[:,0]==angka_dadu_1+1
            sampel_A = simulasi_lemparan[kondisi_A]
            n_A = len(sampel_A)

            # Mencari kejadian B dalam A
            kondisi_B_irisan_A = sampel_A[:,1]==angka_dadu_2+1
            sampel_B_irisan_A = sampel_A[kondisi_B_irisan_A]
            n_B_irisan_A = len(sampel_B_irisan_A)

            # Mencari conditional Probability
            if n_A != 0:
                peluang_B_A = n_B_irisan_A / n_A
            else:
                peluang_B_A = 0.0

            # Masukkan conditional probability kedalam map
            jumlah_lemparan[angka_dadu_1, angka_dadu_2] = n_B_irisan_A
            peluang_lemparan[angka_dadu_1, angka_dadu_2] = np.round(peluang_B_A, 3)

    # Plotting
    sns.set(font_scale=1.5)

    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(20,7))
    sns.heatmap(jumlah_lemparan, annot=True, fmt=".0f",
                vmax=jumlah_pelemparan, vmin=0, ax=ax[0],
                annot_kws={"fontsize":14})
    ax[0].set_xticklabels(range(1,7), size=14)
    ax[0].set_yticklabels(range(1,7), size=14)
    ax[0].set_xlabel("Angka Dadu 2", size=16)
    ax[0].set_ylabel("Angka Dadu 1", size=16)
    ax[0].set_title(f"Jumlah Kejadian {jumlah_pelemparan} Lemparan", size=16)
    
    sns.heatmap(peluang_lemparan, annot=True, 
                vmax=1.0, vmin=0.0, ax=ax[1],
                annot_kws={"fontsize":14})
    ax[1].set_xticklabels(range(1,7), size=14)
    ax[1].set_yticklabels(range(1,7), size=14)
    ax[1].set_xlabel("Angka Dadu 2", size=16)
    ax[1].set_ylabel("Angka Dadu 1", size=16)
    ax[1].set_title(f"Conditional Probability {jumlah_pelemparan} Lemparan", size=16)
    
    plt.show()
	

def playground_pelemparan_dadu():
    pelemparan_slider = widgets.SelectionSlider(
        options=[10, 100, 500, 1000, 10000, 100000],
        value=10,
        description='jumlah:',
        disabled=False,
        continuous_update=False,
        orientation='horizontal',
        readout=True
    )

    print("Masukkan Jumlah Pelemparan:")
    interact(simulasi_lempar_dua_dadu, jumlah_pelemparan=pelemparan_slider);                                                                                                


def summary_data(data_file_name):
    """
    Fungsi untuk merangkum data
    """
    # Import Library Print Hasil
    from tabulate import tabulate

    # Membaca data
    data_operasi = pd.read_csv(data_file_name)

    # Jumlah kejadian
    n_goRide_hujan = len(data_operasi[(data_operasi["Produk yang Digunakan"]=="Go-Ride") 
                                       & (data_operasi["Kondisi Cuaca"]=="Hujan")])
    n_goRide_cerah = len(data_operasi[(data_operasi["Produk yang Digunakan"]=="Go-Ride") 
                                       & (data_operasi["Kondisi Cuaca"]=="Cerah")])
    n_goCar_hujan = len(data_operasi[(data_operasi["Produk yang Digunakan"]=="Go-Car") 
                                      & (data_operasi["Kondisi Cuaca"]=="Hujan")])
    n_goCar_cerah = len(data_operasi[(data_operasi["Produk yang Digunakan"]=="Go-Car") 
                                      & (data_operasi["Kondisi Cuaca"]=="Cerah")])
    
    # Print hasil
    headers = ["Hasil Data Operasi", "Hujan", "Cerah"]
    data = [["Go-Ride", n_goRide_hujan, n_goRide_cerah],
            ["Go-Car", n_goCar_hujan, n_goCar_cerah]]

    print(tabulate(data, headers=headers))