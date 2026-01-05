import logging
import json
import os

def load_config(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def get_env_var(var_name, default=None):
    return os.environ.get(var_name, default)

def setup_logging(log_level, log_file=None):
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s [%(levelname)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    if log_file:
        handler = logging.FileHandler(log_file)
        handler.setLevel(log_level)
        logging.getLogger().addHandler(handler)