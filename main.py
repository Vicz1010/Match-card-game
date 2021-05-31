import random

SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck():
    """This is a Deck Class creating a deck that will be used to play the game"""
    def __init__(self):
        self.allCards = [(s,r) for s in SUITE for r in RANKS]


class Hand():
    """This a Hand class where each player can add or remove cards to their hand."""

    def __init__(self,cards):
        self.cards = cards

    def __str__(self):
        return "{}".format(len(self.cards))

    def add(self, added_cards):
        self.cards.extend(added_cards)


class Player():
    def __init__(self,name,Hand):
        self.name = name
        self.Hand = Hand

    def count_card(self):
        return len(self.Hand.cards)


# Introduction of game
print("Welcome to Match!")

# Input asking for how many decks to be used
deck_number = int(input("How many deck of cards do you want to use? "))

# Shuffling of the cards
deck = []

for x in range(deck_number):
    temp_deck = Deck()
    deck.extend(temp_deck.allCards)

random.shuffle(deck)
print("Creating new deck")

# Creating Players
comp_1 = Player("Player 1", Hand([]))
comp_2 = Player("Player 2", Hand([]))


# Gameplay
table_cards = []

while len(deck) != 0:
#   Cards on the table shown as a list


#   Taking cards from the Deck
    card_one = deck.pop()
    card_two = deck.pop()

#   Cards added to that on the table
    table_cards.append(card_one)
    table_cards.append(card_two)

#   See if there is a Match
    if card_one[0] == card_two[0] and card_one[1] == card_two[1]:
        print("We have a match")
        players = [comp_1,comp_2]
        player_match = random.choice(players)
        print(player_match.name, "Called Match")
        player_match.Hand.add(table_cards)
        table_cards.clear()

    if card_one[0] == card_two[0] or card_one[1] == card_two[1]:
        print("We have a match")
        players = [comp_1,comp_2]
        player_match = random.choice(players)
        print(player_match.name, "Called Match")
        player_match.Hand.add(table_cards)
        table_cards.clear()


if comp_1.count_card() > comp_2.count_card():
    print(comp_1.name, " is the winner with", comp_1.Hand.__str__(), "cards")
elif comp_2.count_card() > comp_1.count_card():
    print(comp_2.name, " is the winner with", comp_2.Hand.__str__(), "cards")
else:
    print("We have a draw")





