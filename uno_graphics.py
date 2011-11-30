from random import randint, shuffle
# Authors: Paul Anderson, Clayton Turner, Patrick Brewer,Your name here

from graphics import *
from string import ascii_letters
import cards1
import cards2

CARDS = cards1 # By default, we'll use these cards

CARD_WIDTH = 10
CARD_HEIGHT = 15

# We need to make this customizable or at least more flexible
USERHOME = str(os.getenv('HOME'))
if USERHOME == "None":
   USERHOME = os.getenv('USERPROFILE')
UNO_GAMES_DIR = USERHOME+"/Dropbox/UNO_Games/"

def decode(input, shift=3):
    return modify_input(input, -shift)

def encode(input, shift=3):
    return modify_input(input, shift)

def modify_input(input, shift):
    trans = str.maketrans(ascii_letters, ascii_letters[shift:] + ascii_letters[:shift])
    return input.translate(trans)

# Creates a card from a string (e.g., green 1)
def create_card(card_str):
    if card_str.find("wild") != -1:
        if card_str == "wild":
            card = CARDS.WildCard()
        elif card_str == "wild draw 4":
            card = CARDS.WildCard()
            card.is_draw_4 = True
            
    elif card_str.find("reverse") != -1:
        color = card_str.split(" ")[0]
        card = CARDS.ReverseCard(color)
    elif card_str.find("skip") != -1:
        color = card_str.split(" ")[0]
        card = CARDS.SkipCard(color)
    elif card_str.find("draw 2") != -1:
        color = card_str.split(" ")[0]
        card = CARDS.Draw2Card(color)
    else:
        color = card_str.split(" ")[0]
        number = int(card_str.split(" ")[1])
        card = CARDS.StandardCard(color,number)
    return card

class Player:
    #Constructs a player object; requires name of the player
    def __init__(self,name):
        self.name = name
        self.cards = []

    #Player inputs color and number, and the functions searches
    #through the player's hand to find a card matching the color
    #and number, then removes the card from the hand and returns
    #the selected card.
    #If a card is not found, returns None
    def play_a_card(self,color,number):
        # Exhaustive search through the cards
        for i in range(len(self.cards)):
            if (self.cards[i].as_string().find(color) >= 0 and
                self.cards[i].as_string().find(str(number)) >= 0 and
                self.cards[i].as_string().find("Draw") == -1):

                card = self.cards[i]
                self.cards.remove
                return card
        return None
      
    #Looks through the player's hand to see if any card matches the top card of the
    #discard pile in color or number. If a card can be played, returns True
    #If no card can be played, returns False.
    def can_play_card(self,discard_pile):
        discard_color = discard_pile[-1].color
        discard_number = discard_pile[-1].number
        for card in self.cards:
            if card.color == discard_color or card.number == discard_number:
                return True
        return False

    #Returns the name of the player, and the player's hand, as a string
    def as_string(self):
        card_strs = []
        for card in self.cards:
            card_strs.append(card.as_string())
        return self.name + ":" + "\t".join(card_strs)

    def sort(self):
        i = 0
        j = 0
        n = len(self.cards)
        for j in range(n):
           key = self.cards.pop(j)
           i = j - 1
           while (i >= 0 and (self.cards[i].color > key.color or
                              (self.cards[i].color == key.color and self.cards[i].number > key.number))):
              i = i -1
           self.cards.insert(i+1,key)

