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

    def draw(self,win):
        if self.drawn:
            return
        self.rect = Rectangle(Point(0,0),Point(CARD_WIDTH,CARD_HEIGHT))
        self.rect.draw(win)
        self.rect.setFill(self.color)
        self.oval=Oval(Point(0,0),Point(CARD_WIDTH,CARD_HEIGHT))
        self.oval.setFill('white')
        self.oval.draw(win)
        self.text = Text(Point(CARD_WIDTH/2,CARD_HEIGHT/2),self.number)
        self.text.setSize(20)
        self.text.setFill(self.color)
        self.text.draw(win)
        self.drawn = True

    def undraw(self):
        self.rect.undraw()
        self.oval.undraw()
        self.text.undraw()

    def move_to(self,x,y):
        center = self.rect.getCenter()
        dx = x - center.getX()
        dy = y - center.getY()
        self.move(dx,dy)
        
    def move(self,dx,dy):
        self.text.move(dx,dy)
        self.rect.move(dx,dy)
        self.oval.move(dx,dy)

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
        self.color = "red"
        self.number = -1
        self.drawn = False

    def draw(self,win):
        if self.drawn:
            return
        self.rect1 = Rectangle(Point(0,0),Point(CARD_WIDTH,CARD_HEIGHT))
        self.rect1.draw(win)
        self.rect1.setFill(self.color)
        self.rect2=Rectangle(Point(CARD_WIDTH,0),Point(CARD_WIDTH/2,CARD_HEIGHT/2))
        self.rect2.setFill('green')
        self.rect2.draw(win)
        self.rect3=Rectangle(Point(0,0),Point(CARD_WIDTH/2,CARD_HEIGHT/2))
        self.rect3.setFill('blue')
        self.rect3.draw(win)
        self.rect4=Rectangle(Point(0,CARD_HEIGHT),Point(CARD_WIDTH/2,CARD_HEIGHT/2))
        self.rect4.setFill('yellow')
        self.rect4.draw(win)
        self.oval=Oval(Point(0,0),Point(CARD_WIDTH,CARD_HEIGHT))
        self.oval.setFill('black')
        self.oval.draw(win)
        if self.is_draw_4 is True:
            self.text = Text(Point(CARD_WIDTH/2,CARD_HEIGHT/2),'Wild')
        elif self.is_draw_4 is False:
            self.text = Text(Point(CARD_WIDTH/2,CARD_HEIGHT/2),'+4')
        self.text.setSize(16)
        self.text.setFill('white')
        self.text.draw(win)
        self.drawn = True

    def undraw(self):
        self.rect1.undraw()
        self.rect2.undraw()
        self.rect3.undraw()
        self.rect4.undraw()
        self.oval.undraw()
        self.text.undraw()

    def move_to(self,x,y):
        center = self.rect1.getCenter()
        dx = x - center.getX()
        dy = y - center.getY()
        self.move(dx,dy)

    def move(self,dx,dy):
        self.text.move(dx,dy)
        self.rect1.move(dx,dy)
        self.rect2.move(dx,dy)
        self.rect3.move(dx,dy)
        self.rect4.move(dx,dy)
        self.oval.move(dx,dy)

    def is_clicked(self,p):
        center = self.rect1.getCenter()
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
        self.oval=Oval(Point(0,0),Point(CARD_WIDTH,CARD_HEIGHT))
        self.oval.setFill('white')
        self.oval.draw(win)
        self.text = Text(Point(CARD_WIDTH/2,CARD_HEIGHT/2),'Reverse')
        self.text.setSize(16)
        self.text.setFill(self.color)
        self.text.draw(win)
        self.drawn = True


    def undraw(self):
        self.rect.undraw()
        self.oval.undraw()
        self.text.undraw()

    def move_to(self,x,y):
        center = self.rect.getCenter()
        dx = x - center.getX()
        dy = y - center.getY()
        self.move(dx,dy)

    def move(self,dx,dy):
        self.text.move(dx,dy)
        self.oval.move(dx,dy)
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
        self.oval=Oval(Point(0,0),Point(CARD_WIDTH,CARD_HEIGHT))
        self.oval.setFill('white')
        self.oval.draw(win)
        self.text = Text(Point(CARD_WIDTH/2,CARD_HEIGHT/2),'Skip')
        self.text.setSize(16)
        self.text.setFill(self.color)
        self.text.draw(win)
        self.drawn = True


    def undraw(self):
        self.rect.undraw()
        self.oval.undraw()
        self.text.undraw()

    def move_to(self,x,y):
        center = self.rect.getCenter()
        dx = x - center.getX()
        dy = y - center.getY()
        self.move(dx,dy)

    def move(self,dx,dy):
        self.text.move(dx,dy)
        self.oval.move(dx,dy)
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
        self.oval=Oval(Point(0,0),Point(CARD_WIDTH,CARD_HEIGHT))
        self.oval.setFill('white')
        self.oval.draw(win)
        self.text = Text(Point(CARD_WIDTH/2,CARD_HEIGHT/2),'+2')
        self.text.setSize(16)
        self.text.setFill(self.color)
        self.text.draw(win)
        self.drawn = True


    def undraw(self):
        self.rect.undraw()
        self.oval.undraw()
        self.text.undraw()

    def move_to(self,x,y):
        center = self.rect.getCenter()
        dx = x - center.getX()
        dy = y - center.getY()
        self.move(dx,dy)

    def move(self,dx,dy):
        self.text.move(dx,dy)
        self.oval.move(dx,dy)
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
