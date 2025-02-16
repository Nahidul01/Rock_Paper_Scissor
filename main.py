import random

class RockPaperScissor:
    #custom exception for invalid choices
    #defined inside the class
    class InvalidChoiceError(Exception):
        # Exception raise when user enter an invalid choice
        pass

    def __init__(self, cmp_choice):
        self.cmp_choice = cmp_choice

    def move(self, player_choice):
        #Determines the outcome of the game based on user preferences and computer preferences.
        #and this condition return a message the player win, lose or draw the game

        if player_choice not in ["rock", "paper", "scissor"]: #Raises: If the player_choice is not on of the option
            raise RockPaperScissor.InvalidChoiceError("Invalid choice! please enter Rock, Paper or Scissor") 

        if (player_choice == "rock" and self.cmp_choice == "paper") or (player_choice == 'paper' and self.cmp_choice == 'scissor') or (player_choice == "scissor" and self.cmp_choice == "rock"):
            return f"Your lose! computer move {self.cmp_choice}, your move {player_choice}"

        elif (player_choice == "rock" and self.cmp_choice == "scissor") or (player_choice == 'paper' and self.cmp_choice == 'rock') or (player_choice == 'scissor' and self.cmp_choice == 'paper'):
            return f"Your win! computer move {self.cmp_choice}, your move {player_choice}"

        else:
            return f"Draw! computer move {self.cmp_choice}, your move {player_choice}"



def main():
    # Runs the game in a loop until the user decides to quit
    is_running = True
    while is_running:
        try:
            # Ask the user if they want to play
            choicce = input("Do you want to play? (y/n): ").strip().lower()
            if choicce == 'y':
                cmp_choice = ["rock", "paper", "scissor"]
                cmp_choice = random.choice(cmp_choice) # Generate a random choice for Computer

                # Display the options for the user
                print("Player move:")
                print("1. Rock")
                print("2. Paper")
                print("3. Scissor")

                player_choice = input("Enter your choice: ").strip().lower() # Get user choice

                game = RockPaperScissor(cmp_choice) # Call the RockPaperScissor class

                try:
                    # Display the result
                    result = game.move(player_choice)
                    print(result)
                except RockPaperScissor.InvalidChoiceError as e: # Handle invalid input for the player choice
                    print(f"Error: {e}") # Print the error message

            elif choicce == 'n': # End the game
                print("Thanks for playing!")
                is_running = False
            
            else: # Handle the ValueError message if the user enters anything other than 'y' or 'n'
                raise ValueError("Invalid input! Please Enter 'y' or 'n'")

        except ValueError as e:
            # Catch and display error for invalid input
            print(f"Error: {e}")
            
if __name__ == "__main__":
    main()