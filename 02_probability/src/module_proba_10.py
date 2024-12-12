import itertools
import random
import numpy as np
from collections import Counter

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.pyplot import figure

import seaborn as sns

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

def one_dice(side=6):
    sides = list(range(1,side+1))
    return random.choice(sides)
    
def dice_rolls(side=6, n=100000):
    result = []
    space = list(range(1,side+1))
    for _ in range(n):
        result.append(one_dice(side))
    return space, result

def dice_PMF(space, roll_result):
    dist_res = Dist(roll_result)
    proba = [dist_res[a]/len(roll_result) for a in space]
    plt.bar(space, proba)
    plt.show()
    
def multiple_dice_rolls(n_dice=2, side=6, n=100000):
    result = []
    space = list(range(1,side+1))
    for _ in range(n):
        mult_dice = ''
        for i in range(n_dice):
            mult_dice += str(one_dice(side)) 
        result.append(mult_dice)
    return space, result

def construct_dist():
    joint_pmf = Dist({'11':0, '12':0, '13':2000, '14':1000, 
                      '21':1000, '22':1000, '23':4000, '24':2000, 
                      '31':0, '32':3000, '33':1000, '34':2000,
                      '41':0, '42':1000, '43':2000, '44':0,})
    temp = []
    for key,val in joint_pmf.items():
        temp.append([key]*val)
    res = [item for sublist in temp for item in sublist]
    return res

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
    
    return outcomes, Dist(outcomes)

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