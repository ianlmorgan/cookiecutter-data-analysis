# load_data.py
import logging
from pathlib import Path

# path for the project directory
project_dir = Path(__file__).resolve().parents[2]
# path for the data directory
data_dir = project_dir / 'data'

def load_raw_filenames():
    """
    Function for finding raw data filenames.
    
    Returns:
        generator: path to files in the raw data directory. 
    """
    logger = logging.getLogger(__name__)
    logger.info('Finding raw data files.')
    raw_data_dir = data_dir / 'raw'
    return raw_data_dir.iterdir()

def load_int_filenames():
    """
    Function for finding intermediate data filenames.

    Returns:
            generator: path to files in the intermediate data directory. 
    """
    logger = logging.getLogger(__name__)
    logger.info('Finding intermediate data files.')
    int_data_dir = data_dir / 'intermediate'
    return int_data_dir.iterdir()

def load_pro_filenames():
    """
    Function for finding processed data filenames.

    Returns:
            generator: path to files in the intermediate data directory. 
    """
    logger = logging.getLogger(__name__)
    logger.info('Finding intermediate data files.')
    pro_data_dir = data_dir / 'processed'
    return pro_data_dir.iterdir()
