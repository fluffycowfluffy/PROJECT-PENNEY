import os
import numpy as np
import seaborn as sns
from tqdm import tqdm
import matplotlib.pyplot as plt
from concurrent.futures import ThreadPoolExecutor  # Parallelization

from src.datagen import decks_to_npy
from src.processing import penneys_game
from src.helpers import PATH_DATA

def calculate_probabilities(i, j, sequences, penney_prob_arr_wins, penney_prob_arr_losses):
    """
    Function to calculate and store the win/loss probability for a given i, j combination.
    """
    P1 = list(map(int, sequences[i]))
    P2 = list(map(int, sequences[j]))
    win_rate = penneys_game(P1, P2)
    penney_prob_arr_wins[i, j] = win_rate[0]
    penney_prob_arr_losses[i, j] = win_rate[1]

def fig_tester():
    """
    Generate a heatmap from the probabilities 
    found in the penneys_game() function
    """
    for i in range(8):
        decks_to_npy()

    sequences = ['000', '001', '010', '011', '100', '101', '110', '111']
    n = len(sequences)

    # create empty array
    penney_prob_arr_wins = np.zeros((n, n))
    penney_prob_arr_losses = np.zeros((n, n))

    print("Calculating probabilities...generating heatmaps...")

    # Use ThreadPoolExecutor for parallelization
    with ThreadPoolExecutor() as executor:
        # Use a nested loop but submit each combination to be processed in parallel
        futures = [
            executor.submit(calculate_probabilities, i, j, sequences, penney_prob_arr_wins, penney_prob_arr_losses)
            for i in range(n) for j in range(n)
        ]
        # Wait for all futures to complete
        for future in tqdm(futures, desc="Processing", total=len(futures)):
            future.result()  # This will block until the task is complete

    # set the diagonal to NaNs for masking purposes
    np.fill_diagonal(penney_prob_arr_wins, np.nan)
    np.fill_diagonal(penney_prob_arr_losses, np.nan)

    # create folder and define directory for generated visualizations
    viz_directory = os.path.join(os.getcwd(), "visualizations")
    os.makedirs(viz_directory, exist_ok=True)

    # Create the figure for the heatmaps
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))  # 1 row, 2 columns

    # Create wins heatmap :)
    sns.heatmap(penney_prob_arr_wins, annot=True, cmap="Reds", ax=ax1)
    ax1.set_xticklabels(sequences)
    ax1.set_yticklabels(sequences)
    ax1.set_title("Probabilities of P1 Winning Against P2", fontsize=16)
    ax1.set_ylabel("P1 Sequences", fontsize=12)
    ax1.set_xlabel("P2 Sequences", fontsize=12)
    ax1.set_aspect('equal')  # Set the aspect ratio to be equal (square)

    # Create losses heatmap
    sns.heatmap(penney_prob_arr_losses, annot=True, cmap="Greys", ax=ax2)
    ax2.set_xticklabels(sequences)
    ax2.set_yticklabels(sequences)
    ax2.set_title("Probabilities of P1 Losing Against P2", fontsize=16)
    ax2.set_ylabel("P1 Sequences", fontsize=12)
    ax2.set_xlabel("P2 Sequences", fontsize=12)
    ax2.set_aspect('equal')  # Set the aspect ratio to be equal (square)

    # Save to visualizations folder
    heatmap_w_l_path = os.path.join(viz_directory, "PenneyProbabilityHeatmap.png")
    plt.savefig(heatmap_w_l_path, dpi=400)

    # Close the plot after saving
    plt.close()

    print(f"Heatmaps saved to: {heatmap_w_l_path}")

    return None
