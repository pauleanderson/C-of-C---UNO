from random import randint, shuffle
from graphics import *
from string import ascii_letters

CARD_WIDTH = 10
CARD_HEIGHT = 15

class StandardCard:
   # Initializes color and number variables.
    def __init__(self,c,n):
        self.color = c
        self.number = n
        self.drawn = False
   # A method to draw a card along with the card's number and fills in the color
    def draw(self,win):
        if self.drawn:
            return
        self.rect = Rectangle(Point(0,0),Point(CARD_WIDTH,CARD_HEIGHT))
        self.rect.draw(win)
        self.rect.setFill(self.color)
        self.circ = Circle(Point(CARD_WIDTH/2,CARD_HEIGHT/2),4)
        self.circ.draw(win)
        self.circ.setFill("Gray")
        self.text = Text(Point(CARD_WIDTH/2,CARD_HEIGHT/2),self.number)
        self.text.draw(win)
        self.text.setFill(self.color)
        self.topleft = Rectangle(Point(0,15),Point(4,12))
        self.topleft.draw(win)
        self.topleft.setFill("black")
        self.topright = Rectangle(Point(10,15),Point(6,12))
        self.topright.draw(win)
        self.topright.setFill("black")
        self.botleft = Rectangle(Point(0,0),Point(4,3))
        self.botleft.draw(win)
        self.botleft.setFill("black")
        self.botright = Rectangle(Point(6,0),Point(10,3))
        self.botright.draw(win)
        self.botright.setFill("black")
        self.drawn = True
   # A method to undraw a card so it can be moved to the hand
    def undraw(self):
        self.rect.undraw()
        self.text.undraw()
        self.circ.undraw()
        self.topleft.undraw()
        self.topright.undraw()
        self.botleft.undraw()
        self.botright.undraw()
   # A method move the card to the hand
    def move_to(self,x,y):
        center = self.rect.getCenter()
        dx = x - center.getX()
        dy = y - center.getY()
        self.move(dx,dy)
   # A method to move the text of a card that has already been moved 
    def move(self,dx,dy):
        self.text.move(dx,dy)
        self.rect.move(dx,dy)
        self.circ.move(dx,dy)
        self.topleft.move(dx,dy)
        self.topright.move(dx,dy)
        self.botleft.move(dx,dy)
        self.botright.move(dx,dy)
   # A method to determine when a card in the hand has been clicked
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
   # Returns the number and color of the card
    def as_string(self):
        return self.color + " " + str(self.number)

class WildCard:
   # Initializes the wildcard and its color
    def __init__(self):
        self.is_draw_4 = False
        self.color = "black"
        self.number = -1
        self.drawn = False
   # Determines if wildcard, if so, draws wildcard and its color and label
    def draw(self,win):
        if self.drawn:
            return
        self.rect = Rectangle(Point(0,0),Point(CARD_WIDTH,CARD_HEIGHT))
        self.rect.draw(win)
        self.rect.setFill(self.color)
        self.text = Text(Point(CARD_WIDTH/2,CARD_HEIGHT/2),self.number)
        self.text.draw(win)
        self.topleft = Rectangle(Point(0,15),Point(2,12))
        self.topleft.draw(win)
        self.topleft.setFill("yellow")
        self.topright = Rectangle(Point(10,15),Point(8,12))
        self.topright.draw(win)
        self.topright.setFill("red")
        self.botleft = Rectangle(Point(0,0),Point(2,3))
        self.botleft.draw(win)
        self.botleft.setFill("green")
        self.botright = Rectangle(Point(8,0),Point(10,3))
        self.botright.draw(win)
        self.botright.setFill("blue")
        self.middle = Circle(Point(CARD_WIDTH/2,CARD_HEIGHT/2),4)
        self.middle.draw(win)
        self.middle.setFill("white")
        self.wild = Text(Point(CARD_WIDTH/2,CARD_HEIGHT/2),"Wild")
        self.wild.draw(win)
        self.drawn = True
   # A method to undraw the wildcard
    def undraw(self):
        self.rect.undraw()
        self.text.undraw()
        self.topleft.undraw()
        self.topright.undraw()
        self.botleft.undraw()
        self.botright.undraw()
        self.middle.undraw()
        self.wild.undraw()
   # Sets location to move wildcard to hand
    def move_to(self,x,y):
        center = self.rect.getCenter()
        dx = x - center.getX()
        dy = y - center.getY()
        self.move(dx,dy)
   # Moves to the determined location
    def move(self,dx,dy):
        self.text.move(dx,dy)
        self.rect.move(dx,dy)
        self.topleft.move(dx,dy)
        self.topright.move(dx,dy)
        self.botleft.move(dx,dy)
        self.botright.move(dx,dy)
        self.middle.move(dx,dy)
        self.wild.move(dx,dy)
   # Determines which card is clicked and stores the location
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
   # Returns the label of the card
    def as_string(self):
        if self.is_draw_4 == False:
            return "wild"
        else:
            return "wild draw 4"

