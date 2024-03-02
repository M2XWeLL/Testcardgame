from random import shuffle,choice
class Player:
    def __init__(self, hand):
        self._hand=hand
    def __repr__(self):
        return str(self._hand)
class Hand:
    def __init__(self, cards):
        self.cards=cards
    def __repr__(self):
        return str(self.cards)
        
class Card:
    def __init__(self, suit, number):
        self._suit=suit
        self.number= number
    def __repr__(self):
        return f'{self.number} of {self._suit}'
    @property
    def suit(self):
        return self._suit
    @suit.setter
    def suit(self, suit):
        if suit in ['hearts', 'clubs', 'diamonds', 'spades']:
            self._suit=suit.upper()
        else:
            print('This is not a suit')
class Deck:
    def __init__(self):
        self._cards = []
        self.populate()
    def populate(self):
        suits = ["hearts", "clubs", "diamonds", "spades"]
        numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        self._cards = [ Card(s, n) for s in suits for n in numbers ]   
    def shuffle(self):
        shuffle(self._cards)
    def deal(self, cards_a, players_a):
        self.shuffle()
        players_l=[]
        for i in range(players_a):
            players_l.append(Player(Hand([choice(self._cards) for i in range(cards_a//players_a)])))
        return players_l


mycard=Card(6,'hearts')
d=Deck()
temp = d.deal(36,6)
print(temp)



