import os
import numpy as np

from src.helpers import PATH_DATA

def total_deck_count() -> int:
   # making sure it can find the correct directory path to the decks
   deck_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "deck_storage")

   # length for calculating win rate
   N = 0

   # loop through decks in the deck_storage folder and count the length of each one for storage in the N variable                  
   deck_arrays = [file for file in os.listdir(deck_directory)if file.endswith(".npy")]
   for deck_array in deck_arrays:
      file_path = os.path.join(deck_directory, deck_array)
      # load the data; pickled objects are allowed in order to load the array .npy files in the folder
      decks = np.load(file_path, allow_pickle = True)
      N += len(decks)

   return N


def penneys_game(P1: list, # store data
                 P2: list):
  """
  Loop through each card in the deck,
  save these cards to a list where the final three cards care always being checked
  for a match to the players' sequences
  if the player sequence matches the last three, this player gets a trick
  """
  # numpy array to store data for win frequency calculation
  win_frequency = np.zeros(3)
  
  # list for trick data
  trick_check = []
  
  # making sure it can find the correct directory path to the decks
  deck_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "deck_storage")
  
  # length for calculating win rate
  N = total_deck_count()

  # loop through decks in the deck_storage folder and count the length of each one for storage in the N variable                  
  deck_arrays = [file for file in os.listdir(deck_directory)if file.endswith(".npy")]
  for deck_array in deck_arrays:
    file_path = os.path.join(deck_directory, deck_array)
    # load the data; pickled objects are allowed in order to load the array .npy files in the folder
    decks = np.load(file_path, allow_pickle = True)
    #N += len(decks)

    # store tricks counts for player 1 and 2 for future calculations
    P1_tricks = 0
    P2_tricks = 0
  
    for deck in decks:
       for card in deck:
          trick_check.append(card)
          if len(trick_check) >= 3:
             if trick_check[-3:] == P1:
                P1_tricks += 1
                trick_check = []
             elif trick_check[-3:] == P2:
                P2_tricks += 1
                trick_check = []
       # calculate win frequency
       if P1_tricks > P2_tricks:
          win_frequency[0] += 1
       elif P2_tricks > P1_tricks:
          win_frequency[1] += 1
       elif P1_tricks == P2_tricks:
          win_frequency[2] += 1
       # reset trick check and trick counts after each deck
       trick_check = []
       P1_tricks = 0
       P2_tricks = 0
  
  # calculate win rate
  win_rate = win_frequency*1.0/N
  return win_rate
