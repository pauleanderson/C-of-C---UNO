from random import randint
from graphics import *

CARD_WIDTH = 10
CARD_HEIGHT = 15

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
        self.text = Text(Point(CARD_WIDTH/2,CARD_HEIGHT/2),"WILD")      ##CHANGED THE WILD CARD LETTERING
        self.text.setFill("white")                                      ##CHANGED THE COLOR OF 'WILD'
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