class Game:
    # Starts a new game with player 'name'
    # Creates three computer players
    # Creates a board object that has a random game id
    # Create a blank board
    # Initialize a new board
    # Deal the cards
    def create_new_game(self,name):
        self.p1 = Player(name)
        self.p2 = Player("Computer 1")
        self.p3 = Player("Computer 2")
        self.p4 = Player("Computer 3")

        self.board = Board(randint(1,100000))
        self.board.create_blank_board()
        self.board.initialize_new_board()
        self.deal()

    #Deals out 7 cards to each player
    def deal(self):
        for i in range(7):
            self.board.deal_one_card(self.p1)
            self.board.deal_one_card(self.p2)
            self.board.deal_one_card(self.p3)
            self.board.deal_one_card(self.p4)
            
    # Starts the game
    # Displays the name of the player,
    # how many cards the player has in his/her hand,
    # and draws the cards in the player's hand.
    def start(self,player):
        if player == self.p1:
            self.board.set_p1(self.p1)
            self.board.set_p2(self.p2)
            self.board.set_p3(self.p3)
            self.board.set_p4(self.p4)
        elif player == self.p2:
            self.board.set_p1(self.p2)
            self.board.set_p2(self.p3)
            self.board.set_p3(self.p4)
            self.board.set_p4(self.p1)
        elif player == self.p3:
            self.board.set_p1(self.p3)
            self.board.set_p2(self.p4)
            self.board.set_p3(self.p1)
            self.board.set_p4(self.p2)
        elif player == self.p4:
            self.board.set_p1(self.p4)
            self.board.set_p2(self.p1)
            self.board.set_p3(self.p2)
            self.board.set_p4(self.p3)

        self.save_game()
        
        response = ""
        while response != None:
            response = self.board.wait_for_click()
            if response == "Card Played":
                self.save_game()
            elif response == "Reload Button Clicked":
                return game_over
        return None

    #Writes the game data in a file in the UNO_GAMES directory
    def save_game(self):
        outfile = open(UNO_GAMES_DIR+str(self.board.game_id),"w")
        print(encode(self.as_string()),file=outfile,end="")
        outfile.close()

    #Reads an UNO game file with the player's cards and board
    def load_game(self,game_id):
        infile = open(UNO_GAMES_DIR+str(game_id),"r")        
        # Load the players
        lines = decode(infile.read()).split("\n")
        infile.close()
        fields = lines[-1].split(":")
        self.p4 = Player(fields[0])
        for card_str in fields[1].split("\t"):
            self.p4.cards.append(create_card(card_str))
            
        fields = lines[-2].split(":")
        self.p3 = Player(fields[0])
        for card_str in fields[1].split("\t"):
            self.p3.cards.append(create_card(card_str))

        fields = lines[-3].split(":")
        self.p2 = Player(fields[0])
        for card_str in fields[1].split("\t"):
            self.p2.cards.append(create_card(card_str))

        fields = lines[-4].split(":")
        self.p1 = Player(fields[0])
        for card_str in fields[1].split("\t"):
            self.p1.cards.append(create_card(card_str))

        self.board = Board(game_id)
        self.board.load_old_board()

    #I honestly do not know what this does
    def as_string(self):
        results = self.board.as_string()
        results += "\n" + self.p1.as_string()
        results += "\n" + self.p2.as_string()
        results += "\n" + self.p3.as_string()
        results += "\n" + self.p4.as_string()
        return results

class MsgBox:
    #Constructs a message box? Don't really know what this does either
    def __init__(self,msg):
        win = GraphWin("",600,100)
        win.setCoords(0,0,100,100)
        Text(Point(50,80),msg).draw(win)
        button = Button(50,40,"OK",win,10,20)
        while True:
            p = win.getMouse()
            if button.is_clicked(p):
                break
        win.close()

class Button:
    #Constructs the button object based on anchor point (x,y), the window,
    #the width of the button, and the height of the button
    def __init__(self,x,y,string,win,width,height):
        self.width = width
        self.height = height
        self.rect = Rectangle(Point(x-self.width/2,y-height/2),Point(x+self.width/2,y+height/2))
        self.rect.draw(win)
        self.text = Text(Point(x,y),string)
        self.text.draw(win)
        self.rect.setFill('magenta')

    #Determines if the button has been clicked
    #Returns true if clicked, false if not clicked
    def is_clicked(self,p):
        center = self.rect.getCenter()
        x1 = center.getX() - self.width/2
        x2 = center.getX() + self.width/2
        y1 = center.getY() - self.height/2
        y2 = center.getY() + self.height/2
        x = p.getX()
        y = p.getY()
        if x >= x1 and x <= x2 and y >= y1 and y <= y2:
            return True
        else:
            return False                    

