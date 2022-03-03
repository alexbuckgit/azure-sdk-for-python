# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from six import with_metaclass
from azure.core import CaseInsensitiveEnumMeta


class AccessLevel(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    NONE = "None"
    READ = "Read"
    WRITE = "Write"

class Architecture(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """CPU architecture supported by an OS disk.
    """

    X64 = "x64"
    ARM64 = "Arm64"

class DataAccessAuthMode(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Additional authentication requirements when exporting or uploading to a disk or snapshot.
    """

    #: When export/upload URL is used, the system checks if the user has an identity in Azure Active
    #: Directory and has necessary permissions to export/upload the data. Please refer to
    #: aka.ms/DisksAzureADAuth.
    AZURE_ACTIVE_DIRECTORY = "AzureActiveDirectory"
    #: No additional authentication would be performed when accessing export/upload URL.
    NONE = "None"

class DiskCreateOption(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """This enumerates the possible sources of a disk's creation.
    """

    #: Create an empty data disk of a size given by diskSizeGB.
    EMPTY = "Empty"
    #: Disk will be attached to a VM.
    ATTACH = "Attach"
    #: Create a new disk from a platform image specified by the given imageReference or
    #: galleryImageReference.
    FROM_IMAGE = "FromImage"
    #: Create a disk by importing from a blob specified by a sourceUri in a storage account specified
    #: by storageAccountId.
    IMPORT_ENUM = "Import"
    #: Create a new disk or snapshot by copying from a disk or snapshot specified by the given
    #: sourceResourceId.
    COPY = "Copy"
    #: Create a new disk by copying from a backup recovery point.
    RESTORE = "Restore"
    #: Create a new disk by obtaining a write token and using it to directly upload the contents of
    #: the disk.
    UPLOAD = "Upload"
    #: Create a new disk by using a deep copy process, where the resource creation is considered
    #: complete only after all data has been copied from the source.
    COPY_START = "CopyStart"
    #: Similar to Import create option. Create a new Trusted Launch VM or Confidential VM supported
    #: disk by importing additional blob for VM guest state specified by securityDataUri in storage
    #: account specified by storageAccountId.
    IMPORT_SECURE = "ImportSecure"
    #: Similar to Upload create option. Create a new Trusted Launch VM or Confidential VM supported
    #: disk and upload using write token in both disk and VM guest state.
    UPLOAD_PREPARED_SECURE = "UploadPreparedSecure"

class DiskEncryptionSetIdentityType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of Managed Identity used by the DiskEncryptionSet. Only SystemAssigned is supported
    for new creations. Disk Encryption Sets can be updated with Identity type None during migration
    of subscription to a new Azure Active Directory tenant; it will cause the encrypted resources
    to lose access to the keys.
    """

    SYSTEM_ASSIGNED = "SystemAssigned"
    NONE = "None"

class DiskEncryptionSetType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of key used to encrypt the data of the disk.
    """

    #: Resource using diskEncryptionSet would be encrypted at rest with Customer managed key that can
    #: be changed and revoked by a customer.
    ENCRYPTION_AT_REST_WITH_CUSTOMER_KEY = "EncryptionAtRestWithCustomerKey"
    #: Resource using diskEncryptionSet would be encrypted at rest with two layers of encryption. One
    #: of the keys is Customer managed and the other key is Platform managed.
    ENCRYPTION_AT_REST_WITH_PLATFORM_AND_CUSTOMER_KEYS = "EncryptionAtRestWithPlatformAndCustomerKeys"
    #: Confidential VM supported disk and VM guest state would be encrypted with customer managed key.
    CONFIDENTIAL_VM_ENCRYPTED_WITH_CUSTOMER_KEY = "ConfidentialVmEncryptedWithCustomerKey"

class DiskSecurityTypes(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Specifies the SecurityType of the VM. Applicable for OS disks only.
    """

    #: Trusted Launch provides security features such as secure boot and virtual Trusted Platform
    #: Module (vTPM).
    TRUSTED_LAUNCH = "TrustedLaunch"
    #: Indicates Confidential VM disk with only VM guest state encrypted.
    CONFIDENTIAL_VM_VMGUEST_STATE_ONLY_ENCRYPTED_WITH_PLATFORM_KEY = "ConfidentialVM_VMGuestStateOnlyEncryptedWithPlatformKey"
    #: Indicates Confidential VM disk with both OS disk and VM guest state encrypted with a platform
    #: managed key.
    CONFIDENTIAL_VM_DISK_ENCRYPTED_WITH_PLATFORM_KEY = "ConfidentialVM_DiskEncryptedWithPlatformKey"
    #: Indicates Confidential VM disk with both OS disk and VM guest state encrypted with a customer
    #: managed key.
    CONFIDENTIAL_VM_DISK_ENCRYPTED_WITH_CUSTOMER_KEY = "ConfidentialVM_DiskEncryptedWithCustomerKey"

class DiskState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """This enumerates the possible state of the disk.
    """

    #: The disk is not being used and can be attached to a VM.
    UNATTACHED = "Unattached"
    #: The disk is currently attached to a running VM.
    ATTACHED = "Attached"
    #: The disk is attached to a stopped-deallocated VM.
    RESERVED = "Reserved"
    #: The disk is attached to a VM which is in hibernated state.
    FROZEN = "Frozen"
    #: The disk currently has an Active SAS Uri associated with it.
    ACTIVE_SAS = "ActiveSAS"
    #: The disk is attached to a VM in hibernated state and has an active SAS URI associated with it.
    ACTIVE_SAS_FROZEN = "ActiveSASFrozen"
    #: A disk is ready to be created by upload by requesting a write token.
    READY_TO_UPLOAD = "ReadyToUpload"
    #: A disk is created for upload and a write token has been issued for uploading to it.
    ACTIVE_UPLOAD = "ActiveUpload"

class DiskStorageAccountTypes(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The sku name.
    """

    #: Standard HDD locally redundant storage. Best for backup, non-critical, and infrequent access.
    STANDARD_LRS = "Standard_LRS"
    #: Premium SSD locally redundant storage. Best for production and performance sensitive workloads.
    PREMIUM_LRS = "Premium_LRS"
    #: Standard SSD locally redundant storage. Best for web servers, lightly used enterprise
    #: applications and dev/test.
    STANDARD_SSD_LRS = "StandardSSD_LRS"
    #: Ultra SSD locally redundant storage. Best for IO-intensive workloads such as SAP HANA, top tier
    #: databases (for example, SQL, Oracle), and other transaction-heavy workloads.
    ULTRA_SSD_LRS = "UltraSSD_LRS"
    #: Premium SSD zone redundant storage. Best for the production workloads that need storage
    #: resiliency against zone failures.
    PREMIUM_ZRS = "Premium_ZRS"
    #: Standard SSD zone redundant storage. Best for web servers, lightly used enterprise applications
    #: and dev/test that need storage resiliency against zone failures.
    STANDARD_SSD_ZRS = "StandardSSD_ZRS"

class EncryptionType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of key used to encrypt the data of the disk.
    """

    #: Disk is encrypted at rest with Platform managed key. It is the default encryption type. This is
    #: not a valid encryption type for disk encryption sets.
    ENCRYPTION_AT_REST_WITH_PLATFORM_KEY = "EncryptionAtRestWithPlatformKey"
    #: Disk is encrypted at rest with Customer managed key that can be changed and revoked by a
    #: customer.
    ENCRYPTION_AT_REST_WITH_CUSTOMER_KEY = "EncryptionAtRestWithCustomerKey"
    #: Disk is encrypted at rest with 2 layers of encryption. One of the keys is Customer managed and
    #: the other key is Platform managed.
    ENCRYPTION_AT_REST_WITH_PLATFORM_AND_CUSTOMER_KEYS = "EncryptionAtRestWithPlatformAndCustomerKeys"

class ExtendedLocationTypes(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of extendedLocation.
    """

    EDGE_ZONE = "EdgeZone"

class HyperVGeneration(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The hypervisor generation of the Virtual Machine. Applicable to OS disks only.
    """

    V1 = "V1"
    V2 = "V2"

class NetworkAccessPolicy(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Policy for accessing the disk via network.
    """

    #: The disk can be exported or uploaded to from any network.
    ALLOW_ALL = "AllowAll"
    #: The disk can be exported or uploaded to using a DiskAccess resource's private endpoints.
    ALLOW_PRIVATE = "AllowPrivate"
    #: The disk cannot be exported.
    DENY_ALL = "DenyAll"

class OperatingSystemTypes(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The Operating System type.
    """

    WINDOWS = "Windows"
    LINUX = "Linux"

class PrivateEndpointConnectionProvisioningState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The current provisioning state.
    """

    SUCCEEDED = "Succeeded"
    CREATING = "Creating"
    DELETING = "Deleting"
    FAILED = "Failed"

class PrivateEndpointServiceConnectionStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The private endpoint connection status.
    """

    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"

class PublicNetworkAccess(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Policy for controlling export on the disk.
    """

    #: You can generate a SAS URI to access the underlying data of the disk publicly on the internet
    #: when NetworkAccessPolicy is set to AllowAll. You can access the data via the SAS URI only from
    #: your trusted Azure VNET when NetworkAccessPolicy is set to AllowPrivate.
    ENABLED = "Enabled"
    #: You cannot access the underlying data of the disk publicly on the internet even when
    #: NetworkAccessPolicy is set to AllowAll. You can access the data via the SAS URI only from your
    #: trusted Azure VNET when NetworkAccessPolicy is set to AllowPrivate.
    DISABLED = "Disabled"

class SnapshotStorageAccountTypes(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The sku name.
    """

    #: Standard HDD locally redundant storage.
    STANDARD_LRS = "Standard_LRS"
    #: Premium SSD locally redundant storage.
    PREMIUM_LRS = "Premium_LRS"
    #: Standard zone redundant storage.
    STANDARD_ZRS = "Standard_ZRS"
