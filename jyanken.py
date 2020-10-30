# -*- coding: utf-8 -*-

import random

player_dic = {"n": "一般人", "h": "ケイスケ・ホンダ"}
dic = {"a": "グー", "b": "チョキ", "c": "パー"}
print("誰と戦う？")
print("n=一般人 h=ケイスケ・ホンダ")
player = input('>>> ')
player = player.lower()
print("じゃんけん！！")
print("a=グー b=チョキ c=パー a,b,cから選んでね")

user = input('>>> ')
user = user.lower()

try:
    player_choice = player_dic[player]
    user_choice = dic[user]

    choice_list = ["a", "b", "c"]
    pc = dic[random.choice(choice_list)]

    draw = 'DRAW'
    win = 'You Win!!'
    lose = 'You Lose!!'
    if player == 'h' :
        pc ="ペプシコーラ"
        judge = lose
    else :
        if user_choice == pc:
            judge = draw
        else:
            if user_choice == "グー":
                if pc == "チョキ":
                    judge = win
                else:
                    judge = lose
            elif user_choice == "チョキ":
                if pc == "パー":
                    judge = win
                else:
                    judge = lose

    print(f"対戦相手はこの人！　{player_choice}")
    print("いざ勝負!!")
    print(f"{user_choice} VS {pc}")
    print(judge)
    if judge == lose:
        print("何で負けたか明日までに考えといてください。")
        print("ほないただきます。ﾌﾟｼｬｰｰｰｰ！！！！！")
except:
    print("a,b,c から選んでね")
