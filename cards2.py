from random import randint, shuffle
from graphics import *
from string import ascii_letters

CARD_WIDTH = 10
CARD_HEIGHT = 15

# represents a standard UNO card 
class StandardCard:
    #object constructor that initializes the variables (color and number) 
    def __init__(self,c,n):
        self.color = c
        self.number = n
        self.drawn = False

    def draw(self,win):#draws the 10 X 15 standard card
        if self.drawn:
            return
        self.rect2 = Rectangle(Point(-1,-1),Point(CARD_WIDTH + 1,CARD_HEIGHT + 1))
        self.rect2.draw(win)
        self.rect2.setFill('white')
        self.rect = Rectangle(Point(0,0),Point(CARD_WIDTH,CARD_HEIGHT))
        self.rect.draw(win)
        self.rect.setFill(self.color)
        self.oval = Oval(Point(1,1),Point(9,14))
        self.oval.setFill('white')
        self.oval.draw(win)
        self.text = Text(Point(CARD_WIDTH/2,CARD_HEIGHT/2),self.number)
        self.text.setFill(self.color)
        self.text.setStyle('bold')
        self.text.setSize(25)
        self.text.draw(win)
        self.text2 = Text(Point(1,14),self.number)
        self.text2.setFill('white')
        self.text2.setStyle('bold')
        self.text2.setSize(9)
        self.text2.draw(win)
        self.text3 = Text(Point(9,1),self.number)
        self.text3.setFill('white')
        self.text3.setStyle('bold')
        self.text3.setSize(9)
        self.text3.draw(win)
        self.drawn = True

    def undraw(self): #undraws the standard card in the discard pile when another card is placed on top
        self.oval.undraw()
        self.rect2.undraw()
        self.rect.undraw()
        self.text.undraw()
        self.text2.undraw()
        self.text3.undraw()

    def move_to(self,x,y): #centers the cards
        center = self.rect.getCenter()
        dx = x - center.getX()
        dy = y - center.getY()
        self.move(dx,dy)

    def move(self,dx,dy): #moves all the components of the card together
        self.text3.move(dx,dy)
        self.text2.move(dx,dy)
        self.text.move(dx,dy)
        self.oval.move(dx,dy)
        self.rect.move(dx,dy)
        self.rect2.move(dx,dy)

    def is_clicked(self,p): #raises the clicked card
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

#retuns the card as a string
    def as_string(self):
        return self.color + " " + str(self.number)
      
