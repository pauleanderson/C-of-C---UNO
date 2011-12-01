from random import randint
from graphics import *

CARD_WIDTH = 10
CARD_HEIGHT = 15

class StandardCard:
    def __init__(self,c,n):
        self.color = c
        self.number = n
        self.drawn = False
#Draws a card with text in it
    def draw(self,win):
        if self.drawn:
            return
        self.rect = Rectangle(Point(0,0),Point(CARD_WIDTH,CARD_HEIGHT))
        self.rect.draw(win)
        center = self.rect.getCenter()
        self.rect.setFill(self.color)
        self.circ = Circle(Point(center.getX(),center.getY()),3)
        self.circ.setFill("White")
        self.circ.draw(win)
        self.text = Text(Point(CARD_WIDTH/2,CARD_HEIGHT/2),self.number)
        self.text.draw(win)
        self.drawn = True
#Removes the card
    def undraw(self):
        self.rect.undraw()
        self.text.undraw()
        self.circ.undraw()
#Moves the rectangle to discard
    def move_to(self,x,y):
        center = self.rect.getCenter()
        dx = x - center.getX()
        dy = y - center.getY()
        self.move(dx,dy)
#Moves the text
    def move(self,dx,dy):
        self.text.move(dx,dy)
        self.rect.move(dx,dy)
        self.circ.move(dx,dy)
#Checks to see if a card has been clicked
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
#Returns the string that is used to make a card
    def as_string(self):
        return self.color + " " + str(self.number)
#Creates the Wild Card Class
class WildCard:
#Gives the Wild Card values and a color
    def __init__(self):
        self.is_draw_4 = False
        self.color = "black"
        self.number = -1
        self.drawn = False
#Draws Wild Card
    def draw(self,win):
        if self.drawn:
            return
        self.rect = Rectangle(Point(0,0),Point(CARD_WIDTH,CARD_HEIGHT))
        self.rect.draw(win)
        self.rect.setFill(self.color)
        self.textWild=Text(Point(CARD_WIDTH/2,CARD_HEIGHT/2-2),"Wild")
        self.textWild.setFill("White")
        self.textWild2=Text(Point(CARD_WIDTH/2,CARD_HEIGHT/2+1),"R B G Y")
        self.textWild2.setFill("White")
        self.text = Text(Point(CARD_WIDTH/2,CARD_HEIGHT/2),self.number)
        self.textWild.draw(win)
        self.text.draw(win)
        self.textWild2.draw(win)
        self.drawn = True
#Removes Wild Card
    def undraw(self):
        self.rect.undraw()
        self.text.undraw()
        self.textWild.undraw()
        self.textWild2.undraw()
#Moves the Rectangle to the Discard Pile
    def move_to(self,x,y):
        center = self.rect.getCenter()
        dx = x - center.getX()
        dy = y - center.getY()
        self.move(dx,dy)
#Moves the text to the discard pile
    def move(self,dx,dy):
        self.text.move(dx,dy)
        self.rect.move(dx,dy)
        self.textWild.move(dx,dy)
        self.textWild2.move(dx,dy)
#Checks for the card to be clicked
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
#Returns whether or not the card is a wild card
    def as_string(self):
        if self.is_draw_4 == False:
            return "wild"
        else:
            return "wild draw 4"
#See Above Card Classes
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
        self.Reversetext = Text(Point(CARD_WIDTH/2,CARD_HEIGHT/2+1),"Reverse")
        self.Reversetext2 = Text(Point(CARD_WIDTH/2,CARD_HEIGHT/2+1),"esreveR")
        self.Reversetext.setFill("White")
        self.Reversetext2.setFill("White")
        self.text.draw(win)
        self.Reversetext.draw(win)
        self.Reversetext2.draw(win)
        self.drawn = True


    def undraw(self):
        self.rect.undraw()
        self.text.undraw()
        self.Reversetext.undraw()
        self.Reversetext2.undraw()

    def move_to(self,x,y):
        center = self.rect.getCenter()
        dx = x - center.getX()
        dy = y - center.getY()
        self.move(dx,dy)

    def move(self,dx,dy):
        self.text.move(dx,dy)
        self.rect.move(dx,dy)
        self.Reversetext.move(dx,dy)
        self.Reversetext2.move(dx,dy)
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
#See Above Card Classes    
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
        self.Skiptext = Text(Point(CARD_WIDTH/2,CARD_HEIGHT/2+1),"Skip")
        self.text.draw(win)
        self.Skiptext.draw(win)
        self.drawn = True


    def undraw(self):
        self.rect.undraw()
        self.text.undraw()
        self.Skiptext.undraw()

    def move_to(self,x,y):
        center = self.rect.getCenter()
        dx = x - center.getX()
        dy = y - center.getY()
        self.move(dx,dy)

    def move(self,dx,dy):
        self.text.move(dx,dy)
        self.rect.move(dx,dy)
        self.Skiptext.move(dx,dy)

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
#See Above Card Classes
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
        self.Draw2text = Text(Point(CARD_WIDTH/2,CARD_HEIGHT/2+1),"Draw 2")
        
        self.text.draw(win)
        self.Draw2text.draw(win)
        self.drawn = True


    def undraw(self):
        self.rect.undraw()
        self.text.undraw()
        self.Draw2text.undraw
    def move_to(self,x,y):
        center = self.rect.getCenter()
        dx = x - center.getX()
        dy = y - center.getY()
        self.move(dx,dy)

    def move(self,dx,dy):
        self.text.move(dx,dy)
        self.rect.move(dx,dy)
        self.Draw2text.move(dx,dy)

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
