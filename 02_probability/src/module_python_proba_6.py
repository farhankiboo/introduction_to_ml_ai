import itertools
import random
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt

class Dist(Counter): 
    "A Distribution of {outcome: frequency} pairs."

def cases(outcomes): 
    "The total frequency of all the outcomes."
    return sum(Dist(outcomes).values())

def favorable(event, space):
    "A distribution of outcomes from the sample space that are in the event."
    space = Dist(space)
    return Dist({x: space[x] 
                 for x in space if x in event})

def Fraction(n, d): 
    "Calculating the probability given outcome n and sample space d"
    return n / d

def Peluang(event, space): 
    "The probability of an event, given a sample space."
    return Fraction(cases(favorable(event, space)), 
                    cases(space))

def single_coin(p):
    return "H" if random.random() <= p else "T"

def coin_tosses(n_coins, head_proba=0.5):
    """
    Simulating single n_coin toss
    """
    coins_face = ""
    for _ in range(n_coins):
        coin_res = single_coin(head_proba)
        coins_face += coin_res
    
    return coins_face

def lempar_koin(n_sim, n_coins, head_proba=0.5):
    """
    Simulating n_coin toss with n_sim trials
    """
    outcomes = []
    for i in range(n_sim):
        one_toss = coin_tosses(n_coins, head_proba)
        outcomes.append(one_toss)
    
    return Dist(outcomes)

def lempar_satu_koin(n_sim, print_hasil=True):
    single_coin_tosses = lempar_koin(n_sim,1)
    p_head = Peluang({'H'}, single_coin_tosses)
    p_tail = Peluang({'T'}, single_coin_tosses)

    print(f"Head Probability: {p_head} \n Tail Probability: {p_tail}")
    if print_hasil:
        print(f"Hasil pelemparan koin {n_sim} kali = {single_coin_tosses}")
    
def eksperimen_lempar(n, n_coin):
    head_proba = []
    tail_proba = []
    n_toss = []
    for i in range(n):
        coin_toss = lempar_koin(i+1,1)
        p_head = Peluang({'H'}, coin_toss)
        p_tail = Peluang({'T'}, coin_toss)
        head_proba.append(p_head)
        tail_proba.append(p_tail)
        n_toss.append(i+1)

    plt.plot(n_toss, head_proba, 'k', label='Head Probability')
    plt.plot(n_toss, tail_proba, 'r', label='Tail Probability')
    plt.plot(n_toss, [0.5]*n, 'b--', label='Theoretical')
    plt.legend()
    plt.show()
    
def simulasi_mesin(n_sim, machine_A, machine_B):
    outcomes = []
    for _ in range(n_sim):
        # 
        out_A = random.choices(*zip(*machine_A.items()))[0]
        out_B = random.choices(*zip(*machine_B.items()))[0]
        state = out_A + out_B
        outcomes.append(state)
    return Dist(outcomes)

def simulasi_sistem(n_sim, components):
    outcomes = []
    for _ in range(n_sim):
        state = ""
        for comp in components:
            out_comp = random.choices(*zip(*comp.items()))[0]
            state += out_comp
        outcomes.append(state)
    return Dist(outcomes)