from matplotlib.colors import ListedColormap
import identify
from visualize import visualize_np

if __name__ == '__main__':
  # TEMPORARY
  blue = f"test-data\\Sentinel-2_L1C_B02.tiff"
  green = f"test-data\\Sentinel-2_L1C_B03.tiff"
  red = f"test-data\\Sentinel-2_L1C_B04.tiff"
  nir = f"test-data\\Sentinel-2_L1C_B08.tiff"
  swir1 = f"test-data\\Sentinel-2_L1C_B11.tiff"
  swir2 = f"test-data\\Sentinel-2_L1C_B12.tiff"

  water = identify.identify_water(green, nir, swir1, swir2)
  cmap = ListedColormap(["white", "blue"])
  visualize_np(water, cmap, "Water")

  ndvi = identify.calculate_ndvi(nir, red)
  visualize_np(ndvi, "RdYlGn", "Normalized Difference Vegetation Index")
