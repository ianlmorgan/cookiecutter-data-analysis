# create_int_data.py
import logging
from load_data import load_raw_filenames

def create_int_data(raw_filenames):
    """
    Takes raw data, converts and saves it.

    Args:
        raw_filenames: Raw data filenames
    """
    logger = logging.getLogger(__name__)
    # Create intermediate data
    logger.info('Creating intermediate data from raw data.')
    # Save intermediate data
    logger.info('Saving intermediate data.')

if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)
    # load raw data filenames
    raw_filenames = load_raw_filenames()
    # create and save intermediate data
    create_int_data(raw_filenames)