import random

def generate_word():
    # Generate a random word for the player to unscramble
    words = ["apple", "banana", "orange", "grape", "kiwi"]
    selected_word = random.choice(words)
    scrambled_word = scramble(selected_word)
    return selected_word, scrambled_word

def scramble(word):
    # Scramble the letters of the word
    shuffled_letters = list(word)
    random.shuffle(shuffled_letters)
    scrambled_word = ''.join(shuffled_letters)
    return scrambled_word

def get_player_input():
    # Get player's guess
    return input("Your guess: ").lower()

def main():
    player_score = 0
    number_of_rounds = 3

    for round_num in range(1, number_of_rounds + 1):
        print("Round", round_num)
        selected_word, scrambled_word = generate_word()
        print("Scrambled Word:", scrambled_word)
        player_guess = get_player_input()

        if player_guess == selected_word:
            print("Correct! You unscrambled the word.")
            player_score += 1
        else:
            print("Incorrect. The correct word is:", selected_word)

    print("Game Over. Your final score is:", player_score, "out of", number_of_rounds)

# Run the game
main()
