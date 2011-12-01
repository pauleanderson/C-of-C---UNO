from random import randint, shuffle
from graphics import *
from string import ascii_letters

CARD_WIDTH = 10
CARD_HEIGHT = 15

###### For the following classes: StandardCard, WildCard, ReverseCard, SkipCard, Draw2Card
###### These functions are used for the creation and manipulation of the cards:
######   draw: Draws the card on the board
######   undraw: Removes the visual representation of the card
######   move_to: Moves the visual card to a specific location
######   move: allows move_to to move the card
######   is_clicked: Determined if the card was clicked by the user

# Creates a standard card
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
        self.rect2 = Rectangle(Point(0,0),Point(CARD_WIDTH/1.1,CARD_HEIGHT/1.1))
        self.rect2.draw(win)
        self.rect2.setFill("white")
        self.text = Text(Point(CARD_WIDTH/2,CARD_HEIGHT/2),self.number)
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
        center = self.rect2.getCenter()
        dx = x - center.getX()
        dy = y - center.getY()
        self.move(dx,dy)

    def move(self,dx,dy):
        self.text.move(dx,dy)
        self.rect.move(dx,dy)
        self.rect2.move(dx,dy)

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

# Creates a wild card
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
        self.text = Text(Point(CARD_WIDTH/2,CARD_HEIGHT/2),"Wild")##########changes the wild name and color
        self.text.draw(win)
        self.text.setFill("white")
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

#Creates a reverse card
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
        self.text = Text(Point(CARD_WIDTH/2,CARD_HEIGHT/2),"Reverse")
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

# Creates a skip card    
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
        self.text = Text(Point(CARD_WIDTH/2,CARD_HEIGHT/2),"Skip")
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

# Creates a draw 2 card
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
        self.text = Text(Point(CARD_WIDTH/2,CARD_HEIGHT/2),"+2")
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
