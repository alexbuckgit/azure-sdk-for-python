# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
from random import randint
from time import time
from wsgiref.handlers import format_date_time

from azure.core.rest import HttpRequest
from azure.core.exceptions import (
    HttpResponseError,
    map_error,
)
from azure.core.paging import ItemPaged
from azure.core.async_paging import AsyncItemPaged

from azure.data.tables.aio import TableClient
from .custom_iterator import CustomIterator, AsyncCustomIterator
from ._test_base import _TableTest

class ListEntitiesPageableTest(_TableTest):
    def __init__(self, arguments):
        super().__init__(arguments)
        self.table_name = f"updateentitytest{randint(1, 1000)}"
        self.connection_string = self.get_from_env("AZURE_STORAGE_CONN_STR")
        self.async_table_client = TableClient.from_connection_string(self.connection_string, self.table_name)
        self.url = f"{self.account_endpoint}{self.table_name}()"

    async def global_setup(self):
        await super().global_setup()
        await self.async_table_client.create_table()
        batch_size = 0
        batch = []
        for row in range(self.args.count):
            entity = self.get_entity(row)
            batch.append(("create", entity))
            batch_size += 1
            if batch_size >= 100:
                await self.async_table_client.submit_transaction(batch)
                batch = []
                batch_size = 0
        if batch_size:
            await self.async_table_client.submit_transaction(batch)

    def _get_list_entities(self, **kwargs):
        current_time = format_date_time(time())
        request = HttpRequest(
            method="GET",
            url=self.url,
            params={},
            headers={
                'x-ms-version': self.api_version,
                'DataServiceVersion': self.data_service_version,
                'Accept': 'application/json;odata=minimalmetadata;',
                'x-ms-date': current_time
            },
        )
        response = self.pipeline_client._pipeline.run(
            request,
        ).http_response
        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=self.error_map)
            raise HttpResponseError(response=response)

        return response

    async def _get_list_entities_async(self, **kwargs):
        current_time = format_date_time(time())
        list_entities_params = {}
        if kwargs.get("top"):
            list_entities_params['$top'] = kwargs.get("top")
        if kwargs.get("next_partition_key"):
            list_entities_params['NextPartitionKey'] = kwargs.get("next_partition_key")
        if kwargs.get("next_row_key"):
            list_entities_params['NextRowKey'] = kwargs.get("next_row_key")
        
        request = HttpRequest(
            method="GET",
            url=self.url,
            params=list_entities_params,
            headers={
                'x-ms-version': self.api_version,
                'DataServiceVersion': self.data_service_version,
                'Accept': 'application/json;odata=minimalmetadata;',
                'x-ms-date': current_time
            },
        )
        response = (await self.async_pipeline_client._pipeline.run(
            request,
        )).http_response
        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=self.error_map)
            raise HttpResponseError(response=response)

        return response

    def run_sync(self):
        for _ in ItemPaged(
            self._get_list_entities,
            page_iterator_class=CustomIterator,
        ):
            pass

    async def run_async(self):
        async for _ in AsyncItemPaged(
            self._get_list_entities_async,
            page_iterator_class=AsyncCustomIterator,
        ):
            pass


    async def global_cleanup(self):
        await self.async_table_client.delete_table()

    async def close(self):
        await self.async_table_client.close()
        await super().close()

    @staticmethod
    def add_arguments(parser):
        super(ListEntitiesPageableTest, ListEntitiesPageableTest).add_arguments(parser)
        #parser.add_argument('--max-results', nargs='?', type=str, help='Max results to return.  Default is None.', default=None)
        parser.add_argument('-c', '--count', nargs='?', type=int, help='Number of blobs to list. Defaults to 100', default=100)

