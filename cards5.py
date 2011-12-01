from random import randint, shuffle
from graphics import *
from string import ascii_letters

CARD_WIDTH = 10
CARD_HEIGHT = 15

##CREATE STANDARD CARD##
class StandardCard:
    def __init__(self,c,n):
        self.color = c
        self.number = n
        self.drawn = False
   ##Draws standard card##
    def draw(self,win):
       if self.drawn:
          return

       self.main_card = []
       card2 = Rectangle(Point(3,14), Point(9,3))
       card2.setFill(self.color)
       card2.draw(win)
       self.main_card.append(card2)
       

       
       rec1 = Rectangle(Point(1,16), Point(11,14))
       rec1.setFill('black')
       rec1.draw(win)
       self.main_card.append(rec1)
       

       rec2 = Rectangle(Point(9,14), Point(11,3))
       rec2.setFill('black')
       rec2.draw(win)
       self.main_card.append(rec2)

       rec3 = Rectangle(Point(3,3), Point(11,1))
       rec3.setFill('black')
       rec3.draw(win)
       self.main_card.append(rec3)

       rec4 = Rectangle(Point(1,14), Point(3,1))
       rec4.setFill('black')
       rec4.draw(win)
       self.main_card.append(rec4)

       rec5 = Rectangle(Point(1,11), Point(11,6))
       rec5.setFill('black')
       rec5.draw(win)
       self.main_card.append(rec5)

       uno = Text(Point(6,8.5), "UNO")
       uno.setSize(10)
       uno.setStyle('bold')
       uno.setFill('white')
       uno.draw(win)
       self.main_card.append(uno)

       number1 = Text(Point(2,14.5), self.number)
       number1.setSize(10)
       number1.setStyle('bold')
       number1.setFill('white')
       number1.draw(win)
       self.main_card.append(number1)

       number2 = Text(Point(10, 2.5), self.number)
       number2.setSize(10)
       number2.setStyle('bold')
       number2.setFill('white')
       number2.draw(win)
       self.main_card.append(number2)

       self.drawn = True
   ##Undraws card##
    def undraw(self):
       for obj in self.main_card:
          obj.undraw()

   ##moves card##
    def move_to(self,x,y):
        center = self.main_card[0].getCenter()
        dx = x - center.getX()
        dy = y - center.getY()
        self.move(dx,dy)



    def move(self,dx,dy):
       for obj in self.main_card:
          obj.move(dx,dy)

    def is_clicked(self,p):
        center = self.main_card[0].getCenter()
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
##CREATES WILDCARD##
class WildCard:
    def __init__(self):
        self.is_draw_4 = False
        self.color = "black"
        self.number = -1
        self.drawn = False
##Draws wildcard##
    def draw(self,win):
        if self.drawn:
            return
 
        self.graphics = []
        card = Rectangle(Point(1, 1), Point(11,16))
        card.draw(win)
        self.graphics.append(card)

        rec1 = Rectangle(Point(1,16), Point(11,14))
        rec1.setFill('black')
        rec1.draw(win)
        self.graphics.append(rec1)

        rec2 = Rectangle(Point(9,14), Point(11,3))
        rec2.setFill('black')
        rec2.draw(win)
        self.graphics.append(rec2)

        rec3 = Rectangle(Point(3,3), Point(11,1))
        rec3.setFill('black')
        rec3.draw(win)
        self.graphics.append(rec3)

        rec4 = Rectangle(Point(1,14), Point(3,1))
        rec4.setFill('black')
        rec4.draw(win)
        self.graphics.append(rec4)

        rec5 = Rectangle(Point(1,11), Point(11,6))
        rec5.setFill('black')
        rec5.draw(win)
        self.graphics.append(rec5)

        ##WILD##

        wild = Text(Point(6,8.5), "WILD")
        wild.setSize(10)
        wild.setFill('white')
        wild.draw(win)
        self.graphics.append(wild)

        rec1 = Rectangle(Point(3,14), Point(6,11))
        rec1.setFill('red')
        rec1.draw(win)
        self.graphics.append(rec1)

        rec2 = Rectangle(Point(6,14), Point(9,11))
        rec2.setFill('blue')
        rec2.draw(win)
        self.graphics.append(rec2)

        rec3 = Rectangle(Point(3,6), Point(6,3))
        rec3.setFill('green')
        rec3.draw(win)
        self.graphics.append(rec3)

        rec4 = Rectangle(Point(6,6), Point(9,3))
        rec4.setFill('yellow')
        rec4.draw(win)
        self.graphics.append(rec4)
         
        self.drawn = True
