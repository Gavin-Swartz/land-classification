from matplotlib.colors import ListedColormap
from config.read_config import read_config_file
import identify
from visualize import visualize_np, visualize_rgb_tiff
from data import get_data, make_bbox

if __name__ == '__main__':
  # Get client credentials.
  creds_config = read_config_file('./config/credentials.yaml')
  client_id = creds_config['client_id']
  client_secret = creds_config['client_secret']

  # Create bounding box from specified central point, get Sentinel-2 data.
  bbox = make_bbox(-95.89, 41.31)
  raster, profile = get_data(bbox, client_id, client_secret)

  # TEMPORARY
  ultra_blue = raster[0]
  blue = raster[1]
  green = raster[2]
  red = raster[3]
  nir = raster[4]
  swir1 = raster[8]
  swir2 = raster[9]
  swir3 = raster[11]

  # Visualize data as RGB images.
  visualize_rgb_tiff(red, green, blue)

  # Identify water and plot water mask.
  water = identify.identify_water(green, nir, swir1, swir2)
  cmap = ListedColormap(["white", "blue"])
  visualize_np(water, cmap, "Water")

  snow = identify.identify_snow(green, swir3, water)
  cmap = ListedColormap(["black", "white"])
  visualize_np(snow, cmap, "Snow Cover")

  # Calculate NDVI for GeoTIFF and plot.
  ndvi = identify.calculate_ndvi(nir, red)
  visualize_np(ndvi, "RdYlGn", "Normalized Difference Vegetation Index")
