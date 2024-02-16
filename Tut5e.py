secret="water"
turns=6
print("Game is starting....")
print("You have 6 turns ....")
guess=input("Enter Word:")
y=" _ "
print(len(guess)*y)
for letter in secret:
    if letter in guesses:
        print('', letter, '', end='')
    else:
        print(' _ ', end='')


