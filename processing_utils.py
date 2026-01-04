import rasterio
import numpy as np

# Normalize band values for displaying as RGB image, removing extreme values to avoid distorting content.
def normalize(band):
  low, high = np.percentile(band, (2, 98))
  return np.clip((band - low) / (high - low), 0, 1)

# Read single band and returns as floating-point NumPy array.
def load(band):
  with rasterio.open(band) as b:
    return b.read(1).astype(float)
