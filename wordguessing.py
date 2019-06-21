import random
from collections import Counter
Words1 = '''apple banana mango strawberry orange grape pineapple apricot lemon coconut watermelon
cherry papaya berry peach  muskmelon'''
Words2= '''bournville kitkat milkybar dairymilk gems perk silk munch barone ferrerorocher snickers eclairs'''
Words3= '''nokia oneplus oppo vivo xiaomi htc jio samsung huawei honor blackberry apple lenovo'''
Words4='''audi bmw ferrari ford honda mercedes nissan porsche toyota volkswagen bugatti hyundai jaguar lamborghini '''
Cat=input("pick your category 1.Fruits 2. Chocolates 3.Mobile Company 4. Cars\n")
if Cat == '1':
    someWords = Words1.split(' ')
    word = random.choice(someWords)
elif Cat=='2':
    someWords = Words2.split(' ')
    word = random.choice(someWords)
elif Cat == '3':
    someWords = Words3.split(' ')
    word = random.choice(someWords)
elif Cat == '4':
    someWords = Words4.split(' ')
    word = random.choice(someWords)
print('Guess the word!')
for i in word:
        print('_', end = ' ')
letterGuessed = ''
chances = len(word) + 2
correctGuess = 0
flag = 0
print()
while (chances != 0) and flag == 0:
        print("you have ",chances," chances left")
        chances -= 1
        guess = str(input('Enter a letter to guess: '))

        if not guess.isalpha():
            print('Enter only a LETTER')
            continue
        elif len(guess) > 1:
            print('Enter only a SINGLE letter')
            continue
        elif guess in letterGuessed:
            print('You have already guessed that letter')
            continue

        if guess not in word:
            print("Wrong Guess")
        if guess in word:
            counts = word.count(guess)
            for _ in range(counts):
                letterGuessed += guess

        for char in word:
            if char in letterGuessed and (Counter(letterGuessed) != Counter(word)):
                print(char, end=' ')
                correctGuess += 1

            elif (Counter(letterGuessed) == Counter(word)):

                print("The word is: ",word)
                flag = 1
                print('Congratulations, You won!')
                break
                break
            else:
                print('_', end=' ')


if chances <= 0 and (Counter(letterGuessed) != Counter(word)):
        print()
        print('You lost! Try again..')
        print('The word was {}'.format(word))

