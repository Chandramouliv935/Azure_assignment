import tkinter
def set_title(row,column):
    global curr_player
    if board[row][column]["text"] != "":
        return

    board[row][column]["text"] = curr_player

    if curr_player == playero:
        curr_player = playerx
    else:
        curr_player=playero

    label["text"] = curr_player+"'s turn"    
    
    
def new_game():
    pass

playerx = "X"
playero = "O"
curr_player = playerx
board = [[0,0,0],
         [0,0,0],
         [0,0,0]]

color_blue = "#1017b6"
color_yellow = "#dfe70d"
color_grey = "#3a3a3a"
color_light_grey = "#c3bdbd"

window = tkinter.Tk()
window.title("TIC TAC TOE")

window.resizable(False,False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text=curr_player+"'s turn", font=("consolas",20), background=color_grey, 
                      foreground="white")

label.grid(row=0,column=0,columnspan=3,sticky="we")
for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text="", font=("consolas",50,"bold"), 
                                            background=color_grey, foreground=color_blue, width=4, height=1,
                                            command=lambda row=row, column=column : set_title(row,column))
        board[row][column].grid(row=row+1, column=column) 
button = tkinter.Button(frame, text="RESTART", font=("Consolas",20), background=color_grey, foreground="white", command=new_game)
button.grid(row=4,column=0,columnspan=3,sticky="we")        
frame.pack()

window.mainloop()


