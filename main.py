import random
from tkinter import *
from PIL import Image, ImageTk

master = Tk()
master.geometry("460x460")
master.title("Memory")

# can = Canvas(master, width=460, height=460)
# can.pack()

cards = [{'id': 1, 'nb': 2}, {'id': 2, 'nb': 2}]
card_state = ["Face", "Dos"]

current_cards = []

board = [[None, None],
         [None, None]]


def card_appear():
    for row in range(len(board)):
        for col in range(len(board[row])):  # deux boucles for pour accéder à ligne puis colonne
            card = board[row][col]  # card correspond à la ligne et à la colonne
            # Deux possibilité en fonction de si la carte est de dos ou de face
            if card['state'] == "Dos":  # chemin de l'image du dos
                drink = Image.open('0.gif')
                photo = ImageTk.PhotoImage(drink)
                can = Canvas(master, width=200, height=200, bg='cyan')  # le cyan c'est pour repérer le canvas
                can.create_image((0, 0), image=photo, anchor="nw")
                can.pack()

                # pour afficher en fonction de la ligne et de la colonne choisie
            # if state is on front -> img is in dict of card
            else:
                drink = Image.open(card['img'])  # cf init_board
                photo = ImageTk.PhotoImage(drink)
                can = Canvas(master, width=200, height=200, bg='cyan')
                can.create_image((0, 0), image=photo)


def init_board():
    for row in range(len(board)):
        for col in range(len(board[row])):
            ran = random.choice(cards)  # on extrait un dico de la liste au hasard
            while ran.get('nb') <= 0:  # pour pas qu'on prenne plus de deux fois la même carte
                ran = random.choice(
                    cards)  # donc la on recommence à choisir jusqu'à ce qu'on tombe sur une carte qui y est moins de deux fois

            picked_card = ran.get('id')  # on extrait d'id du dictionnaire voulu
            card_state = "Dos"  # Etat par défaut
            ran['nb'] -= 1  # On marque que la carte apparaît une fois de plus
            identity = {'id': picked_card, 'state': card_state,
                        'img': str(picked_card) + '.gif'}  # on crée un dico : pour la carte choisie,
            # on met l'id correspondant, et 'id' correspond au chemin de l'image désormais
            board[row][
                col] = identity  # identity est ajouté à board --> le dictionnaire apparaît à l'emplacement de la carte
    print(board)
    card_appear()


# def OnButtonClick(event):
#   l=event.x//200
#  c=event.y//230
# print(l)
# print(c)
# item = master.find_closest(c, l)

# print(item)
# card_state = "Face"
# init_board()

def main():
    init_board()


main()
# master.bind("<Button-1>", OnButtonClick)

master.mainloop()