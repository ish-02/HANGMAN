import random
from string import ascii_lowercase
print("H A N G M A N")
menu = input('Type "play" to play the game, "exit" to quit:')
if menu == 'play':
    word_list = ['python', 'java', 'kotlin']
    random_word = random.choice(word_list)
    dashes = '-' * len(random_word)
    guessed_word = set()
    i = 0
    while i <= 8:
        print("\n" + dashes)
        guess = input("Input a letter:")
        if len(guess) == 1:
            if guess in ascii_lowercase:
                if guess in guessed_word:
                    print("You already typed this letter")
                else:
                    if guess in list(random_word):
                        pos = [p for p in range(len(random_word)) if random_word.startswith(guess, p)]
                        dashes = list(dashes)
                        for p in pos:
                            dashes[p] = guess
                        dashes = "".join(dashes)
                    else:
                        print("No such letter in the word")
                        i += 1
            else:
                print("It is not an ASCII lowercase letter")
        else:
            print("You should input a single letter")
        if dashes == random_word:
            print("You guessed the word!\nYou survived!")
            exit()
        elif i == 8:
            print("You are hanged!")
            exit()
        guessed_word.add(guess)
elif menu == 'exit':
    exit()