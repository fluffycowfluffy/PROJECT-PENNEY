import os
import numpy as np
from tqdm import tqdm

from src.datagen import decks_to_npy
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
                 P2: list) -> np.ndarray:
   """
   Loop through each card in the deck,
   save these cards to a list where the final three cards care always being checked
   for a match to the players' sequences
   if the player sequence matches the last three, this player gets a trick
   """
   # numpy array to store data for win frequency calculation
   win_frequency = np.zeros((2,3))

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

      # store tricks counts for player 1 and 2 for future calculations
      P1_tricks = 0
      P2_tricks = 0

      # store card counts for players 1 and 2
      P1_cards = 0
      P2_cards = 0

      for deck in decks:
         deck_check = []
         for card in deck:
            deck_check.append(card)
            if len(deck_check) >= 3:
               if deck_check[-3:] == P1:
                  P1_tricks += 1
                  P1_cards += len(deck_check)
                  deck_check = []
               elif deck_check[-3:] == P2:
                  P2_tricks += 1
                  P2_cards += len(deck_check)
                  deck_check = []
            else:
               pass
         # store win frequency data for tricks
         if P1_tricks > P2_tricks:
            win_frequency[0, 0] += 1
         elif P1_tricks < P2_tricks:
            win_frequency[0, 1] += 1
         elif P1_tricks == P2_tricks:
            win_frequency[0, 2] += 1

         # store win frequency data for cards
         if P1_cards > P2_cards:
            win_frequency[1, 0] += 1
         elif P1_cards < P2_cards:
            win_frequency[1, 1] += 1
         elif P1_cards == P2_cards:
            win_frequency[1, 2] += 1

         # reset deck check and trick/card counts after each deck
         deck_check = []
         P1_tricks = 0
         P2_tricks = 0
         P1_cards = 0
         P2_cards = 0
  
   # calculate win rate
   win_rate = win_frequency*1.0/N
   return win_rate

def data_storage() -> tuple:
  """
  Generate arrays from the probabilities 
  found in the penneys_game() function by tricks/cards
  """
  # as 1,000,000 decks have already been provided
  # this prompts users to enter more decks if they so choose
  decks_to_npy()

  sequences = ['000','001','010','011','100','101','110', '111']
  n = len(sequences)

  # create empty array for tricks
  trick_wins = np.zeros((n,n))
  trick_losses = np.zeros((n,n))
  # create empty array for cards
  card_wins = np.zeros((n,n))
  card_losses = np.zeros((n,n))

  print("Calculating probabilities...generating heatmaps...")
  # iterate twice over sequences; create progress bar
  for i in tqdm(range(n)):
    P1 = list(map(int, sequences[i]))
    for j in range(n):
      # create all possible sequences for players 1 and 2 so they may be
      # used in the penneys_game() function as list objects
      P2 = list(map(int, sequences[j]))
      # save win rate to variable
      win_rate = penneys_game(P1, P2)
      # fill dataframe with combonation data 
      # for each sequence played against another
      trick_wins[i,j] = win_rate[0, 0]
      trick_losses[i,j] = win_rate[0, 1]
      # repeat for card count
      card_wins[i,j] = win_rate[1, 0]
      card_losses[i,j] = win_rate[1, 1]

  # set the diagonal to NaNs for masking purposes
  np.fill_diagonal(trick_wins, np.nan)
  np.fill_diagonal(trick_losses, np.nan)
  # again for card count arrays
  np.fill_diagonal(card_wins, np.nan)
  np.fill_diagonal(card_losses, np.nan)

  win_loss_tuple = (trick_wins, trick_losses, card_wins, card_losses)
  return win_loss_tuple
