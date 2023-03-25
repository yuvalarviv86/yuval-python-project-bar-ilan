# Import the random to make a random options
import random
# Import time to know when 30 seconds are done
import time


def generate_phrase():
    # Make a list of few words from the doc
    phrases = [['always', 'be', 'yourself'], ['keep', 'it', 'cool'], ['never', 'give', 'up'],
               ['live', 'laugh', 'love'], ['stay', 'positive', 'always'], ['dream', 'big', 'today'],
               ['never', 'stop', 'learning'], ['do', 'what', 'you', 'love'], ['be', 'your', 'best'],
               ['never', 'lose', 'hope']]
    # Make 1 random phrase from the list and hide it
    index = random.randint(0, len(phrases) - 1)
    phrase = phrases[index]
    hidden_phrase = ['_ ' * len(phrase[i]) for i in range(len(phrase))]
    return phrase, hidden_phrase


def display_phrase(hidden_phrase):
    for i in range(len(hidden_phrase)):
        print(hidden_phrase[i])


def update_hidden_phrase(hidden_phrase, phrase, letter):
    for i in range(len(phrase)):
        for j in range(len(phrase[i])):
            if phrase[i][j] == letter:
                hidden_phrase[i] = hidden_phrase[i][:2 * j] + letter + hidden_phrase[i][2 * j + 1:]
    return hidden_phrase


def play_game():
    phrase, hidden_phrase = generate_phrase()
    display_phrase(hidden_phrase)
    # Start the time count
    start_time = time.time()
    # Set score to 0
    score = 0
    while True:
        # Let the user enter 1 letter
        letter = input("Guess 1 letter: ").lower()
        # If function
        if letter in phrase[0] or letter in phrase[1] or letter in phrase[2]:
            hidden_phrase = update_hidden_phrase(hidden_phrase, phrase, letter)
            display_phrase(hidden_phrase)
            # Add 5 points
            score += 5
        else:
            # Remove 1 point
            score -= 1
        if '_ ' not in hidden_phrase[0] and '_ ' not in hidden_phrase[1] and '_ ' not in hidden_phrase[2]:
            # Time is stop and calculate the points if was less than 30 seconds
            end_time = time.time()
            time_taken = end_time - start_time
            # Make the time less than 30 to get 100 points
            if time_taken < 30:
                score += 100
            # Message if the user has done and print the pharse as well
            print("Congratulations! You guessed the", phrase)
            # Show the user his score based on the actions
            print("Your score is:", score)
            break


play_game()
