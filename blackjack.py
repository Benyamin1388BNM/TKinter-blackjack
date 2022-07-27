import tkinter as tk
import random
import os
from tkinter import messagebox
from PIL import Image, ImageTk

scriptDir = os.path.dirname(__file__)
os.chdir(scriptDir)

root = tk.Tk()
root.title('Blackjack card game')
root.geometry('1200x800')
root.configure(background='green')

#Test for blackjack on shuffle
def blackjack_shuffle(player):
    global player_total, dealer_total
    #Keep track of score
    player_total=0
    dealer_total=0

    if player=='dealer':
        if len(dealer_score) == 2:
            if dealer_score[0]+dealer_score[1]==21:
                #Update status
                blackjack_status['dealer'] = 'yes'


    if player=='player':
        if len(player_score) == 2:
            if player_score[0]+player_score[1]==21:
                #Update status
                blackjack_status['player'] = 'yes'
        else:
            #loop through player score list
            for score in player_score:
                #Add upscore
                player_total += score
                if player_total==21:
                    blackjack_status['player']='yes'
                elif player_total>21:
                    blackjack_status['player']='bust'


    if len(dealer_score) == 2 and len(player_score) == 2:
        if blackjack_status['dealer'] == 'yes' and blackjack_status['player'] == 'yes':
            #Tie
            messagebox.showinfo('Push!', r"It's a Tie!")
            #Disable buttons
            card_button.config(state='disabled')
            stand_button.config(state='disabled')
        elif blackjack_status['dealer'] == 'yes':
            #Delaer won
            messagebox.showinfo('Dealer Wins!', 'Blackjack, Delaer wins!')
            #Disable buttons
            card_button.config(state='disabled')
            stand_button.config(state='disabled')
        elif blackjack_status['player'] == 'yes':
            #Player won
            messagebox.showinfo('Player Wins!', 'Blackjack, Player wins!')
            #Player buttons 
            card_button.config(state='disabled')
            stand_button.config(state='disabled')
    elif len(dealer_score) == 2 and len(player_score) > 2:
        if blackjack_status['dealer'] == 'yes' and blackjack_status['player'] == 'yes':
            #Tie
            messagebox.showinfo('Push!', r"It's a Tie!")
            #Disable buttons
            card_button.config(state='disabled')
            stand_button.config(state='disabled')
        elif blackjack_status['dealer'] == 'yes':
            #Delaer won
            messagebox.showinfo('Dealer Wins!', '21!, Delaer wins!')
            #Disable buttons
            card_button.config(state='disabled')
            stand_button.config(state='disabled')
        elif blackjack_status['player'] == 'yes':
            #Player won
            messagebox.showinfo('Player Wins!', '21!, Player wins!')
            #Player buttons
            card_button.config(state='disabled')
            stand_button.config(state='disabled')

        
    if blackjack_status['player']=='bust':
        #Player bust
        messagebox.showinfo('Player Busts!', f'Player loses! {player_total}')
        #Player buttons
        card_button.config(state='disabled')
        stand_button.config(state='disabled')


#Resize cards
def resize_cards(card):
    #Open the image
    our_card_img = Image.open(card)

    #Resize
    our_card_resized_img = our_card_img.resize((150, 218))
    global final_image
    final_image = ImageTk.PhotoImage(our_card_resized_img)
    return final_image

#Shuffle cards
def shuffle():
    #Keep track of winning
    global blackjack_status, player_total, dealer_total
    
    #Keep track of score
    player_total=0
    dealer_total=0

    blackjack_status = {'dealer':'no', 'player':'no'}

    #Enable buttons
    card_button.config(state='normal')
    stand_button.config(state='normal')
    #Clear previous game cards
    dealer_label_1.config(image="")
    dealer_label_2.config(image="")
    dealer_label_3.config(image="")
    dealer_label_4.config(image="")
    dealer_label_5.config(image="")

    player_label_1.config(image="")
    player_label_2.config(image="")
    player_label_3.config(image="")
    player_label_4.config(image="")
    player_label_5.config(image="")

    #Create deck
    suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
    values = range(2,15)

    global deck
    deck = []

    for suit in suits:
        for value in values:
            deck.append(f'{value}_of_{suit}')

    #Create players   
    global dealer, player, dealer_spot, player_spot, dealer_score, player_score
    dealer=[]
    player=[]
    player_score=[]
    dealer_score=[]
    dealer_spot=0
    player_spot=0

    #shuffle two cards for player and dealer
    dealer_hit()
    dealer_hit()

    player_hit()
    player_hit()

    #remaining cards
    remaining_cards.configure(text=f'remaining cards = {len(deck)}')

def dealer_hit():
    global dealer_spot
    if dealer_spot < 5:
        try:
            
            #Output card to screen
            global dealer_image1, dealer_image1, dealer_image2, dealer_image3, dealer_image4, dealer_image5

            #Get dealer card
            dealer_card = random.choice(deck)
            deck.remove(dealer_card)
            dealer.append(dealer_card)
            dcard = int(dealer_card.split("_", 1)[0])
            if dcard==14:
                dealer_score.append(11)
            elif dcard>=11:
                dealer_score.append(10)
            else:
                dealer_score.append(dcard)

            if dealer_spot==0:
                dealer_image1 = resize_cards(f'{dealer_card}.png')
                dealer_label_1.config(image=dealer_image1)
                dealer_spot+=1
            elif dealer_spot==1:
                dealer_image2 = resize_cards(f'{dealer_card}.png')
                dealer_label_2.config(image=dealer_image2)
                dealer_spot+=1
            elif dealer_spot==2:
                dealer_image3 = resize_cards(f'{dealer_card}.png')
                dealer_label_3.config(image=dealer_image3)
                dealer_spot+=1
            elif dealer_spot==3:
                dealer_image4 = resize_cards(f'{dealer_card}.png')
                dealer_label_4.config(image=dealer_image4)
                dealer_spot+=1
            elif dealer_spot==4:
                dealer_image5 = resize_cards(f'{dealer_card}.png')
                dealer_label_5.config(image=dealer_image5)
                dealer_spot+=1

            #remaining cards
            remaining_cards.configure(text=f'remaining cards = {len(deck)}')
        except:
            remaining_cards.configure(text='Game over!')

        #Check for blackjack
        blackjack_shuffle('dealer')


