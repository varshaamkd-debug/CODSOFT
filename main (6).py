'''

                            Online Python Debugger.
                Code, Run and Debug Python program online.
Write your code in this editor and press "Debug" button to debug program.

'''
import random

def play_game():
    # Choices mapping for easy validation
    choices = ["rock", "paper", "scissors"]
    
    # Score tracking
    user_score = 0
    computer_score = 0
    
    print("=" * 40)
    print("Welcome to Rock, Paper, Scissors!")
    print("Rules: Rock beats Scissors | Scissors beats Paper | Paper beats Rock")
    print("=" * 40)
    
    while True:
        # 1. User Input with validation
        user_choice = input("\nChoose rock, paper, or scissors (or type 'quit' to exit): ").lower().strip()
        
        if user_choice == 'quit':
            break
            
        if user_choice not in choices:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue
            
        # 2. Computer Selection
        computer_choice = random.choice(choices)
        
        # 3. Display Choices
        print(f"\nYou chose: {user_choice.capitalize()}")
        print(f"Computer chose: {computer_choice.capitalize()}")
        
        # 4. Game Logic & Display Result
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("🎉 You win this round!")
            user_score += 1
        else:
            print("😢 You lose this round.")
            computer_score += 1
            
        # 5. Display Score
        print(f"Current Score -> You: {user_score} | Computer: {computer_score}")
        
        # 6. Play Again
        play_again = input("\nDo you want to play another round? (yes/no): ").lower().strip()
        if play_again not in ['yes', 'y']:
            break
            
    print("\n" + "=" * 40)
    print("Thanks for playing!")
    print(f"Final Score -> You: {user_score} | Computer: {computer_score}")
    print("=" * 40)

if __name__ == "__main__":
    play_game()