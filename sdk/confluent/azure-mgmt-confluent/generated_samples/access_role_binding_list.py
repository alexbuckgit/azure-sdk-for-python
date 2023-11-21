# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.confluent import ConfluentManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-confluent
# USAGE
    python access_role_binding_list.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = ConfluentManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="00000000-0000-0000-0000-000000000000",
    )

    response = client.access.list_role_bindings(
        resource_group_name="myResourceGroup",
        organization_name="myOrganization",
        body={"searchFilters": {"pageSize": "10", "pageToken": "asc4fts4ft"}},
    )
    print(response)


# x-ms-original-file: specification/confluent/resource-manager/Microsoft.Confluent/stable/2023-08-22/examples/Access_RoleBindingList.json
if __name__ == "__main__":
    main()
