# To get a random word
import wonderwords

r = wonderwords.RandomWord()
random_word = r.word().lower()

Hangman_ascii = [r'''
  +---+
  |   |
      |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
incorrect_tries = 0
guessed_word = ['_' for elem in random_word]

while incorrect_tries != 6:
    guessed_word_str = ''

    print("Current state is\n")
    print(Hangman_ascii[incorrect_tries])

    print(f"Tries left {6 - incorrect_tries}")
    for elem in guessed_word:
        guessed_word_str += elem
    print(guessed_word_str)

    if guessed_word_str != random_word:
        guessed_letters = input("Guess the word, Guess the entire word or a single letter\n").lower()
    if guessed_word_str == random_word:
        print(f"You Won, The word actually was {random_word}")
        break
    elif guessed_letters == random_word:
        guessed_word = guessed_letters
        print(f'The word was {guessed_word}', "You Won!!!!")
        break
    elif len(random_word) != len(guessed_word) or len(guessed_letters) != 1:
        print("Choose the correct amount of letters")
    elif guessed_letters in random_word:
        for elem_idx in range(0, len(random_word)):
            if random_word[elem_idx] == guessed_letters:
                guessed_word[elem_idx] = guessed_letters

    elif guessed_letters not in random_word:
        print('Oops!!Wrong guess')
        incorrect_tries += 1
    else:
        print("Enter a valid input")
else:
    print("You lost sucker, The word was", random_word)
