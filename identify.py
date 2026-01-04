import numpy as np
from processing_utils import load


def identify_water(band3, band8, band11, band12):
  # Load bands
  green = load(band3)
  nir = load(band8)
  swir1 = load(band11)
  swir2 = load(band12)

  # Compute AWEI_NSH
  awei_nsh = 4 * (green - swir1) - (0.25 * nir + 2.75 * swir2)

  # Apply mask where only positive AWEI_NSH are identified as water
  water = awei_nsh > 0
  return water


def calculate_ndvi(band8, band4):
  # Load bands
  nir = load(band8)
  red = load(band4)

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