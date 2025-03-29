import os
import random
import numpy as np
import subprocess as sp

from src.helpers import PATH_DATA

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
  ### code for the ascii art loading screen:
  # generate seed to iterate through card txt files
  card_seed = random.randint(1, 6)

  # folder for cards loading screen and create it if it doesn't exist to avoid issues
  card_directory = os.path.join(os.getcwd(), "cards_ascii")
  os.makedirs(card_directory, exist_ok = True)

  # navigate to varying card pictures for the loading screen
  card_path = os.path.join(card_directory, f"cards_{card_seed}.txt")

  ### code for decks:
  # create folder and make sure path exists
  deck_directory = os.path.join(os.getcwd(), "deck_storage") 
  os.makedirs(deck_directory, exist_ok = True)

  # generate seed by incrementing base seed of 0
  _,_,files = next(os.walk(deck_directory))
  # increment by number of files in directory
  seed_increment = len(files)
  deck_seed = -1 + seed_increment
  
  # generate the decks
  more_decks = input("Would you like to generate more decks? (Y/N)").strip().upper()

  while more_decks == "Y":
    additional_decks = input("How many more decks would you like to generate? Please enter a number:")
    try:
      # generate additional decks based on user input
      my_decks = get_decks(int(additional_decks), deck_seed)
      my_decks_array = np.asarray(my_decks)

      # save decks to .npy file
      deck_path = os.path.join(deck_directory, f"my_decks_{deck_seed}.npy")
      np.save(deck_path, my_decks_array)

      # check function is saving decks correctly
      print(f"Decks saved to: {deck_path} with random seed {deck_seed}")
      try: 
        sp.run(["cat", card_path])
      except Exception as e:
        pass
    except Exception as e:
      print("Experienced error: {e}. Continuing without additional deck generation.")
    break
  if more_decks == "N":
    print("Continuing on to calculations...")
  elif(more_decks != "Y" and more_decks != "N"):
    print("Invalid input. Continuing on to calculations...")
