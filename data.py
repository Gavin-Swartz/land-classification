from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
from config.read_config import read_config_file
from rasterio.io import MemoryFile

# Given a center point, get the optimal bounding box for Sentinel-2.
def make_bbox(lon, lat, km=2):
  d = km / 111          # Convert km to degrees
  return [lon-d, lat-d, lon+d, lat+d]


def get_data(bbox_coords, client_id, client_secret):
  client = BackendApplicationClient(client_id=client_id)
  oauth = OAuth2Session(client=client)

  token = oauth.fetch_token(
    token_url="https://identity.dataspace.copernicus.eu/auth/realms/CDSE/protocol/openid-connect/token",
    client_secret=client_secret,
    include_client_id=True,
  )

  evalscript = """
  //VERSION=3
  function setup() {
    return {
      input: ["B01", "B02", "B03", "B04", "B05", "B06", "B07", "B08", "B8A", "B09", "B10", "B11", "B12"],
      output: {
        bands: 13,
        sampleType: "FLOAT32"
      }
    };
  }

  function evaluatePixel(sample) {
    return [
      sample.B01,
      sample.B02,
      sample.B03,
      sample.B04,
      sample.B05,
      sample.B06,
      sample.B07,
      sample.B08,
      sample.B8A,
      sample.B09,
      sample.B10,
      sample.B11,
      sample.B12,
    ]
  }
  """

  request = {
      "input": {
          "bounds": {
              "properties": {"crs": "http://www.opengis.net/def/crs/OGC/1.3/CRS84"},
              "bbox": bbox_coords,
          },
          "data": [
              {
                  "type": "sentinel-2-l1c",
                  "dataFilter": {
                      "timeRange": {
                          "from": "2024-01-01T00:00:00Z",
                          "to": "2024-01-31T00:00:00Z",
                      }, 
                      "maxCloudCoverage": 10
                  },
              }
          ],
      },
      "output": {
          "width": 512, 
          "height": 512, 
          "responses": [
              {
                "identifier": "default",
                "format": {
                    "type": "image/tiff"
                }   
              }
      ]},
      "evalscript": evalscript,
  }

  url = "https://sh.dataspace.copernicus.eu/api/v1/process"
  response = oauth.post(url, json=request)

  # Check if response is valid.
  if response.headers["Content-Type"] != "image/tiff":
    print(response.text)
    raise RuntimeError("No valid Sentinel-2 data for this request.")

  # Convert bytes to NumPy array.
  with MemoryFile(response.content) as memfile:
    with memfile.open() as dataset:
      raster = dataset.read()      # shape: (bands, height, width)
      profile = dataset.profile

  print("Raster shape:", raster.shape)
  print("Number of bands:", raster.shape[0])
  print("Raster size:", raster.shape[1], "x", raster.shape[2])
  return raster, profile


def map_bands(raster):
  band_config = read_config_file('./config/band_config.yaml')

  bands = {}
  for band_name, band_meta in band_config.items():
    bands[band_name] = raster[band_meta['index']]

  return bands
