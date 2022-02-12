# create_pro_data.py
import logging
from load_data import load_int_filenames

def create_pro_data(int_filenames):
    """
    Takes intermediate data, processes and saves it.

    Args:
        int_filenames: Intermediate data filenames.
    """
    logger = logging.getLogger(__name__)
    # Create intermediate data
    logger.info('Creating processed data from intermediate data.')
    # Save intermediate data
    logger.info('Saving processed data.')

if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)
    # load intermediate data filenames
    int_filenames = load_int_filenames()
    # create and save processed data
    create_pro_data(int_filenames)