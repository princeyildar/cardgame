import random

class Card(object):
    """represents a standard playing card."""

    suit_labels = ["Clubs", "Hearts", "Diamonds", "Spades"]
    rank_labels = [None, "Ace", "2", "3", "4", "5", "6", "7", 
              "8", "9", "10", "Jack", "Queen", "King"]
    

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank
        
    def __lt__(self, other_card):
        if self.suit < other_card.suit:
            return True
        elif self.suit > other_card.suit:
            return False
        else:
            return self.rank < other_card.rank    
    def __cmp__(self, other_card):
        ss1 = self.suit, self.rank
        ss2 = other_card.suit, other_card.rank
        ra =  (ss1 > ss2) - (ss1 < ss2) 
        return ra        

    def __str__(self):
        return '%s of %s' % (Card.rank_labels[self.rank],
                             Card.suit_labels[self.suit])


class Deck(object):
    """represents a deck of cards"""
    
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                cd= Card(suit, rank)
                self.cards.append(cd)

    def __str__(self):
        res = []
        for cd in self.cards:
            res.append(str(cd))
        return '\n'.join(res)

    def add_card(self, card):
        """add a card to the deck"""
        self.cards.append(card)

    def get_card(self, i=-1):
        """2. get from the top of the deck: get one card from the top of the card deck.
        return a card and if there is no card left in the deck, rerurn or exception"""
        
        try:    
            return self.cards.pop(i)
        except Exception:
            print("there is no card left in the deck")    

    def shuffle(self):
        """1. Shuffle the cards in this deck"""
        random.shuffle(self.cards)

    def sort(self):
        """3. Sort the cards in ascending order suit and rank(ace high)"""
        self.cards.sort()
        

    def move_cards(self, hand, num):
        """move the given number of cards from the deck into the Hand"""
        for i in range(num):
            hand.add_card(self.get_card())


class Player(Deck):
    """represents a hand of playing cards"""
    
    def __init__(self, name=''):
        self.name = name
        self.cards = []
    def get_winining_value(self):
        winining_value = 0
        suite_number = [4, 3, 2, 1] 
        for i in range(len(self.cards)):
            
             winining_value = winining_value + suite_number[self.cards[i].suit] * self.cards[i].rank

        return winining_value
def play_game():
    
    #create card deck
    deck = Deck()
    #shuffle cards in the decks    
    deck.shuffle()
    
    #create the player 1
    player1 = Player('player 1')
    
    #player 1 draw  3 cards
    deck.move_cards(player1, 3)
    player1.sort()
    
    print('cards of player 1')
    print(player1)
    
    winning_value1 = player1.get_winining_value()
    print('The wining value of player 1:', winning_value1)
    print('\n')

    #create the player 2
    player2 = Player('player 2')
    
    #player 2 draw 3 cards
    deck.move_cards(player2, 3)
    player2.sort()
    print('cards of player 2')
    print(player2)    
    winning_value2 = player2.get_winining_value()
    print('The wining value of player 2:',winning_value2)
    
    if (winning_value1 > winning_value2):
       print('The player 1 wins')
    else:
        print('The player 2 wins')
                  
        

if __name__ == '__main__':
    
    play_game()
    
    
    
    
    
    