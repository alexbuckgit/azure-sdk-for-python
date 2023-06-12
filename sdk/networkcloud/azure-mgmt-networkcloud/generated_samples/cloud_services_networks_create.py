# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.networkcloud import NetworkCloudMgmtClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-networkcloud
# USAGE
    python cloud_services_networks_create.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = NetworkCloudMgmtClient(
        credential=DefaultAzureCredential(),
        subscription_id="subscriptionId",
    )

    response = client.cloud_services_networks.begin_create_or_update(
        resource_group_name="resourceGroupName",
        cloud_services_network_name="cloudServicesNetworkName",
        cloud_services_network_parameters={
            "extendedLocation": {
                "name": "/subscriptions/subscriptionId/resourceGroups/resourceGroupName/providers/Microsoft.ExtendedLocation/customLocations/clusterExtendedLocationName",
                "type": "CustomLocation",
            },
            "location": "location",
            "properties": {
                "additionalEgressEndpoints": [
                    {
                        "category": "azure-resource-management",
                        "endpoints": [{"domainName": "https://storageaccountex.blob.core.windows.net", "port": 443}],
                    }
                ],
                "enableDefaultEgressEndpoints": "False",
            },
            "tags": {"key1": "myvalue1", "key2": "myvalue2"},
        },
    ).result()
    print(response)


# x-ms-original-file: specification/networkcloud/resource-manager/Microsoft.NetworkCloud/preview/2022-12-12-preview/examples/CloudServicesNetworks_Create.json
if __name__ == "__main__":
    main()
