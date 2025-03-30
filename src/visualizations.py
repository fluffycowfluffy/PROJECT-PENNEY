import os
import numpy as np
import seaborn as sns
import subprocess as sp
import matplotlib.pyplot as plt

#from src.datagen import decks_to_npy
from src.processing import total_deck_count, data_storage
from src.helpers import PATH_DATA

def create_tricks_heatmap(win_loss_tuple: tuple) -> None:
  # create folder and define directory for generated visualizations
  viz_directory = os.path.join(os.getcwd(), "visualizations")
  os.makedirs(viz_directory, exist_ok = True)

  # access data
  sequences = ['000','001','010','011','100','101','110', '111']

  ### create plt figure (tricks)
  plt.figure(figsize = (14, 7))
  plt.suptitle(f"Penney's Game Win/Loss Percentages by Tricks (N = {total_deck_count()})", fontsize = 16)
  offset = 0.5
  
  # create wins heatmap :)
  # set to first position in joint visualization
  plt.subplot(1, 2, 1)
  ax1 = sns.heatmap(win_loss_tuple[0],
                    annot = True, 
                    cmap = "Reds",
                    fmt = ".1%",
                    cbar = False)
  plt.xticks(ticks = np.arange(len(sequences)) + offset, labels = ['RRR','RRB','RBR','RBB','BRR','BRB','BBR', 'BBB'])
  plt.yticks(ticks = np.arange(len(sequences)) + offset, labels = ['RRR','RRB','RBR','RBB','BRR','BRB','BBR', 'BBB'])
  plt.tick_params(axis = "x", which = "both", length = 0)
  plt.tick_params(axis = "y", which = "both", length = 0)
  plt.title("Probabilities of P1 Winning Against P2", fontsize = 12)
  plt.ylabel("P1 Sequences", fontsize = 12)
  plt.xlabel("P2 Sequences", fontsize = 12)
  ax1.set_aspect("equal")
  
  # create losses heatmap
  # set to second position in joint visualization
  plt.subplot(1, 2, 2)
  ax2 = sns.heatmap(win_loss_tuple[1],
                    annot = True, 
                    cmap = "Blues",
                    fmt = ".1%",
                    cbar = False)
  plt.xticks(ticks = np.arange(len(sequences)) + offset, labels = ['RRR','RRB','RBR','RBB','BRR','BRB','BBR', 'BBB'])
  plt.yticks(ticks = np.arange(len(sequences)) + offset, labels = ['RRR','RRB','RBR','RBB','BRR','BRB','BBR', 'BBB'])
  plt.tick_params(axis = "x", which = "both", length = 0)
  plt.tick_params(axis = "y", which = "both", length = 0)
  plt.title("Probabilities of P1 Losing Against P2", fontsize = 12)
  plt.ylabel("P1 Sequences", fontsize = 12)
  plt.xlabel("P2 Sequences", fontsize = 12)
  ax2.set_aspect("equal")

  # save to visualizations folder
  heatmap_w_l_path = os.path.join(viz_directory, f"PenneyProbabilityHeatmapTricks.png")
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

def create_cards_heatmap(win_loss_tuple: tuple) -> None:
  # create folder and define directory for generated visualizations
  viz_directory = os.path.join(os.getcwd(), "visualizations")
  os.makedirs(viz_directory, exist_ok = True)

  # access data
  sequences = ['000','001','010','011','100','101','110', '111']

  ### create plt figure (cards)
  plt.figure(figsize = (14, 7))
  plt.suptitle(f"Penney's Game Win/Loss Percentages by Cards (N = {total_deck_count()})", fontsize = 16)
  offset = 0.5
  
  # create wins heatmap :)
  # set to first position in joint visualization
  plt.subplot(1, 2, 1)
  ax1 = sns.heatmap(win_loss_tuple[2],
                    annot = True, 
                    cmap = "Reds",
                    fmt = ".1%",
                    cbar = False)
  plt.xticks(ticks = np.arange(len(sequences)) + offset, labels = ['RRR','RRB','RBR','RBB','BRR','BRB','BBR', 'BBB'])
  plt.yticks(ticks = np.arange(len(sequences)) + offset, labels = ['RRR','RRB','RBR','RBB','BRR','BRB','BBR', 'BBB'])
  plt.tick_params(axis = "x", which = "both", length = 0)
  plt.tick_params(axis = "y", which = "both", length = 0)
  plt.title("Probabilities of P1 Winning Against P2", fontsize = 12)
  plt.ylabel("P1 Sequences", fontsize = 12)
  plt.xlabel("P2 Sequences", fontsize = 12)
  ax1.set_aspect("equal")
  
  # create losses heatmap
  # set to second position in joint visualization
  plt.subplot(1, 2, 2)
  ax2 = sns.heatmap(win_loss_tuple[3],
                    annot = True, 
                    cmap = "Blues",
                    fmt = ".1%",
                    cbar = False)
  plt.xticks(ticks = np.arange(len(sequences)) + offset, labels = ['RRR','RRB','RBR','RBB','BRR','BRB','BBR', 'BBB'])
  plt.yticks(ticks = np.arange(len(sequences)) + offset, labels = ['RRR','RRB','RBR','RBB','BRR','BRB','BBR', 'BBB'])
  plt.tick_params(axis = "x", which = "both", length = 0)
  plt.tick_params(axis = "y", which = "both", length = 0)
  plt.title("Probabilities of P1 Losing Against P2", fontsize = 12)
  plt.ylabel("P1 Sequences", fontsize = 12)
  plt.xlabel("P2 Sequences", fontsize = 12)
  ax2.set_aspect("equal")

  # save to visualizations folder
  heatmap_w_l_path = os.path.join(viz_directory, f"PenneyProbabilityHeatmapCards.png")
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