class ReverseCard:
   # Initializes the reversecard and its color
    def __init__(self,c):
        self.color = c
        self.number = -1
        self.drawn = False
   # Draws the reversecard and its color
    def draw(self,win):
        if self.drawn:
            return
        self.rect = Rectangle(Point(0,0),Point(CARD_WIDTH,CARD_HEIGHT))
        self.rect.draw(win)
        self.rect.setFill(self.color)
        self.text = Text(Point(CARD_WIDTH/2,CARD_HEIGHT/2),self.number)
        self.text.draw(win)
        self.circ = Circle(Point(CARD_WIDTH/2,CARD_HEIGHT/2),4)
        self.circ.draw(win)
        self.circ.setFill("white")
        self.write = Text(Point(CARD_WIDTH/2,CARD_HEIGHT/2),"Reverse")
        self.write.draw(win)
        self.drawn = True
   
   # Undraws the reversecard
    def undraw(self):
        self.rect.undraw()
        self.text.undraw()
        self.circ.undraw()
        self.write.undraw()
   # Positions the reversecard
    def move_to(self,x,y):
        center = self.rect.getCenter()
        dx = x - center.getX()
        dy = y - center.getY()
        self.move(dx,dy)
   # Moves the reversecard to hand
    def move(self,dx,dy):
        self.text.move(dx,dy)
        self.rect.move(dx,dy)
        self.circ.move(dx,dy)
        self.write.move(dx,dy)
   # Determines if the card is clicked and sets its position
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
   # Returns the cards identity
    def as_string(self):
        return self.color + " reverse"
    
class SkipCard:
   # Initializes the skipcard and color
    def __init__(self,c):
        self.color = c
        self.number = -1
        self.drawn = False
   # Draws the skipcard and its color
    def draw(self,win):
        if self.drawn:
            return
        self.rect = Rectangle(Point(0,0),Point(CARD_WIDTH,CARD_HEIGHT))
        self.rect.draw(win)
        self.rect.setFill(self.color)
        self.text = Text(Point(CARD_WIDTH/2,CARD_HEIGHT/2),self.number)
        self.text.draw(win)
        self.bigcirc = Circle(Point(CARD_WIDTH/2,CARD_HEIGHT/2),4)
        self.bigcirc.draw(win)
        self.bigcirc.setFill(white)
        self.smallcirc = Circle(Point(CARD_WIDTH/2,CARD_HEIGHT/2),3)
        self.smallcirc.draw(win)
        self.smallcirc.setFill(self.color)
        self.line = Line(Point(3,5),Point(7,10))
        self.line.draw(win)
        self.line.setFill("white")
        self.skip = Text(Point(CARD_WIDTH/2,CARD_HEIGHT/2),"Skip")
        self.skip.draw(win)
        self.drawn = True

   # Undraws the skipcard so it can be moved
    def undraw(self):
        self.rect.undraw()
        self.text.undraw()
        self.bigcirc.undraw()
        self.smallcirc.undraw()
        self.line.undraw()
        self.skip.undraw()
        
   # Sets location in the hand to move the skipcard
    def move_to(self,x,y):
        center = self.rect.getCenter()
        dx = x - center.getX()
        dy = y - center.getY()
        self.move(dx,dy)
   # Moves the skipcard
    def move(self,dx,dy):
        self.text.move(dx,dy)
        self.rect.move(dx,dy)
        self.bigcirc.move(dx,dy)
        self.smallcirc.move(dx,dy)
        self.line.move(dx,dy)
        self.skip.move(dx,dy)
   # Stores the location if skipcard is clicked
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
   # Returns the color and identification of the skipcard
    def as_string(self):
        return self.color + " skip"

class Draw2Card:
   # Initializes the draw2card variables
    def __init__(self,c):
        self.color = c
        self.number = -1
        self.drawn = False
   # Draws the draw2card
    def draw(self,win):
        if self.drawn:
            return
        self.rect = Rectangle(Point(0,0),Point(CARD_WIDTH,CARD_HEIGHT))
        self.rect.draw(win)
        self.rect.setFill(self.color)
        self.text = Text(Point(CARD_WIDTH/2,CARD_HEIGHT/2),self.number)
        self.text.draw(win)
        self.circ = Circle(Point(CARD_WIDTH/2,CARD_HEIGHT/2),4)
        self.circ.draw(win)
        self.circ.setFill("white")
        self.onecard = Rectangle(Point(6,7),Point(7,9))
        self.onecard.draw(win)
        self.onecard.setFill(self.color)
        self.twocard = Rectangle(Point(7,8),Point(8,10))
        self.twocard.draw(win)
        self.twocard.setFill(self.color)
        self.drawtwo = Text(Point(CARD_WIDTH/2,CARD_HEIGHT/2),"Draw 2")
        self.drawtwo.draw(win)
        self.drawtwo.setFill("black")
        self.drawn = True

   # Undraws the draw2card so it can be moved to a set destination
    def undraw(self):
        self.rect.undraw()
        self.text.undraw()
        self.circ.undraw()
        self.onecard.undraw()
        self.twocard.undraw()
        self.drawtwo.undraw()
   # Sets destination to move draw2card
    def move_to(self,x,y):
        center = self.rect.getCenter()
        dx = x - center.getX()
        dy = y - center.getY()
        self.move(dx,dy)
   # Moves the draw2card
    def move(self,dx,dy):
        self.text.move(dx,dy)
        self.rect.move(dx,dy)
        self.circ.move(dx,dy)
        self.onecard.move(dx,dy)
        self.twocard.move(dx,dy)
        self.drawtwo.move(dx,dy)
   # Stores location of a card if clicked
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
   # Returns identification and color 
    def as_string(self):
        return self.color + " draw 2"
