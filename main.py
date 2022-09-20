import random

deck = [
    "Ace♠", "2♠", "3♠", "4♠", "5♠", "6♠", "7♠", "8♠", "9♠", "10♠", "Jack♠",
    "Queen♠", "King♠", "Ace♣", "2♣", "3♣", "4♣", "5♣", "6♣", "7♣", "8♣", "9♣",
    "10♣", "Jack♣", "Queen♣", "King♣", "Ace♡", "2♡", "3♡", "4♡", "5♡", "6♡",
    "7♡", "8♡", "9♡", "10♡", "Jack♡", "Queen♡", "King♡", "Ace♢", "2♢", "3♢",
    "4♢", "5♢", "6♢", "7♢", "8♢", "9♢", "10♢", "Jack♢", "Queen♢", "King♢"
]

shuffle_card = ""
for i in range(208):
    x = random.randrange(0, 52)
    shuffle_card = deck[x]
    deck.pop(x)
    y = random.randrange(len(deck))
    deck.insert(y, shuffle_card)

print (deck[random.randrange(0, 52)])
