from src.setup import import_libs
from src.datagen import decks_to_npy
from src.visualizations import create_heatmap

if __name__ == "__main__":
   import_libs()
   create_heatmap()

