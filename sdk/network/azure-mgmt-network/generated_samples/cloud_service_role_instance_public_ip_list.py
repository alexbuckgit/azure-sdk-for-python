# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.network import NetworkManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-network
# USAGE
    python cloud_service_role_instance_public_ip_list.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = NetworkManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="subid",
    )

    response = client.public_ip_addresses.list_cloud_service_role_instance_public_ip_addresses(
        resource_group_name="cs-tester",
        cloud_service_name="cs1",
        role_instance_name="Test_VM_0",
        network_interface_name="nic1",
        ip_configuration_name="ip1",
    )
    for item in response:
        print(item)


# x-ms-original-file: specification/network/resource-manager/Microsoft.Network/stable/2023-05-01/examples/CloudServiceRoleInstancePublicIpList.json
if __name__ == "__main__":
    main()
