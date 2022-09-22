#!/usr/bin/env python3
# Reference example: https://github.com/Azure-Samples/azure-samples-python-management/blob/main/samples/network/virtual_network/manage_subnet.py
# 
import os
from azure.identity import ClientSecretCredential
import azure.mgmt.network
from azure.identity import DefaultAzureCredential
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.resource import ResourceManagementClient

credential = ClientSecretCredential(
    tenant_id=os.environ.get("AZURE_TENANT_ID"),
    client_id=os.environ.get("AZURE_CLIENT_ID"),
    client_secret=os.environ.get("AZURE_CLIENT_SECRET")
)
subscription_id = os.environ.get("SUBSCRIPTION_ID")
GROUP_NAME = "Mastering-Python-Networking"
VIRTUAL_NETWORK_NAME = "WEST-US-2_VNet_1"
SUBNET = "WEST-US-2_VNet_1_Subnet_2"
network_client = azure.mgmt.network.NetworkManagementClient(
    credential=credential, subscription_id=subscription_id)

# Get subnet
subnet = network_client.subnets.get(
    GROUP_NAME,
    VIRTUAL_NETWORK_NAME,
    SUBNET
)
print("Get subnet:\n{}".format(subnet))

subnet = network_client.subnets.begin_create_or_update(
    GROUP_NAME,
    VIRTUAL_NETWORK_NAME,
    SUBNET,
    {
        "address_prefix": "192.168.0.128/25"
    }
).result()
print("Create subnet:\n{}".format(subnet))
