from random import randint, shuffle
from graphics import *
from string import ascii_letters

CARD_WIDTH = 10
CARD_HEIGHT = 15

#This is a class for all of the standard cards with a number and color.
#It draws the card on the board
#Undraws the card on the board
#Moves the card to the input area
#Moves the card by the amount input
#Determines whether the card was clicked or not
#Returns a string that describes the card's color and number
class StandardCard:
    def __init__(self,c,n):
        self.color = c
        self.number = n
        self.drawn = False

    def draw(self,win):
        if self.drawn:
            return
        self.rect = Rectangle(Point(0,0),Point(CARD_WIDTH,CARD_HEIGHT))
        self.rect.draw(win)
        self.rect.setFill(self.color)
        self.text = Text(Point(CARD_WIDTH/2,CARD_HEIGHT/2),self.number)
        self.text.setFill("white")
        if self.color=="yellow":
            self.text.setFill("red")
        self.text.draw(win)
        self.drawn = True

    def undraw(self):
        self.rect.undraw()
        self.text.undraw()

    def move_to(self,x,y):
        center = self.rect.getCenter()
        dx = x - center.getX()
        dy = y - center.getY()
        self.move(dx,dy)

    def move(self,dx,dy):
        self.text.move(dx,dy)
        self.rect.move(dx,dy)

    def is_clicked(self,p):
        center = self.rect.getCenter()
        x1 = center.getX() - CARD_WIDTH/2
        x2 = center.getX() + CARD_WIDTH/2
        y1 = center.getY() - CARD_HEIGHT/2
        y2 = center.getY() + CARD_HEIGHT/2
        x = p.getX()
        y = p.getY()
        if x >= x1 and x <= x2 and y >= y1 and y <= y2:
            return True
        else:
            return False

    def as_string(self):
        return self.color + " " + str(self.number)
#Creates wildcards, as default these are not draw 4 wild cards
#Draws a wild card on the board
#Undraws a wildcard on the board
#Moves the card to the input area
#Moves the card by the amount input
#Determines whether the card was clicked or not
#Returns a string that describes whether the card is a wild or wild draw 4

class WildCard:
    def __init__(self):
        self.is_draw_4 = False
        self.color = "black"
        self.number = -1
        self.drawn = False

    def draw(self,win):
        if self.drawn:
            return
        self.rect = Rectangle(Point(0,0),Point(CARD_WIDTH,CARD_HEIGHT))
        self.rect.draw(win)
        self.rect.setFill(self.color)
        self.text = Text(Point(CARD_WIDTH/2,CARD_HEIGHT/2),self.number)
        self.text.setFill("white")
        self.text.draw(win)
        self.drawn = True

    def undraw(self):
        self.rect.undraw()
        self.text.undraw()

    def move_to(self,x,y):
        center = self.rect.getCenter()
        dx = x - center.getX()
        dy = y - center.getY()
        self.move(dx,dy)

    def move(self,dx,dy):
        self.text.move(dx,dy)
        self.rect.move(dx,dy)

    def is_clicked(self,p):
        center = self.rect.getCenter()
        x1 = center.getX() - CARD_WIDTH/2
        x2 = center.getX() + CARD_WIDTH/2
        y1 = center.getY() - CARD_HEIGHT/2
        y2 = center.getY() + CARD_HEIGHT/2
        x = p.getX()
        y = p.getY()
        if x >= x1 and x <= x2 and y >= y1 and y <= y2:
            return True
        else:
            return False

    def as_string(self):
        if self.is_draw_4 == False:
            return "wild"
        else:
            return "wild draw 4"
##Creates a reverse card
#Draws a reverse card on the board
#Undraws a reverse card on the board
#Moves the card to the input area
#Moves the card by the amount input
#Determines whether the card was clicked or not
#Returns a string that describes whether the color of the card and that it is a reverse
class ReverseCard:
    def __init__(self,c):
        self.color = c
        self.number = -1
        self.drawn = False

    def draw(self,win):
        if self.drawn:
            return
        self.rect = Rectangle(Point(0,0),Point(CARD_WIDTH,CARD_HEIGHT))
        self.rect.draw(win)
        self.rect.setFill(self.color)
        self.text = Text(Point(CARD_WIDTH/2,CARD_HEIGHT/2),self.number)
        self.text.setFill("white")
        if self.color=="yellow":
            self.text.setFill("red")
        self.text.draw(win)
        self.drawn = True


    def undraw(self):
        self.rect.undraw()
        self.text.undraw()

    def move_to(self,x,y):
        center = self.rect.getCenter()
        dx = x - center.getX()
        dy = y - center.getY()
        self.move(dx,dy)

    def move(self,dx,dy):
        self.text.move(dx,dy)
        self.rect.move(dx,dy)

    def is_clicked(self,p):
        center = self.rect.getCenter()
        x1 = center.getX() - CARD_WIDTH/2
        x2 = center.getX() + CARD_WIDTH/2
        y1 = center.getY() - CARD_HEIGHT/2
        y2 = center.getY() + CARD_HEIGHT/2
        x = p.getX()
        y = p.getY()
        if x >= x1 and x <= x2 and y >= y1 and y <= y2:
            return True
        else:
            return False

    def as_string(self):
        return self.color + " reverse"
