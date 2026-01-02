import rasterio
import numpy as np
import matplotlib.pyplot as plt

# Normalize band values for displaying as RGB image, removing extreme values to avoid distorting content.
def normalize(band):
  low, high = np.percentile(band, (2, 98))
  return np.clip((band - low) / (high - low), 0, 1)

# Read single band and returns as floating-point NumPy array.
def load(band):
  with rasterio.open(band) as b:
    return b.read(1).astype(float)


def visiualize_single_tiff(tif_path):
  norm_band = normalize(load(tif_path))
  plt.imshow(norm_band, cmap='gray')
  plt.axis('off')
  plt.show()


def visualize_rgb_tiff(red, green, blue):
  rgb = np.dstack([normalize(load(red)), normalize(load(green)), normalize(load(blue))])
  plt.imshow(rgb)
  plt.axis("off")
  plt.show()


if __name__ == '__main__':
  blue = f"test-data\\Sentinel-2_L1C_B02.tiff"
  green = f"test-data\\Sentinel-2_L1C_B03.tiff"
  red = f"test-data\\Sentinel-2_L1C_B04.tiff"

  visiualize_single_tiff(blue)
  visualize_rgb_tiff(red, green, blue)
