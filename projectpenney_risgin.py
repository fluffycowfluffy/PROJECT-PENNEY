# required imports
import os
import random
import numpy as np
from tqdm import tqdm
import seaborn as sns
import matplotlib.pyplot as plt

from src.helpers import PATH_DATA

HALF_DECK_SIZE = 26

def get_decks(n_decks: int,
              seed: int,
              half_deck_size: int = HALF_DECK_SIZE
              ) -> tuple[np.ndarray, np.ndarray]:
    """
    Generate n number ('n_decks') of shuffled decks using NumPy

    -> Return:
       decks (np.nd.array): 2D array of shape (n_decks, num_cards),
       each row is a shuffled deck
    """
    init_deck = [1]*half_deck_size + [0]*half_deck_size # Create the initial deck: half 1's and half 0's
    decks = np.tile(init_deck, (n_decks, 1)) # repeat the inital deck n_decks times
    rng = np.random.default_rng(seed)
    rng.permuted(decks, 
                 axis=1, 
                 out=decks) # each slice along the axis of 1 is shuffled independently
    print(decks)
    return decks

def decks_to_npy():
   """
   save decks to a .npy files
   """
   # generate seed
   seed = random.randint(0,100)

   # generate the decks
   my_decks = get_decks(100000, seed)
   my_decks_array = np.asarray(my_decks)

   # create folder and make sure path exists
   storage_dir = os.path.join(os.getcwd(), "deck_storage")  # Absolute path to the current working directory
   os.makedirs(storage_dir, exist_ok=True)

   # save decks to .npy file
   file_path = os.path.join("deck_storage", f"my_decks_{seed}.npy")
   np.save(file_path, my_decks_array)

   print(f"Decks saved to: {file_path} with random seed {seed}")

def penneys_game(P1: list, # store data
                 P2: list):
   """
   loop through each card in the deck,
   save these cards to a list where the final three cards care always being checked
   for a match to the players' sequences
   if the player sequence matches the last three, this player gets a trick
   """
   # numpy array to story data for win frequency calculation
   win_frequency = np.zeros(3)

   # list for trick data
   trick_check = []

   # our directory to the decks
   directory = "deck_storage"

   # length for calculating win rate
   N = 0

   deck_arrays = [file for file in os.listdir(directory)if file.endswith(".npy")]
   for deck_array in deck_arrays:
      file_path = os.path.join(directory, deck_array)
      decks = np.load(file_path, allow_pickle = True)
      N += len(decks)

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

def create_heatmap():
   """
   generate a heatmap from the probabilities 
   found in the penneys_game() function
   """
   # generate 1 million decks (or more idk how many you want :/)
   for i in range(10):
      decks_to_npy()

   # try deck.index() where deck str
   # make the middle diagonal blank
   sequences = ['000','001','010','011','100','101','110', '111']
   n = len(sequences)

   # create empty array
   penney_prob_arr_wins = np.zeros((n,n))
   penney_prob_arr_losses = np.zeros((n,n))
   
   # iterate twice over sequences
   for i in tqdm(range(n)):
      for j in range(n):
         # create all possible sequences for players 1 and 2 so they may be
         # used in the penneys_game() function as list objects
         P1 = list(map(int, sequences[i]))
         P2 = list(map(int, sequences[j]))
         # save win rate to variable
         win_rate = penneys_game(P1, P2)
         # fill dataframe with combonation data 
         # for each sequence played against another
         penney_prob_arr_wins[i,j] = win_rate[0]
         penney_prob_arr_losses[i,j] = win_rate[1]

   # set the diagonal to NaNs for masking purposes
   np.fill_diagonal(penney_prob_arr_wins, np.nan)
   np.fill_diagonal(penney_prob_arr_losses, np.nan)

   # make sure data are floats so the heatmap can be generated
   penney_prob_arr_wins = penney_prob_arr_wins.astype(float)
   penney_prob_arr_losses = penney_prob_arr_losses.astype(float)

   # create my wins heatmap :)
   ax1 = plt.axes()
   my_heatmap_wins = sns.heatmap(penney_prob_arr_wins,
                            ax = ax1, 
                            annot = True, 
                            cmap = "YlGn")
   ax1.set_xticklabels(sequences)
   ax1.set_yticklabels(sequences)
   ax1.set_title("Probabilities of P1 Winning Against P2", fontsize = 20)
   ax1.set_ylabel("P1 Sequences", fontsize = 15)
   ax1.set_xlabel("P2 Sequences", fontsize = 15)
   heatmap_path_wins = 'penneys_prob_heatmap_wins.png'
   plt.savefig(heatmap_path_wins, dpi = 400)

   # clear the figure
   plt.clf()

   # losses heatmap
   ax2 = plt.axes()
   my_heatmap_losses = sns.heatmap(penney_prob_arr_losses,
                            ax = ax2, 
                            annot = True, 
                            cmap = "YlOrBr")
   ax2.set_xticklabels(sequences)
   ax2.set_yticklabels(sequences)
   ax2.set_title("Probabilities of P1 Losing Against P2", fontsize = 20)
   ax2.set_ylabel("P1 Sequences", fontsize = 15)
   ax2.set_xlabel("P2 Sequences", fontsize = 15)
   heatmap_path_losses = 'penneys_prob_heatmap_losses.png'
   plt.savefig(heatmap_path_losses, dpi = 400)


   print(penney_prob_arr_wins)
   print(penney_prob_arr_losses)

if __name__ == "__main__":
   create_heatmap()