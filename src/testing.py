import os
import numpy as np

from helpers import PATH_DATA

def penneys_game(P1: list, # store data
                 P2: list) -> np.ndarray:
  """
  Loop through each card in the deck,
  save these cards to a list where the final three cards care always being checked
  for a match to the players' sequences
  if the player sequence matches the last three, this player gets a trick
  """
  # numpy array to store data for win frequency calculation
  win_frequency_tricks = np.zeros(3)
  win_frequency_cards = np.zeros(3)
  
  # list for trick/card data
  deck_check = []
  
  # making sure it can find the correct directory path to the decks
  #deck_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "deck_storage")
  deck_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "deck_storage")
  
  # length for calculating win rate
  N = 0

  # loop through decks in the deck_storage folder and count the length of each one for storage in the N variable                  
  deck_arrays = [file for file in os.listdir(deck_directory)if file.endswith(".npy")]
  for deck_array in deck_arrays:
    file_path = os.path.join(deck_directory, deck_array)
    # load the data; pickled objects are allowed in order to load the array .npy files in the folder
    decks = np.load(file_path, allow_pickle = True)
    N += len(decks)

    # store tricks counts for player 1 and 2 for future calculations
    P1_tricks = 0
    P2_tricks = 0
    # store card counts for player 1 and 2 for future calculations
    P1_cards = 0
    P2_cards = 0
  
    for deck in decks:
       for card in deck:
          deck_check.append(card)
          if len(deck_check) >= 3:
             if deck_check[-3:] == P1:
                P1_tricks += 1
                #print(f" P1 trick count: {P1_tricks}")
                P1_cards += len(deck_check)
                #print(f" P1 card count: {P1_cards}")
                deck_check = []
             elif deck_check[-3:] == P2:
                P2_tricks += 1
                #print(f" P2 trick count: {P2_tricks}")
                P2_cards += len(deck_check)
                #print(f" P2 card count:{P2_cards}")
                deck_check = []
       # calculate win frequency for tricks
       if P1_tricks > P2_tricks:
          win_frequency_tricks[0] += 1
       elif P1_tricks < P2_tricks:
          win_frequency_tricks[1] += 1
       elif P1_tricks == P2_tricks:
          win_frequency_tricks[2] += 1
       # calculate win frequency for card count
       if P1_cards > P2_cards:
           win_frequency_cards[0] += 1
       elif P1_cards < P2_cards:
           win_frequency_cards[1] += 1
       elif P1_cards == P2_cards:
           win_frequency_cards[2] += 1
       # reset deck_check and trick/card counts after each deck
       #deck_check = []
       P1_tricks = 0
       P2_tricks = 0
       P1_cards = 0
       P2_cards = 0
  
  # calculate win rate and store both to arrays
  win_rate_tricks = win_frequency_tricks*1.0/N
  win_rate_cards = win_frequency_cards*1.0/N
  win_rate = np.array([win_rate_tricks, win_rate_cards])
  #print(win_rate)
  print(deck_check)
  #return win_rate

if __name__ == "__main__":
  penneys_game([0,0,0], [1,0,0])
