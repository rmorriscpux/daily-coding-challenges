'''
Alice wants to join her school's Probability Student Club. Membership dues are computed via one of two simple probabilistic games.

The first game: roll a die repeatedly. Stop rolling once you get a five followed by a six. Your number of rolls is the amount you pay, in dollars.

The second game: same, except that the stopping condition is a five followed by a five.

Which of the two games should Alice elect to play? Does it even matter? Write a program to simulate the two games and calculate their expected value.
'''

# The choice of game does not matter. Each roll is independent and each outcome has a 1 in 6 chance of occurring.

from random import randint

def game1(rounds: int):
    assert rounds > 0

    total_rolls = 0
    for i in range(0, rounds):
        five_rolled = False
        outcome = 0
        while True:
            outcome = randint(1, 6)
            total_rolls += 1

            if five_rolled == True and outcome == 6:
                break

            if five_rolled == False and outcome == 5:
                five_rolled = True

    return total_rolls / rounds

print(game1(1000))

def game2(rounds: int):
    assert rounds > 0

    total_rolls = 0
    for i in range(0, rounds):
        five_rolled = False
        outcome = 0
        while True:
            outcome = randint(1, 6)
            total_rolls += 1

            if five_rolled == True and outcome == 5:
                break

            if five_rolled == False and outcome == 5:
                five_rolled = True

    return total_rolls / rounds

print(game2(1000))