#represents a wild card
class WildCard:
    #object constructor that initializes the color as black and number as -1
    def __init__(self):
        self.is_draw_4 = False
        self.color = "black"
        self.number = -1
        self.drawn = False

    def draw(self,win):#draws the 10 X 15 wild card
        if self.drawn:
            return
        self.rect2 = Rectangle(Point(-1,-1),Point(CARD_WIDTH + 1,CARD_HEIGHT + 1))
        self.rect2.draw(win)
        self.rect2.setFill('white')
        self.rect = Rectangle(Point(0,0),Point(CARD_WIDTH,CARD_HEIGHT))
        self.rect.draw(win)
        self.rect.setFill(self.color)
        self.oval = Oval(Point(1,1),Point(9,14))
        self.oval.setFill('white')
        self.oval.draw(win)
        self.block1 = Rectangle(Point(3.5,5),Point(5,7.5))
        self.block1.setFill('red')
        self.block1.draw(win)
        self.block2 = Rectangle(Point(5,5),Point(6.5,7.5))
        self.block2.setFill('yellow')
        self.block2.draw(win)
        self.block3 = Rectangle(Point(5,7.5),Point(6.5,10))
        self.block3.setFill('green')
        self.block3.draw(win)
        self.block4 = Rectangle(Point(3.5,7.5),Point(5,10))
        self.block4.setFill('blue')
        self.block4.draw(win)
        self.text = Text(Point(CARD_WIDTH/2,CARD_HEIGHT/2),"Wild")
        self.text.setFill('black')
        self.text.setStyle('bold')
        self.text.setSize(19)
        self.text.draw(win)
        self.drawn = True
        if self.is_draw_4:
           self.text3 = Text(Point(1,14),"+4")
           self.text3.setFill('white')
           self.text3.setStyle('bold')
           self.text3.setSize(9)
           self.text3.draw(win)
           self.text4 = Text(Point(9,1),"+4")
           self.text4.setFill('white')
           self.text4.setStyle('bold')
           self.text4.setSize(9)
           self.text4.draw(win)

    def undraw(self):#undraws the wild card when another card is placed on top of it in the discard pile
        self.rect2.undraw()
        self.rect.undraw()
        self.oval.undraw()
        self.block1.undraw()
        self.block2.undraw()
        self.block3.undraw()
        self.block4.undraw()
        self.text.undraw()
        if self.is_draw_4:
           self.text3.undraw()
           self.text4.undraw()

    def move_to(self,x,y):#centers the cards
        center = self.rect.getCenter()
        dx = x - center.getX()
        dy = y - center.getY()
        self.move(dx,dy)

    def move(self,dx,dy):#moves all the components of the wild card together.
        self.text.move(dx,dy)
        self.block4.move(dx,dy)
        self.block3.move(dx,dy)
        self.block2.move(dx,dy)
        self.block1.move(dx,dy)
        self.oval.move(dx,dy)
        self.rect.move(dx,dy)
        self.rect2.move(dx,dy)
        if self.is_draw_4:
           self.text3.move(dx,dy)
           self.text4.move(dx,dy)

    def is_clicked(self,p):#raises the wild card using point(x,y) from the click
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

    def as_string(self):#returns strings to name the different wild cards
        if self.is_draw_4 == False:
            return "wild"
        else:
            return "wild draw 4"

#represents a reverse card
class ReverseCard:
    #object constructor that initializes the color as the c parameter and the number -1
    def __init__(self,c):
        self.color = c
        self.number = -1
        self.drawn = False

   #draws a 10 X 15 reverse card
    def draw(self,win):
        if self.drawn:
            return
        self.rect2 = Rectangle(Point(-1,-1),Point(CARD_WIDTH + 1,CARD_HEIGHT + 1))
        self.rect2.draw(win)
        self.rect2.setFill('white')
        self.rect = Rectangle(Point(0,0),Point(CARD_WIDTH,CARD_HEIGHT))
        self.rect.draw(win)
        self.rect.setFill(self.color)
        self.oval = Oval(Point(1,1),Point(9,14))
        self.oval.setFill('white')
        self.oval.draw(win)
        self.text = Text(Point(3,14),"Reverse")
        self.text.setFill('white')
        self.text.setStyle('bold')
        self.text.setSize(5)
        self.text.draw(win)
        self.text2 = Text(Point(8,1),"Reverse")
        self.text2.setFill('white')
        self.text2.setStyle('bold')
        self.text2.setSize(5)
        self.text2.draw(win)
        self.l = Line(Point(3,CARD_HEIGHT/4),Point(CARD_WIDTH/2+1.5,7.3))
        self.l.setFill(self.color)
        self.l.setWidth(12)
        self.l.setArrow("first")
        self.l.draw(win)
        self.l2 = Line(Point(CARD_WIDTH/2-1.5,7.3),Point(7,3*CARD_HEIGHT/4))
        self.l2.setFill(self.color)
        self.l2.setWidth(12)
        self.l2.setArrow("last")
        self.l2.draw(win)
        self.l3 = Line(Point(3.75,CARD_HEIGHT/4+1.9),Point(CARD_WIDTH/2+.8,8.15))
        self.l3.setWidth(3)
        self.l3.draw(win)
        self.l4 = Line(Point(3,CARD_HEIGHT/4+2.3),Point(3.73,CARD_HEIGHT/4+1.6))
        self.l4.setWidth(2)
        self.l4.draw(win)
        self.l5 = Line(Point(3,CARD_HEIGHT/4+.3),Point(3,CARD_HEIGHT/4+2.3))
        self.l5.draw(win)
        self.l6 = Line(Point(CARD_WIDTH/2-1.8,8.4),Point(5.4,3*CARD_HEIGHT/4-.45))
        self.l6.move(-.15,-.05)
        self.l6.setWidth(2)
        self.l6.draw(win)
        self.l7 = Line(Point(4.9,3*CARD_HEIGHT/4-.2),Point(5.4,3*CARD_HEIGHT/4-.6))
        self.l7.setWidth(2)
        self.l7.draw(win)
        self.l8 = Line(Point(4.9,3*CARD_HEIGHT/4-.2),Point(7,3*CARD_HEIGHT/4-.2))
        self.l8.setWidth(3)
        self.l8.draw(win)     
        self.drawn = True


    def undraw(self): #undraws the reverse card and its components so another card can be placed on top in the discard pile
        self.rect2.undraw()
        self.rect.undraw()
        self.oval.undraw()
        self.text.undraw()
        self.text2.undraw()
        self.l.undraw()
        self.l2.undraw()
        self.l3.undraw()
        self.l4.undraw()
        self.l5.undraw()
        self.l6.undraw()
        self.l7.undraw()
        self.l8.undraw()

    def move_to(self,x,y): #centers the cards
        center = self.rect.getCenter()
        dx = x - center.getX()
        dy = y - center.getY()
        self.move(dx,dy)

    def move(self,dx,dy): #moves all the components of the reverse card together
        self.l8.move(dx,dy)
        self.l7.move(dx,dy)
        self.l6.move(dx,dy)
        self.l5.move(dx,dy)
        self.l4.move(dx,dy)
        self.l3.move(dx,dy)
        self.l2.move(dx,dy)
        self.l.move(dx,dy)
        self.text2.move(dx,dy)
        self.text.move(dx,dy)
        self.oval.move(dx,dy)
        self.rect.move(dx,dy)
        self.rect2.move(dx,dy)

    def is_clicked(self,p): #moves the reverse card when it is clicked
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

    def as_string(self): #returns the reverse card as a string (ex. red reverse)
        return self.color + " reverse"
    
