import tkinter as tk

class GUI1:

    def __init__(self):

        self.root = tk.Tk()
        self.root.geometry("1600x800")
        self.root.title("Rock Paper Scissors")

        self.label = tk.Label(self.root, text="Make Your Choice Player 1", font=("Arial", 28))
        self.label.pack(padx=20, pady=20)

        self.buttonframe = tk.Frame(self.root)
        self.buttonframe.columnconfigure(0, weight=1)
        self.buttonframe.columnconfigure(1, weight=1)
        self.buttonframe.columnconfigure(2, weight=1)
        
        self.btn1 = tk.Button(self.buttonframe, text="Rock", font=("Arial", 12), command=self.p1_select_rock)
        self.btn1.grid(row = 0, column = 0, sticky = tk.W + tk.E)

        self.btn2 = tk.Button(self.buttonframe, text="Paper", font=("Arial", 12), command=self.p1_select_paper)
        self.btn2.grid(row = 0, column = 1, sticky = tk.W + tk.E)

        self.btn3 = tk.Button(self.buttonframe, text="Scissors", font=("Arial", 12), command=self.p1_select_scissors)
        self.btn3.grid(row = 0, column = 2, sticky = tk.W + tk.E)

        self.buttonframe.pack(fill = 'x')

        self.root.mainloop()
    
    def p1_select_rock(self):
        self.player1_choice = "rock"
        self.next_player()


    def p1_select_paper(self):
        self.player1_choice = "paper"
        self.next_player()


    def p1_select_scissors(self):
        self.player1_choice = "scissors"
        self.next_player()




    def next_player(self):
        self.second_window = tk.Toplevel(self.root)
        self.second_window.geometry("1600x800")
        self.second_window.title("Rock Paper Scissors")

        self.label = tk.Label(self.second_window, text="Make Your Choice Player 2", font=("Arial", 28))
        self.label.pack(padx=20, pady=20)

        self.buttonframe = tk.Frame(self.second_window)
        self.buttonframe.columnconfigure(0, weight=1)
        self.buttonframe.columnconfigure(1, weight=1)
        self.buttonframe.columnconfigure(2, weight=1)
        
        self.btn1 = tk.Button(self.buttonframe, text="Rock", font=("Arial", 12), command=self.p2_select_rock)
        self.btn1.grid(row = 0, column = 0, sticky = tk.W + tk.E)

        self.btn2 = tk.Button(self.buttonframe, text="Paper", font=("Arial", 12), command=self.p2_select_paper)
        self.btn2.grid(row = 0, column = 1, sticky = tk.W + tk.E)

        self.btn3 = tk.Button(self.buttonframe, text="Scissors", font=("Arial", 12), command=self.p2_select_scissors)
        self.btn3.grid(row = 0, column = 2, sticky = tk.W + tk.E)

        self.buttonframe.pack(fill = 'x')

        self.second_window.mainloop()
    
    def p2_select_rock(self):
        self.player2_choice = "rock"
        self.show_winner()

    def p2_select_paper(self):
        self.player2_choice = "paper"
        self.show_winner()

    def p2_select_scissors(self):
        self.player2_choice = "scissors"
        self.show_winner()

    def show_winner(self):
        if self.player1_choice == self.player2_choice:
            print("It's a tie!")
        elif (self.player1_choice == "rock" and self.player2_choice == "scissors"):
            print("Player 1 wins!")
        elif (self.player1_choice == "paper" and self.player2_choice == "rock"):
            print("Player 1 wins!")
        elif (self.player1_choice == "scissors" and self.player2_choice == "paper"):
            print("Player 1 wins!")
        elif (self.player2_choice == "rock" and self.player1_choice == "scissors"):
            print("Player 2 wins!")
        elif (self.player2_choice == "paper" and self.player1_choice == "rock"):
            print("Player 2 wins!")
        elif (self.player2_choice == "scissors" and self.player1_choice == "paper"):
            print("Player 2 wins!")

GUI1()