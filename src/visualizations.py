import os
import numpy as np
import seaborn as sns
from tqdm import tqdm
import matplotlib.pyplot as plt

from src.datagen import decks_to_npy
from src.processing import penneys_game
from src.helpers import PATH_DATA

def create_heatmap():
   """
   Generate a heatmap from the probabilities 
   found in the penneys_game() function
   """
   # create visualization folder or check if it already exists
   viz_directory = os.path.join(os.getcwd(), "visualizations")
   os.makedirs(viz_directory, exist_ok = True)

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
   # save the win heatmap to the visualization folder
   heatmap_path_wins = os.path.join(viz_directory, "penneys_prob_heatmap_wins.png")
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
   # save the loss heat to the visualization folder
   heatmap_path_losses = os.path.join(viz_directory, "penneys_prob_heatmap_losses.png")
   plt.savefig(heatmap_path_losses, dpi = 400)

   # show the final probability arrays
   print(penney_prob_arr_wins)
   print(penney_prob_arr_losses)
