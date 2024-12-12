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
    sum_lemparan = np.zeros((6, 6))
    joint_pmf = np.zeros((6, 6))
    expected_value = np.zeros((6, 6))
    for angka_dadu_1 in range(6):
        for angka_dadu_2 in range(6):
            # Mencari kejadian A
            kondisi_A = simulasi_lemparan[:,0]==angka_dadu_1+1
            sampel_A = simulasi_lemparan[kondisi_A]
            n_A = len(sampel_A)
            # Mencari kejadian B
            kondisi_B = simulasi_lemparan[:,1]==angka_dadu_2+1
            sampel_B = simulasi_lemparan[kondisi_B]
            n_B = len(sampel_B)

            # Mencari A_B 
            kondisi_B_irisan_A = sampel_A[:,1]==angka_dadu_2+1
            sampel_B_irisan_A = sampel_A[kondisi_B_irisan_A]
            n_B_irisan_A = len(sampel_B_irisan_A)

            # Mencari joint probability
            if (n_A and n_B)!= 0:
                peluang_B_A = n_B_irisan_A / len(simulasi_lemparan)
            else:
                peluang_B_A = 0.0

            # Masukkan sum probability kedalam map
            jumlah_lemparan[angka_dadu_1, angka_dadu_2] = n_B_irisan_A
            sum_lemparan[angka_dadu_1, angka_dadu_2] = angka_dadu_1+1+angka_dadu_2+1
            joint_pmf[angka_dadu_1, angka_dadu_2] = peluang_B_A
            expected_value = sum_lemparan*joint_pmf
     
    # Plotting
    sns.set(font_scale=1.5)

    fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(20,14))
    sns.heatmap(jumlah_lemparan, annot=True, fmt=".0f",
                vmax=jumlah_pelemparan, vmin=0, ax=ax[0][0],
                annot_kws={"fontsize":14})
    ax[0][0].set_xticklabels(range(1,7), size=14)
    ax[0][0].set_yticklabels(range(1,7), size=14)
    ax[0][0].set_xlabel("Angka Dadu 2", size=16)
    ax[0][0].set_ylabel("Angka Dadu 1", size=16)
    ax[0][0].set_title(f"Jumlah Kejadian {jumlah_pelemparan} Lemparan", size=16)
    
    sns.heatmap(joint_pmf, annot=True, 
                vmax=1.0, vmin=0.0, ax=ax[0][1],
                annot_kws={"fontsize":14})
    ax[0][1].set_xticklabels(range(1,7), size=14)
    ax[0][1].set_yticklabels(range(1,7), size=14)
    ax[0][1].set_xlabel("Angka Dadu 2", size=16)
    ax[0][1].set_ylabel("Angka Dadu 1", size=16)
    ax[0][1].set_title(f"Joint PMF {jumlah_pelemparan} Lemparan", size=16)

    sns.heatmap(sum_lemparan, annot=True, 
                vmax=1.0, vmin=0.0, ax=ax[1][0],
                annot_kws={"fontsize":14})
    ax[1][0].set_xticklabels(range(1,7), size=14)
    ax[1][0].set_yticklabels(range(1,7), size=14)
    ax[1][0].set_xlabel("Angka Dadu 2", size=16)
    ax[1][0].set_ylabel("Angka Dadu 1", size=16)
    ax[1][0].set_title(f"Jumlah Angka Dadu", size=16)

    sns.heatmap(expected_value, annot=True, 
                vmax=1.0, vmin=0.0, ax=ax[1][1],
                annot_kws={"fontsize":14})
    ax[1][1].set_xticklabels(range(1,7), size=14)
    ax[1][1].set_yticklabels(range(1,7), size=14)
    ax[1][1].set_xlabel("Angka Dadu 2", size=16)
    ax[1][1].set_ylabel("Angka Dadu 1", size=16)
    ax[1][1].set_title(f"Jumlah Angka Dadu * Joint PMF", size=16)
    
    plt.show()
    print(f"Ekspektasi jumlah angka mata dadu yang keluar {round(np.sum(expected_value),2)}")

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
