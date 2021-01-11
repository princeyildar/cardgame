from card_game import Card, Deck, Player
import unittest
from copy import copy, deepcopy

class DeckTests(unittest.TestCase):
    """Tests decks"""
    def setUp(self):
        self.deck = Deck()

    #test numbr of cards
    def testNumberOfCards(self):
        self.assertEqual(len(self.deck.cards), 52)
        
    #shuffle testing    
    def testShuffle(self):
        shuffled = []
        prev_deck = self.deck.cards.copy()
        self.deck.shuffle()
        
        after_deck = self.deck.cards

        self.assertFalse(prev_deck == after_deck)

    #test get card
    def testGet_card(self):
        for i in range(52):
            self.deck.get_card()
        self.assertTrue(self.deck.get_card() == None )  
        
    #sort test
    def testsort(self):
        
        for i in range(52):
            self.deck.get_card()
        deck2 = deepcopy(self.deck)
        self.deck.add_card(Card(suit=0, rank=2))   
        self.deck.add_card(Card(suit=2, rank=5))
        self.deck.add_card(Card(suit=3, rank=8))
        self.deck.add_card(Card(suit=1, rank=6))
        
        print(self.deck)
        
        print('sort array after sorting')        
        self.deck.sort()
        print(self.deck)
        deck2.add_card(Card(suit=0, rank=2))   
        deck2.add_card(Card(suit=1, rank=6))
        deck2.add_card(Card(suit=2, rank=5))
        deck2.add_card(Card(suit=3, rank=8))
        
        
        self.assertTrue(str(self.deck) == str(deck2) )

class PlayerTests(unittest.TestCase):
    """Tests decks"""
    def setUp(self):
        self.player = Player()
    # test get winining value
    def testGetWininingValue(self):
        self.player.add_card(Card(suit=0, rank=2))
        self.player.add_card(Card(suit=2, rank=5))
        self.player.add_card(Card(suit=3, rank=8))
        self.player.add_card(Card(suit=2, rank=6))
        self.assertTrue(self.player.get_winining_value() ==38)
        
  



def main():
    unittest.main()

if __name__ == '__main__':
    main()