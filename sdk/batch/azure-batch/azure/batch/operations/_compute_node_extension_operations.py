# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
from typing import Any, Callable, Dict, Iterable, Optional, TypeVar
from urllib.parse import parse_qs, urljoin, urlparse

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict

from .. import models as _models
from .._serialization import Serializer
from .._vendor import _convert_request, _format_url_section

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_get_request(
    pool_id: str,
    node_id: str,
    extension_name: str,
    *,
    select: Optional[str] = None,
    timeout: int = 30,
    client_request_id: Optional[str] = None,
    return_client_request_id: bool = False,
    ocp_date: Optional[datetime.datetime] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2022-01-01.15.0"))  # type: str
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/pools/{poolId}/nodes/{nodeId}/extensions/{extensionName}")
    path_format_arguments = {
        "poolId": _SERIALIZER.url("pool_id", pool_id, "str"),
        "nodeId": _SERIALIZER.url("node_id", node_id, "str"),
        "extensionName": _SERIALIZER.url("extension_name", extension_name, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    if select is not None:
        _params["$select"] = _SERIALIZER.query("select", select, "str")
    if timeout is not None:
        _params["timeout"] = _SERIALIZER.query("timeout", timeout, "int")
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if client_request_id is not None:
        _headers["client-request-id"] = _SERIALIZER.header("client_request_id", client_request_id, "str")
    if return_client_request_id is not None:
        _headers["return-client-request-id"] = _SERIALIZER.header(
            "return_client_request_id", return_client_request_id, "bool"
        )
    if ocp_date is not None:
        _headers["ocp-date"] = _SERIALIZER.header("ocp_date", ocp_date, "rfc-1123")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_list_request(
    pool_id: str,
    node_id: str,
    *,
    select: Optional[str] = None,
    max_results: int = 1000,
    timeout: int = 30,
    client_request_id: Optional[str] = None,
    return_client_request_id: bool = False,
    ocp_date: Optional[datetime.datetime] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2022-01-01.15.0"))  # type: str
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/pools/{poolId}/nodes/{nodeId}/extensions")
    path_format_arguments = {
        "poolId": _SERIALIZER.url("pool_id", pool_id, "str"),
        "nodeId": _SERIALIZER.url("node_id", node_id, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    if select is not None:
        _params["$select"] = _SERIALIZER.query("select", select, "str")
    if max_results is not None:
        _params["maxresults"] = _SERIALIZER.query("max_results", max_results, "int", maximum=1000, minimum=1)
    if timeout is not None:
        _params["timeout"] = _SERIALIZER.query("timeout", timeout, "int")
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if client_request_id is not None:
        _headers["client-request-id"] = _SERIALIZER.header("client_request_id", client_request_id, "str")
    if return_client_request_id is not None:
        _headers["return-client-request-id"] = _SERIALIZER.header(
            "return_client_request_id", return_client_request_id, "bool"
        )
    if ocp_date is not None:
        _headers["ocp-date"] = _SERIALIZER.header("ocp_date", ocp_date, "rfc-1123")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


class ComputeNodeExtensionOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure-batch.BatchServiceClient`'s
        :attr:`compute_node_extension` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def get(
        self,
        pool_id: str,
        node_id: str,
        extension_name: str,
        compute_node_extension_get_options: Optional[_models.ComputeNodeExtensionGetOptions] = None,
        **kwargs: Any
    ) -> _models.NodeVMExtension:
        """Gets information about the specified Compute Node Extension.

        Gets information about the specified Compute Node Extension.

        :param pool_id: The ID of the Pool that contains the Compute Node. Required.
        :type pool_id: str
        :param node_id: The ID of the Compute Node that contains the extensions. Required.
        :type node_id: str
        :param extension_name: The name of the of the Compute Node Extension that you want to get
         information about. Required.
        :type extension_name: str
        :param compute_node_extension_get_options: Parameter group. Default value is None.
        :type compute_node_extension_get_options: ~azure-batch.models.ComputeNodeExtensionGetOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: NodeVMExtension or the result of cls(response)
        :rtype: ~azure-batch.models.NodeVMExtension
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.NodeVMExtension]

        _select = None
        _timeout = None
        _client_request_id = None
        _return_client_request_id = None
        _ocp_date = None
        if compute_node_extension_get_options is not None:
            _client_request_id = compute_node_extension_get_options.client_request_id
            _ocp_date = compute_node_extension_get_options.ocp_date
            _return_client_request_id = compute_node_extension_get_options.return_client_request_id
            _select = compute_node_extension_get_options.select
            _timeout = compute_node_extension_get_options.timeout

        request = build_get_request(
            pool_id=pool_id,
            node_id=node_id,
            extension_name=extension_name,
            select=_select,
            timeout=_timeout,
            client_request_id=_client_request_id,
            return_client_request_id=_return_client_request_id,
            ocp_date=_ocp_date,
            api_version=api_version,
            template_url=self.get.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        path_format_arguments = {
            "batchUrl": self._serialize.url("self._config.batch_url", self._config.batch_url, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.BatchError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers["client-request-id"] = self._deserialize("str", response.headers.get("client-request-id"))
        response_headers["request-id"] = self._deserialize("str", response.headers.get("request-id"))
        response_headers["ETag"] = self._deserialize("str", response.headers.get("ETag"))
        response_headers["Last-Modified"] = self._deserialize("rfc-1123", response.headers.get("Last-Modified"))

        deserialized = self._deserialize("NodeVMExtension", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    get.metadata = {"url": "/pools/{poolId}/nodes/{nodeId}/extensions/{extensionName}"}  # type: ignore

    @distributed_trace
    def list(
        self,
        pool_id: str,
        node_id: str,
        compute_node_extension_list_options: Optional[_models.ComputeNodeExtensionListOptions] = None,
        **kwargs: Any
    ) -> Iterable["_models.NodeVMExtension"]:
        """Lists the Compute Nodes Extensions in the specified Pool.

        Lists the Compute Nodes Extensions in the specified Pool.

        :param pool_id: The ID of the Pool that contains Compute Node. Required.
        :type pool_id: str
        :param node_id: The ID of the Compute Node that you want to list extensions. Required.
        :type node_id: str
        :param compute_node_extension_list_options: Parameter group. Default value is None.
        :type compute_node_extension_list_options: ~azure-batch.models.ComputeNodeExtensionListOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either NodeVMExtension or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure-batch.models.NodeVMExtension]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.NodeVMExtensionList]

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:
                _select = None
                _max_results = None
                _timeout = None
                _client_request_id = None
                _return_client_request_id = None
                _ocp_date = None
                if compute_node_extension_list_options is not None:
                    _client_request_id = compute_node_extension_list_options.client_request_id
                    _max_results = compute_node_extension_list_options.max_results
                    _ocp_date = compute_node_extension_list_options.ocp_date
                    _return_client_request_id = compute_node_extension_list_options.return_client_request_id
                    _select = compute_node_extension_list_options.select
                    _timeout = compute_node_extension_list_options.timeout

                request = build_list_request(
                    pool_id=pool_id,
                    node_id=node_id,
                    select=_select,
                    max_results=_max_results,
                    timeout=_timeout,
                    client_request_id=_client_request_id,
                    return_client_request_id=_return_client_request_id,
                    ocp_date=_ocp_date,
                    api_version=api_version,
                    template_url=self.list.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                path_format_arguments = {
                    "batchUrl": self._serialize.url(
                        "self._config.batch_url", self._config.batch_url, "str", skip_quote=True
                    ),
                }
                request.url = self._client.format_url(request.url, **path_format_arguments)  # type: ignore

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urlparse(next_link)
                _next_request_params = case_insensitive_dict(parse_qs(_parsed_next_link.query))
                _next_request_params["api-version"] = self._config.api_version
                request = HttpRequest("GET", urljoin(next_link, _parsed_next_link.path), params=_next_request_params)
                request = _convert_request(request)
                path_format_arguments = {
                    "batchUrl": self._serialize.url(
                        "self._config.batch_url", self._config.batch_url, "str", skip_quote=True
                    ),
                }
                request.url = self._client.format_url(request.url, **path_format_arguments)  # type: ignore
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("NodeVMExtensionList", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.odata_next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.BatchError, pipeline_response)
                raise HttpResponseError(response=response, model=error)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    list.metadata = {"url": "/pools/{poolId}/nodes/{nodeId}/extensions"}  # type: ignore
