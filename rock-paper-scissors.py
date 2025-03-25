import random

# Rock, Paper, Scissors Function
def game():
    options = ["rock", "paper", "scissors"]
    while True:
        users_pick = input("Choose Rock, Paper, or Scissors: ").strip().lower()
        if users_pick not in options:
            print("Sorry, that's not an option. Try again?")
            continue
        comps_pick = random.choice(options)
        if users_pick == comps_pick:
            print(f"Ha! I also chose {comps_pick}, try again!")
        elif (users_pick == "paper" and comps_pick == "rock") or \
            (users_pick == "scissors" and comps_pick == "paper") or \
            (users_pick == "rock" and comps_pick == "scissors"):
            print(f"Shoot, I chose {comps_pick}. You won!")
            break
        else:
            print(f"Ha, I got you! I chose {comps_pick}. Try it again!")
        
# Execute
game()
