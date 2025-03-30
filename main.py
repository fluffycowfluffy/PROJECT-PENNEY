# import automated pip install function from setup first
from src.setup import import_libs

if __name__ == "__main__":
   # automate installations on mac terminal
   import_libs()

   # then import the other necessary functions, which are dependent
   # on the requirements installed with import_libs()
   from src.datagen import decks_to_npy
   from src.processing import data_storage
   from src.visualizations import create_tricks_heatmap, create_cards_heatmap

   # run the visualization generators!
   #win_loss_tuple = data_storage()
   #create_tricks_heatmap(win_loss_tuple)
   #create_cards_heatmap(win_loss_tuple)

   decks_to_npy()
