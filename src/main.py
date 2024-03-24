"""
@author: sta
"""
import requests

from utils.configuration import Configuration
from utils.logger import logger




# Configuration
POWERBI_CLIENT_ID = Configuration.POWERBI_CLIENT_ID
POWERBI_CLIENT_SECRET = Configuration.POWERBI_CLIENT_SECRET
POWERBI_TENANT_ID = Configuration.POWERBI_TENANT_ID
POWERBI_GROUP_ID = Configuration.POWERBI_GROUP_ID
POWERBI_DATASET_ID = Configuration.POWERBI_DATASET_ID

# URL pour obtenir le token
token_url = f'https://login.microsoftonline.com/{POWERBI_TENANT_ID}/oauth2/v2.0/token'

# Paramètres pour obtenir le token
token_data = {
    'grant_type': 'client_credentials',
    'client_id': POWERBI_CLIENT_ID,
    'client_secret': POWERBI_CLIENT_SECRET,
    'scope': 'https://graph.microsoft.com/.default'
}

# Obtenir le token
token_r = requests.post(token_url, data=token_data, timeout=30)
print(token_r)
token = token_r.json().get("access_token")
print(token)
# URL pour le rafraîchissement du dataset
refresh_url = f'https://api.powerbi.com/v1.0/myorg/groups/{POWERBI_GROUP_ID}/datasets/{POWERBI_DATASET_ID}/refreshes'

# En-têtes pour la requête de rafraîchissement
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

# Envoyer la requête de rafraîchissement
refresh_r = requests.post(refresh_url, headers=headers, timeout=30)

if refresh_r.status_code == 202:
    print("Le rafraîchissement du dataset a été initié avec succès.")
else:
    print("Erreur lors de la tentative de rafraîchissement du dataset:", refresh_r)
