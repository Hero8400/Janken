"""ブラックジャックのルール
1.　初期カードは52枚 済
2.  引く際にカードの重複は無いようにする 済
3.  プレイヤーとディーラーの2人対戦。
4.  プレイヤーは実行者、ディーラーは自動的に実行
5.  実行開始時、プレイヤーとディーラーはそれぞれ、カードを2枚引く。
    引いたカードは画面に表示する。ただし、ディーラーの2枚目のカードは分からないようにする
6.  その後、先にプレイヤーがカードを引く。
    プレイヤーが21を超えていたらバースト、その時点でゲーム終了
7.  プレイヤーは、カードを引くたびに、次のカードを引くか選択できる
8.  プレイヤーが引き終えたら、その後ディーラーは、自分の手札が17以上になるまで引き続ける
9.  プレイヤーとディーラーが引き終えたら勝負。より21に近い方の勝ち
10. JとQとKは10として扱う
11. Aはとりあえず「1」としてだけ扱う。「11」にはしない
12. ダブルダウンなし、スピリットなし、サレンダーなし、その他特殊そうなルールなし
"""
from enum import Enum
from typing import List
import random
import pprint

#2020/11/18 目標：カードを一枚引くとこまで。

class Suit(Enum):
    HEART = ("♥")
    SPADE = ("♠")
    DIAMOND = ("◆")
    CLUB = ("♣")

    def __init__(self, icon):
        self.icon = icon

class Card:
    # マーク
    suit: Suit
    # 数字
    num: int

    #コンストラクタの定義
    def __init__(self, suit: Suit, num: int):
        self.suit = suit
        self.num = num

#山札
Deck: List[Card]
#手札
PlayerHands: List[Card]

def main():
    global Deck
    setUp()
    suit = Suit.HEART
    num = 3
    card = Card(suit,num)
    print(f"選んだカード：{card.suit.icon} の {card.num}")
    #pprint.pprint(deck)

    #↓Python流do_while文
    while True:
        pick()
        if not choiceAction():
            break
    #print(pick.suit)

def setUp():
    global Deck
    global PlayerHands
    Deck = []
    PlayerHands = []
    for suit in Suit:
        for number in range(13):
            card = Card(suit, number + 1)
            Deck.append(card)

    random.shuffle(Deck)

def choiceAction() -> bool:
    point: int = sum(map(lambda x: x.num, PlayerHands))
    if point > 21:
        print("bust!!!!!!!!")
        return False
    elif point ==  21:
        print("BlackJack!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        return False
    
    print("更にカードを引きますか？[y/n]")
    action = input('>>> ')

    return action.lower() == 'y'
    # ↓上記の処理の意味
    # if action.lower() == 'y':
    #     return True
    # else:
    #     return False

def pick():
    global Deck
    global PlayerHands
    PlayerHands.append(Deck.pop(0))
    # pick = Deck.pop(random.randint(0, len(Deck - 1)))
    print(f"あなたが引いたカード:{vars(PlayerHands[-1])}")
    print(f"現在の合計値：{sum(map(lambda x: x.num, PlayerHands))}")


if __name__ == "__main__":
    main()
