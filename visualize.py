import numpy as np
import matplotlib.pyplot as plt
from processing_utils import normalize, load


def visualize_single_tiff(tif_path):
  norm_band = normalize(load(tif_path))
  plt.imshow(norm_band, cmap='gray')
  plt.axis('off')
  plt.show()


def visualize_rgb_tiff(red, green, blue):
  rgb = np.dstack([normalize(load(red)), normalize(load(green)), normalize(load(blue))])
  plt.imshow(rgb)
  plt.axis("off")
  plt.show()


# Visualize a NumPy array
def visualize_np(arr, cmap, title):
  plt.imshow(arr, cmap=cmap)
  plt.title(title)
  plt.axis("off")
  plt.show()