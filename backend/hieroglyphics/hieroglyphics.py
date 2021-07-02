# egyptian hieroglyphs unicode
from h_glyphics import aeh
from logos import alien_hieroglyphic
from logos import a_bet

import random

# choose random letter
def choose():
    # random me hieroglyphic
    abet_rand = random.randint(0, 25)
    alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alphabet_rand=alphabet[abet_rand]
    return alphabet_rand

class stone(aeh, h_glyphics, a_bet, random_letter):
    # logos -[alphabet]-(insert_random)-> print
    def write(hieroglyphics=aeh, a_func=alien_hieroglyphic, abet=a_bet):
        # random hieroglyphic
        aeh_len = len(hieroglyphics)
        aeh_rand = random.randint(0, aeh_len)
        hieroglyph_rand=hieroglyphics[aeh_rand]
        
        # run me hieroglyphic
        if alphabet_rand=='a':
            x=a_func.funxion_a
        elif alphabet_rand=='b':
            x=a_func.funxion_b
        elif alphabet_rand=='c':
            x=a_func.funxion_c
        elif alphabet_rand=='d':
            x=a_func.funxion_d
        elif alphabet_rand=='e':
            a=a_func.funxion_e()[0]
            b=a_func.funxion_e()[1]
            return [a,b]
        elif alphabet_rand=='f':
            x=a_func.funxion_f
        elif alphabet_rand=='g':
            x=a_func.funxion_g
        elif alphabet_rand=='h':
            x=a_func.funxion_h
        elif alphabet_rand=='i':
            x=a_func.funxion_i
        elif alphabet_rand=='j':
            x=a_func.funxion_j
        elif alphabet_rand=='k':
            x=a_func.funxion_k
        elif alphabet_rand=='l':
            x=a_func.funxion_l
        elif alphabet_rand=='m':
            x=a_func.funxion_m
        elif alphabet_rand=='n':
            x=a_func.funxion_n
        elif alphabet_rand=='o':
            x=a_func.funxion_o
        elif alphabet_rand=='p':
            x=a_func.funxion_p
        elif alphabet_rand=='q':
            x=a_func.funxion_q
        elif alphabet_rand=='r':
            x=a_func.funxion_r
        elif alphabet_rand=='s':
            x=a_func.funxion_s
        elif alphabet_rand=='t':
            x=a_func.funxion_t
        elif alphabet_rand=='u':
            x=a_func.funxion_u
        elif alphabet_rand=='v':
            x=a_func.funxion_v
        elif alphabet_rand=='w':
            x=a_func.funxion_w
        elif alphabet_rand=='x':
            x=a_func.funxion_x
        elif alphabet_rand=='y':
            x=a_func.funxion_y
        elif alphabet_rand=='z':
            x=a_func.funxion_z

stone.write()