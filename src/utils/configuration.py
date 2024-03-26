"""
@author: sta
"""

import os

from dotenv import load_dotenv, find_dotenv

# Le chargement du dotenv doit ce faire avant la creation de la classe.
load_dotenv(dotenv_path=find_dotenv(), override=True)


class Configuration:
    """
    Get Ringover, and Snowflake connection information
    """

    LOG_FORMAT = os.environ.get("LOG_FORMAT")
    LOG_LEVEL = os.environ.get("LOG_LEVEL")
    POWERBI_CLIENT_ID = os.environ.get("POWERBI_CLIENT_ID")
    POWERBI_CLIENT_SECRET = os.environ.get("POWERBI_CLIENT_SECRET")
    POWERBI_TENANT_ID = os.environ.get("POWERBI_TENANT_ID")
    POWERBI_GROUP_ID = os.environ.get("POWERBI_GROUP_ID")
    POWERBI_DATASET_ID = os.environ.get("POWERBI_DATASET_ID")
    