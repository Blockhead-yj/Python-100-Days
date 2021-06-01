# -*- coding: utf-8 -*-
"""
Created on Mon May 31 15:31:56 2021

@author: YJ-Dai
"""
import random
money = 1000

def CRAPS():
    init_dice = random.randint(1,12)
    out = 0
    if init_dice in [7,11]:
        out = 1
    elif init_dice in [2,3,12]:
        out = -1
    else:
        while out==0:
            dice = random.randint(1, 12)
            if dice==7:
                out = -1
            elif dice==init_dice:
                out = 1
            else:
                out = 0
    return out

play_times = 0
while money > 0:
    bet = int(input("请下注："))
    money += CRAPS()*bet
    play_times += 1
    print("你已进行%d次游戏，剩余金额为%d" % (play_times, money))
print("您当前的资产为%d,您已破产！" % money)