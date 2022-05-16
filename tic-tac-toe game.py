''' The user will play this game choosing a side ("X" or "O") before the game starts .
    
    for this game,
    we will need to have a code that will check if anyone has gotten 
    3 in a row, or if there has been a tie.

    we will also need an option that resets the game after there is a win or a tie. 

    We also need to make sure no two X's or O's share the same spot, and also that all the buttons are disabled after a win or tie.

 '''

from cgitb import reset
from importlib.machinery import WindowsRegistryFinder
from tkinter import *
from tkinter import messagebox


def main():
    # create the root object
    global root, lat_main
    root = Tk()

    # create the main window
    lat_main = root
    lat_main.title('Promise-emmanuel - Tic Tac-Toe')
    # root.geometry('1200*710')

    # call functions that will draw the buttons and other functions necessary for the game to work properly
    #  start the game by building the buttons, giving the buttons commands when clicked and checking as each player's clicks,
    #  if it's a tie, or a win.
    game(lat_main)
    

    my_menu = Menu(lat_main)
    lat_main.config(menu=my_menu)

    # create options menu
    options_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Options", menu=options_menu)
    options_menu.add_command(label="Reset Game", command=reset)


    root.mainloop()

# when the reset option is clicked, the reset function would be called.
# this function would load the game from scratch anytime it is called
def reset():
    game(root)