##Creates skipcards,
#Draws a skip card on the board
#Undraws a skipcard on the board
#Moves the card to the input area
#Moves the card by the amount input
#Determines whether the card was clicked or not
#Returns a string that describes what color the skipcard is
class SkipCard:
    def __init__(self,c):
        self.color = c
        self.number = -1
        self.drawn = False

    def draw(self,win):
        if self.drawn:
            return
        self.rect = Rectangle(Point(0,0),Point(CARD_WIDTH,CARD_HEIGHT))
        self.rect.draw(win)
        self.rect.setFill(self.color)
        self.text = Text(Point(CARD_WIDTH/2,CARD_HEIGHT/2),self.number)
        self.text.setFill("white")
        if self.color=="yellow":
            self.text.setFill("red")
        self.text.draw(win)
        self.drawn = True


    def undraw(self):
        self.rect.undraw()
        self.text.undraw()

    def move_to(self,x,y):
        center = self.rect.getCenter()
        dx = x - center.getX()
        dy = y - center.getY()
        self.move(dx,dy)

    def move(self,dx,dy):
        self.text.move(dx,dy)
        self.rect.move(dx,dy)

    def is_clicked(self,p):
        center = self.rect.getCenter()
        x1 = center.getX() - CARD_WIDTH/2
        x2 = center.getX() + CARD_WIDTH/2
        y1 = center.getY() - CARD_HEIGHT/2
        y2 = center.getY() + CARD_HEIGHT/2
        x = p.getX()
        y = p.getY()
        if x >= x1 and x <= x2 and y >= y1 and y <= y2:
            return True
        else:
            return False

    def as_string(self):
        return self.color + " skip"
#Creates draw2cards
#Draws a draw2 card on the board
#Undraws a draw2card on the board
#Moves the card to the input area
#Moves the card by the amount input
#Determines whether the card was clicked or not
#Returns a string that describes what color the draw2card is
class Draw2Card:
    def __init__(self,c):
        self.color = c
        self.number = -1
        self.drawn = False

    def draw(self,win):
        if self.drawn:
            return
        self.rect = Rectangle(Point(0,0),Point(CARD_WIDTH,CARD_HEIGHT))
        self.rect.draw(win)
        self.rect.setFill(self.color)
        self.text = Text(Point(CARD_WIDTH/2,CARD_HEIGHT/2),self.number)
        self.text.setFill("white")
        if self.color=="yellow":
            self.text.setFill("red")
        self.text.draw(win)
        self.drawn = True


    def undraw(self):
        self.rect.undraw()
        self.text.undraw()

    def move_to(self,x,y):
        center = self.rect.getCenter()
        dx = x - center.getX()
        dy = y - center.getY()
        self.move(dx,dy)

    def move(self,dx,dy):
        self.text.move(dx,dy)
        self.rect.move(dx,dy)

    def is_clicked(self,p):
        center = self.rect.getCenter()
        x1 = center.getX() - CARD_WIDTH/2
        x2 = center.getX() + CARD_WIDTH/2
        y1 = center.getY() - CARD_HEIGHT/2
        y2 = center.getY() + CARD_HEIGHT/2
        x = p.getX()
        y = p.getY()
        if x >= x1 and x <= x2 and y >= y1 and y <= y2:
            return True
        else:
            return False

    def as_string(self):
        return self.color + " draw 2"
    #Creates a pleyer class
    #removes a card from your hand and selects it
    #determines if you can play a card or not
    #determines a description of the person's name and the cards in their hand
class Player:
    def __init__(self,name):
        self.name = name
        self.cards = []

    def play_a_card(self,color,number):
        # Exhaustive search through the cards
        for i in range(len(self.cards)):
            if (self.cards[i].as_string().find(color) >= 0 and
                self.cards[i].as_string().find(str(number)) >= 0 and
                self.cards[i].as_string().find("Draw") == -1):

                card = self.cards[i]
                self.cards.remove
                return card
        return None

    def can_play_card(self,discard_pile):
        discard_color = discard_pile[-1].color
        discard_number = discard_pile[-1].number
        for card in self.cards:
            if card.color == discard_color or card.number == discard_number:
                return True
        return False

    def as_string(self):
        card_strs = []
        for card in self.cards:
            card_strs.append(card.as_string())
        return self.name + ":" + "\t".join(card_strs)
