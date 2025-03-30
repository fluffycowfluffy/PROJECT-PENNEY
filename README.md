# Project Penney
### Greta Lin Risgin
### Automation & Workflows
### Spring 2025
---
[Penney's Game](https://en.wikipedia.org/wiki/Penney%27s_game) is a game where two players select a binary sequence. When using a coin this would be heads and tails, while for cards this would be red and black cards. For this project, Project Penney, we will be using a sequence of three and decks of cards encoded in binary. Project Penney calculates the win/loss probability for player 1 versus player 2 based on all combinations of card sequences. This data is used to create four heatmaps: a win probability heatmap and a loss probability heatmap for both games by tricks (number of sequences) and games by total card count. The code runs for ~10 minutes for 1 million decks on my local device. However, I have noticed longer runtimes after being cloned to other devices. A sample size of 1,000,000 decks with random seeds 0, 1, 2, 3, and 4 have been provided within the `deck_storage` folder.
---
Quick Start
---
Run the following in command line in order to clone this repository.
```
git clone https://github.com/fluffycowfluffy/PROJECT-PENNEY
```
Then run the main function
```
python main.py
```
More About Project Penney
---
Project Penney includes the following Python files:
- `main.py`
  - The main function calls `import_libs`, `create_tricks_heatmap`, and `create_cards_heatmap`. It runs for ~10 minutes. Heatmaps will be stored in the `visualizations` folder created by the same function.
- `setup.py`
  - `import_libs`: Automates the importation of required libraries via subprocess
- `helpers.py`
  - This is the original debugger factory code from Professor Smith 
- `datagen.py`
  - `get_decks`: The initial code from Professor Smith's original GitHub. This function will generate n decks; it will generate 100,000 decks for each `.npy` file, which are created and saved in the next function. 
  - `decks_to_npy`: This function will prompt the user to add more decks and add these to  `.npy` files. It will generate a new  seed for new decks based on previously used seeds and save the file to the `deck_storage` folder. Each deck file will be named accordingly with its corresponding random seed.
- `processing.py`
  - `total_deck_count`: This function merely counts the number of decks currently in the `deck_storage` folder for later calculations.
  - `penneys_game`: This does all the calculations for Penney's Game. Data for wins, losses, and draws are all collected by this function, however, I only use wins and losses to create my heatmaps. It will loop through all the generated deck files in the `deck_Storage` folder, so the more files you've saved to your storage folder the slower it will be.
  - `data_storage`: This function generates the NumPy arrays that will be used for heatmap generation. This stores the win/loss data for the games in four arrays (trick-win, trick-loss, card-win, card-loss) stored in a tuple. This tuple is accessed in the visualization portion of the code.
- `visualizations.py`
  - `create_tricks_heatmap`: This function is what will be called in the main function. It creates two heatmaps for wins AND losses probabilities for games by tricks, therefore draw probability can be inferred. Heatmaps are created using `seaborn`.
  - `create_cards_heatmap`
     - Identical to the above function, except now this is based on games by card count.
- All Python files besides `main.py` are stored in the `src` folder. 
- The `visualization examples` folder has examples of how your heatmaps should come out after a 1 million deck run. The cmaps can be changed in for different aesthetic choices, currently, they are set to reds corresponding with wins, and blues corresponding with losses.
- `requirements.txt` and `pyproject.toml` both contain information for the required Python libraries for this project
---
