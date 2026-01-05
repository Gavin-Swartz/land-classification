import numpy as np
from processing_utils import load


def identify_water(green, nir, swir1, swir2):
  # Compute AWEI_NSH
  awei_nsh = 4 * (green - swir1) - (0.25 * nir + 2.75 * swir2)

  # Apply mask where only positive AWEI_NSH are identified as water
  water = awei_nsh > 0
  return water


def calculate_ndvi(nir, red):
  # Compute NDVIs
  ndvi = (nir - red) / (nir + red)
  ndvi = np.clip(ndvi, -1, 1)
  return ndvi


def identify_snow():
  pass


def identify_buildings():
  pass


def identify_roads():
  pass


def identify_vegetation():
  pass


def identify_bare_soil():
  pass