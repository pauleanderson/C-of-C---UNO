from random import randint, shuffle
from graphics import *

CARD_WIDTH = 10
CARD_HEIGHT = 15

class StandardCard:
   #creates constructor for standard cards
    def __init__(self,c,n):
        self.color = c
        self.number = n
        self.drawn = False

    def draw(self,win):
        if self.drawn:
            return #if the card is drawn, then don't draw again
        self.rect = Rectangle(Point(0,0),Point(CARD_WIDTH,CARD_HEIGHT))
        self.rect.draw(win)
        self.rect.setFill(self.color)
        self.text = Text(Point(CARD_WIDTH/2,CARD_HEIGHT/2),self.number) #draws number on card
##        self.point1 = Point(CARD_WIDTH/2,CARD_HEIGHT/2)
        self.text2 = Text(Point((CARD_WIDTH*4)/5,(CARD_HEIGHT*4)/5),self.number)
        #self.point = Point(CARD_WIDTH*4/5,CARD_HEIGHT*4/5)
##        self.point3 = Point(CARD_WIDTH/5,CARD_HEIGHT/5)
##        self.text = Text(self.point1,self.number)
        self.text.setTextColor('white')
        self.text.setStyle('bold')
        self.text.setSize(16)
        self.text.draw(win)
        self.text2.setTextColor('white')
        self.text2.setSize(10)
        self.text2.draw(win)
        self.drawn = True

    def undraw(self): #undraws card
        self.rect.undraw()
        self.text.undraw()
        self.text2.undraw()

    def move_to(self,x,y): #moves card to x, y
        center = self.rect.getCenter()
        dx = x - center.getX()
        dy = y - center.getY()
        self.move(dx,dy)

    def move(self,dx,dy):
        self.text.move(dx,dy)
        self.rect.move(dx,dy)
        self.text2.move(dx,dy)

    def is_clicked(self,p): #checks if card is clicked for use in-game
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
        if self.is_draw_4 is False:
           self.text = Text(Point(CARD_WIDTH/2,CARD_HEIGHT/2),'Wild')
           self.text.setSize(18)
        else:
           self.text = Text(Point(CARD_WIDTH/2,CARD_HEIGHT/2),'Wild \nDraw 4')
           self.text.setSize(8)
        self.text.setTextColor('white')
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
        self.text = Text(Point(CARD_WIDTH/2,CARD_HEIGHT/2),'Reverse')
        self.text.setTextColor('white')
        self.text.setSize(18)
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
        self.text = Text(Point(CARD_WIDTH/2,CARD_HEIGHT/2),'Skip')
        self.text.setTextColor('white')
        self.text.setSize(18)
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
        self.text = Text(Point(CARD_WIDTH/2,CARD_HEIGHT/2),'Draw 2')
        self.text.setTextColor('white')
        self.text.setSize(18)
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
