import random
from tkinter import *

cards = [{'id': 1, 'nb': 2}, {'id': 2, 'nb': 2}]
card_state = ["Face", "Dos"]

current_cards = []

board = [[None, None],
         [None, None]]

GAP = 20
COL = len(board[0])
ROW = len(board)
IMG_WIDTH = 200
IMG_HEIGHT = 200
WIDTH = (IMG_WIDTH * COL) + (GAP * (COL + 1))
HEIGHT = (IMG_HEIGHT * ROW) + (GAP * (ROW + 1))
sq_sz_x = WIDTH // COL - GAP // 2
sq_sz_y = HEIGHT // ROW - GAP // 2

master = Tk()
master.geometry("460x460")
master.title("Memory")

can = Canvas(master, width=WIDTH, height=HEIGHT)
can.pack()

previous_clicked = []


def card_appear():
    for row in range(len(board)):
        for col in range(len(board[row])):
            card = board[row][col]
            x = (col * sq_sz_x + GAP)
            y = (row * sq_sz_y + GAP)

            if card['state'] == "Dos":
                drink = PhotoImage(file='Images/0.gif')
                card['drink'] = drink  # reference must be kept bc of garbage collector
                i = can.create_image(x, y, image=drink, anchor="nw")
                card['tkimg'] = i
            else:
                drink = PhotoImage(file="Images/" + card['img'])
                card['drink'] = drink
                i = can.create_image(x, y, image=drink, anchor='nw')
                card['tkimg'] = i


def click(evt):
    x, y = evt.x, evt.y
    clicked = can.find_closest(x, y)[0]
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col]['tkimg'] == clicked:
                board[row][col]['state'] = "Face"
                card_appear()


def init_board():
    for row in range(len(board)):
        for col in range(len(board[row])):
            ran = random.choice(cards)
            while ran.get('nb') <= 0:
                ran = random.choice(cards)
            picked_card = ran.get('id')
            card_state = "Dos"
            ran['nb'] -= 1
            identity = {'id': picked_card, 'state': card_state,
                        'img': str(picked_card) + '.gif', 'tkimg': None, 'drink' : None}
            board[row][col] = identity
    card_appear()
    can.bind("<Button-1>", click)


def main():
    init_board()


main()

master.mainloop()