import os
import random
import numpy as np
from tqdm import tqdm
import seaborn as sns
import matplotlib.pyplot as plt

import src.datagen
from src.helpers import PATH_DATA

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
  
  # directory to the decks
  directory = "deck_storage"
  
  # length for calculating win rate
  N = 0

  # loop through decks in the deck_storage folder and count the length of each one for stoarge in the N variable                  
  deck_arrays = [file for file in os.listdir(directory)if file.endswith(".npy")]
  for deck_array in deck_arrays:
    file_path = os.path.join(directory, deck_array)
    # load the data; pickled objects are allowed in order to load the array .npy files in the folder
    decks = np.load(file_path, allow_pickle = True)
    N += len(decks)

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

def create_heatmap():
  """
  Generate a heatmap from the probabilities 
  found in the penneys_game() function
  """
  # as one group 10 100,000 decks has already been provided
  # this has been set to run 9 times in order to result in a final count of 1,000,000 decks
  for i in range(9):
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
  
  # show the final probability arrays
  print(penney_prob_arr_wins)
  print(penney_prob_arr_losses)
  
  if __name__ == "__main__":
    create_heatmap()
