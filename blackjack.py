"""ブラックジャックのルール
1.　初期カードは52枚
2.  引く際にカードの重複は無いようにする
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
    
    def deck():
        #self.suit = {'heart':"♥",'spade':"♠", 'diamond':"♦",'club':"♣"}
        cardNum = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

def main():
    suit = Suit.HEART
    num = 3
    card = Card(suit,num)
    print(f"選んだカード：{card.suit.icon} の {card.num}")
    deck = initDeck()
    random.shuffle(deck)
    pprint.pprint(deck)
    pick = deck[0]
    print(vars(pick))
    print(pick.suit)

def initDeck():
    deck = []    
    for suit in Suit:
        for number in range(13):
            card = Card(suit, number + 1)
            deck.append(card)

    return deck


if __name__ == "__main__":
    main()
