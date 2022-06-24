""" This script makes the datasets.
"""
import logging

log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=log_fmt)
logger = logging.getLogger(__name__)
# %%
# Make intermediate data
logger.info("Making intermediate data.")
# %%
# Make processed data
logger.info("Making processed data.")
# %%
# Indicate that it completed
logger.info("Done. I can't beleive that actually worked!")
