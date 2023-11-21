# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import AgentConfiguration
from ._models_py3 import AgentUpgrade
from ._models_py3 import AgentVersion
from ._models_py3 import AgentVersionsList
from ._models_py3 import AvailablePatchCountByClassification
from ._models_py3 import CloudMetadata
from ._models_py3 import ConfigurationExtension
from ._models_py3 import ConnectionDetail
from ._models_py3 import ErrorAdditionalInfo
from ._models_py3 import ErrorDetail
from ._models_py3 import ErrorDetailAutoGenerated
from ._models_py3 import ErrorResponse
from ._models_py3 import ErrorResponseAutoGenerated
from ._models_py3 import EsuKey
from ._models_py3 import ExtensionTargetProperties
from ._models_py3 import ExtensionValue
from ._models_py3 import ExtensionValueListResult
from ._models_py3 import HybridComputePrivateLinkScope
from ._models_py3 import HybridComputePrivateLinkScopeListResult
from ._models_py3 import HybridComputePrivateLinkScopeProperties
from ._models_py3 import HybridIdentityMetadata
from ._models_py3 import HybridIdentityMetadataList
from ._models_py3 import Identity
from ._models_py3 import IpAddress
from ._models_py3 import License
from ._models_py3 import LicenseDetails
from ._models_py3 import LicenseProfile
from ._models_py3 import LicenseProfileArmEsuProperties
from ._models_py3 import LicenseProfileArmEsuPropertiesWithoutAssignedLicense
from ._models_py3 import LicenseProfileMachineInstanceView
from ._models_py3 import LicenseProfileMachineInstanceViewEsuProperties
from ._models_py3 import LicenseProfileStorageModelEsuProperties
from ._models_py3 import LicenseProfileUpdate
from ._models_py3 import LicenseProfilesListResult
from ._models_py3 import LicenseUpdate
from ._models_py3 import LicensesListResult
from ._models_py3 import LinuxParameters
from ._models_py3 import LocationData
from ._models_py3 import Machine
from ._models_py3 import MachineAssessPatchesResult
from ._models_py3 import MachineExtension
from ._models_py3 import MachineExtensionInstanceView
from ._models_py3 import MachineExtensionInstanceViewStatus
from ._models_py3 import MachineExtensionProperties
from ._models_py3 import MachineExtensionUpdate
from ._models_py3 import MachineExtensionUpgrade
from ._models_py3 import MachineExtensionsListResult
from ._models_py3 import MachineInstallPatchesParameters
from ._models_py3 import MachineInstallPatchesResult
from ._models_py3 import MachineListResult
from ._models_py3 import MachineUpdate
from ._models_py3 import NetworkInterface
from ._models_py3 import NetworkProfile
from ._models_py3 import OSProfile
from ._models_py3 import OSProfileLinuxConfiguration
from ._models_py3 import OSProfileWindowsConfiguration
from ._models_py3 import OperationListResult
from ._models_py3 import OperationValue
from ._models_py3 import OperationValueDisplay
from ._models_py3 import PrivateEndpointConnection
from ._models_py3 import PrivateEndpointConnectionDataModel
from ._models_py3 import PrivateEndpointConnectionListResult
from ._models_py3 import PrivateEndpointConnectionProperties
from ._models_py3 import PrivateEndpointProperty
from ._models_py3 import PrivateLinkResource
from ._models_py3 import PrivateLinkResourceListResult
from ._models_py3 import PrivateLinkResourceProperties
from ._models_py3 import PrivateLinkScopeValidationDetails
from ._models_py3 import PrivateLinkScopesResource
from ._models_py3 import PrivateLinkServiceConnectionStateProperty
from ._models_py3 import ProxyResource
from ._models_py3 import Resource
from ._models_py3 import ResourceUpdate
from ._models_py3 import ServiceStatus
from ._models_py3 import ServiceStatuses
from ._models_py3 import Subnet
from ._models_py3 import SystemData
from ._models_py3 import TagsResource
from ._models_py3 import TrackedResource
from ._models_py3 import WindowsParameters

