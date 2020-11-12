# -*- coding: utf-8 -*-

import random
import datetime
import spreadAutoWrite


judge_dic = {"draw": "DRAW", "win": "You WIN!!", "lose": "You LOSE!!"}
player_dic = {"n": "一般人", "h": "ケイスケ・ホンダ"}
dic = {"a": "グー", "b": "チョキ", "c": "パー"}

def choicePlayer():
    """ 対戦相手の選択 """

    print("誰と戦う？")
    print(" ".join(list(map(lambda x: f"{x[0]}={x[1]}", player_dic.items()))))
    player = input('>>> ')
    player = player.lower()
    return player

def janken():
    """ グー、チョキ、パーを選択 """

    print("じゃんけん！！")
    print(" ".join(list(map(lambda x: f"{x[0]}={x[1]}", dic.items()))))
    user = input('>>> ')
    user = user.lower() 
    return user

def gameResult(user_choice, pc, player):
    """ 対戦結果を判定 """

    if player == 'h':
        pc = "ペプシコーラ"
        judge = judge_dic["lose"]
    else:
        if user_choice == pc:
            judge = judge_dic["draw"]
        else:
            if user_choice == "グー":
                if pc == "チョキ":
                    judge = judge_dic["win"]
                else:
                    judge = judge_dic["lose"]
            elif user_choice == "チョキ":
                if pc == "パー":
                    judge = judge_dic["win"]
                else:
                    judge = judge_dic["lose"]
    return judge


def main():
    """メイン処理 """

    player = choicePlayer()
    if player not in player_dic:
        separator = ","
        print(f"{separator.join(player_dic.keys())} から選んでね")
        return

    user = janken()
    if user not in dic:
        separator = ","
        print(f"{separator.join(dic.keys())} から選んでね")
        return

    player_choice = player_dic[player]
    user_choice = dic[user]
    choice_list = list(dic.keys())
    pc = dic[random.choice(choice_list)]

    judge = gameResult(user_choice, pc, player)

    print(f"対戦相手はこの人！　{player_choice}")
    print("いざ勝負!!")
    print(f"{user_choice} VS {pc}")
    print(judge)
    if judge == judge_dic["lose"]:
        print("何で負けたか明日までに考えといてください。")
        print("ほないただきます。ﾌﾟｼｬｰｰｰｰ！！！！！")
    
    print("対戦成績を記録します。")

    dateTime = datetime.datetime.now()
    resultDic = {
        "datetime":dateTime.strftime('%Y年%m月%d日 %H:%M:%S'),
        "player_choice":player_choice,
        "judge":judge,
        "user_choice":user_choice,
        "pc":pc
        }
    spreadAutoWrite.jankenRecord(resultDic)
    print("対戦成績を記録しました。")

if __name__ == "__main__":
    main()
