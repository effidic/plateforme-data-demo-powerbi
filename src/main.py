"""
@author: sta
"""

import requests
from msal import ConfidentialClientApplication

from utils.configuration import Configuration
from utils.logger import logger


# Configuration
POWERBI_CLIENT_ID = Configuration.POWERBI_CLIENT_ID
POWERBI_CLIENT_SECRET = Configuration.POWERBI_CLIENT_SECRET
POWERBI_TENANT_ID = Configuration.POWERBI_TENANT_ID
POWERBI_GROUP_ID = Configuration.POWERBI_GROUP_ID
POWERBI_DATASET_ID = Configuration.POWERBI_DATASET_ID
authority_url = f"https://login.microsoftonline.com/{POWERBI_TENANT_ID}"
scope = ["https://analysis.windows.net/powerbi/api/.default"]

# Création de l'instance de l'application
app = ConfidentialClientApplication(
    client_id=POWERBI_CLIENT_ID,
    authority=authority_url,
    client_credential=POWERBI_CLIENT_SECRET,
)
token_response = app.acquire_token_for_client(scopes=scope)
access_token = token_response.get("access_token", "")

# URL pour obtenir le token
token_url = f"https://login.microsoftonline.com/{POWERBI_TENANT_ID}/oauth2/v2.0/token"

# Paramètres pour obtenir le token
token_data = {
    "grant_type": "client_credentials",
    "client_id": POWERBI_CLIENT_ID,
    "client_secret": POWERBI_CLIENT_SECRET,
    "scope": "https://graph.microsoft.com/.default",
}


# URL pour le rafraîchissement du dataset
refresh_url = f"https://api.powerbi.com/v1.0/myorg/groups/{POWERBI_GROUP_ID}/datasets/{POWERBI_DATASET_ID}/refreshes"
# En-têtes pour la requête de rafraîchissement
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json",
}

# Envoyer la requête de rafraîchissement
refresh_r = requests.post(refresh_url, headers=headers, timeout=30)

if refresh_r.status_code == 202:
    logger.info("Le rafraîchissement du dataset a été initié avec succès.")
else:
    logger.error("Erreur rafraîchissement du dataset: %s", refresh_r)
