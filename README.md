# Project Penney
### Greta Lin Risgin
### Automation & Workflows
### Spring 2025
---
Project Penney generates 100,000 decks per file and calculates the win/loss probability for player 1 versus player 2 based on all combinations of card sequences. This data is used to create two heatmaps: a win probability heatmap and a loss probability heatmap. The code runs for ~10 minutes for 1 million decks on my local device. However, I have noticed longer runtimes after being cloned to other devices. I would like to be able to optimize my code to run much faster for this large number of decks. Every 100,000 deck NumPy file is ~ 40 MB. An initial 100,000 decks with random seed 42 have been uploaded to the `deck_storage` folder. I think some areas to target could reducing use of for loops, as well as perhaps finding a more optimal way to store these large amounts of data.
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
  - The main function calls `import_libs` and `create_heatmap` and runs for ~10 minutes. Heatmaps will be stored in the `visualizations` folder created by the same function.
- `setup.py`
  - `import_libs`: Automates the importation of required libraries via subprocess
- `helpers.py`
  - This is the original debugger factory code from Professor Smith 
- `processors.py`
  - `get_decks`: The initial code from Professor Smith's original GitHub. This function will generate n decks; it will generate 100,000 decks for each `.npy` file, which are created and saved in the next function. 
  - `decks_to_npy`: This function will save your generated decks to  `.npy` files. It will generate a new random seed for each round of decks and save the file to the `deck_storage` folder. Each deck file will be named accordingly with its corresponding random seed.
  - **NOTE:** I believe there is a 1% chance that the same random seed will be generated twice. Reminder to come back and troubleshoot for potential naming errors from this.
- `processing.py`
  - `penneys_game`: This does all the calculations for Penney's Game. Data for wins, losses, and draws are all collected by this function, however, I only use wins and losses to create my heatmaps. It will loop through all the generated deck files in the `deck_Storage` folder, so the more files you've saved to your storage folder the slower it will be.
- `visualizations.py`
  - `create_heatmap`: This function is what will be called in the main function. It creates two heatmaps for wins AND losses probabilities, therefore draw probability can be inferred. Heatmaps are created using `seaborn`. 
  - **NOTE:** Reminder to come back and edit the code so that it generates one output with both heatmaps side by side instead of two separate heatmap files.
- All Python files besides `main.py` are stored in the `src` folder. 
- The `visualization examples` folder has examples of how your heatmaps should come out after a 1 million deck run. The cmaps can be changed in for different aesthetic choices, currently, they are set to reds corresponding with wins, and blues corresponding with losses.
- `requirements.txt` and `pyproject.toml` both contain information for the required Python libraries for this project

**Current targeted areas of improvement:** 
1. Fixing possible bugs with `.npy` file naming, and standardize random seeds generated so every cloned git starts with the same seeds.
2. Make it easy for users can add more decks of any amount they want
3. Speed up the code.
4. Add code for win/loss probablity based on overall card count, not just tricks.
5. Make sure heatmap includes the sample size; remove color bar
---
