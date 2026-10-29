import json
from pathlib import Path

from src.config import Config


def load_config(name=Config.GPT_CONFIG_NAME):
    """Read config/gptconfig_<name>.json."""
    config_path = Path(Config.CONFIG_DIR) / f"gptconfig_{name}.json"
    with config_path.open(encoding="utf-8") as config_file:
        return json.load(config_file)


_CONFIG = load_config()

# Model architecture, and training settings, of the selected config file
GPT_CONFIG = _CONFIG["model"]
TRAIN_CONFIG = _CONFIG["training"]
