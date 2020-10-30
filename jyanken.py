# -*- coding: utf-8 -*-

import random


def main():
    """メイン処理
    """

    player_dic = {"n": "一般人", "h": "ケイスケ・ホンダ"}
    dic = {"a": "グー", "b": "チョキ", "c": "パー"}

    print("誰と戦う？")
    print(" ".join(list(map(lambda x: f"{x[0]}={x[1]}", player_dic.items()))))
    player = input('>>> ')
    player = player.lower()
    if player not in player_dic:
        separator = ","
        print(f"{separator.join(player_dic.keys())} から選んでね")
        return

    print("じゃんけん！！")
    print(" ".join(list(map(lambda x: f"{x[0]}={x[1]}", dic.items()))))
    user = input('>>> ')
    user = user.lower()
    if user not in dic:
        separator = ","
        print(f"{separator.join(dic.keys())} から選んでね")
        return

    player_choice = player_dic[player]
    user_choice = dic[user]

    choice_list = list(dic.keys())
    pc = dic[random.choice(choice_list)]

    draw = 'DRAW'
    win = 'You Win!!'
    lose = 'You Lose!!'
    if player == 'h':
        pc = "ペプシコーラ"
        judge = lose
    else:
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


if __name__ == "__main__":
    main()
