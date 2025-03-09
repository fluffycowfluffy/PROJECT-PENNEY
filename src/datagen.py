import os
import random
import numpy as np
import subprocess as sp

from helpers import PATH_DATA

HALF_DECK_SIZE = 26

def get_decks(n_decks: int,
              seed: int, 
              half_deck_size: int = HALF_DECK_SIZE 
              ) -> tuple[np.ndarray, np.ndarray]:
  """
  Efficiently generate `n_decks` shuffled decks using NumPy.
  
  Returns:
    decks (np.ndarray): 2D array of shape (n_decks, num_cards), 
    each row is a shuffled deck.
  """
  # create the initial deck: half 1's and half 0's          
  init_deck = [0]*half_deck_size + [1]*half_deck_size
  # repeat the initial deck n_decks times
  decks = np.tile(init_deck, (n_decks, 1))
  rng = np.random.default_rng(seed)
  rng.permuted(decks, axis=1, out=decks) # each slice along the axis of 1 is shuffled independently
  return decks

def decks_to_npy():
  """
  Save 100,000 decks to a .npy file
  """
  ### code for decks:
  # generate seed
  deck_seed = random.randint(0, 100)
  
  # generate the decks
  my_decks = get_decks(1, deck_seed)
  my_decks_array = np.asarray(my_decks)
  
  # create folder and make sure path exists
  deck_directory = os.path.join(os.getcwd(), "deck_storage") 
  os.makedirs(deck_directory, exist_ok = True)

  # save decks to .npy file
  deck_path = os.path.join(deck_directory, f"my_decks_{deck_seed}.npy")
  np.save(deck_path, my_decks_array)

  ### code for the ascii art loading screen:
  # generate seed to iterate through card txt files
  card_seed = random.randint(1, 6)

  # folder for cards loading screen and create it if it doesn't exist to avoid issues
  #card_directory = os.path.join(os.getcwd(), "cards_ascii")
  #os.makedirs(card_directory, exist_ok = True)

  # navigate to varying card pictures for the loading screen
  #card_path = os.path.join(card_directory, f"cards_{card_seed}.txt")
  
  # check function is saving decks correctly
  print(f"Decks saved to: {deck_path} with random seed {deck_seed}")
  print(my_decks)
  try: 
    sp.run(["cat", card_path])
  except Exception as e:
    pass

if __name__ == "__main__":
  decks_to_npy()
