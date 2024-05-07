import random
suits = ('Hearts','Clubs','Diamonds','Spades')
ranks = ('Two','Three','Four','Five','Six','seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values ={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}

# class for cards:
class Card:
    def __init__(self,suit,rank,):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'
    
# class for making deck and shffuling:
class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                card_created = Card(suit,rank)
                self.all_cards.append(card_created)

    def shuffel (self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop(0)
    
# player class for holding cards and chips:
class Player:
    def __init__(self,name):
        self.name = name
        self.all_cards = []
        self.total_value = 0
        self.ace = 0

    
    def add_cards(self,new_card):
        self.all_cards.append(new_card)
        self.total_value += values[new_card.rank]
        if new_card.rank == 'Ace':
            self.ace += 1

    def adjust_for_ace(self):
        while self.total_value > 21 and self.ace:
            self.total_value -= 10
            self.ace -= 1
        
    def __str__(self):
        return f'Hi! {self.name}, you have {chip.chips} chips to start with...'
    
# class for chips:
class Chips:
    def __init__(self):
        self.chips = 100

    def add_chips(self,bet):
        self.chips += bet 
    
    def remove_chips(self,bet):
        self.chips -= bet

# bet class for taking bet amount form player:
def bets():
    while True:
        while True:
            try:
                bet = int(input('Enter your Bet : '))
            except:
                print('Please enter correct value!!!')
                print() 
            else:
                break
        if bet > chip.chips:
            print('Your bet exceed your total holding!!!')
            print()
        elif bet == 0:
            print('Bet cannot be 0!!!')
            print()
        else:
            print(f'YOUR BET IS : {bet}')
            print()
            print()
            return bet
            break

# show function to print player and computer hand cards:
def show_some():
    print(f"DEALER's CARDS : | HIDDEN CARD | {computer.all_cards[1]}  ")
    print('----------------------------------------------------------------------')
    print("PLAYER's CARDS : " , *player.all_cards , sep = ' | ')

def show_all():
    print("DEALER's CARDS : " , *computer.all_cards , sep = ' | ')
    print("PLAYER's CARDS : " , *player.all_cards , sep = ' | ')

# hit fuction to perfome HIT :
def hit(player):
    player.add_cards(new_deck.deal_one())
    player.adjust_for_ace()

# hit_or_stand function to ask player choise:
def hit_or_stand():
    global playing
    while True:
        ask = input("Would you like to Hit or Stand? Enter 'h' or 's' : ")
        print()

        if ask.lower() == 'h':
            hit(player)

        elif ask.lower() == 's':
            print('Player stands. Dealer is playing')
            print()
            playing = False

        else:
            print('Sorry, please try again!!')
            print()
            continue
        break

# Funciont to perfom busts win and push actions:
def busts(who):
    print(who.name , 'Busts')
    print()
    if who == player:
        chip.remove_chips(bet)
    else:
        chip.add_chips(bet)

def wins(who):
    print(who.name , 'WINS')
    print()
    if who == player:
        chip.add_chips(bet)
    else:
        chip.remove_chips(bet)

def push():
    print("Dealer and Player tie! It's a push.")
    print()


# GAME STARTS:
# print opening statement:
start = True
while start:
    round = 0
    print('Starting New Game')
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
        Dealer hits until s/he reaches 17. Aces count as 1 or 11.')
    print()
    print()
    chip = Chips() 

 # asking player name and bet:
    name = input('Enter your name : ')
    
    while True:
        
        if chip.chips > 0:
            round += 1
            print('ROUND : ',round )

            player = Player(name) 
            computer = Player('Computer Dealer')
            print('GAME STARTS')
            print(player)
            print()
            bet = bets()

            # shffule and distribute cards and show :
            new_deck = Deck()
            new_deck.shuffel()

            for i in range(2):
                player.add_cards(new_deck.deal_one())
                player.adjust_for_ace()
                computer.add_cards(new_deck.deal_one())
                computer.adjust_for_ace()

            show_some()
            print()
            print()

            # ask user hit or stand and perform action:
            playing = True
            while playing:
                hit_or_stand()
                print()
                print()
                
                show_some()
                print()
                print()

                # if player busts end game:
                if player.total_value > 21:
                    busts(player)
                    break

            if player.total_value <= 21:    # check that dealer has not busts
                print()
                show_all()
                print()

                while computer.total_value < 17:     # if dealer hand value less than 17 it hits 
                    hit(computer)
                    show_all()
                    print()
                    print()

                if computer.total_value > 21:     #check if dealer has busts
                    print(computer.total_value)    
                    busts(computer)
        
                elif computer.total_value > player.total_value:    # check if player looses
                    wins(computer)

                elif computer.total_value < player.total_value:     # check if player wins
                    wins(player)

                    if player.total_value == 21:     # check if it is a blackjack!
                        print('BLACK JACk!!')
                        print()
    
                else:       # check if it is a tie
                    push()  
            
            print()
            print(f"Player's winning stand at {chip.chips}")  # print player's winning
            print()

        else:  # if player looses all its money it prints:
            print('Sorry!!!.....Insufficient chips!!!')
            print()
            

        while True:  # ask user to play again
            ask = int(input('Press .1 to play again \n\
Press .2 to restart \n\
Press .3 to quit game\n\
  --> ' ))
            
            if ask == 1 or ask == 2 or ask == 3:
                break
            
        if ask == 1:  # it starts the new round with the chips left:
            print(f'Total chips you have is : {chip.chips}')
            print()
            print()
            continue

        elif ask == 2:      # it restarts the game again:
            print('Starting game from start')
            print()
            break

        else:    # it ends the game:
            print('Thanks for playing!!!')
            start = False
            break
        
