import os
import numpy as np
from tqdm import tqdm
import seaborn as sns
import subprocess as sp
import matplotlib.pyplot as plt

from src.datagen import decks_to_npy
from src.processing import penneys_game
from src.helpers import PATH_DATA

def fig_tester():
  """
  Generate a heatmap from the probabilities 
  found in the penneys_game() function
  """
  # as one group 10 100,000 decks has already been provided
  # this has been set to run 9 times in order to result in a final count of 1,000,000 decks
  for i in range(1):
    decks_to_npy()

  sequences = ['000','001','010','011','100','101','110', '111']
  n = len(sequences)

  # create empty array
  penney_prob_arr_wins = np.zeros((n,n))
  penney_prob_arr_losses = np.zeros((n,n))

  print("Calculating probabilities...generating heatmaps...")
  # iterate twice over sequences; create progress bar
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

  # create folder and define directory for generated visualizations
  viz_directory = os.path.join(os.getcwd(), "visualizations")
  os.makedirs(viz_directory, exist_ok = True)

  # create plt figure
  plt.figure(figsize = (14, 7))
  
  # create wins heatmap :)
  # set to first position in joint visualization
  plt.subplot(1, 2, 1)
  sns.heatmap(penney_prob_arr_wins,
              ax = ax1, 
              annot = True, 
              cmap = "Reds")
  plt.xticks(ticks = np.arange(len(sequences)), labels = sequences)
  plt.yticks(ticks = np.arange(len(sequences)), labels = sequences)
  plt.title("Probabilities of P1 Winning Against P2", fontsize = 16)
  plt.ylabel("P1 Sequences", fontsize = 12)
  plt.xlabel("P2 Sequences", fontsize = 12)
  
  # create losses heatmap
  # set to second position in joint visualization
  plt.subplot(1, 2, 2)
  sns.heatmap(penney_prob_arr_losses,
              ax = ax2, 
              annot = True, 
              cmap = "Greys")
  plt.xticks(ticks = np.arange(len(sequences)), labels = sequences)
  plt.yticks(ticks = np.arange(len(sequences)), labels = sequences)
  plt.title("Probabilities of P1 Losing Against P2", fontsize = 16)
  plt.ylabel("P1 Sequences", fontsize = 12)
  plt.xlabel("P2 Sequences", fontsize = 12)

  # save to visualizations folder
  heatmap_w_l_path = os.path.join(viz_directory, "PenneyProbabilityHeatmap.png")
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
