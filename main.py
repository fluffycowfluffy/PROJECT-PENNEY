# import automated pip install function from setup first
from src.setup import import_libs

if __name__ == "__main__":
   # automate installations on mac terminal
   import_libs()

   # then import the other necessary functions, which are dependent
   # on the requirements installed with import_libs()
   from src.datagen import decks_to_npy
   from src.visualizations import create_heatmap
   create_heatmap()

   # from src.testing import fig_tester
   # fig_tester()

