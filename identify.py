import numpy as np

def identify_water(green, nir, swir1, swir2):
  # Compute AWEI_NSH
  awei_nsh = 4 * (green - swir1) - (0.25 * nir + 2.75 * swir2)

  # Apply mask where only positive AWEI_NSH are identified as water
  water = awei_nsh > 0
  return water


def calculate_ndvi(nir, red):
  # Compute NDVI
  ndvi = (nir - red) / (nir + red)
  ndvi = np.clip(ndvi, -1, 1)
  return ndvi


def identify_snow(green, swir3, water):
  # Compute NDSI
  ndsi = (green - swir3) / (green + swir3)
  
  # Apply mask where only NDSI > 0.4 is snow cover. Threshold value rationale explained in README
  snow = (ndsi > 0.4) & ~water
  return snow


def identify_buildings():
  pass


def identify_roads():
  pass


def identify_vegetation():
  pass


def identify_bare_soil():
  pass