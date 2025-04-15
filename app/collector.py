import requests, os
from dotenv import load_dotenv

load_dotenv()
ABUSE_KEY = os.getenv("ABUSEIPDB_API_KEY")
OTX_KEY = os.getenv("OTX_API_KEY")

def fetch_abuseipdb():
    url = "https://api.abuseipdb.com/api/v2/reports"
    headers = {"Key": ABUSE_KEY, "Accept": "application/json"}
    params = {"maxAgeInDays": "7", "limit": 10}
    response = requests.get(url, headers=headers, params=params)
    return response.json()

def fetch_otx():
    url = "https://otx.alienvault.com/api/v1/pulses/subscribed"
    headers = {
        "X-OTX-API-KEY": OTX_KEY
    }
    response = requests.get(url, headers=headers)
    data = response.json()

    # Extract indicators from pulses
    iocs = []
    for pulse in data.get("results", []):
        for indicator in pulse.get("indicators", []):
            iocs.append(indicator.get("indicator"))
    return iocs

