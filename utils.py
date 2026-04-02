import logging
import json
import os
from typing import Any, Optional, Dict
from pathlib import Path

def load_config(file_path: str) -> Dict[str, Any]:
    """Load configuration from JSON file with error handling."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        logging.error(f"Config file not found: {file_path}")
        raise
    except json.JSONDecodeError as e:
        logging.error(f"Invalid JSON in config file: {file_path} - {str(e)}")
        raise
    except Exception as e:
        logging.error(f"Error loading config file: {file_path} - {str(e)}")
        raise

def get_env_var(var_name: str, default: Optional[str] = None) -> Optional[str]:
    """Get environment variable with optional default value."""
    value = os.environ.get(var_name, default)
    if value is None:
        logging.warning(f"Environment variable {var_name} not set and no default provided")
    return value

def setup_logging(log_level: str, log_file: Optional[str] = None) -> None:
    """Configure logging with optional file output."""
    log_format = '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
    date_format = '%Y-%m-%d %H:%M:%S'
    
    # Clear any existing handlers
    logging.getLogger().handlers.clear()
    
    # Set up basic config
    logging.basicConfig(
        level=log_level,
        format=log_format,
        datefmt=date_format
    )
    
    # Add file handler if specified
    if log_file:
        try:
            Path(log_file).parent.mkdir(parents=True, exist_ok=True)
            file_handler = logging.FileHandler(log_file, encoding='utf-8')
            file_handler.setLevel(log_level)
            file_handler.setFormatter(logging.Formatter(log_format, datefmt=date_format))
            logging.getLogger().addHandler(file_handler)
        except Exception as e:
            logging.error(f"Failed to setup file logging: {str(e)}")
            raise