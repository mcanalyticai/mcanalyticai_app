from random import *
import random
import ctypes

# <, >, l, v alphabet
a_bet = ["<", ">", "L", "vl", "l-", "-vl", "v", "l-", "l", "l", "-^l", "lc-", "-l)", "l", "c", "-l", 
"-l", "l-", "-l", "-l", "-l", "v", "V", "l-", "l-", "|v)"]
# l, - alphabet 
abet = ["l", "l", "l-", "-l", "l-", "-l", "-", "l-", "l", "l", "-l", "l-", "-l", "l", "-", "-l",
"-l", "l-", "-l", "-l", "-l", "-", "l", "l-", "l-", "l-"]


class me_hieroglyphic:
    '''
    def __init__(self):
        self.alphabet=["<", ">", "L", "vl", "l", "vl", "v", "l", "l", "l", "^l", "l)", "l)", 
        "l", "c", "-l", "-l", "l-", "-l", "-l", "-l", "v", "V", "l-", "l-", "|v)"]
    '''
    a_bet = ["<", ">", "L", "vl", "l-", "-vl", "v", "l-", "l", "l", "-^l", "lc-", "-l)", "l", "c", "-l", 
    "-l", "l-", "-l", "-l", "-l", "v", "V", "l-", "l-", "|v)"] 
    abet = ["l", "l", "l-", "-l", "l-", "-l", "-", "l-", "l", "l", "-l", "l-", "-l", "l", "-", "-l",
    "-l", "l-", "-l", "-l", "-l", "-", "l", "l-", "l-", "l-"]
    def make_perc():
        num1=random.uniform(0,3.84615385)
        num1=str(num1)
        print(num1)
        return num1
    def discern():
        # vl = d, f
        # l = e, h, i, j, n
        # l) = l, m
        # -l = p, q, s, t, u
        # l- = r, x, y
        alpha=["<", ">", "L", "vl", "l", "vl", "v", "l", "l", "l", "^l", "l)", "l)", 
        "l", "c", "-l", "-l", "l-", "-l", "-l", "-l", "v", "V", "l-", "l-", "|v)"] 
        a=alpha[0]
        b=alpha[1]
        c=alpha[2]
        d=alpha[3]
        e=alpha[4]
        f=alpha[5]
        g=alpha[6]
        h=alpha[7]
        i=alpha[8]
        j=alpha[9]
        k=alpha[10]
        l=alpha[11]
        m=alpha[12]
        n=alpha[13]
        o=alpha[14]
        p=alpha[15]
        q=alpha[16]
        r=alpha[17]
        s=alpha[18]
        t=alpha[19]
        u=alpha[20]
        v=alpha[21]
        w=alpha[22]
        x=alpha[23]
        y=alpha[24]
        z=alpha[25]
        
    def assign(alpha=None, func=make_perc):
        alpha=["<", ">", "L", "vl", "l", "vl", "v", "l", "l", "l", "^l", "l)", "l)", 
        "l", "c", "-l", "-l", "l-", "-l", "-l", "-l", "v", "V", "l-", "l-", "|v)"] 
        al=random.randint(0,25)
        al=alpha[al]
        merge=str(al)+"--"+str(func)
        add_num=str(func).find('at')
        mem=str(func)
        mem=mem[add_num+3:len(mem)-1]
        # mem_py=id(mem)
        # conversion from python memory address to c memory address
        # y=hex(mem)
        # print(y)
        # z=int(y,base=16)
        # print(z)
        # va=ctypes.cast(mem,ctypes.py_object).value
        
        # print(va)
        # val=ctypes.cast(mem,ctypes.py_object).value
        # print(val)

        # python memory address and 'merge' string
        # print(merge)
        # print(mem)
        return [merge, mem]

    
    def sub_letter(letter, abet=abet):
        if letter=="a":
            return abet[0]
        elif letter=="b":
            return abet[1]
        elif letter=="c":
            return abet[2]
        elif letter=="d":
            return abet[3]
        elif letter=="e":
            return abet[4]
        elif letter=="f":
            return abet[5]
        elif letter=="g":
            return abet[6]
        elif letter=="h":
            return abet[7]
        elif letter=="i":
            return abet[8]
        elif letter=="j":
            return abet[9]
        elif letter=="k":
            return abet[10]
        elif letter=="l":
            return abet[11]
        elif letter=="m":
            return abet[12]
        elif letter=="n":
            return abet[13]
        elif letter=="o":
            return abet[14]
        elif letter=="p":
            return abet[15]
        elif letter=="q":
            return abet[16]
        elif letter=="r":
            return abet[17]
        elif letter=="s":
            return abet[18]
        elif letter=="t":
            return abet[19]
        elif letter=="u":
            return abet[20]
        elif letter=="v":
            return abet[21]
        elif letter=="w":
            return abet[22]
        elif letter=="x":
            return abet[23]
        elif letter=="y":
            return abet[24]
        elif letter=="z":
            return abet[25]

    def make_word(word, func=sub_letter):
        li_word=""
        for i in range(len(word)):
            letter=func(word[i])
            li_word=li_word+letter
        print(li_word)
        return li_word
    # funxions: make alien hieroglyphics
    def funxion_a():
        hieroglyph1 =a_bet[0]
        x=hieroglyph1
        return [hieroglyph1, x]
    def funxion_b():
        hieroglyph2 = a_bet[1]
        x=hieroglyph2
        return [hieroglyph2, x]
    def funxion_c():
        hieroglyph3 = a_bet[2]
        x=hieroglyph3
        return [hieroglyph3, x]
    def funxion_d():
        hieroglyph4 = a_bet[3]
        x=hieroglyph4
        return [hieroglyph4, x]
    def funxion_e():
        hieroglyph5 = a_bet[4]
        x=hieroglyph5[0]+hieroglyph5[0]+hieroglyph5[1]
        return [hieroglyph5, x]
    def funxion_f():
        hieroglyph6 = a_bet[5]
        x=hieroglyph6[0]+hieroglyph6[1]+hieroglyph6[2]
        print(x)
        return hieroglyph6
    def funxion_g():
        hieroglyph7 = a_bet[6]
        x=hieroglyph7+hieroglyph7
        print(x)
        return hieroglyph7
    def funxion_h():
        hieroglyph8 = a_bet[7]
        x=hieroglyph8[0]+hieroglyph8[1]+hieroglyph8[0]
        print(x)
        return hieroglyph8
    def funxion_i():
        hieroglyph9 = a_bet[8]
        x=hieroglyph9
        print(x)
        return hieroglyph9
    def funxion_j():
        hieroglyph10 = a_bet[9]
        x=hieroglyph10+hieroglyph10+hieroglyph10
        print(x)
        return hieroglyph10
    def funxion_k():
        hieroglyph11 = a_bet[10]
        x=hieroglyph11[0]+hieroglyph11[1]+hieroglyph11[2]+hieroglyph11[0]
        print(x)
        return hieroglyph11
    def funxion_l():
        hieroglyph12 = a_bet[11]
        x=hieroglyph12[0]+hieroglyph12[1]+hieroglyph12[2]
        print(x)
        return hieroglyph12
    def funxion_m():
        hieroglyph13 = a_bet[12]
        x=hieroglyph13[0]+hieroglyph13[1]+hieroglyph13[2]
        print(x)
        return hieroglyph13
    def funxion_n():
        hieroglyph14 = a_bet[13]
        x=hieroglyph14+hieroglyph14
        print(x)
        return hieroglyph14
    def funxion_o():
        hieroglyph15 = a_bet[14]
        x=hieroglyph15+hieroglyph15
        print(x)
        return hieroglyph15
    def funxion_p():
        hieroglyph16 = a_bet[15]
        x=hieroglyph16[0]+hieroglyph16[1]+hieroglyph16[1]+hieroglyph16[1]
        print(x)
        return hieroglyph16
    def funxion_q():
        hieroglyph17 = a_bet[16]
        x=hieroglyph17[0]+hieroglyph17[0]+hieroglyph17[1]+hieroglyph17[1]
        print(x)
        return hieroglyph17
    def funxion_r():
        hieroglyph18 = a_bet[17]
        x=hieroglyph18[0]+hieroglyph18[0]+hieroglyph18[0]+hieroglyph18[0]+hieroglyph18[1]+hieroglyph18[1]
        print(x)
        return hieroglyph18
    def funxion_s():
        hieroglyph19 = a_bet[18]
        x=hieroglyph19[0]+hieroglyph19[1]+hieroglyph19[1]
        print(x)
        return hieroglyph19
    def funxion_t():
        hieroglyph20 = a_bet[19]
        x=hieroglyph20[0]+hieroglyph20[1]+hieroglyph20[1]
        print(x)
        return hieroglyph20
    def funxion_u():
        hieroglyph21 = a_bet[20]
        x=hieroglyph21[0]+hieroglyph21[0]+hieroglyph21[0]+hieroglyph21[1]
        print(x)
        return hieroglyph21
    def funxion_v():
        hieroglyph22 = a_bet[21]
        x=hieroglyph22+hieroglyph22
        print(x)
        return hieroglyph22
    def funxion_w():
        hieroglyph23 = a_bet[22]
        x=hieroglyph23+hieroglyph23
        print(x)
        return hieroglyph23
    def funxion_x():
        hieroglyph24 = a_bet[23]
        x=hieroglyph24[0]+hieroglyph24[0]+hieroglyph24[0]+hieroglyph24[0]+hieroglyph24[1]
        print(x)
        return hieroglyph24
    def funxion_y():
        hieroglyph25 = a_bet[24]
        x=hieroglyph25[0]+hieroglyph25[0]+hieroglyph25[0]+hieroglyph25[1]
        print(x)
        return hieroglyph25
    def funxion_z():
        hieroglyph26 = a_bet[25]
        x=hieroglyph26[0]+hieroglyph26[1]+hieroglyph26[2]
        print(x)
        return hieroglyph26

