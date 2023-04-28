
suits = ["\u2666", "\u2663", "\u2665", "\u2660"]

class Card:
    def __init__(self, suit, value):
        self.value = suit
        self.suit = value

    def __str__(self):
        return f"{self.suit}{self.value}"
    
class Deck:
    def __init__(self):
        self._create_deck()

    def _create_deck(self):
        self.deck = []
        for suit in suits:
            for card in range(1, 14):
                self.deck.append(Card(card, suit))
    
    def skrivUt(self):
        for card in self.deck:
            print(card)
                

if __name__ == "__main__":
    deck = Deck()
    deck.skrivUt()