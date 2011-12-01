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
        self.rect.setOutline("purple")
        self.text = Text(Point(CARD_WIDTH-2,CARD_HEIGHT-2),self.number)
        self.text.setFace("arial")
        self.text.setStyle("italic")
        self.text.setSize(18)
        self.text.draw(win)
        self.circ = Circle(Point(CARD_WIDTH/2,CARD_HEIGHT/2), 4)
        self.circ.setFill('black')
        self.circ.setOutline("purple")
        self.circ.draw(win)
        self.text1 = Text(Point(CARD_WIDTH/2,CARD_HEIGHT/2),self.number)
        self.text1.setTextColor(self.color)
        self.text1.setSize(22)
        self.text1.draw(win)
        self.drawn = True

    def undraw(self):
        self.rect.undraw()
        self.text.undraw()
        self.circ.undraw()
        self.text1.undraw()

    def move_to(self,x,y):
        center = self.rect.getCenter()
        dx = x - center.getX()
        dy = y - center.getY()
        self.move(dx,dy)

    def move(self,dx,dy):
        self.text.move(dx,dy)
        self.rect.move(dx,dy)
        self.circ.move(dx,dy)
        self.text1.move(dx,dy)

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
        self.rect.setFill(self.color)
        self.rect.draw(win)
        
        self.rect2 = Rectangle(Point(0,0),Point(CARD_WIDTH/2,CARD_HEIGHT/2))
        self.rect2.setFill("blue")
        self.rect2.draw(win)
        self.rect3 = Rectangle(Point(CARD_WIDTH/2,CARD_HEIGHT/2),Point(CARD_WIDTH,CARD_HEIGHT))
        self.rect3.setFill("yellow")
        self.rect3.draw(win)
        self.rect4 = Rectangle(Point(0,CARD_HEIGHT),Point(CARD_WIDTH/2,CARD_HEIGHT/2))
        self.rect4.setFill('green')
        self.rect4.draw(win)
        self.rect5 = Rectangle(Point(CARD_WIDTH/2, CARD_HEIGHT/2),Point(CARD_WIDTH,0))
        self.rect5.setFill("red")
        self.rect5.draw(win)
        self.text = Text(Point(CARD_WIDTH/2,CARD_HEIGHT/2),"WILD")
        self.text.setTextColor("white")
        self.text.setStyle("bold")
        self.text.setSize(23)
        self.text.draw(win)
        self.drawn = True
        
    def undraw(self):
        self.rect.undraw()
        self.rect2.undraw()
        self.rect3.undraw()
        self.rect4.undraw()
        self.rect5.undraw()
        self.text.undraw()

    def move_to(self,x,y):
        center = self.rect.getCenter()
        dx = x - center.getX()
        dy = y - center.getY()
        self.move(dx,dy)

    def move(self,dx,dy):
        self.text.move(dx,dy)
        self.rect.move(dx,dy)
        self.rect2.move(dx,dy)
        self.rect3.move(dx,dy)
        self.rect4.move(dx,dy)
        self.rect5.move(dx,dy)

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
