#!/usr/bin/env python3
#
# Referenced: https://github.com/Azure-Samples/azure-samples-python-management/blob/main/samples/network/virtual_network/manage_virtual_network_peering.py 
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
LOCATION = 'eastus'
network_client = azure.mgmt.network.NetworkManagementClient(
    credential=credential, subscription_id=subscription_id)


def create_vnet(network_client):
    vnet_params = {
        'location': LOCATION,
        'address_space': {
            'address_prefixes': ['10.0.0.0/16']
        }
    }
    creation_result = network_client.virtual_networks.create_or_update(
        GROUP_NAME,
        'EAST-US_VNet_1',
        vnet_params
    )
    return creation_result.result()


creation_result = create_vnet(network_client)
print("------------------------------------------------------")
print(creation_result)
input('Press enter to continue...')


def create_subnet(network_client):
    subnet_params = {
        'address_prefix': '10.0.1.0/24'
    }
    creation_result = network_client.subnets.create_or_update(
        GROUP_NAME,
        'EAST-US_VNet_1',
        'EAST-US_VNet_1_Subnet_1',
        subnet_params
    )

    return creation_result.result()


creation_result = create_subnet(network_client)
print("------------------------------------------------------")
print(creation_result)
input('Press enter to continue...')


