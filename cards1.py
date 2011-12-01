from random import randint, shuffle
from graphics import *
from string import ascii_letters

CARD_WIDTH = 10
CARD_HEIGHT = 15

class StandardCard:
   #Standard Card object constructor: requires color and number
    def __init__(self,c,n):
        self.color = c
        self.number = n
        self.drawn = False

   #Draws the standard card
    def draw(self,win):
        if self.drawn:
            return   
        self.rect = Rectangle(Point(0,0),Point(CARD_WIDTH,CARD_HEIGHT))
        self.rect.draw(win)
        self.circ = Circle(Point(CARD_WIDTH/2,CARD_HEIGHT/2),4.5)
        self.circ.setFill('white')
        self.circ.draw(win)
        self.rect.setFill(self.color)
        self.text = Text(Point(CARD_WIDTH/2,CARD_HEIGHT/2),self.number)
        self.text.setSize(20)
        self.text.setStyle('bold')
        self.text.setTextColor(self.color)
        self.text.draw(win)
        self.CardList = []
        self.CardList.append(self.rect)
        self.CardList.append(self.circ)
        self.CardList.append(self.text)
        self.drawn = True

   #Undraws standard card
    def undraw(self):
        for graphic in self.CardList:
           graphic.undraw()

   #Determines where to move the standard card 
    def move_to(self,x,y):
        center = self.CardList[0].getCenter()
        dx = x - center.getX()
        dy = y - center.getY()
        self.move(dx,dy)

   #Moves the standard card dx,dy
    def move(self,dx,dy):
        for graphic in self.CardList:
           graphic.move(dx,dy)

   #Determines if the standard card has been clicked; True if clicked, false if not
    def is_clicked(self,p):
        center = self.CardList[0].getCenter()
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

   #Returns the color and number of a standard card as a string
    def as_string(self):
        return self.color + " " + str(self.number)

class WildCard:

   #Constructor for the Wild Card object; color and number is the same for all Wild Cards
   #Uses a boolean expression to separate Wilds from Wild Draw 4's
    def __init__(self):
        self.is_draw_4 = False
        self.color = "black"
        self.number = -1
        self.drawn = False
   #Draws the Wild Card and Wild Draw 4's
    def draw(self,win):
        if self.drawn:
            return
        if not(self.is_draw_4):
           self.rect = Rectangle(Point(0,0),Point(CARD_WIDTH,CARD_HEIGHT))
           self.rect.draw(win)
           self.box1 = Rectangle(Point(0,0),Point(CARD_WIDTH/2,CARD_HEIGHT/2))
           self.box2 = Rectangle(Point(CARD_WIDTH/2,0),Point(CARD_WIDTH,CARD_HEIGHT/2))
           self.box3 = Rectangle(Point(0,CARD_HEIGHT/2),Point(CARD_WIDTH/2,CARD_HEIGHT))
           self.box4 = Rectangle(Point(CARD_WIDTH/2,CARD_HEIGHT/2),Point(CARD_WIDTH,CARD_HEIGHT))
           self.box1.setFill('yellow')
           self.box2.setFill('green')
           self.box3.setFill('red')
           self.box4.setFill('blue')
           self.box1.draw(win)
           self.box2.draw(win)
           self.box3.draw(win)
           self.box4.draw(win)
           self.circ = Circle(Point(CARD_WIDTH/2,CARD_HEIGHT/2),4)
           self.circ.setFill('white')
           self.circ.draw(win)
           self.text = Text(Point(CARD_WIDTH/2,CARD_HEIGHT/2),'WILD')
           self.text.setSize(15)
           self.text.setStyle('bold')
           self.text.setTextColor(self.color)
           self.text.draw(win)
           self.CardList = []
           self.CardList.append(self.rect)
           self.CardList.append(self.box1)
           self.CardList.append(self.box2)
           self.CardList.append(self.box3)
           self.CardList.append(self.box4)
           self.CardList.append(self.circ)
           self.CardList.append(self.text)
           self.drawn = True
        elif self.is_draw_4:
           self.rect = Rectangle(Point(0,0),Point(CARD_WIDTH,CARD_HEIGHT))
           self.rect.draw(win)
           self.rect.setFill(self.color)
           self.circ = Circle(Point(CARD_WIDTH/2,CARD_HEIGHT/2),5)
           self.circ.setFill('white')
           self.circ.draw(win)
           self.center = self.circ.getCenter()
           x_center = self.center.getX()
           y_center = self.center.getY()
           self.box1 = Rectangle(Point(x_center - 1,y_center - 4),Point(x_center + 1,y_center - 1))
           self.box2 = Rectangle(Point(x_center - 3,y_center - 1),Point(x_center - 1,y_center + 2))
           self.box3 = Rectangle(Point(x_center - 1,y_center + 1),Point(x_center + 1,y_center + 4))
           self.box4 = Rectangle(Point(x_center + 1,y_center - 1),Point(x_center + 3,y_center + 2))
           self.box1.setFill('red')
           self.box2.setFill('blue')
           self.box3.setFill('green')
           self.box4.setFill('yellow')
           self.text1 = Text(Point(CARD_WIDTH/2,CARD_HEIGHT/2),'Draw 4')
           self.text2 = Text(Point(CARD_WIDTH/2,CARD_HEIGHT/2 + 2),'Wild')
           self.text1.setStyle('bold')
           self.text1.setTextColor(self.color)
           self.text1.setSize(12)
           self.text2.setStyle('bold')
           self.text2.setTextColor(self.color)
           self.text2.setSize(12)
           self.box1.draw(win)
           self.box2.draw(win)
           self.box3.draw(win)
           self.box4.draw(win)
           self.text1.draw(win)
           self.text2.draw(win)
           self.CardList = []
           self.CardList.append(self.rect)
           self.CardList.append(self.box1)
           self.CardList.append(self.box2)
           self.CardList.append(self.box3)
           self.CardList.append(self.box4)
           self.CardList.append(self.circ)
           self.CardList.append(self.text1)
           self.CardList.append(self.text2)
           self.drawn = True

   #Undraws Wild Cards and Wild Draw 4's
    def undraw(self):
        for graphic in self.CardList:
           graphic.undraw()
   #Determines where to move the Wild Cards and Wild Draw 4's
    def move_to(self,x,y):
        center = self.rect.getCenter()
        dx = x - center.getX()
        dy = y - center.getY()
        self.move(dx,dy)
   #Moves the Wild Cards and Wild Draw 4's dx,dy
    def move(self,dx,dy):
        for graphic in self.CardList:
           graphic.move(dx,dy)
   #Determines if the Wild Card/Wild Draw 4 card has been clicked
   #returns true = clicked, false = not clicked
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
   #Returns identity of the card, either wild or wild draw 4, as a string
    def as_string(self):
        if self.is_draw_4 == False:
            return "wild"
        else:
            return "wild draw 4"

