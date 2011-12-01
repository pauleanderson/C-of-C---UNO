from random import randint, shuffle
from graphics import *
from string import ascii_letters

CARD_WIDTH = 10
CARD_HEIGHT = 15

class StandardCard:
    def __init__(self,c,n):
        self.color = c
        self.number = n
        self.drawn = False
#Draws the Card in window
    def draw(self,win):
        if self.drawn:
            return
        self.rect = Rectangle(Point(0,0),Point(CARD_WIDTH,CARD_HEIGHT))
        self.rect.draw(win)
        self.circ = Circle(Point(CARD_WIDTH/2,CARD_HEIGHT/2),CARD_WIDTH/2)
        self.circ.draw(win)
        self.circ.setFill("white")
        self.rect.setFill(self.color)
        self.text = Text(Point(CARD_WIDTH/2,CARD_HEIGHT/2),self.number)
        self.text.setFill(self.color)
        self.text.draw(win)
        self.drawn = True
#Undraws the Card
    def undraw(self):
        self.rect.undraw()
        self.circ.undraw()
        self.text.undraw()
#Moves card
    def move_to(self,x,y):
        center = self.rect.getCenter()
        dx = x - center.getX()
        dy = y - center.getY()
        self.move(dx,dy)

    def move(self,dx,dy):
        self.text.move(dx,dy)
        self.rect.move(dx,dy)
        self.circ.move(dx,dy)
#Determines if a card is clicked
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
#Creates object a string
    def as_string(self):
        return self.color + " " + str(self.number)
#Creates Wild Card
class WildCard:
    def __init__(self):
        self.is_draw_4 = False
        self.color = "black"
        self.number = -1
        self.drawn = False
#Draw Wild Card in window
    def draw(self,win):
        if self.drawn:
            return
        self.rect = Rectangle(Point(0,0),Point(CARD_WIDTH,CARD_HEIGHT))
        self.rect.draw(win)
        self.rect.setFill(self.color)
        self.circ = Circle(Point(CARD_WIDTH/2,CARD_HEIGHT/2),CARD_WIDTH/2)
        self.circ.draw(win)
        self.circ.setFill("white")
        self.text = Text(Point(CARD_WIDTH/2,CARD_HEIGHT/2),"WILD")
        self.text.draw(win)
        self.drawn = True
#Undraw Wild Card
    def undraw(self):
        self.rect.undraw()
        self.circ.undraw()
        self.text.undraw()
#Moves Wild Card
    def move_to(self,x,y):
        center = self.rect.getCenter()
        dx = x - center.getX()
        dy = y - center.getY()
        self.move(dx,dy)

    def move(self,dx,dy):
        self.text.move(dx,dy)
        self.rect.move(dx,dy)
        self.circ.move(dx,dy)
#Determines if Wild Card was clicked
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
#Outputs as a string
    def as_string(self):
        if self.is_draw_4 == False:
            return "wild"
        else:
            return "wild draw 4"
#Creates Reverse Card
class ReverseCard:
    def __init__(self,c):
        self.color = c
        self.number = -1
        self.drawn = False
#Draws Reverse Card in window
    def draw(self,win):
        if self.drawn:
            return
        self.rect = Rectangle(Point(0,0),Point(CARD_WIDTH,CARD_HEIGHT))
        self.rect.draw(win)
        self.rect.setFill(self.color)
        self.circ = Circle(Point(CARD_WIDTH/2,CARD_HEIGHT/2),CARD_WIDTH/2)
        self.circ.draw(win)
        self.circ.setFill("white")
        self.text = Text(Point(CARD_WIDTH/2,CARD_HEIGHT/2),"Reverse")
        self.text.draw(win)
        self.text.setFill(self.color)
        self.drawn = True

#Undraws Reverse Card
    def undraw(self):
        self.rect.undraw()
        self.text.undraw()
        self.circ.undraw()
#Moves Reverse card
    def move_to(self,x,y):
        center = self.rect.getCenter()
        dx = x - center.getX()
        dy = y - center.getY()
        self.move(dx,dy)

    def move(self,dx,dy):
        self.text.move(dx,dy)
        self.rect.move(dx,dy)
        self.circ.move(dx,dy)
#Determines if Reverse card is clicked
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
#Outputs as a string
    def as_string(self):
        return self.color + " reverse"
#Creates a Skip Card    
class SkipCard:
    def __init__(self,c):
        self.color = c
        self.number = -1
        self.drawn = False
#Draws Skip Card in window
    def draw(self,win):
        if self.drawn:
            return
        self.rect = Rectangle(Point(0,0),Point(CARD_WIDTH,CARD_HEIGHT))
        self.rect.draw(win)
        self.rect.setFill(self.color)
        self.circ = Circle(Point(CARD_WIDTH/2,CARD_HEIGHT/2),CARD_WIDTH/2)
        self.circ.draw(win)
        self.circ.setFill("white")
        self.text = Text(Point(CARD_WIDTH/2,CARD_HEIGHT/2),"Skip")
        self.text.draw(win)
        self.text.setFill(self.color)
        self.drawn = True

#Undraws Skip Card
    def undraw(self):
        self.rect.undraw()
        self.text.undraw()
        self.circ.undraw()
#Moves Skip Card
    def move_to(self,x,y):
        center = self.rect.getCenter()
        dx = x - center.getX()
        dy = y - center.getY()
        self.move(dx,dy)

    def move(self,dx,dy):
        self.text.move(dx,dy)
        self.rect.move(dx,dy)
        self.circ.move(dx,dy)
#Determines if Skip Card is clicked
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
#Outputs as a string
    def as_string(self):
        return self.color + " skip"
#Creates a Draw 2 Card
class Draw2Card:
    def __init__(self,c):
        self.color = c
        self.number = -1
        self.drawn = False
#Draws Draw 2 card in window
    def draw(self,win):
        if self.drawn:
            return
        self.rect = Rectangle(Point(0,0),Point(CARD_WIDTH,CARD_HEIGHT))
        self.rect.draw(win)
        self.rect.setFill(self.color)
        self.circ = Circle(Point(CARD_WIDTH/2,CARD_HEIGHT/2),CARD_WIDTH/2)
        self.circ.draw(win)
        self.circ.setFill("white")
        self.text = Text(Point(CARD_WIDTH/2,CARD_HEIGHT/2),"Draw 2")
        self.text.draw(win)
        self.text.setFill(self.color)
        self.drawn = True

#Undraws card
    def undraw(self):
        self.rect.undraw()
        self.text.undraw()
        self.circ.undraw()
#Moves card
    def move_to(self,x,y):
        center = self.rect.getCenter()
        dx = x - center.getX()
        dy = y - center.getY()
        self.move(dx,dy)

    def move(self,dx,dy):
        self.text.move(dx,dy)
        self.rect.move(dx,dy)
        self.circ.move(dx,dy)
#Determines if Draw 2 card is clicked
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
#Outputs as a string
    def as_string(self):
        return self.color + " draw 2"