class SkipCard: #represents a skip card
    def __init__(self,c):#object constructor that initiaizes the parameter c as the color and the number as -1
        self.color = c
        self.number = -1
        self.drawn = False

    def draw(self,win):#draws a 10 X 15 skip card
        if self.drawn:
            return
        self.rect2 = Rectangle(Point(-1,-1),Point(CARD_WIDTH + 1,CARD_HEIGHT + 1))
        self.rect2.draw(win)
        self.rect2.setFill('white')
        self.rect = Rectangle(Point(0,0),Point(CARD_WIDTH,CARD_HEIGHT))
        self.rect.draw(win)
        self.rect.setFill(self.color)
        self.oval = Oval(Point(1,1),Point(9,14))
        self.oval.setFill('white')
        self.oval.draw(win)
        self.c1 = Circle(Point(CARD_WIDTH/2,CARD_HEIGHT/2),3)
        self.c1.setFill(self.color)
        self.c1.draw(win)
        self.c2 = Circle(Point(CARD_WIDTH/2,CARD_HEIGHT/2),2)
        self.c2.setFill('white')
        self.c2.draw(win)
        self.text = Text(Point(2,14),"Skip")
        self.text.setFill('white')
        self.text.setStyle('bold')
        self.text.setSize(9)
        self.text.draw(win)
        self.text2 = Text(Point(8,1),"Skip")
        self.text2.setFill('white')
        self.text2.setStyle('bold')
        self.text2.setSize(9)
        self.text2.draw(win)
        self.l = Line(Point(3,5.5),Point(7,9.5))
        self.l.setFill(self.color)
        self.l.setWidth(4)
        self.l.draw(win)
        self.l2 = Line(Point(3.3,6.5),Point(5.95,9.1))
        self.l2.draw(win)
        self.l3 = Line(Point(4.2,6.1),Point(6.8,8.8))
        self.l3.draw(win)
        self.drawn = True


    def undraw(self): #undraws the skip card when another card is placed on top of it in the discard pile
        self.rect2.undraw()
        self.rect.undraw()
        self.oval.undraw()
        self.c1.undraw()
        self.c2.undraw()
        self.text.undraw()
        self.text2.undraw()
        self.l.undraw()
        self.l2.undraw()
        self.l3.undraw()

    def move_to(self,x,y): #centers the cards
        center = self.rect.getCenter()
        dx = x - center.getX()
        dy = y - center.getY()
        self.move(dx,dy)

    def move(self,dx,dy): #moves the card's components together
        self.l3.move(dx,dy)
        self.l2.move(dx,dy)
        self.l.move(dx,dy)
        self.text2.move(dx,dy)
        self.text.move(dx,dy)
        self.c2.move(dx,dy)
        self.c1.move(dx,dy)
        self.oval.move(dx,dy)
        self.rect.move(dx,dy)
        self.rect2.move(dx,dy)

    def is_clicked(self,p): #moves the card when it is clicked
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

    def as_string(self): #returns the skip card as a string
        return self.color + " skip"