from ._hybrid_compute_management_client_enums import AgentConfigurationMode
from ._hybrid_compute_management_client_enums import ArcKindEnum
from ._hybrid_compute_management_client_enums import AssessmentModeTypes
from ._hybrid_compute_management_client_enums import CreatedByType
from ._hybrid_compute_management_client_enums import EsuEligibility
from ._hybrid_compute_management_client_enums import EsuKeyState
from ._hybrid_compute_management_client_enums import EsuServerType
from ._hybrid_compute_management_client_enums import InstanceViewTypes
from ._hybrid_compute_management_client_enums import LastAttemptStatusEnum
from ._hybrid_compute_management_client_enums import LicenseAssignmentState
from ._hybrid_compute_management_client_enums import LicenseCoreType
from ._hybrid_compute_management_client_enums import LicenseEdition
from ._hybrid_compute_management_client_enums import LicenseState
from ._hybrid_compute_management_client_enums import LicenseTarget
from ._hybrid_compute_management_client_enums import LicenseType
from ._hybrid_compute_management_client_enums import OsType
from ._hybrid_compute_management_client_enums import PatchModeTypes
from ._hybrid_compute_management_client_enums import PatchOperationStartedBy
from ._hybrid_compute_management_client_enums import PatchOperationStatus
from ._hybrid_compute_management_client_enums import PatchServiceUsed
from ._hybrid_compute_management_client_enums import ProvisioningState
from ._hybrid_compute_management_client_enums import PublicNetworkAccessType
from ._hybrid_compute_management_client_enums import StatusLevelTypes
from ._hybrid_compute_management_client_enums import StatusTypes
from ._hybrid_compute_management_client_enums import VMGuestPatchClassificationLinux
from ._hybrid_compute_management_client_enums import VMGuestPatchClassificationWindows
from ._hybrid_compute_management_client_enums import VMGuestPatchRebootSetting
from ._hybrid_compute_management_client_enums import VMGuestPatchRebootStatus
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AgentConfiguration",
    "AgentUpgrade",
    "AgentVersion",
    "AgentVersionsList",
    "AvailablePatchCountByClassification",
    "CloudMetadata",
    "ConfigurationExtension",
    "ConnectionDetail",
    "ErrorAdditionalInfo",
    "ErrorDetail",
    "ErrorDetailAutoGenerated",
    "ErrorResponse",
    "ErrorResponseAutoGenerated",
    "EsuKey",
    "ExtensionTargetProperties",
    "ExtensionValue",
    "ExtensionValueListResult",
    "HybridComputePrivateLinkScope",
    "HybridComputePrivateLinkScopeListResult",
    "HybridComputePrivateLinkScopeProperties",
    "HybridIdentityMetadata",
    "HybridIdentityMetadataList",
    "Identity",
    "IpAddress",
    "License",
    "LicenseDetails",
    "LicenseProfile",
    "LicenseProfileArmEsuProperties",
    "LicenseProfileArmEsuPropertiesWithoutAssignedLicense",
    "LicenseProfileMachineInstanceView",
    "LicenseProfileMachineInstanceViewEsuProperties",
    "LicenseProfileStorageModelEsuProperties",
    "LicenseProfileUpdate",
    "LicenseProfilesListResult",
    "LicenseUpdate",
    "LicensesListResult",
    "LinuxParameters",
    "LocationData",
    "Machine",
    "MachineAssessPatchesResult",
    "MachineExtension",
    "MachineExtensionInstanceView",
    "MachineExtensionInstanceViewStatus",
    "MachineExtensionProperties",
    "MachineExtensionUpdate",
    "MachineExtensionUpgrade",
    "MachineExtensionsListResult",
    "MachineInstallPatchesParameters",
    "MachineInstallPatchesResult",
    "MachineListResult",
    "MachineUpdate",
    "NetworkInterface",
    "NetworkProfile",
    "OSProfile",
    "OSProfileLinuxConfiguration",
    "OSProfileWindowsConfiguration",
    "OperationListResult",
    "OperationValue",
    "OperationValueDisplay",
    "PrivateEndpointConnection",
    "PrivateEndpointConnectionDataModel",
    "PrivateEndpointConnectionListResult",
    "PrivateEndpointConnectionProperties",
    "PrivateEndpointProperty",
    "PrivateLinkResource",
    "PrivateLinkResourceListResult",
    "PrivateLinkResourceProperties",
    "PrivateLinkScopeValidationDetails",
    "PrivateLinkScopesResource",
    "PrivateLinkServiceConnectionStateProperty",
    "ProxyResource",
    "Resource",
    "ResourceUpdate",
    "ServiceStatus",
    "ServiceStatuses",
    "Subnet",
    "SystemData",
    "TagsResource",
    "TrackedResource",
    "WindowsParameters",
    "AgentConfigurationMode",
    "ArcKindEnum",
    "AssessmentModeTypes",
    "CreatedByType",
    "EsuEligibility",
    "EsuKeyState",
    "EsuServerType",
    "InstanceViewTypes",
    "LastAttemptStatusEnum",
    "LicenseAssignmentState",
    "LicenseCoreType",
    "LicenseEdition",
    "LicenseState",
    "LicenseTarget",
    "LicenseType",
    "OsType",
    "PatchModeTypes",
    "PatchOperationStartedBy",
    "PatchOperationStatus",
    "PatchServiceUsed",
    "ProvisioningState",
    "PublicNetworkAccessType",
    "StatusLevelTypes",
    "StatusTypes",
    "VMGuestPatchClassificationLinux",
    "VMGuestPatchClassificationWindows",
    "VMGuestPatchRebootSetting",
    "VMGuestPatchRebootStatus",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