class ReverseCard:
   #Constructs a reverse card object; color is required, number kept the same
   #for all cards 
    def __init__(self,c):
        self.color = c
        self.number = -1
        self.drawn = False
   #Draws the reverse card
    def draw(self,win):
        if self.drawn:
            return
        self.rect = Rectangle(Point(0,0),Point(CARD_WIDTH,CARD_HEIGHT))
        self.rect.draw(win)
        self.rect.setFill(self.color)
        self.circ = Circle(Point(CARD_WIDTH/2,CARD_HEIGHT/2),4.5)
        self.circ.setFill('white')
        self.circ.draw(win)
        self.arrow1 = Polygon(Point(CARD_WIDTH/2,CARD_HEIGHT/2+2),Point(CARD_WIDTH/2+2,CARD_HEIGHT/2+2),Point(CARD_WIDTH/2+2,CARD_HEIGHT/2))
        self.arrow2 = Polygon(Point(CARD_WIDTH/2,CARD_HEIGHT/2-2),Point(CARD_WIDTH/2-2,CARD_HEIGHT/2-2),Point(CARD_WIDTH/2-2,CARD_HEIGHT/2))
        self.arrow1.setFill(self.color)
        self.arrow2.setFill(self.color)
        self.arrow1.setOutline(self.color)
        self.arrow2.setOutline(self.color)
        self.arrow1.draw(win)
        self.arrow2.draw(win)
        self.box1 = Polygon(Point(CARD_WIDTH/2,CARD_HEIGHT/2),Point(CARD_WIDTH/2+1.5,CARD_HEIGHT/2+1),Point(CARD_WIDTH/2+0.5,CARD_HEIGHT/2+1.5),Point(CARD_WIDTH/2-1,CARD_HEIGHT/2+0.5))
        self.box2 = Polygon(Point(CARD_WIDTH/2,CARD_HEIGHT/2),Point(CARD_WIDTH/2-1.5,CARD_HEIGHT/2-1),Point(CARD_WIDTH/2-0.5,CARD_HEIGHT/2-1.5),Point(CARD_WIDTH/2+1,CARD_HEIGHT/2-0.5))
        self.box1.setFill(self.color)
        self.box2.setFill(self.color)
        self.box1.setOutline(self.color)
        self.box2.setOutline(self.color)
        self.box1.draw(win)
        self.box2.draw(win)
        self.CardList = []
        self.CardList.append(self.rect)
        self.CardList.append(self.circ)
        self.CardList.append(self.arrow1)
        self.CardList.append(self.arrow2)
        self.CardList.append(self.box1)
        self.CardList.append(self.box2)
        self.drawn = True

   #Undraws the reverse card
    def undraw(self):
        for graphic in self.CardList:
           graphic.undraw()
   #Determines where to move the reverse card
    def move_to(self,x,y):
        center = self.rect.getCenter()
        dx = x - center.getX()
        dy = y - center.getY()
        self.move(dx,dy)
   #Moves the reverse card dx,dy
    def move(self,dx,dy):
        for graphic in self.CardList:
           graphic.move(dx,dy)
   #Determines if the reverse card has been clicked
   #Returns true if clicked, false if not clicked
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
   #Returns the color of the card, and reverse, as a string
    def as_string(self):
        return self.color + " reverse"
    
