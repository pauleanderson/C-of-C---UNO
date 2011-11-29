from random import randint

class StandardCard:
    def __init__(self,c,n):
        self.color = c
        self.number = n

    def as_string(self):
        return self.color + " " + str(self.number)

class WildCard:
    def __init__(self):
        self.is_draw_4 = False

    def as_string(self):
        if self.is_draw_4 == False:
            return "Wild"
        else:
            return "Wild Draw 4"

class ReverseCard:
    def __init__(self,c):
        self.color = c

    def as_string(self):
        return self.color + " Reverse"

class SkipCard:
    def __init__(self,c):
        self.color = c

    def as_string(self):
        return self.color + " Skip"


class Draw2Card:
    def __init__(self,c):
        self.color = c

    def as_string(self):
        return self.color + " Draw 2"

class Player:
    def __init__(self,name,pid):
        self.name = name
        self.pid = pid
        self.cards = []

    def play_a_card(self,color,number):
        # Exhaustive search through the cards
        for i in range(len(self.cards)):
            if (self.cards[i].as_string().find(color) >= 0 and
                self.cards[i].as_string().find(str(number)) >= 0 and
                self.cards[i].as_string().find("Draw") == -1):

                card = self.cards[i]
                self.cards.remove(card)
                return card
        return None

    def as_string(self):
        results = self.name
        sorted_cards = []
        for card in self.cards:
            insert_index = 0
            
            
        for card in self.cards:
            results = results + " " + card.as_string()
        return results

def create_deck():
    deck = []

    for i in range(10):
        for color in ['blue','green','red','yellow']:
            if i == 0:
                card = StandardCard(color,i)
                deck.append(card)
            else:
                card = StandardCard(color,i)
                deck.append(card)
                card = StandardCard(color,i)
                deck.append(card)

##    # Makes the standard wild card
##    for i in range(4):
##        card = WildCard()
##        deck.append(card)
##
##    # Makes wild card that is a draw 4
##    for i in range(4):
##        card = WildCard()
##        card.is_draw_4 = True
##        deck.append(card)
        
    return deck

def deal_one_card(p,deck):
    if len(deck) == 0:
        return None
    i = randint(0,len(deck)-1)
    card = deck[i]
    p.cards.append(card)
    deck.remove(deck[i])
    return card

def create_discard_pile(deck):
    discard_pile = []
    i = randint(0,len(deck)-1)
    discard_pile.append(deck[i])
    deck.remove(deck[i])
    return discard_pile

def deal(p1,p2,p3,p4,deck):
    for i in range(1):
        deal_one_card(p1,deck)
        deal_one_card(p2,deck)
        deal_one_card(p3,deck)
        deal_one_card(p4,deck)

def check_card(discard_card,card_to_play):
    if discard_card.color == card_to_play.color or discard_card.number == card_to_play.number:
        return True
    return False

def can_play_card(player,discard_pile):
    discard_color = discard_pile[-1].color
    discard_number = discard_pile[-1].number
    for card in player.cards:
        if card.color == discard_color or card.number == discard_number:
            return True
    return False

p1 = Player("Paul",1)
p2 = Player("John",2)
p3 = Player("Jim",3)
p4 = Player("Jill",4)

deck = create_deck()
deal(p1,p2,p3,p4,deck)
discard_pile = create_discard_pile(deck)

cp = p1
while not(len(p1.cards) == 0 or len(p2.cards) == 0 or len(p3.cards) == 0 or len(p4.cards) == 0):
    print("\nDiscard pile: ",discard_pile[-1].as_string())

    # Execute a turn
    print(cp.as_string())

    # Check to see if they can play a card
    if can_play_card(cp,discard_pile) == False:
        print("You do not have any cards to play in your hand.")
        card = deal_one_card(cp,deck)
        print("You drew",card.as_string())        
    else:
        # Ask the user to play a card
        color = input("Color: ")
        number = input("Number: ")
        card = cp.play_a_card(color,number)
        if check_card(discard_pile[-1],card):
            discard_pile.append(card)
        else:
            cp.cards.append(card)
            deal_one_card(cp,deck)
            continue

        if cp == p1:
            cp = p2
        elif cp == p2:
            cp = p3
        elif cp == p3:
            cp = p4
        elif cp == p4:
            cp = p1

if len(p1.cards) == 0:
    print("Player",p1.name,"wins!")
elif len(p2.cards) == 0:
    print("Player",p2.name,"wins!")
elif len(p3.cards) == 0:
    print("Player",p3.name,"wins!")
elif len(p4.cards) == 0:
    print("Player",p4.name,"wins!")
    
