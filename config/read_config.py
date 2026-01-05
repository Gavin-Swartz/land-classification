import yaml

def read_config_file(path):
  with open(path) as file:
    try:
      return yaml.safe_load(file)
    except yaml.YAMLError as e:
      print(e.with_traceback())
    