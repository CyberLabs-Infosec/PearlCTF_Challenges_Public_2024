#!/usr/local/bin/python

import numpy as np
import pickle
import signal
import os

TIMEOUT_TIME = 5

words = []
vectors = np.array([])
word_vectors = {}

class TimeoutException(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutException("Input timed out")

def load_word_vectors():
    global words, vectors, word_vectors
    with open("save.pkl", "rb") as f:
        words, vectors = pickle.load(f)
        word_vectors = {k: v for k, v in zip(words, vectors)}

def similarity(guess, target):
    val = np.dot(word_vectors[guess], word_vectors[target])
    return abs(round(val * 100, 2))

def word_guess_challenge():
    global words, word_vectors
    target_word = np.random.choice(words)
    print(f"Welcome to the Word Guess Challenge!\nYou have 5 attempts to guess the word based on the similarity hints.")

    for attempt in range(1, 6):
        while True:
            signal.signal(signal.SIGALRM, timeout_handler)
            signal.alarm(TIMEOUT_TIME)
            try:
                user_guess = input(f"\nAttempt {attempt}: Enter your guess: ").lower().strip()

                if user_guess in words:
                    break
                else:
                    print("Error: The entered word is not in the model vocabulary. Try another word.")
            except TimeoutException:
                print("\nError: Input timed out. Exiting the program.")
                exit(1)
            finally:
                signal.alarm(0)
        
        sim_score = similarity(user_guess, target_word)

        if user_guess == target_word:
            print(f"Congratulations! You guessed the correct word '{target_word}' in {attempt} attempts.")
            print("pearl{d4yumm_y0u_kn0w_y0ur_v3ct0rs}")
            break
        else:
            print(f"Similarity to the target word: {sim_score}")

    if user_guess != target_word:
        print(f"Sorry, you did not guess the correct word. ")

if __name__ == '__main__':
    load_word_vectors()
    word_guess_challenge()