class SkipCard:
   #Constructs a skip card object; requires color, while number
   #is kept the same for all cards
    def __init__(self,c):
        self.color = c
        self.number = -1
        self.drawn = False
   #Draws the skip card
    def draw(self,win):
        if self.drawn:
            return
        self.rect = Rectangle(Point(0,0),Point(CARD_WIDTH,CARD_HEIGHT))
        self.rect.draw(win)
        self.rect.setFill(self.color)
        self.circ = Circle(Point(CARD_WIDTH/2,CARD_HEIGHT/2),4.5)
        self.circ.setFill('white')
        self.circ.draw(win)
        self.skipcirc = Circle(Point(CARD_WIDTH/2,CARD_HEIGHT/2),3)
        self.skipcirc.setOutline(self.color)
        self.skipcirc.draw(win)
        self.skipcirc.setWidth(3)
        self.skipline = Line(Point(CARD_WIDTH/2 + 2,CARD_HEIGHT/2 + 2),Point(CARD_WIDTH/2 - 2,CARD_HEIGHT/2 - 2))
        self.skipline.setFill(self.color)
        self.skipline.setWidth(3)
        self.skipline.draw(win)
        self.CardList = []
        self.CardList.append(self.rect)
        self.CardList.append(self.circ)
        self.CardList.append(self.skipcirc)
        self.CardList.append(self.skipline)
        self.drawn = True

   #Undraws the skip card
    def undraw(self):
        for graphic in self.CardList:
           graphic.undraw()
   #Determines where to move the skip card
    def move_to(self,x,y):
        center = self.rect.getCenter()
        dx = x - center.getX()
        dy = y - center.getY()
        self.move(dx,dy)
   #Moves the skip card dx,dy
    def move(self,dx,dy):
        for graphic in self.CardList:
           graphic.move(dx,dy)
   #Determines if the skip card has been clicked
   #Returns true if clicked, false if not clicked
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
   #Returns the color of the card, and skip, as a string
    def as_string(self):
        return self.color + " skip"

class Draw2Card:
   #Constructs a Draw 2 card object; requires a color, while number
   #is kept the same for all cards
    def __init__(self,c):
        self.color = c
        self.number = -1
        self.drawn = False
   #Draws the draw 2 card
    def draw(self,win):
        if self.drawn:
            return
        self.rect = Rectangle(Point(0,0),Point(CARD_WIDTH,CARD_HEIGHT))
        self.rect.draw(win)
        self.rect.setFill(self.color)
        self.circ = Circle(Point(CARD_WIDTH/2,CARD_HEIGHT/2),4.5)
        self.circ.setFill('white')
        self.circ.draw(win)
        self.box1 = Rectangle(Point(CARD_WIDTH/2,CARD_HEIGHT/2+2),Point(CARD_WIDTH/2+2,CARD_HEIGHT/2-1))
        self.box2 = Rectangle(Point(CARD_WIDTH/2-1,CARD_HEIGHT/2),Point(CARD_WIDTH/2+1,CARD_HEIGHT/2-3))
        self.box1.setFill(self.color)
        self.box2.setFill(self.color)
        self.box1.draw(win)
        self.box2.draw(win)
        self.text = Text(Point(CARD_WIDTH/2 - 2.5,CARD_HEIGHT/2 + 0.5),'+ 2')
        self.text.setStyle('bold')
        self.text.setSize(10)
        self.text.draw(win)
        self.CardList = []
        self.CardList.append(self.rect)
        self.CardList.append(self.circ)
        self.CardList.append(self.box1)
        self.CardList.append(self.box2)
        self.CardList.append(self.text)
        self.drawn = True

   #Undraws the draw 2 card
    def undraw(self):
        for graphic in self.CardList:
           graphic.undraw()
   #Determines where to move the draw 2 card
    def move_to(self,x,y):
        center = self.rect.getCenter()
        dx = x - center.getX()
        dy = y - center.getY()
        self.move(dx,dy)
   #Moves the draw 2 card dx,dy
    def move(self,dx,dy):
        for graphic in self.CardList:
           graphic.move(dx,dy)
   #Determines if the draw 2 card has been clicked
   #Returns true if clicked, false if not clicked
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
   #Returns the color of the card and draw 2 as a string
    def as_string(self):
        return self.color + " draw 2"