# Board class
class Board:
    def __init__(self,game_id):
        self.game_id = game_id

    # Creates the graphics objects of a blank board
    def create_blank_board(self):
        self.win = GraphWin("UNO",600,600)
        self.win.setCoords(0,0,100,100)
        self.win.setBackground(color_rgb(100, 255, 100))
        self.text_p1 = Text(Point(50,10),'Computer 1: 0')
        self.text_p1.draw(self.win)
        self.text_p2 = Text(Point(10,50),'Computer 2: 0')
        self.text_p2.draw(self.win)
        self.text_p3 = Text(Point(50,90),'Computer 3: 0')
        self.text_p3.draw(self.win)
        self.text_p4 = Text(Point(90,50),'Computer 4: 0')
        self.text_p4.draw(self.win)

        self.rect_discard_pile = Rectangle(Point(80,80),Point(80+CARD_WIDTH,80+CARD_HEIGHT))
        self.rect_discard_pile.draw(self.win)
        self.rect_discard_pile.setFill('gray')
        self.text_discard_pile = Text(Point(80+CARD_WIDTH/2,80+CARD_HEIGHT/2),"Discard")
        self.text_discard_pile.draw(self.win)

        self.quit_button = Button(10,90,"Quit",self.win,8,4)
        self.reload_button = Button(10,80,"Reload",self.win,12,4)
        self.uno_button = Button(20,2,"UNO",self.win,8,4)
        self.draw_button = Button(40,2,"Draw",self.win,12,4)
        self.shift_button = Button(60,2,"Shift",self.win,12,4)
        self.sort_button = Button(80,2,"Sort",self.win,12,4)

        self.text_game_id = Text(Point(20,90),str(self.game_id))
        self.text_game_id.draw(self.win)

    #Creates the deck and discard pile
    def initialize_new_board(self):
        self.create_deck()

        self.create_discard_pile()
        self.discard_pile[-1].draw(self.win)
        self.discard_pile[-1].move_to(50,50)
        
        self.card_selected = None

    #Opens and reads an old UNO game file and displays the old game
    def load_old_board(self):
        self.create_blank_board()

        infile = open(UNO_GAMES_DIR+str(self.game_id),"r")
        lines = decode(infile.read()).split("\n")
        infile.close()
        
        deck_strs = lines[2].split(":")[1].split("\t")
        self.deck = []
        for deck_str in deck_strs:
            self.deck.append(create_card(deck_str))            

        discard_pile_strs = lines[1].split(":")[1].split("\t")
        self.discard_pile = []
        for discard_pile_str in discard_pile_strs:
            self.discard_pile.append(create_card(discard_pile_str))                    
        
        self.discard_pile[-1].draw(self.win)
        self.discard_pile[-1].move_to(50,50)

        self.card_selected = None

    #Removes one card from the deck and appends that card to the chosen player's hand
    #Returns the drawn card        
    def deal_one_card(self,p):
        if len(self.deck) == 0:
            return None
        i = randint(0,len(self.deck)-1)
        card = self.deck[i]
        p.cards.append(card)
        self.deck.remove(self.deck[i])
        return card
        
    def check_card(self,discard_card,card_to_play):
        if discard_card.color == card_to_play.color or discard_card.number == card_to_play.number:
            return True
        return False
   
    def can_play_card(self,player,discard_pile):
        discard_color = discard_pile[-1].color
        discard_number = discard_pile[-1].number
        for card in player.cards:
            if card.color == discard_color or card.number == discard_number:
                return True
        return False

    def wait_for_click(self):
        p = self.win.getMouse()
        # Check to see if card was clicked
        for card in self.p1.cards:
            if card.is_clicked(p):
                # Reset the card positions
                for i in range(len(self.p1.cards)):
                    self.p1.cards[i].move_to(self.x_positions[i],20)
                
                card.move(0,5)
                self.card_selected = card
                return "Card Clicked"

            elif self.discard_pile[-1].is_clicked(p):
                if self.card_selected != None:
                    if self.check_card(self.discard_pile[-1],self.card_selected):
                       self.discard_pile[-1].undraw()
                       self.card_selected.move_to(50,50)
                       self.p1.cards.remove(self.card_selected)
                       self.discard_pile.append(self.card_selected)
                       self.card_selected = None                    
                       self.draw_cards()
                       return "Card Played"

                return "Discard Pile Clicked"

            elif self.draw_button.is_clicked(p):
                if self.can_play_card(self.p1,self.discard_pile) == False:
                   card = self.deal_one_card(self.p1)
                   self.draw_cards()
            
            elif self.shift_button.is_clicked(p):
                card = self.p1.cards[-1]
                self.p1.cards.remove(self.p1.cards[-1])
                self.p1.cards.insert(0,card)
                self.draw_cards()
                return "Shift Button Clicked"

            elif self.sort_button.is_clicked(p):
                self.p1.sort()
                self.draw_cards()
                return "Sort Button Clicked"

            elif self.reload_button.is_clicked(p):
                return "Reload Button Clicked"

            elif self.quit_button.is_clicked(p):
                self.win.close()
                return None

        return "Other Spot Clicked"

    #Creates the UNO deck
    def create_deck(self):
        deck = []

        for i in range(10):
            for color in ['blue','green','red','yellow']:
                if i == 0:
                    card = CARDS.StandardCard(color,i)
                    deck.append(card)
                else:
                    card = CARDS.StandardCard(color,i)
                    deck.append(card)
                    card = CARDS.StandardCard(color,i)
                    deck.append(card)

        # Makes the standard wild card
        for i in range(4):
            card = CARDS.WildCard()
            deck.append(card)

        # Makes wild card that is a draw 4
        for i in range(4):
            card = CARDS.WildCard()
            card.is_draw_4 = True
            deck.append(card)
            
        # Makes Skips,Reverses, and Draw 2's 
        for color in ['blue','green','red','yellow']:
           card = CARDS.SkipCard(color)
           deck.append(card)
           card = CARDS.SkipCard(color)
           deck.append(card)
           card = CARDS.ReverseCard(color)
           deck.append(card)
           card = CARDS.ReverseCard(color)
           deck.append(card)
           card = CARDS.Draw2Card(color)
           deck.append(card)
           card = CARDS.Draw2Card(color)
           deck.append(card)
           
        self.deck = deck

    #Creates the discard pile
    def create_discard_pile(self):
        discard_pile = []
        i = randint(0,len(self.deck)-1)
        discard_pile.append(self.deck[i])
        self.deck.remove(self.deck[i])
        self.discard_pile = discard_pile

    #Displays the player's name, length of hand, and draws the cards in the player's hand
    def set_p1(self,p1):
        self.p1 = p1
        self.text_p1.setText(p1.name + ": " + str(len(p1.cards)))
        self.draw_cards()

    #Draws the cards in a player's hand
    def draw_cards(self):
        p1 = self.p1
        self.text_p1.setText(p1.name + ": " + str(len(p1.cards)))
        num_cards = len(p1.cards)
        card_width_with_buffer = CARD_WIDTH + 2
        if len(p1.cards) % 2 != 0: # Odd
            x_positions = list(range(50 - (card_width_with_buffer)*(num_cards-1)//2,
                                     50 + (card_width_with_buffer+2)*(num_cards-1)//2 + card_width_with_buffer,
                                     card_width_with_buffer))
        else:
            x_positions = list(range(50 - card_width_with_buffer*num_cards//2 + card_width_with_buffer//2,
                                     50 + card_width_with_buffer*num_cards//2 + card_width_with_buffer//2,
                                     card_width_with_buffer))
            
        for i in range(len(p1.cards)):
            card = p1.cards[i]
            card.draw(self.win)
            card.move_to(x_positions[i],20)

        self.x_positions = x_positions

    #Does the same thing as set_p1
    def set_p2(self,p2):
        self.text_p2.setText(p2.name + ": " + str(len(p2.cards)))

    def set_p3(self,p3):
        self.text_p3.setText(p3.name + ": " + str(len(p3.cards)))

    def set_p4(self,p4):
        self.text_p4.setText(p4.name + ": " + str(len(p4.cards)))

    #Returns the game ID, the cards in the discard pile, and the cards in the deck as a string
    def as_string(self):
        discard_pile_results = []
        for card in self.discard_pile:
            discard_pile_results.append(card.as_string())
        deck_results = []
        for card in self.deck:
            deck_results.append(card.as_string())
        return str(self.game_id) + "\nDiscard pile:" + "\t".join(discard_pile_results) + "\n" + "Deck:" + "\t".join(deck_results)

