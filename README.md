# Project Penney
### Greta Lin Risgin
### Automation & Workflows
### Spring 2025

**NOTE:** I have included an initial 100,000 decks within the `deck_storage` folder. However, they are currently compressed. Please unzip this file.
**ANOTHER NOTE:** I have to confess I have not been using uv, I just run this out of my own virtual environment. I don't know if that's wrong, but it runs so a win is a win.

---

Files included from Professor Smith's Original GitHub:

`src/`

- datagen.py: Code related to data generation and storage should go here.

- helpers.py: Helper functions and variables needed across various other modules should go here.

- processing.py: Code related to scoring the games should go here.

- visualization.py: Code related to creating figures should go here. [Not currently included]

The `pp_greta.py` file will generate your heatmaps and runs for ~10 minutes to go through 1 million decks. It includes the following functions:
- `get_decks()`
  - The inital code from Professor Smith's original GitHub. This function will generate n decks; I have it generating 100,000 decks for each `.npy` file. 
- `decks_to_npy()`
  - This function will save your generated decks to  `.npy` files. It will generate a new random seed for each round of decks and save the file to the `deck_storage` folder. Each deck file will be named accordingly with its corresponding random seed.
  - **NOTE:** I believe there is a 1% chance that the same random seed will be generated twice. Reminder to come back and troubleshoot for potential naming errors from this.
- `penneys_game()`
  - This does all the calculations for Penney's Game. Data for wins, losses, and draws are all collected by this function, however, I only use wins and losses to create my heatmaps. It will loop through all the generated deck files in the `deck_Storage` folder, so the more files you've saved to your storage folder the slower it will be.
- `create_heatmap()`
  - This function is what will be called in the main function. It creates two heatmaps for wins AND losses probabilities, therefore draw probability can be inferred. Heatmaps are created using `seaborn`. 
  - **NOTE:** Reminder to comeback and edit the code so that it generates one output with both heatmaps side by side instead of two separate heatmap files.

yay enjoy the heatmaps :)
---
