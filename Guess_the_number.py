import random
art = '''
██████╗ ██╗   ██╗███████╗███████╗███████╗    ████████╗██╗  ██╗███████╗
██╔════╝ ██║   ██║██╔════╝██╔════╝██╔════╝    ╚══██╔══╝██║  ██║██╔════╝
██║  ███╗██║   ██║█████╗  ███████╗███████╗       ██║   ███████║█████╗  
██║   ██║██║   ██║██╔══╝  ╚════██║╚════██║       ██║   ██╔══██║██╔══╝  
╚██████╔╝╚██████╔╝███████╗███████║███████║       ██║   ██║  ██║███████╗
 ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝       ╚═╝   ╚═╝  ╚═╝╚══════╝

███╗   ██╗██╗   ██╗███╗   ███╗██████╗ ███████╗██████╗ 
████╗  ██║██║   ██║████╗ ████║██╔══██╗██╔════╝██╔══██╗
██╔██╗ ██║██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
'''
chances = {'easy': 10, 'hard': 5}
print("Welcome to the number guessing game!!")
mode = input("Choose a difficulty: Type 'easy' or 'hard'\n").lower()
print("I am thinking of a number between 1 to 100 (inclusive)")

def play():
    num = random.randint(1, 100)
    for i in range(chances[mode], 0, -1):
        guess = int(input(f"You have {i} chances remaining : guess the number:\n"))
        if i == 1:
            print("oops You ran out of chances!")
            break
        elif guess == num:
            print(f"You Won!! The number was {num}")
            break
        elif guess > num:
            print("Too high")
        elif guess < num:
            print("Too low")

play()





