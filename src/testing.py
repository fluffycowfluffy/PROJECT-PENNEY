import matplotlib.pyplot as plt
import numpy as np
import os

def fig_tester():
  viz_directory = os.path.join(os.getcwd(), "visualizations")
  os.makedirs(viz_directory, exist_ok = True)
  
  x = np.array([1,2,3,4])
  y = np.array([5,6,7,8])
  
  plt.subplot(1, 2, 1)
  plt.plot(x, y)
  
  x = np.array([0,1,2,3])
  y = np.array([10,20,30,40])
  
  plt.subplot(1, 2, 2)
  plt.plot(x, y)
  
  testfig_path = os.path.join(viz_directory, "test.png")
  plt.savefig(testfig_path, dpi=400)

  return None