##Undraws wildcard##
    def undraw(self):
       for obj in self.graphics:
          obj.undraw()
   ##Moves wildcard##
    def move_to(self,x,y):
        center = self.graphics[0].getCenter()
        dx = x - center.getX()
        dy = y - center.getY()
        self.move(dx,dy)

    def move(self,dx,dy):
       for obj in self.graphics:
          obj.move(dx,dy)

    def is_clicked(self,p):
        center = self.graphics[0].getCenter()
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
##CREATES REVERSE CARD##
class ReverseCard:
    def __init__(self,c):
        self.color = c
        self.number = -1
        self.drawn = False

    def draw(self,win):
        if self.drawn:
            return
         
        self.reverse = []
        
        card2 = Rectangle(Point(3,14), Point(9,3))
        card2.setFill(self.color)
        card2.draw(win)
        self.reverse.append(card2)
       

       
        rec1 = Rectangle(Point(1,16), Point(11,14))
        rec1.setFill('black')
        rec1.draw(win)
        self.reverse.append(rec1)
       

        rec2 = Rectangle(Point(9,14), Point(11,3))
        rec2.setFill('black')
        rec2.draw(win)
        self.reverse.append(rec2)

        rec3 = Rectangle(Point(3,3), Point(11,1))
        rec3.setFill('black')
        rec3.draw(win)
        self.reverse.append(rec3)

        rec4 = Rectangle(Point(1,14), Point(3,1))
        rec4.setFill('black')
        rec4.draw(win)
        self.reverse.append(rec4)

        rec5 = Rectangle(Point(1,11), Point(11,6))
        rec5.setFill('black')
        rec5.draw(win)
        self.reverse.append(rec5)

        uno = Text(Point(6,8.5), "UNO")
        uno.setSize(10)
        uno.setStyle('bold')
        uno.setFill('white')
        uno.draw(win)
        self.reverse.append(uno)
##Numbers on card##
        number1 = Text(Point(2,14.5), self.number)
        number1.setSize(10)
        number1.setStyle('bold')
        number1.setFill('white')
        number1.draw(win)
        self.reverse.append(number1)

        number2 = Text(Point(10, 2.5), self.number)
        number2.setSize(10)
        number2.setStyle('bold')
        number2.setFill('white')
        number2.draw(win)
        self.reverse.append(number2)
##Sign on card##
        rev = Text(Point(6,8.5), "<- REVERSE ->")
        rev.setSize(10)
        rev.setFill('white')
        rev.draw(win)
        self.reverse.append(rev)


        self.drawn = True

   ##Undraws card##    
    def undraw(self):
       for obj in self.reverse:
          obj.undraw()
          
##Moves Card##
    def move_to(self,x,y):
        center = self.reverse[0].getCenter()
        dx = x - center.getX()
        dy = y - center.getY()
        self.move(dx,dy)

    def move(self,dx,dy):
        self.text.move(dx,dy)
        self.reverse.move(dx,dy)

    def is_clicked(self,p):
        center = self.reverse[0].getCenter()
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
##SKIP CARD##   
class SkipCard:
    def __init__(self,c):
        self.color = c
        self.number = -1
        self.drawn = False
##DRAWING THE SKIP CARD##
    def draw(self,win):
        if self.drawn:
            return

        self.skip = []
        
        card2 = Rectangle(Point(3,14), Point(9,3))
        card2.setFill(self.color)
        card2.draw(win)
        self.skip.append(card2)
      
        rec1 = Rectangle(Point(1,16), Point(11,14))
        rec1.setFill('black')
        rec1.draw(win)
        self.skip.append(rec1)
       

        rec2 = Rectangle(Point(9,14), Point(11,3))
        rec2.setFill('black')
        rec2.draw(win)
        self.skip.append(rec2)

        rec3 = Rectangle(Point(3,3), Point(11,1))
        rec3.setFill('black')
        rec3.draw(win)
        self.skip.append(rec3)

        rec4 = Rectangle(Point(1,14), Point(3,1))
        rec4.setFill('black')
        rec4.draw(win)
        self.skip.append(rec4)

        rec5 = Rectangle(Point(1,11), Point(11,6))
        rec5.setFill('black')
        rec5.draw(win)
        self.skip.append(rec5)
