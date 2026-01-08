from matplotlib.colors import ListedColormap
from config.read_config import read_config_file
import identify
from visualize import visualize_np, visualize_rgb_tiff
from data import get_data, get_data_params, make_bbox, map_bands

if __name__ == '__main__':
  # Get client credentials
  creds_config = read_config_file('./config/credentials.yaml')
  client_id = creds_config['client_id']
  client_secret = creds_config['client_secret']

  # Create bounding box from specified central point, get Sentinel-2 data
  data_params = get_data_params()
  bbox = make_bbox(data_params['lon'], data_params['lat'])
  raster, profile = get_data(bbox, client_id, client_secret, data_params['from_date'], data_params['to_date'])
  bands = map_bands(raster)

  # Visualize data as RGB images
  visualize_rgb_tiff(bands['B04'], bands['B03'], bands['B02'])

  # Identify water and plot water mask
  water = identify.identify_water(bands['B03'], bands['B05'], bands['B8A'], bands['B09'])
  cmap = ListedColormap(["white", "blue"])
  visualize_np(water, cmap, "Water")

  # Identify snow and plot snow mask
  snow = identify.identify_snow(bands['B03'], bands['B11'], water)
  cmap = ListedColormap(["black", "white"])
  visualize_np(snow, cmap, "Snow Cover")

  # Calculate NDVI for GeoTIFF and plot
  ndvi = identify.calculate_ndvi(bands['B05'], bands['B04'])
  visualize_np(ndvi, "RdYlGn", "Normalized Difference Vegetation Index")