def game(frm_main):
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global clicked, count
    clicked = True
    count= 0

    #build our boxes and give it a command when clicked 
    b1 = Button(frm_main, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b1))
    b2 = Button(frm_main, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b2))
    b3 = Button(frm_main, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b3))


    b4 = Button(frm_main, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b4))
    b5 = Button(frm_main, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b5))
    b6 = Button(frm_main, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b6))

    b7 = Button(frm_main, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b7))
    b8 = Button(frm_main, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b8))
    b9 = Button(frm_main, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b9))

        # grid our buttons to the screen
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)






    #check to see if someone won, then disable the buttons

    def disable_buttons():
        b1.config(state=DISABLED)
        b2.config(state=DISABLED)
        b3.config(state=DISABLED)
        b4.config(state=DISABLED)
        b5.config(state=DISABLED)
        b6.config(state=DISABLED)
        b7.config(state=DISABLED)
        b8.config(state=DISABLED)
        b9.config(state=DISABLED)

    def won():
        global winner
        winner = False

        if b1["text"] == "X" and b2["text"] =="X" and b3["text"] == "X":
            b1.config(bg="red")
            b2.config(bg="red")
            b3.config(bg="red")
            winner = True
            messagebox.showinfo("Tic-Tac-Toe", "Congratulations!!! X wins.")
            disable_buttons()

        elif b4["text"] == "X" and b5["text"] =="X" and b6["text"] == "X":
            b4.config(bg="red")
            b5.config(bg="red")
            b6.config(bg="red")
            winner = True
            messagebox.showinfo("Tic-Tac-Toe", "Congratulations!!! X wins.")
            disable_buttons()
            
        elif b7["text"] == "X" and b8["text"] =="X" and b9["text"] == "X":
            b7.config(bg="red")
            b8.config(bg="red")
            b9.config(bg="red")
            winner = True
            messagebox.showinfo("Tic-Tac-Toe", "Congratulations!!! X wins.")              
            disable_buttons()

        elif b1["text"] == "X" and b4["text"] =="X" and b7["text"] == "X":
            b1.config(bg="red")
            b4.config(bg="red")
            b7.config(bg="red")
            winner = True
            messagebox.showinfo("Tic-Tac-Toe", "Congratulations!!! X wins.")
            disable_buttons()

        elif b2["text"] == "X" and b5["text"] =="X" and b8["text"] == "X":
            b2.config(bg="red")
            b5.config(bg="red")
            b8.config(bg="red")
            winner = True
            messagebox.showinfo("Tic-Tac-Toe", "Congratulations!!! X wins.")
            disable_buttons()
            
        elif b3["text"] == "X" and b6["text"] =="X" and b9["text"] == "X":
            b1.config(bg="red")
            b2.config(bg="red")
            b3.config(bg="red")
            winner = True
            messagebox.showinfo("Tic-Tac-Toe", "Congratulations!!! X wins.")
            disable_buttons()
            
        elif b1["text"] == "X" and b5["text"] =="X" and b9["text"] == "X":
            b1.config(bg="red")
            b5.config(bg="red")
            b9.config(bg="red")
            winner = True
            messagebox.showinfo("Tic-Tac-Toe", "Congratulations!!! X wins.")
            disable_buttons()


        elif b3["text"] == "X" and b5["text"] =="X" and b7["text"] == "X":
                b3.config(bg="red")
                b5.config(bg="red")
                b7.config(bg="red")
                winner = True
                messagebox.showinfo("Tic-Tac-Toe", "Congratulations!!! X wins.")
                disable_buttons()
            
            # check if the O's win

        elif b1["text"] == "O" and b2["text"] =="O" and b3["text"] == "O":
            b1.config(bg="red")
            b2.config(bg="red") 
            b3.config(bg="red")
            winner = True
            messagebox.showinfo("Tic-Tac-Toe", "Congratulations!!! O wins.")
            disable_buttons()

        elif b4["text"] == "O" and b5["text"] =="O" and b6["text"] == "O":
            b4.config(bg="red")
            b5.config(bg="red")
            b6.config(bg="red")
            winner = True
            messagebox.showinfo("Tic-Tac-Toe", "Congratulations!!! O wins.")
            disable_buttons()
            
        elif b7["text"] == "O" and b8["text"] =="O" and b9["text"] == "O":
            b7.config(bg="red")
            b8.config(bg="red")
            b9.config(bg="red")
            winner = True
            messagebox.showinfo("Tic-Tac-Toe", "Congratulations!!! O wins.")
            disable_buttons()

        elif b1["text"] == "O" and b4["text"] =="O" and b7["text"] == "O":
            b1.config(bg="red")
            b4.config(bg="red")
            b7.config(bg="red")
            winner = True
            messagebox.showinfo("Tic-Tac-Toe", "Congratulations!!! O wins.")
            disable_buttons()

        elif b2["text"] == "O" and b5["text"] =="O" and b8["text"] == "O":
            b2.config(bg="red")
            b5.config(bg="red")
            b8.config(bg="red")
            winner = True
            messagebox.showinfo("Tic-Tac-Toe", "Congratulations!!! O wins.")
            disable_buttons()
            
        elif b3["text"] == "O" and b6["text"] =="O" and b9["text"] == "O":
            b3.config(bg="red")
            b6.config(bg="red")
            b9.config(bg="red")
            winner = True
            messagebox.showinfo("Tic-Tac-Toe", "Congratulations!!! O wins.")
            disable_buttons()
            
        elif b1["text"] == "O" and b5["text"] =="O" and b9["text"] == "O":
            b1.config(bg="red")
            b5.config(bg="red")
            b9.config(bg="red")
            winner = True
            messagebox.showinfo("Tic-Tac-Toe", "Congratulations!!! O wins.")
            disable_buttons()


        elif b3["text"] == "O" and b5["text"] =="O" and b7["text"] == "O":
            b3.config(bg="red")
            b5.config(bg="red")
            b7.config(bg="red")
            winner = True
            messagebox.showinfo("Tic-Tac-Toe", "Congratulations!!! O wins.")
            disable_buttons()


        # check if tie
        elif count == 9 and winner == False:
            messagebox.showinfo("Tic-Tac-Toe", "It's a Tie!!. No one wins. \n kindly reset or exit the game.")

            

        #button clicked function
    def b_click(b):
        global clicked, count

        if b["text"] == " " and clicked == True:
            b["text"] = "X"
            clicked = False
            count += 1
            won()
        elif b["text"] == " " and clicked == False:
            b["text"] = "O"
            clicked = True
            count += 1
            won()
        else:
            messagebox.showerror("Tic Tac Toe", "Hey! That box has already been selected \n pick an empty box" )


# call the main function
if __name__ == "__main__":
    main()
