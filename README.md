# land-classification
A project for classifying land cover using multispectral data from Sentinel-2.

## Indexes and Classification Methodology
### Water
AWEI_NSH is used to identify water based on findings from [this](https://doi.org/10.1016/j.rsase.2024.101367) source. AWEI_NSH uses the following bands:
- Green (band 3)
- NIR (band 8)
- SWIR1 (band 11)
- SWIR2 (band 12)

### Snow
[NDSI](https://www.usgs.gov/landsat-missions/normalized-difference-snow-index) is used to identify snow cover. NDSI uses the following bands:
- Green (band 3)
- SWIR3 (band 11)

NDSI values of 0.4 or greater indicate snow cover. However, as explained in [this Earth Lab blog](https://earthlab.colorado.edu/blog/how-differentiate-between-water-and-snow-remote-sensing), NDSI struggles to differentiate between water and snow. The solution is to ignore areas identified using NDSI as snow which intersect with pixels identified as water.  

### Vegetation Health
[NDVI](https://www.earthdata.nasa.gov/topics/land-surface/normalized-difference-vegetation-index-ndvi) is a common and simple vegetation index used to monitor vegetation health. NDVI uses the following bands:
- Red (band 4)
- NIR (band 8)
