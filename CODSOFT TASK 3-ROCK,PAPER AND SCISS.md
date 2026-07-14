## CODSOFT TASK 3-ROCK,PAPER AND SCISSORS GAME



import random



def play\_game():

&#x20;   # Choices mapping for easy validation

&#x20;   choices = \["rock", "paper", "scissors"]

&#x20;   

&#x20;   # Score tracking

&#x20;   user\_score = 0

&#x20;   computer\_score = 0

&#x20;   

&#x20;   print("=" \* 40)

&#x20;   print("Welcome to Rock, Paper, Scissors!")

&#x20;   print("Rules: Rock beats Scissors | Scissors beats Paper | Paper beats Rock")

&#x20;   print("=" \* 40)

&#x20;   

&#x20;   while True:

&#x20;       # 1. User Input with validation

&#x20;       user\_choice = input("\\nChoose rock, paper, or scissors (or type 'quit' to exit): ").lower().strip()

&#x20;       

&#x20;       if user\_choice == 'quit':

&#x20;           break

&#x20;           

&#x20;       if user\_choice not in choices:

&#x20;           print("Invalid choice! Please choose rock, paper, or scissors.")

&#x20;           continue

&#x20;           

&#x20;       # 2. Computer Selection

&#x20;       computer\_choice = random.choice(choices)

&#x20;       

&#x20;       # 3. Display Choices

&#x20;       print(f"\\nYou chose: {user\_choice.capitalize()}")

&#x20;       print(f"Computer chose: {computer\_choice.capitalize()}")

&#x20;       

&#x20;       # 4. Game Logic \& Display Result

&#x20;       if user\_choice == computer\_choice:

&#x20;           print("It's a tie!")

&#x20;       elif (user\_choice == "rock" and computer\_choice == "scissors") or \\

&#x20;            (user\_choice == "scissors" and computer\_choice == "paper") or \\

&#x20;            (user\_choice == "paper" and computer\_choice == "rock"):

&#x20;           print("🎉 You win this round!")

&#x20;           user\_score += 1

&#x20;       else:

&#x20;           print("😢 You lose this round.")

&#x20;           computer\_score += 1

&#x20;           

&#x20;       # 5. Display Score

&#x20;       print(f"Current Score -> You: {user\_score} | Computer: {computer\_score}")

&#x20;       

&#x20;       # 6. Play Again

&#x20;       play\_again = input("\\nDo you want to play another round? (yes/no): ").lower().strip()

&#x20;       if play\_again not in \['yes', 'y']:

&#x20;           break

&#x20;           

&#x20;   print("\\n" + "=" \* 40)

&#x20;   print("Thanks for playing!")

&#x20;   print(f"Final Score -> You: {user\_score} | Computer: {computer\_score}")

&#x20;   print("=" \* 40)



if \_\_name\_\_ == "\_\_main\_\_":

&#x20;   play\_game()

