# -*- coding: utf-8 -*-

import random

dic = {"a": "グー", "b": "チョキ", "c": "パー"}

print("じゃんけん！！")
print("a=グー b=チョキ c=パー a,b,cから選んでね")

user = input('>>> ')
user = user.lower()

try:
    user_choice = dic[user]

    choice_list = ["a", "b", "c"]
    pc = dic[random.choice(choice_list)]

    draw = 'DRAW'
    win = 'You Win!!'
    lose = 'You Lose!!'

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
            
    print("君 VS 相手")
    print("%s VS %s" % (user_choice,pc))
    print("%s" % judge)
except:
    print("a,b,c から選んでね")
