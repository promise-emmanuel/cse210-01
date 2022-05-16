from game.card import Card
from random import randint


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        current_card (int): The value of the current card.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """

        card = Card()
        self.cards = [card]
        self.is_playing = True
        self.score = 300

        

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
            self.reset()
            
    
    def get_inputs(self):
        """Ask the user if they want to play.

        Args:
            self (Director): An instance of Director.
        """
        if self.score > 0:
            play_again = input("\nPlay? [y/n]: ")

            if play_again == "y":
                self.is_playing = True
            elif play_again == "n":
                self.end_game()
                
            else:
                while play_again != ("y" or "n"):
                    print("Invalid Input! \nEnter y/n.")
                    play_again = input("Play? [y/n]: ")
        else:
            self.end_game()
        
    
    def do_updates(self):
        """Update the player's score.
        
        Args: 
        self (Director): An instance of Director
        """
        if not self.is_playing:
            return 
        
        for i in range(len(self.cards)):
            cards = self.cards[i]
            cards.guess()
            self.score += cards.point

    def do_outputs(self):
        """Display next card and player's score.
        
        Args: 
        self (Director): An instance of Director
        """
        if not self.is_playing:
            return 
        
        for i in range(len(self.cards)):
            cards = self.cards[i]
            next_card = cards.next_card
            print(f"\nNext card was {next_card}")
            print(f"Score for this round: {self.score}") 

    def reset(self):
        """Reset the card point to 0.
        
        Args: 
        self (Director): An instance of Director
        """

        for i in range(len(self.cards)):
            cards = self.cards[i]
            cards.point = 0
        

    def end_game(self):
        """Display end of game mesaage.
        
        Args: 
        self (Director): An instance of Director
        """
        if self.score < 0: 
            print("GAME OVER!")
        
        print("Thanks for playing HILO.")
        print(f"Your final score is {self.score}\n")
        self.is_playing = False

        
        
        
       
