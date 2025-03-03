import numpy as np
import os
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
  save decks to a .npy files
  """
  # generate seed
  seed = random.randint(0, 100)
  
  # generate the decks
  my_decks = get_decks(100000, seed)
  my_decks_array = np.asarray(my_decks)
  
  # create folder and make sure path exists
  storage_dir = os.path.join(os.getcwd(), "deck_storage") 
  os.makedirs(storage_dir, exist_ok = True)
  
  # save decks to .npy file
  file_path = os.path.join("deck_storage", f"my_decks_{seed}.npy")
  np.save(file_path, my_decks_array)
  
  # check function is saving decks correctly
  print(f"Decks saved to: {file_path} with random seed {seed}")
