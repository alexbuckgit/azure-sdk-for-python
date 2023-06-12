# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import AccessUri
from ._models_py3 import AdditionalUnattendContent
from ._models_py3 import ApiEntityReference
from ._models_py3 import ApiError
from ._models_py3 import ApiErrorBase
from ._models_py3 import AutoOSUpgradePolicy
from ._models_py3 import AvailabilitySet
from ._models_py3 import AvailabilitySetListResult
from ._models_py3 import AvailabilitySetUpdate
from ._models_py3 import BootDiagnostics
from ._models_py3 import BootDiagnosticsInstanceView
from ._models_py3 import ComputeOperationListResult
from ._models_py3 import ComputeOperationValue
from ._models_py3 import CreationData
from ._models_py3 import DataDisk
from ._models_py3 import DataDiskImage
from ._models_py3 import DiagnosticsProfile
from ._models_py3 import Disk
from ._models_py3 import DiskEncryptionSettings
from ._models_py3 import DiskInstanceView
from ._models_py3 import DiskList
from ._models_py3 import DiskSku
from ._models_py3 import DiskUpdate
from ._models_py3 import EncryptionSettings
from ._models_py3 import GrantAccessData
from ._models_py3 import HardwareProfile
from ._models_py3 import Image
from ._models_py3 import ImageDataDisk
from ._models_py3 import ImageDiskReference
from ._models_py3 import ImageListResult
from ._models_py3 import ImageOSDisk
from ._models_py3 import ImageReference
from ._models_py3 import ImageStorageProfile
from ._models_py3 import ImageUpdate
from ._models_py3 import InnerError
from ._models_py3 import InstanceViewStatus
from ._models_py3 import KeyVaultAndKeyReference
from ._models_py3 import KeyVaultAndSecretReference
from ._models_py3 import KeyVaultKeyReference
from ._models_py3 import KeyVaultSecretReference
from ._models_py3 import LinuxConfiguration
from ._models_py3 import ListUsagesResult
from ._models_py3 import LogAnalyticsInputBase
from ._models_py3 import LogAnalyticsOperationResult
from ._models_py3 import LogAnalyticsOutput
from ._models_py3 import MaintenanceRedeployStatus
from ._models_py3 import ManagedDiskParameters
from ._models_py3 import NetworkInterfaceReference
from ._models_py3 import NetworkProfile
from ._models_py3 import OSDisk
from ._models_py3 import OSDiskImage
from ._models_py3 import OSProfile
from ._models_py3 import Plan
from ._models_py3 import ProximityPlacementGroup
from ._models_py3 import ProximityPlacementGroupListResult
from ._models_py3 import ProximityPlacementGroupUpdate
from ._models_py3 import PurchasePlan
from ._models_py3 import RecoveryWalkResponse
from ._models_py3 import RequestRateByIntervalInput
from ._models_py3 import Resource
from ._models_py3 import RollbackStatusInfo
from ._models_py3 import RollingUpgradePolicy
from ._models_py3 import RollingUpgradeProgressInfo
from ._models_py3 import RollingUpgradeRunningStatus
from ._models_py3 import RollingUpgradeStatusInfo
from ._models_py3 import RunCommandDocument
from ._models_py3 import RunCommandDocumentBase
from ._models_py3 import RunCommandInput
from ._models_py3 import RunCommandInputParameter
from ._models_py3 import RunCommandListResult
from ._models_py3 import RunCommandParameterDefinition
from ._models_py3 import RunCommandResult
from ._models_py3 import Sku
from ._models_py3 import Snapshot
from ._models_py3 import SnapshotList
from ._models_py3 import SnapshotSku
from ._models_py3 import SnapshotUpdate
from ._models_py3 import SourceVault
from ._models_py3 import SshConfiguration
from ._models_py3 import SshPublicKey
from ._models_py3 import StorageProfile
from ._models_py3 import SubResource
from ._models_py3 import SubResourceReadOnly
from ._models_py3 import ThrottledRequestsInput
from ._models_py3 import UpdateResource
from ._models_py3 import UpgradeOperationHistoricalStatusInfo
from ._models_py3 import UpgradeOperationHistoricalStatusInfoProperties
from ._models_py3 import UpgradeOperationHistoryStatus
from ._models_py3 import UpgradePolicy
from ._models_py3 import Usage
from ._models_py3 import UsageName
from ._models_py3 import VaultCertificate
from ._models_py3 import VaultSecretGroup
from ._models_py3 import VirtualHardDisk
from ._models_py3 import VirtualMachine
from ._models_py3 import VirtualMachineAgentInstanceView
from ._models_py3 import VirtualMachineCaptureParameters
from ._models_py3 import VirtualMachineCaptureResult
from ._models_py3 import VirtualMachineExtension
from ._models_py3 import VirtualMachineExtensionHandlerInstanceView
from ._models_py3 import VirtualMachineExtensionImage
from ._models_py3 import VirtualMachineExtensionInstanceView
from ._models_py3 import VirtualMachineExtensionUpdate
from ._models_py3 import VirtualMachineExtensionsListResult
from ._models_py3 import VirtualMachineHealthStatus
from ._models_py3 import VirtualMachineIdentity
from ._models_py3 import VirtualMachineImage
from ._models_py3 import VirtualMachineImageResource
from ._models_py3 import VirtualMachineInstanceView
from ._models_py3 import VirtualMachineListResult
from ._models_py3 import VirtualMachineScaleSet
from ._models_py3 import VirtualMachineScaleSetDataDisk
from ._models_py3 import VirtualMachineScaleSetExtension
from ._models_py3 import VirtualMachineScaleSetExtensionListResult
from ._models_py3 import VirtualMachineScaleSetExtensionProfile
from ._models_py3 import VirtualMachineScaleSetIPConfiguration
from ._models_py3 import VirtualMachineScaleSetIdentity
from ._models_py3 import VirtualMachineScaleSetInstanceView
from ._models_py3 import VirtualMachineScaleSetInstanceViewStatusesSummary
from ._models_py3 import VirtualMachineScaleSetIpTag
from ._models_py3 import VirtualMachineScaleSetListOSUpgradeHistory
from ._models_py3 import VirtualMachineScaleSetListResult
from ._models_py3 import VirtualMachineScaleSetListSkusResult
from ._models_py3 import VirtualMachineScaleSetListWithLinkResult
from ._models_py3 import VirtualMachineScaleSetManagedDiskParameters
from ._models_py3 import VirtualMachineScaleSetNetworkConfiguration
from ._models_py3 import VirtualMachineScaleSetNetworkConfigurationDnsSettings
from ._models_py3 import VirtualMachineScaleSetNetworkProfile
from ._models_py3 import VirtualMachineScaleSetOSDisk
from ._models_py3 import VirtualMachineScaleSetOSProfile
from ._models_py3 import VirtualMachineScaleSetPublicIPAddressConfiguration
from ._models_py3 import VirtualMachineScaleSetPublicIPAddressConfigurationDnsSettings
from ._models_py3 import VirtualMachineScaleSetSku
from ._models_py3 import VirtualMachineScaleSetSkuCapacity
from ._models_py3 import VirtualMachineScaleSetStorageProfile
from ._models_py3 import VirtualMachineScaleSetUpdate
from ._models_py3 import VirtualMachineScaleSetUpdateIPConfiguration
from ._models_py3 import VirtualMachineScaleSetUpdateNetworkConfiguration
from ._models_py3 import VirtualMachineScaleSetUpdateNetworkProfile
from ._models_py3 import VirtualMachineScaleSetUpdateOSDisk
from ._models_py3 import VirtualMachineScaleSetUpdateOSProfile
from ._models_py3 import VirtualMachineScaleSetUpdatePublicIPAddressConfiguration
from ._models_py3 import VirtualMachineScaleSetUpdateStorageProfile
from ._models_py3 import VirtualMachineScaleSetUpdateVMProfile
from ._models_py3 import VirtualMachineScaleSetVM
from ._models_py3 import VirtualMachineScaleSetVMExtensionsSummary
from ._models_py3 import VirtualMachineScaleSetVMInstanceIDs
from ._models_py3 import VirtualMachineScaleSetVMInstanceRequiredIDs
from ._models_py3 import VirtualMachineScaleSetVMInstanceView
from ._models_py3 import VirtualMachineScaleSetVMListResult
from ._models_py3 import VirtualMachineScaleSetVMProfile
from ._models_py3 import VirtualMachineSize
from ._models_py3 import VirtualMachineSizeListResult
from ._models_py3 import VirtualMachineStatusCodeCount
from ._models_py3 import VirtualMachineUpdate
from ._models_py3 import WinRMConfiguration
from ._models_py3 import WinRMListener
from ._models_py3 import WindowsConfiguration