def player_hit():
    global player_spot
    if player_spot < 5:
        try:
            
            #Output card to screen
            global player_image1, player_image1, player_image2, player_image3, player_image4, player_image5

            #Get player card
            player_card = random.choice(deck)
            deck.remove(player_card)
            player.append(player_card)

            pcard = int(player_card.split("_", 1)[0])
            if pcard==14:
                player_score.append(11)
            elif pcard>=11:
                player_score.append(10)
            else:
                player_score.append(pcard)

            if player_spot==0:
                player_image1 = resize_cards(f'{player_card}.png')
                player_label_1.config(image=player_image1)
                player_spot+=1
            elif player_spot==1:
                player_image2 = resize_cards(f'{player_card}.png')
                player_label_2.config(image=player_image2)
                player_spot+=1
            elif player_spot==2:
                player_image3 = resize_cards(f'{player_card}.png')
                player_label_3.config(image=player_image3)
                player_spot+=1
            elif player_spot==3:
                player_image4 = resize_cards(f'{player_card}.png')
                player_label_4.config(image=player_image4)
                player_spot+=1
            elif player_spot==4:
                player_image5 = resize_cards(f'{player_card}.png')
                player_label_5.config(image=player_image5)
                player_spot+=1

            #remaining cards
            remaining_cards.configure(text=f'remaining cards = {len(deck)}')
        except:
            remaining_cards.configure(text='Game over!')
        
        #Check for blackjack
        blackjack_shuffle('player')

#Deal cards
def deal_cards():
    try:
        #Get dealer card
        card = random.choice(deck)
        deck.remove(card)
        dealer.append(card)
        #Output card to screen
        global dealer_image
        dealer_image = resize_cards(f'{card}.png')
        #dealer_label_1.config(image=dealer_image)

        #Get player card
        card = random.choice(deck)
        deck.remove(card)
        player.append(card)
        #Output card to screen
        global player_image
        player_image = resize_cards(f'{card}.png')
        #player_label_1.config(image=player_image)

        #remaining cards
        remaining_cards.configure(text=f'remaining cards = {len(deck)}')
    except:
        remaining_cards.configure(text='Game over!')

my_frame = tk.Frame(root, bg='green')
my_frame.pack(pady=20)

#Create frames for cards
dealer_frame = tk.LabelFrame(my_frame, text='Dealer', bd=0)
dealer_frame.pack(padx=20, ipadx=20)

player_frame = tk.LabelFrame(my_frame, text='Player', bd=0)
player_frame.pack(ipadx=20, pady=10)

#Put cards in frames
dealer_label_1 = tk.Label(dealer_frame, text='')
dealer_label_1.grid(row=0, column=0, pady=20, padx=20)

dealer_label_2 = tk.Label(dealer_frame, text='')
dealer_label_2.grid(row=0, column=1, pady=20, padx=20)

dealer_label_3 = tk.Label(dealer_frame, text='')
dealer_label_3.grid(row=0, column=2, pady=20, padx=20)

dealer_label_4 = tk.Label(dealer_frame, text='')
dealer_label_4.grid(row=0, column=3, pady=20, padx=20)

dealer_label_5 = tk.Label(dealer_frame, text='')
dealer_label_5.grid(row=0, column=4, pady=20, padx=20)

player_label_1 = tk.Label(player_frame, text='')
player_label_1.grid(row=0, column=0, pady=20, padx=20)

player_label_2 = tk.Label(player_frame, text='')
player_label_2.grid(row=0, column=1, pady=20, padx=20)

player_label_3 = tk.Label(player_frame, text='')
player_label_3.grid(row=0, column=2, pady=20, padx=20)

player_label_4 = tk.Label(player_frame, text='')
player_label_4.grid(row=0, column=3, pady=20, padx=20)

player_label_5 = tk.Label(player_frame, text='')
player_label_5.grid(row=0, column=4, pady=20, padx=20)

#Create button frame
button_frame = tk.Frame(root, bg='green')
button_frame.pack(pady=20)

#Create buttons
shuffle_button = tk.Button(button_frame, text='shuffle deck', font=('Helvetica', 14), command=shuffle)
shuffle_button.grid(row=0, column=0)

card_button = tk.Button(button_frame, text='hit', font=('Helvetica', 14), command=player_hit)
card_button.grid(row=0, column=1, padx=10)

stand_button = tk.Button(button_frame, text='stand', font=('Helvetica', 14), command=deal_cards)
stand_button.grid(row=0, column=2)


#Remaining cards label
remaining_cards = tk.Label(root, text=(f'remaining cards = {52}'), font=('Helvetica', 14))
remaining_cards.pack(pady=20)

shuffle()

root.mainloop()