class Draw2Card: # represents a draw 2 card
    def __init__(self,c):#object constructor that initializes the c parameter as the color and -1 as the number
        self.color = c
        self.number = -1
        self.drawn = False

    def draw(self,win):#draws a 10 X 15 draw 2 card
        if self.drawn:
            return
        self.rect2 = Rectangle(Point(-1,-1),Point(CARD_WIDTH + 1,CARD_HEIGHT + 1))
        self.rect2.draw(win)
        self.rect2.setFill('white')
        self.rect = Rectangle(Point(0,0),Point(CARD_WIDTH,CARD_HEIGHT))
        self.rect.draw(win)
        self.rect.setFill(self.color)
        self.oval = Oval(Point(1,1),Point(9,14))
        self.oval.setFill('white')
        self.oval.draw(win)
        self.r = Rectangle(Point(CARD_WIDTH/2-1,CARD_HEIGHT/2+4),Point(CARD_WIDTH/2+2,CARD_HEIGHT/2))
        self.r.setFill('white')
        self.r.move(.5,-1)
        self.r.draw(win)
        self.r3 = Rectangle(Point(CARD_WIDTH/2,CARD_HEIGHT/2+2.5),Point(CARD_WIDTH/2+2,CARD_HEIGHT/2-.5))
        self.r3.setFill(self.color)
        self.r3.draw(win)
        self.r2 = self.r.clone()
        self.r2.move(-2,-2)
        self.r2.draw(win)
        self.r4 = self.r3.clone()
        self.r4.move(-2,-2)
        self.r4.draw(win)
        self.t = Text(Point(1,14),"+2")
        self.t.setFill('white')
        self.t.setStyle('bold')
        self.t.setSize(9)
        self.t.draw(win)
        self.t2 = Text(Point(9,1),"+2")
        self.t2.setFill('white')
        self.t2.setStyle('bold')
        self.t2.setSize(9)
        self.t2.draw(win)
        self.drawn = True


    def undraw(self): #undraws the draw 2 card when anothe card is placed on top of it in the discard pile
        self.rect2.undraw()
        self.rect.undraw()
        self.oval.undraw()
        self.r.undraw()
        self.r2.undraw()
        self.r3.undraw()
        self.r4.undraw()
        self.t.undraw()
        self.t2.undraw()

    def move_to(self,x,y): #centers the cards
        center = self.rect.getCenter()
        dx = x - center.getX()
        dy = y - center.getY()
        self.move(dx,dy)

    def move(self,dx,dy): #moves all card components together
        self.t2.move(dx,dy)
        self.t.move(dx,dy)
        self.r4.move(dx,dy)
        self.r3.move(dx,dy)
        self.r2.move(dx,dy)
        self.r.move(dx,dy)
        self.oval.move(dx,dy)
        self.rect.move(dx,dy)
        self.rect2.move(dx,dy)

    def is_clicked(self,p): #moves the draw 2 card when it is clicked
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

    def as_string(self): #returns the draw 2 card as a string
        return self.color + " draw 2"
