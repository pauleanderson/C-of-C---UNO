from random import randint, shuffle
from graphics import *
from string import ascii_letters

CARD_WIDTH = 10
CARD_HEIGHT = 15
CARDS_DIR = "Cards/"

class StandardCard:
    def __init__(self,c,n):
        self.color = c
        self.number = n
        self.drawn = False

    def draw(self,win):
        if self.drawn:
            return
        filename = CARDS_DIR+"{0}{1}.gif".format(self.color, self.number)
        self.card = Image(Point(0, 0), filename)
        self.card.draw(win)
        self.drawn = True

    def undraw(self):
        self.card.undraw()

    def move_to(self,x,y):
        center = self.card.getAnchor()
        dx = x - center.getX()
        dy = y - center.getY()
        self.move(dx,dy)

    def move(self,dx,dy):
        self.card.move(dx,dy)

    def is_clicked(self,p):
        center = self.card.getAnchor()
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

class WildCard:
    def __init__(self):
        self.is_draw_4 = False
        self.color = "black"
        self.number = -1
        self.drawn = False

    def draw(self,win):
        if self.drawn:
            return
        if self.is_draw_4 == False:
            filename = CARDS_DIR+"wild.gif"
        else:
            filename = CARDS_DIR+"wildDraw4.gif"
        self.card = Image(Point(0, 0), filename)
        self.card.draw(win)
        self.drawn = True

    def undraw(self):
        self.card.undraw()

    def move_to(self,x,y):
        center = self.card.getAnchor()
        dx = x - center.getX()
        dy = y - center.getY()
        self.move(dx,dy)

    def move(self,dx,dy):
        self.card.move(dx,dy)

    def is_clicked(self,p):
        center = self.card.getAnchor()
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

class ReverseCard:
    def __init__(self,c):
        self.color = c
        self.number = -1
        self.drawn = False

    def draw(self,win):
        if self.drawn:
            return
        filename = CARDS_DIR+"{0}Reverse.gif".format(self.color)
        self.card = Image(Point(0, 0), filename)
        self.card.draw(win)
        self.drawn = True


    def undraw(self):
        self.card.undraw()

    def move_to(self,x,y):
        center = self.card.getAnchor()
        dx = x - center.getX()
        dy = y - center.getY()
        self.move(dx,dy)

    def move(self,dx,dy):
        self.card.move(dx,dy)

    def is_clicked(self,p):
        center = self.card.getAnchor()
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
    
class SkipCard:
    def __init__(self,c):
        self.color = c
        self.number = -1
        self.drawn = False

    def draw(self,win):
        if self.drawn:
            return
        filename = CARDS_DIR+"{0}Skip.gif".format(self.color)
        self.card = Image(Point(0, 0), filename)
        self.card.draw(win)
        self.drawn = True


    def undraw(self):
        self.card.undraw()

    def move_to(self,x,y):
        center = self.card.getAnchor()
        dx = x - center.getX()
        dy = y - center.getY()
        self.move(dx,dy)

    def move(self,dx,dy):
        self.card.move(dx,dy)

    def is_clicked(self,p):
        center = self.card.getAnchor()
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

class Draw2Card:
    def __init__(self,c):
        self.color = c
        self.number = -1
        self.drawn = False

    def draw(self,win):
        if self.drawn:
            return
        filename = CARDS_DIR+"{0}Draw2.gif".format(self.color)
        self.card = Image(Point(0, 0), filename)
        self.card.draw(win)
        self.drawn = True


    def undraw(self):
        self.card.undraw()

    def move_to(self,x,y):
        center = self.card.getAnchor()
        dx = x - center.getX()
        dy = y - center.getY()
        self.move(dx,dy)

    def move(self,dx,dy):
        self.card.move(dx,dy)

    def is_clicked(self,p):
        center = self.card.getAnchor()
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