##draws sign on card##
        uno = Text(Point(6,8.5), "UNO")
        uno.setSize(10)
        uno.setStyle('bold')
        uno.setFill('white')
        uno.draw(win)
        self.skip.append(uno)
##Number/letter on card##
        number1 = Text(Point(2,14.5), "S")
        number1.setSize(10)
        number1.setStyle('bold')
        number1.setFill('white')
        number1.draw(win)
        self.skip.append(number1)

        number2 = Text(Point(10, 2.5), "S")
        number2.setSize(10)
        number2.setStyle('bold')
        number2.setFill('white')
        number2.draw(win)
        self.skip.append(number2)
##Draws sign on card##
        rev = Text(Point(6,8.5), "SKIP")
        rev.setSize(10)
        rev.setFill('white')
        rev.draw(win)
        self.skip.append(rev)

        self.drawn = True



##UNDRAW SKIP CARD##        
    def undraw(self):
       for obj in self.skip:
          obj.undraw()

    def move_to(self,x,y):
        center = self.skip[0].getCenter()
        dx = x - center.getX()
        dy = y - center.getY()
        self.move(dx,dy)
##MOVE SKIP CARD##
    def move(self,dx,dy):
        self.text.move(dx,dy)
        self.skip.move(dx,dy)
##CHECKS TO SEE IF CARD IS CLICKED##
    def is_clicked(self,p):
        center = self.skip[0].getCenter()
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
##CREATES DRAW 2 CARD##
class Draw2Card:
    def __init__(self,c):
        self.color = c
        self.number = -1
        self.drawn = False

##DRAWS CARD##
    def draw(self,win):
        if self.drawn:
            return

        self.draw2 = []
        
        card2 = Rectangle(Point(3,14), Point(9,3))
        card2.setFill(self.color)
        card2.draw(win)
        self.draw2.append(card2)
      
        rec1 = Rectangle(Point(1,16), Point(11,14))
        rec1.setFill('black')
        rec1.draw(win)
        self.draw2.append(rec1)
       

        rec2 = Rectangle(Point(9,14), Point(11,3))
        rec2.setFill('black')
        rec2.draw(win)
        self.draw2.append(rec2)

        rec3 = Rectangle(Point(3,3), Point(11,1))
        rec3.setFill('black')
        rec3.draw(win)
        self.draw2.append(rec3)

        rec4 = Rectangle(Point(1,14), Point(3,1))
        rec4.setFill('black')
        rec4.draw(win)
        self.draw2.append(rec4)

        rec5 = Rectangle(Point(1,11), Point(11,6))
        rec5.setFill('black')
        rec5.draw(win)
        self.draw2.append(rec5)
##DRAWS SIGN ON CARD##

        uno = Text(Point(6,8.5), "DRAW 2")
        uno.setSize(10)
        uno.setStyle('bold')
        uno.setFill('white')
        uno.draw(win)
        self.skip.append(uno)
##Number/letter on card##
        number1 = Text(Point(2,14.5), "+2")
        number1.setSize(10)
        number1.setStyle('bold')
        number1.setFill('white')
        number1.draw(win)
        self.skip.append(number1)

        number2 = Text(Point(10, 2.5), "+2")
        number2.setSize(10)
        number2.setStyle('bold')
        number2.setFill('white')
        number2.draw(win)
        self.skip.append(number2)

        self.drawn = True
##Undraws card##
    def undraw(self):
       for obj in self.draw2:
          obj.undraw()
##Moves card##
    def move_to(self,x,y):
        center = self.draw2[0].getCenter()
        dx = x - center.getX()
        dy = y - center.getY()
        self.move(dx,dy)

    def move(self,dx,dy):
        self.text.move(dx,dy)
        self.draw2.move(dx,dy)

    def is_clicked(self,p):
        center = self.draw2[0].getCenter()
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
        return self.color + " Draw 2"