from ._compute_management_client_enums import AccessLevel
from ._compute_management_client_enums import CachingTypes
from ._compute_management_client_enums import DiskCreateOption
from ._compute_management_client_enums import DiskCreateOptionTypes
from ._compute_management_client_enums import IPVersion
from ._compute_management_client_enums import IntervalInMins
from ._compute_management_client_enums import MaintenanceOperationResultCodeTypes
from ._compute_management_client_enums import OperatingSystemStateTypes
from ._compute_management_client_enums import OperatingSystemTypes
from ._compute_management_client_enums import ProtocolTypes
from ._compute_management_client_enums import ProximityPlacementGroupType
from ._compute_management_client_enums import ResourceIdentityType
from ._compute_management_client_enums import RollingUpgradeActionType
from ._compute_management_client_enums import RollingUpgradeStatusCode
from ._compute_management_client_enums import SettingNames
from ._compute_management_client_enums import SnapshotStorageAccountTypes
from ._compute_management_client_enums import StatusLevelTypes
from ._compute_management_client_enums import StorageAccountTypes
from ._compute_management_client_enums import UpgradeMode
from ._compute_management_client_enums import UpgradeOperationInvoker
from ._compute_management_client_enums import UpgradeState
from ._compute_management_client_enums import VirtualMachineEvictionPolicyTypes
from ._compute_management_client_enums import VirtualMachinePriorityTypes
from ._compute_management_client_enums import VirtualMachineScaleSetSkuScaleType
from ._compute_management_client_enums import VirtualMachineSizeTypes
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AccessUri",
    "AdditionalUnattendContent",
    "ApiEntityReference",
    "ApiError",
    "ApiErrorBase",
    "AutoOSUpgradePolicy",
    "AvailabilitySet",
    "AvailabilitySetListResult",
    "AvailabilitySetUpdate",
    "BootDiagnostics",
    "BootDiagnosticsInstanceView",
    "ComputeOperationListResult",
    "ComputeOperationValue",
    "CreationData",
    "DataDisk",
    "DataDiskImage",
    "DiagnosticsProfile",
    "Disk",
    "DiskEncryptionSettings",
    "DiskInstanceView",
    "DiskList",
    "DiskSku",
    "DiskUpdate",
    "EncryptionSettings",
    "GrantAccessData",
    "HardwareProfile",
    "Image",
    "ImageDataDisk",
    "ImageDiskReference",
    "ImageListResult",
    "ImageOSDisk",
    "ImageReference",
    "ImageStorageProfile",
    "ImageUpdate",
    "InnerError",
    "InstanceViewStatus",
    "KeyVaultAndKeyReference",
    "KeyVaultAndSecretReference",
    "KeyVaultKeyReference",
    "KeyVaultSecretReference",
    "LinuxConfiguration",
    "ListUsagesResult",
    "LogAnalyticsInputBase",
    "LogAnalyticsOperationResult",
    "LogAnalyticsOutput",
    "MaintenanceRedeployStatus",
    "ManagedDiskParameters",
    "NetworkInterfaceReference",
    "NetworkProfile",
    "OSDisk",
    "OSDiskImage",
    "OSProfile",
    "Plan",
    "ProximityPlacementGroup",
    "ProximityPlacementGroupListResult",
    "ProximityPlacementGroupUpdate",
    "PurchasePlan",
    "RecoveryWalkResponse",
    "RequestRateByIntervalInput",
    "Resource",
    "RollbackStatusInfo",
    "RollingUpgradePolicy",
    "RollingUpgradeProgressInfo",
    "RollingUpgradeRunningStatus",
    "RollingUpgradeStatusInfo",
    "RunCommandDocument",
    "RunCommandDocumentBase",
    "RunCommandInput",
    "RunCommandInputParameter",
    "RunCommandListResult",
    "RunCommandParameterDefinition",
    "RunCommandResult",
    "Sku",
    "Snapshot",
    "SnapshotList",
    "SnapshotSku",
    "SnapshotUpdate",
    "SourceVault",
    "SshConfiguration",
    "SshPublicKey",
    "StorageProfile",
    "SubResource",
    "SubResourceReadOnly",
    "ThrottledRequestsInput",
    "UpdateResource",
    "UpgradeOperationHistoricalStatusInfo",
    "UpgradeOperationHistoricalStatusInfoProperties",
    "UpgradeOperationHistoryStatus",
    "UpgradePolicy",
    "Usage",
    "UsageName",
    "VaultCertificate",
    "VaultSecretGroup",
    "VirtualHardDisk",
    "VirtualMachine",
    "VirtualMachineAgentInstanceView",
    "VirtualMachineCaptureParameters",
    "VirtualMachineCaptureResult",
    "VirtualMachineExtension",
    "VirtualMachineExtensionHandlerInstanceView",
    "VirtualMachineExtensionImage",
    "VirtualMachineExtensionInstanceView",
    "VirtualMachineExtensionUpdate",
    "VirtualMachineExtensionsListResult",
    "VirtualMachineHealthStatus",
    "VirtualMachineIdentity",
    "VirtualMachineImage",
    "VirtualMachineImageResource",
    "VirtualMachineInstanceView",
    "VirtualMachineListResult",
    "VirtualMachineScaleSet",
    "VirtualMachineScaleSetDataDisk",
    "VirtualMachineScaleSetExtension",
    "VirtualMachineScaleSetExtensionListResult",
    "VirtualMachineScaleSetExtensionProfile",
    "VirtualMachineScaleSetIPConfiguration",
    "VirtualMachineScaleSetIdentity",
    "VirtualMachineScaleSetInstanceView",
    "VirtualMachineScaleSetInstanceViewStatusesSummary",
    "VirtualMachineScaleSetIpTag",
    "VirtualMachineScaleSetListOSUpgradeHistory",
    "VirtualMachineScaleSetListResult",
    "VirtualMachineScaleSetListSkusResult",
    "VirtualMachineScaleSetListWithLinkResult",
    "VirtualMachineScaleSetManagedDiskParameters",
    "VirtualMachineScaleSetNetworkConfiguration",
    "VirtualMachineScaleSetNetworkConfigurationDnsSettings",
    "VirtualMachineScaleSetNetworkProfile",
    "VirtualMachineScaleSetOSDisk",
    "VirtualMachineScaleSetOSProfile",
    "VirtualMachineScaleSetPublicIPAddressConfiguration",
    "VirtualMachineScaleSetPublicIPAddressConfigurationDnsSettings",
    "VirtualMachineScaleSetSku",
    "VirtualMachineScaleSetSkuCapacity",
    "VirtualMachineScaleSetStorageProfile",
    "VirtualMachineScaleSetUpdate",
    "VirtualMachineScaleSetUpdateIPConfiguration",
    "VirtualMachineScaleSetUpdateNetworkConfiguration",
    "VirtualMachineScaleSetUpdateNetworkProfile",
    "VirtualMachineScaleSetUpdateOSDisk",
    "VirtualMachineScaleSetUpdateOSProfile",
    "VirtualMachineScaleSetUpdatePublicIPAddressConfiguration",
    "VirtualMachineScaleSetUpdateStorageProfile",
    "VirtualMachineScaleSetUpdateVMProfile",
    "VirtualMachineScaleSetVM",
    "VirtualMachineScaleSetVMExtensionsSummary",
    "VirtualMachineScaleSetVMInstanceIDs",
    "VirtualMachineScaleSetVMInstanceRequiredIDs",
    "VirtualMachineScaleSetVMInstanceView",
    "VirtualMachineScaleSetVMListResult",
    "VirtualMachineScaleSetVMProfile",
    "VirtualMachineSize",
    "VirtualMachineSizeListResult",
    "VirtualMachineStatusCodeCount",
    "VirtualMachineUpdate",
    "WinRMConfiguration",
    "WinRMListener",
    "WindowsConfiguration",
    "AccessLevel",
    "CachingTypes",
    "DiskCreateOption",
    "DiskCreateOptionTypes",
    "IPVersion",
    "IntervalInMins",
    "MaintenanceOperationResultCodeTypes",
    "OperatingSystemStateTypes",
    "OperatingSystemTypes",
    "ProtocolTypes",
    "ProximityPlacementGroupType",
    "ResourceIdentityType",
    "RollingUpgradeActionType",
    "RollingUpgradeStatusCode",
    "SettingNames",
    "SnapshotStorageAccountTypes",
    "StatusLevelTypes",
    "StorageAccountTypes",
    "UpgradeMode",
    "UpgradeOperationInvoker",
    "UpgradeState",
    "VirtualMachineEvictionPolicyTypes",
    "VirtualMachinePriorityTypes",
    "VirtualMachineScaleSetSkuScaleType",
    "VirtualMachineSizeTypes",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