# function vars '𓀀', '𓀁', '𓀂', '𓀃', '𓀄', '𓀅'
# 𓀀
# def 𓀀():
    # s=[1,2,3,4,5,6,7,8,9,10]
    # d=[[1,2,3,4,5,6,7,8,9,10], [1,2,3,4,5,6,7,8,9,10]]
    # f=100
    
# def funxion_s(t1, t2):
    # stack=[0,1,2,3]



    '''
    circ=[90, 180, 270]
    circ1=[45, 135, 225, 315]
    length=len(x)

    
    # refer
    attach=[0,1,2]

    for i in range(length):
        if x[i]=="L":
            circy=str(circ[0])
            a_hieroglyphic=x[i]+circy
            ah3=a_hieroglyphic
            print(ah3)
        elif x[i]=="Vl":
            circy=str(circ[1])
            a_hieroglyphic=x[i][0]+circy
            stacky="s"+str(stack[0])
            a_hieroglyphic=a_hieroglyphic+x[i][1]+stacky
            ah4=a_hieroglyphic
            print(ah4)
        elif x[i]=="lll":
            circy=str(circ[0])
            a_hieroglyphic=x[i][0]+circy
            a_hieroglyphic=a_hieroglyphic+x[i][1]+a_hieroglyphic
            ah5=a_hieroglyphic
            print(ah5)
        elif x[i]=="lvl":
            circy=str(circ1[0])
            attachy="a"+str(attach[0])
            term=x[i][0]+attachy+x[i][1]
            stacky="s"+str(stack[0])
            a_hieroglyphic=term+stacky+x[i][2]
            ah6=a_hieroglyphic
            print(ah6)
        elif x[i]=="llll":
            circy=str(circ1[0])
            circy1=str(circ[0])
            attachy="a"+str(attach[3])
            attachy1="a"+str(attach[4])
            a_hieroglyphic=circy+x[i][0]+attachy+x[i][0]+attachy1+circy1+x[i][0]+attachy+x[i][0]
            ah7=a_hieroglyphic       
    '''   
    
# print(len(a_bet))
# hiero=alien_hieroglyphic
# hiero.funxion_m()
# hiero.assign()
# hiero.make_perc()

hiero=me_hieroglyphic
hiero.make_word("onomonopia")