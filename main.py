import tkinter as tk

class GUI1:

    def __init__(self):

        self.root = tk.Tk()
        self.root.geometry("1600x800")
        self.root.title("Rock Paper Scissors")

        self.p1_wins = 0
        self.p2_wins = 0

        self.starterpage = tk.Frame(self.root)
        self.page1 = tk.Frame(self.root)
        self.page2 = tk.Frame(self.root)

        self.starterpage.grid(row=0, column=0, sticky='nsew')
        self.page1.grid(row=0, column=0, sticky='nsew')
        self.page2.grid(row=0, column=0, sticky='nsew')


        self.starterlabel = tk.Label(self.starterpage, text="Welcome to Rock Paper Scissors! (Best of Three)", font=("Arial", 28))
        self.label1 = tk.Label(self.page1, text="Make Your Choice Player 1", font=("Arial", 28))
        self.label2 = tk.Label(self.page2, text="Make Your Choice Player 2", font=("Arial", 28))

        self.starterlabel.pack(padx=20, pady=20)
        self.label1.pack(padx=20, pady=20)
        self.label2.pack(padx=20, pady=20)

        self.buttonframestart = tk.Frame(self.starterpage)
        self.buttonframestart.columnconfigure(0, weight=1)
        self.buttonframestart.columnconfigure(1, weight=1)

        self.startbtn = tk.Button(self.buttonframestart, text="Start Game", font=("Arial", 12), command=lambda: self.page1.tkraise())
        self.startbtn.grid(row = 0, column = 0, sticky = tk.W + tk.E)

        self.quitbtn = tk.Button(self.buttonframestart, text="Quit", font=("Arial", 12), command=self.root.quit)
        self.quitbtn.grid(row = 0, column = 1, sticky = tk.W + tk.E)

        self.buttonframestart.pack(fill = 'x')

        self.buttonframe1 = tk.Frame(self.page1)
        self.buttonframe1.columnconfigure(0, weight=1)
        self.buttonframe1.columnconfigure(1, weight=1)
        self.buttonframe1.columnconfigure(2, weight=1)
        
        self.btn1 = tk.Button(self.buttonframe1, text="Rock", font=("Arial", 12), command=self.p1_select_rock)
        self.btn1.grid(row = 0, column = 0, sticky = tk.W + tk.E)

        self.btn2 = tk.Button(self.buttonframe1, text="Paper", font=("Arial", 12), command=self.p1_select_paper)
        self.btn2.grid(row = 0, column = 1, sticky = tk.W + tk.E)

        self.btn3 = tk.Button(self.buttonframe1, text="Scissors", font=("Arial", 12), command=self.p1_select_scissors)
        self.btn3.grid(row = 0, column = 2, sticky = tk.W + tk.E)

        self.buttonframe1.pack(fill = 'x')

        self.buttonframe2 = tk.Frame(self.page2)
        self.buttonframe2.columnconfigure(0, weight=1)
        self.buttonframe2.columnconfigure(1, weight=1)
        self.buttonframe2.columnconfigure(2, weight=1)
        
        self.btn4 = tk.Button(self.buttonframe2, text="Rock", font=("Arial", 12), command=self.p2_select_rock)
        self.btn4.grid(row = 0, column = 0, sticky = tk.W + tk.E)

        self.btn5 = tk.Button(self.buttonframe2, text="Paper", font=("Arial", 12), command=self.p2_select_paper)
        self.btn5.grid(row = 0, column = 1, sticky = tk.W + tk.E)

        self.btn6 = tk.Button(self.buttonframe2, text="Scissors", font=("Arial", 12), command=self.p2_select_scissors)
        self.btn6.grid(row = 0, column = 2, sticky = tk.W + tk.E)

        self.buttonframe2.pack(fill = 'x')

        self.starterpage.tkraise()

        self.root.mainloop()
    
    def p1_select_rock(self):
        self.player1_choice = "rock"
        self.page2.tkraise()

    def p1_select_paper(self):
        self.player1_choice = "paper"
        self.page2.tkraise()

    def p1_select_scissors(self):
        self.player1_choice = "scissors"
        self.page2.tkraise()
    
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
            print("It's a tie! Let the match continue...")
            self.page1.tkraise()

        elif (self.player1_choice == "rock" and self.player2_choice == "scissors"):
            print("Player 1 wins!")
            self.p1_wins += 1
            if self.p1_wins > 2:
                print("Player 1 is the overall winner!")
                self.root.quit()
            self.page1.tkraise()
        elif (self.player1_choice == "paper" and self.player2_choice == "rock"):
            print("Player 1 wins!")
            self.p1_wins += 1
            if self.p1_wins > 2:
                print("Player 1 is the overall winner!")
                self.root.quit()
            self.page1.tkraise()
        elif (self.player1_choice == "scissors" and self.player2_choice == "paper"):
            print("Player 1 wins!")
            self.p1_wins += 1
            if self.p1_wins > 2:
                print("Player 1 is the overall winner!")
                self.root.quit()
            self.page1.tkraise()
        elif (self.player2_choice == "rock" and self.player1_choice == "scissors"):
            print("Player 2 wins!")
            self.p2_wins += 1
            if self.p2_wins > 2:
                print("Player 2 is the overall winner!")
                self.root.quit()
            self.page1.tkraise()
        elif (self.player2_choice == "paper" and self.player1_choice == "rock"):
            print("Player 2 wins!")
            self.p2_wins += 1
            if self.p2_wins > 2:
                print("Player 2 is the overall winner!")
                self.root.quit()
            self.page1.tkraise()
        elif (self.player2_choice == "scissors" and self.player1_choice == "paper"):
            print("Player 2 wins!")
            self.p2_wins += 1
            if self.p2_wins > 2:
                print("Player 2 is the overall winner!")
                self.root.quit()
            self.page1.tkraise()

GUI1()