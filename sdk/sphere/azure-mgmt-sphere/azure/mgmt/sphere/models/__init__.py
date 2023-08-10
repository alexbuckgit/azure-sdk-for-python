# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models import Catalog
from ._models import CatalogProperties
from ._models import CatalogUpdate
from ._models import Certificate
from ._models import CertificateChainResponse
from ._models import CertificateProperties
from ._models import ClaimDevicesRequest
from ._models import CountDeviceResponse
from ._models import CountElementsResponse
from ._models import Deployment
from ._models import DeploymentProperties
from ._models import Device
from ._models import DeviceGroup
from ._models import DeviceGroupProperties
from ._models import DeviceGroupUpdate
from ._models import DeviceGroupUpdateProperties
from ._models import DeviceInsight
from ._models import DevicePatchProperties
from ._models import DeviceProperties
from ._models import DeviceUpdate
from ._models import DeviceUpdateProperties
from ._models import ErrorAdditionalInfo
from ._models import ErrorDetail
from ._models import ErrorResponse
from ._models import GenerateCapabilityImageRequest
from ._models import Image
from ._models import ImageProperties
from ._models import ImageUploadRequestBody
from ._models import ListDeviceGroupsRequest
from ._models import Operation
from ._models import OperationDisplay
from ._models import Product
from ._models import ProductProperties
from ._models import ProductUpdate
from ._models import ProductUpdateProperties
from ._models import ProofOfPossessionNonceRequest
from ._models import ProofOfPossessionNonceResponse
from ._models import ProxyResource
from ._models import Resource
from ._models import SignedCapabilityImageResponse
from ._models import SystemData
from ._models import TrackedResource

from ._enums import ActionType
from ._enums import AllowCrashDumpCollection
from ._enums import CapabilityType
from ._enums import CertificateStatus
from ._enums import CreatedByType
from ._enums import ImageType
from ._enums import OSFeedType
from ._enums import Origin
from ._enums import ProvisioningState
from ._enums import RegionalDataBoundary
from ._enums import UpdatePolicy
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "Catalog",
    "CatalogProperties",
    "CatalogUpdate",
    "Certificate",
    "CertificateChainResponse",
    "CertificateProperties",
    "ClaimDevicesRequest",
    "CountDeviceResponse",
    "CountElementsResponse",
    "Deployment",
    "DeploymentProperties",
    "Device",
    "DeviceGroup",
    "DeviceGroupProperties",
    "DeviceGroupUpdate",
    "DeviceGroupUpdateProperties",
    "DeviceInsight",
    "DevicePatchProperties",
    "DeviceProperties",
    "DeviceUpdate",
    "DeviceUpdateProperties",
    "ErrorAdditionalInfo",
    "ErrorDetail",
    "ErrorResponse",
    "GenerateCapabilityImageRequest",
    "Image",
    "ImageProperties",
    "ImageUploadRequestBody",
    "ListDeviceGroupsRequest",
    "Operation",
    "OperationDisplay",
    "Product",
    "ProductProperties",
    "ProductUpdate",
    "ProductUpdateProperties",
    "ProofOfPossessionNonceRequest",
    "ProofOfPossessionNonceResponse",
    "ProxyResource",
    "Resource",
    "SignedCapabilityImageResponse",
    "SystemData",
    "TrackedResource",
    "ActionType",
    "AllowCrashDumpCollection",
    "CapabilityType",
    "CertificateStatus",
    "CreatedByType",
    "ImageType",
    "OSFeedType",
    "Origin",
    "ProvisioningState",
    "RegionalDataBoundary",
    "UpdatePolicy",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
