import random


Rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
Paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
Scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
gestures = [Rock, Paper, Scissors]
draws = 0
Noobs_score = 0
Comp_score = 0
rounds = int(input("Enter tries in a round You piece of shit"))
for chance in range(rounds):
    Comp_Choice = random.randint(0, 2)
    Noobs_Choice = int(input("Enter 0 for Rock, 1 for Paper, 2 for Scissor"))
    print('Comp Chose\n', gestures[Comp_Choice])
    print('You chose\n', gestures[Noobs_Choice])
    if Comp_Choice == Noobs_Choice:
        print(f'No one gets a point, rounds left are {rounds-1-chance}')
        draws += 1
    elif Comp_Choice == 0 and Noobs_Choice == 1:
        print(f"You won this round, rounds left are {rounds - 1 - chance}")
        Noobs_score += 1
    elif Comp_Choice == 0 and Noobs_Choice == 2:
        print(f"You lost This round, rounds left are {rounds-1-chance}")
        Comp_score += 1
    elif Comp_Choice == 1 and Noobs_Choice == 0:
        print(f"You lost This round, rounds left are {rounds-1-chance}")
        Comp_score += 1
    elif Comp_Choice == 1 and Noobs_Choice == 2:
        print(f"You won this round, rounds left are {rounds-1-chance}")
        Noobs_score += 1
    elif Comp_Choice == 2 and Noobs_Choice == 0:
        print(f"You won this round, rounds left are {rounds-1-chance}")
        Noobs_score += 1
    elif Comp_Choice == 2 and Noobs_Choice == 1:
        print(f"You lost This round, rounds left are {rounds-1-chance}")
        Comp_score += 1
    else:
        print("Invalid input")

if Comp_score > Noobs_score:
    print("You were destined to loose you turd")
elif Comp_score < Noobs_score:
    print("Every dog has his days, You won!")
elif Comp_score == Noobs_score:
    print("Draw")



