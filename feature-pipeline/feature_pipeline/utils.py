import json
import logging
from pathlib import Path


from feature_pipeline import settings


def get_logger(name: str) -> logging.Logger:
    """
    Template for getting a logger.

    Args:
        name (str): Name of the logger.

    Returns:
        Logger.
    """

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(name)

    return logger

def save_json(data: dict, file_name: str, save_dir: str = settings.OUTPUT_DIR) -> None:
    """
    Save a dictionary as a JSON file.
    
    Args:
        data (dict): data to save.
        file_name (str): Name of the JSON file.
        save_dir (str, optional): Directory to save the JSON file. Defaults to settings.OUTPUT_DIR.

    Returns:
        None
    """

    data_path = Path(save_dir) / file_name
    with open(data_path, 'w') as f:
        json.dump(data, f)

def load_json(file_name: str, save_dir: str = settings.OUTPUT_DIR) -> dict:
    """
    Load a JSON file.

    Args:
        file_name (str): Name of the JSON file.
        save_dir (str, optional): Directory of the JSON file. 
                                Defaults to settings.OUTPUT_DIR.

    Returns:
        dict: Dictionary with the data.
    """

    data_path = Path(save_dir) / file_name
    if not data_path.exists():
        raise FileNotFoundError(f"Cached JSON from {data_path} does not exist.")
    
    with open(data_path, 'r') as f:
        return json.load(f)