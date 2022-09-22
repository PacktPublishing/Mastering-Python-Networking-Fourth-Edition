#!/usr/bin/env python3
import os 
import azure.mgmt.network
from azure.identity import ClientSecretCredential

credential = ClientSecretCredential(
    tenant_id=os.environ.get("AZURE_TENANT_ID"),
    client_id=os.environ.get("AZURE_CLIENT_ID"),
    client_secret=os.environ.get("AZURE_CLIENT_SECRET")
)
subscription_id = os.environ.get("SUBSCRIPTION_ID")
network_client = azure.mgmt.network.NetworkManagementClient(credential=credential, subscription_id=subscription_id)
print("Network Management Client API Version: " + network_client.DEFAULT_API_VERSION)