# Main loop of the program
def main():
    global CARDS
    
    if not os.path.exists(UNO_GAMES_DIR):
        MsgBox("Directory " + UNO_GAMES_DIR + " does not exist")
        return
    
    # Log into the game, continue a game, or exit
    win = GraphWin("UNO",300,300)
    win.setCoords(0,0,100,100)
    U = Text(Point(35,80),'U')
    N = Text(Point(50,80),'N')
    O = Text(Point(65,80),'O')
    punc = Text(Point(75,80),'!')
    U.setTextColor('red')
    N.setTextColor('yellow')
    O.setTextColor('green')
    punc.setTextColor('blue')
    win.setBackground('cyan')
    card1 = Polygon(Point(9*4,19*4),Point(7*4,17*4),Point(3*4,21*4),Point(5*4,23*4))
    card1.setFill('yellow')
    card1.draw(win)
    card2 = Polygon(Point(17*4,19*4),Point(19*4,17*4),Point(23*4,21*4),Point(21*4,23*4))
    card2.setFill('red')
    card2.draw(win)
    circ = Circle(Point(6*4,20*4),5)
    circ.setFill('white')
    circ.draw(win)
    circ2 = circ.clone()
    circ2.move(14*4,0)
    circ2.draw(win)
    text1 = Text(Point(24,80),'1')
    text1.setTextColor('yellow')
    text1.draw(win)
    text2 = text1.clone()
    text2.move(56,0)
    text2.setTextColor('red')
    text2.setText('3')
    text2.draw(win)
    text1.setSize(15)
    text2.setSize(15)
    UNO = []
    UNO.append(U)
    UNO.append(N)
    UNO.append(O)
    UNO.append(punc)
    for text in UNO:
       text.setStyle('bold italic')
       text.setSize(35)
       text.draw(win)
    start_new_game_button = Button(55,50,"Start New Game",win,50,10)
    continue_game_button = Button(55,25,"Continue/Join Game",win,50,10)
    Text(Point(12,60),"Name: ").draw(win)
    name_entry = Entry(Point(45,60),10)
    name_entry.draw(win)
    quit_button = Button(90,8,"Quit",win,20,10)
    Text(Point(15,35),"Game ID: ").draw(win)
    game_id_entry = Entry(Point(45,35),10)
    game_id_entry.draw(win)
    Text(Point(10,5),"Cards: ").draw(win)
    cards_entry = Entry(Point(30,5),5)
    cards_entry.draw(win)
    cards_entry.setText('1')
    game_id = None
    # Loop until the user clicks on one of the buttons
    while True:
        p = win.getMouse()
        if start_new_game_button.is_clicked(p): # The user wants to start a new game
            name = name_entry.getText() # Get the name of the player
            break
        elif continue_game_button.is_clicked(p): # The user wants to continue/join a game
            name = name_entry.getText() # Get name
            game_id = eval(game_id_entry.getText()) # Get ID
            break
        elif quit_button.is_clicked(p):
            win.close()
            return
         
    # Pick the cards
    if cards_entry.getText().strip() == '1':
       CARDS = cards1
    elif cards_entry.getText().strip() == '2':
       CARDS = cards2
    else:
       CARDS = cards1
       
    win.close()

    # Play the game
    game = Game()
    player = None
    if game_id == None: # Start a new game
        game.create_new_game(name)
        player = game.p1
    else: # Continue/join a new game
        # Load a previous game
        game.load_game(game_id)

        # Check to see if the player has already joined the game
        if game.p1.name == name:
            player = game.p1
        elif game.p2.name == name:
            player = game.p2
        elif game.p3.name == name:
            player = game.p3
        elif game.p4.name == name:
            player = game.p4
        else: # Check to see if there is a seat, because the player has not joined yet
            if game.p1.name.find("Computer") != -1:
                player = game.p1
            elif game.p2.name.find("Computer") != -1:
                player = game.p2
            elif game.p3.name.find("Computer") != -1:
                player = game.p3
            elif game.p4.name.find("Computer") != -1:
                player = game.p4
            else: # No more room in the game
                MsgBox("No more room in the game")
            player.name = name

    # Start/join the game
    while game.start(player) != None:
        # A reload command was issued, so let's reload

        # Save the game ID
        game_id = game.board.game_id
        # Close the game board
        game.board.win.close()
        # Load the game from the hard drive
        game.load_game(game_id)

        # Locate the player
        if player.name == game.p1.name:
            player = game.p1
        elif player.name == game.p2.name:
            player = game.p2
        elif player.name == game.p3.name:
            player = game.p3
        elif player.name == game.p4.name:
            player = game.p4
            
main()
