from pathlib import Path

CONFIG_FILE_PATH = Path("config/config.yaml")
PARAMS_FILE_PATH = Path("params.yaml")

print("CONFIG_FILE_PATH exists:", CONFIG_FILE_PATH.exists())
print("PARAMS_FILE_PATH exists:", PARAMS_FILE_PATH.exists())
