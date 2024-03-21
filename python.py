import random

# Initializing player's score and number of rounds
playerScore = 0
numOfRounds = 5

# Function to generate a scrambled word
def scramble():
    words = ["kyoto", "hiroshima", "shibuya", "yokohama", "ishikawa", "hokkaido", "kitakyushu", "himeji", "aomori", "saitama"]
    randomWord = random.choice(words)
    letters = []
    # Shuffling the letters of the chosen word
    for i in randomWord:
        letters.append(i)
    random.shuffle(letters)
    scrambledWord = ""
    for i in letters:
        scrambledWord += i
    return [scrambledWord, randomWord]

# Looping through the number of rounds
for i in range(1, numOfRounds + 1):
    # Generating a scrambled word for each round
    scrambledWordArray = scramble()
    scrambledWord = scrambledWordArray[0]
    unscrambledWord = scrambledWordArray[1]
    print("Round number:", i)
    print("Scrambled word:", scrambledWord)
    # Asking the player to enter the unscrambled word
    userWord = input("Enter the unscrambled word: ")
    # Checking if the player's input matches the unscrambled word
    if userWord == unscrambledWord:
        playerScore += 1

# Printing the player's score after all rounds
print("The result of the game:", playerScore)

# Providing the result based on the player's score
if playerScore == 0:
    print("You didn't score any points. Better luck next time!")
elif playerScore == 1:
    print("You scored 1 point. Keep practicing!")
elif playerScore == 2:
    print("You scored 2 points. Well done, but you can do better!")
elif playerScore == 3:
    print("Congratulations! You scored 3 points. You're a word-scrambling expert!")
else:
    print("Invalid score.")
