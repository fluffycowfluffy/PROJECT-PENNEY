import os
import numpy as np
from tqdm import tqdm
import seaborn as sns
import subprocess as sp
import matplotlib.pyplot as plt

from src.datagen import decks_to_npy
from src.processing import penneys_game, total_deck_count
from src.helpers import PATH_DATA

def create_heatmap():
  """
  Generate a heatmap from the probabilities 
  found in the penneys_game() function
  """
  # as 1,000,000 decks have already been provided
  # this prompts users to enter more decks if they so choose
  decks_to_npy()

  sequences = ['000','001','010','011','100','101','110', '111']
  n = len(sequences)

  # create empty array
  penney_prob_arr_wins = np.zeros((n,n))
  penney_prob_arr_losses = np.zeros((n,n))

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
      penney_prob_arr_wins[i,j] = win_rate[0]
      penney_prob_arr_losses[i,j] = win_rate[1]

  # set the diagonal to NaNs for masking purposes
  np.fill_diagonal(penney_prob_arr_wins, np.nan)
  np.fill_diagonal(penney_prob_arr_losses, np.nan)

  # create folder and define directory for generated visualizations
  viz_directory = os.path.join(os.getcwd(), "visualizations")
  os.makedirs(viz_directory, exist_ok = True)

  ### create plt figure (tricks)
  plt.figure(figsize = (14, 7))
  plt.suptitle(f"Penney's Game Win/Loss Percentages by Tricks (N = {total_deck_count()})", fontsize = 16)
  
  # create wins heatmap :)
  # set to first position in joint visualization
  plt.subplot(1, 2, 1)
  ax1 = sns.heatmap(penney_prob_arr_wins,
                    annot = True, 
                    cmap = "Reds",
                    fmt = ".1%",
                    cbar = False)
  plt.xticks(ticks = np.arange(len(sequences)), labels = ['RRR','RRB','RBR','RBB','BRR','BRB','BBR', 'BBB'])
  plt.yticks(ticks = np.arange(len(sequences)), labels = ['RRR','RRB','RBR','RBB','BRR','BRB','BBR', 'BBB'])
  plt.title("Probabilities of P1 Winning Against P2", fontsize = 12)
  plt.ylabel("P1 Sequences", fontsize = 12)
  plt.xlabel("P2 Sequences", fontsize = 12)
  ax1.set_aspect("equal")
  
  # create losses heatmap
  # set to second position in joint visualization
  plt.subplot(1, 2, 2)
  ax2 = sns.heatmap(penney_prob_arr_losses,
                    annot = True, 
                    cmap = "Blues",
                    fmt = ".1%",
                    cbar = False)
  plt.xticks(ticks = np.arange(len(sequences)), labels = ['RRR','RRB','RBR','RBB','BRR','BRB','BBR', 'BBB'])
  plt.yticks(ticks = np.arange(len(sequences)), labels = ['RRR','RRB','RBR','RBB','BRR','BRB','BBR', 'BBB'])
  plt.title("Probabilities of P1 Losing Against P2", fontsize = 12)
  plt.ylabel("P1 Sequences", fontsize = 12)
  plt.xlabel("P2 Sequences", fontsize = 12)
  ax2.set_aspect("equal")

  # save to visualizations folder
  _,_,files = next(os.walk(viz_directory))
  viz_increment = len(files)
  print(viz_increment)
  heatmap_w_l_path = os.path.join(viz_directory, f"PenneyProbabilityHeatmapTricks_{viz_increment}.png")
  plt.savefig(heatmap_w_l_path, dpi=400)

  # close the figure window
  plt.close()
  # card illustration directory
  card_directory = os.path.join(os.getcwd(), "cards_ascii")
  card_path = os.path.join(card_directory, f"cards_1.txt")

  # show completion message
  try: 
    sp.run(["cat", card_path])
  except Exception as e:
    pass
  print(f"Heatmaps saved to {heatmap_w_l_path}")

  return None
