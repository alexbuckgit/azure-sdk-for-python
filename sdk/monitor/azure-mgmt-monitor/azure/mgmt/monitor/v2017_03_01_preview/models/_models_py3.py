# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Dict, List, Optional, TYPE_CHECKING

from ... import _serialization

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models


class ActivityLogAlertActionGroup(_serialization.Model):
    """A pointer to an Azure Action Group.

    All required parameters must be populated in order to send to Azure.

    :ivar action_group_id: The resourceId of the action group. This cannot be null or empty.
     Required.
    :vartype action_group_id: str
    :ivar webhook_properties: The dictionary of custom properties to include with the post
     operation. These data are appended to the webhook payload.
    :vartype webhook_properties: dict[str, str]
    """

    _validation = {
        "action_group_id": {"required": True},
    }

    _attribute_map = {
        "action_group_id": {"key": "actionGroupId", "type": "str"},
        "webhook_properties": {"key": "webhookProperties", "type": "{str}"},
    }

    def __init__(
        self, *, action_group_id: str, webhook_properties: Optional[Dict[str, str]] = None, **kwargs: Any
    ) -> None:
        """
        :keyword action_group_id: The resourceId of the action group. This cannot be null or empty.
         Required.
        :paramtype action_group_id: str
        :keyword webhook_properties: The dictionary of custom properties to include with the post
         operation. These data are appended to the webhook payload.
        :paramtype webhook_properties: dict[str, str]
        """
        super().__init__(**kwargs)
        self.action_group_id = action_group_id
        self.webhook_properties = webhook_properties


class ActivityLogAlertActionList(_serialization.Model):
    """A list of activity log alert actions.

    :ivar action_groups: The list of activity log alerts.
    :vartype action_groups:
     list[~azure.mgmt.monitor.v2017_03_01_preview.models.ActivityLogAlertActionGroup]
    """

    _attribute_map = {
        "action_groups": {"key": "actionGroups", "type": "[ActivityLogAlertActionGroup]"},
    }

    def __init__(
        self, *, action_groups: Optional[List["_models.ActivityLogAlertActionGroup"]] = None, **kwargs: Any
    ) -> None:
        """
        :keyword action_groups: The list of activity log alerts.
        :paramtype action_groups:
         list[~azure.mgmt.monitor.v2017_03_01_preview.models.ActivityLogAlertActionGroup]
        """
        super().__init__(**kwargs)
        self.action_groups = action_groups


class ActivityLogAlertAllOfCondition(_serialization.Model):
    """An Activity Log alert condition that is met when all its member conditions are met.

    All required parameters must be populated in order to send to Azure.

    :ivar all_of: The list of activity log alert conditions. Required.
    :vartype all_of:
     list[~azure.mgmt.monitor.v2017_03_01_preview.models.ActivityLogAlertLeafCondition]
    """

    _validation = {
        "all_of": {"required": True},
    }

    _attribute_map = {
        "all_of": {"key": "allOf", "type": "[ActivityLogAlertLeafCondition]"},
    }

    def __init__(self, *, all_of: List["_models.ActivityLogAlertLeafCondition"], **kwargs: Any) -> None:
        """
        :keyword all_of: The list of activity log alert conditions. Required.
        :paramtype all_of:
         list[~azure.mgmt.monitor.v2017_03_01_preview.models.ActivityLogAlertLeafCondition]
        """
        super().__init__(**kwargs)
        self.all_of = all_of


class ActivityLogAlertLeafCondition(_serialization.Model):
    """An Activity Log alert condition that is met by comparing an activity log field and value.

    All required parameters must be populated in order to send to Azure.

    :ivar field: The name of the field that this condition will examine. The possible values for
     this field are (case-insensitive): 'resourceId', 'category', 'caller', 'level',
     'operationName', 'resourceGroup', 'resourceProvider', 'status', 'subStatus', 'resourceType', or
     anything beginning with 'properties.'. Required.
    :vartype field: str
    :ivar equals: The field value will be compared to this value (case-insensitive) to determine if
     the condition is met. Required.
    :vartype equals: str
    """

    _validation = {
        "field": {"required": True},
        "equals": {"required": True},
    }

    _attribute_map = {
        "field": {"key": "field", "type": "str"},
        "equals": {"key": "equals", "type": "str"},
    }

    def __init__(self, *, field: str, equals: str, **kwargs: Any) -> None:
        """
        :keyword field: The name of the field that this condition will examine. The possible values for
         this field are (case-insensitive): 'resourceId', 'category', 'caller', 'level',
         'operationName', 'resourceGroup', 'resourceProvider', 'status', 'subStatus', 'resourceType', or
         anything beginning with 'properties.'. Required.
        :paramtype field: str
        :keyword equals: The field value will be compared to this value (case-insensitive) to determine
         if the condition is met. Required.
        :paramtype equals: str
        """
        super().__init__(**kwargs)
        self.field = field
        self.equals = equals


class ActivityLogAlertList(_serialization.Model):
    """A list of activity log alerts.

    :ivar value: The list of activity log alerts.
    :vartype value: list[~azure.mgmt.monitor.v2017_03_01_preview.models.ActivityLogAlertResource]
    """

    _attribute_map = {
        "value": {"key": "value", "type": "[ActivityLogAlertResource]"},
    }

    def __init__(self, *, value: Optional[List["_models.ActivityLogAlertResource"]] = None, **kwargs: Any) -> None:
        """
        :keyword value: The list of activity log alerts.
        :paramtype value: list[~azure.mgmt.monitor.v2017_03_01_preview.models.ActivityLogAlertResource]
        """
        super().__init__(**kwargs)
        self.value = value


class Resource(_serialization.Model):
    """An azure resource object.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Azure resource Id.
    :vartype id: str
    :ivar name: Azure resource name.
    :vartype name: str
    :ivar type: Azure resource type.
    :vartype type: str
    :ivar location: Resource location. Required.
    :vartype location: str
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "location": {"required": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "location": {"key": "location", "type": "str"},
        "tags": {"key": "tags", "type": "{str}"},
    }

    def __init__(self, *, location: str, tags: Optional[Dict[str, str]] = None, **kwargs: Any) -> None:
        """
        :keyword location: Resource location. Required.
        :paramtype location: str
        :keyword tags: Resource tags.
        :paramtype tags: dict[str, str]
        """
        super().__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.location = location
        self.tags = tags


class ActivityLogAlertResource(Resource):
    """An activity log alert resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Azure resource Id.
    :vartype id: str
    :ivar name: Azure resource name.
    :vartype name: str
    :ivar type: Azure resource type.
    :vartype type: str
    :ivar location: Resource location. Required.
    :vartype location: str
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar scopes: A list of resourceIds that will be used as prefixes. The alert will only apply to
     activityLogs with resourceIds that fall under one of these prefixes. This list must include at
     least one item.
    :vartype scopes: list[str]
    :ivar enabled: Indicates whether this activity log alert is enabled. If an activity log alert
     is not enabled, then none of its actions will be activated.
    :vartype enabled: bool
    :ivar condition: The condition that will cause this alert to activate.
    :vartype condition:
     ~azure.mgmt.monitor.v2017_03_01_preview.models.ActivityLogAlertAllOfCondition
    :ivar actions: The actions that will activate when the condition is met.
    :vartype actions: ~azure.mgmt.monitor.v2017_03_01_preview.models.ActivityLogAlertActionList
    :ivar description: A description of this activity log alert.
    :vartype description: str
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "location": {"required": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "location": {"key": "location", "type": "str"},
        "tags": {"key": "tags", "type": "{str}"},
        "scopes": {"key": "properties.scopes", "type": "[str]"},
        "enabled": {"key": "properties.enabled", "type": "bool"},
        "condition": {"key": "properties.condition", "type": "ActivityLogAlertAllOfCondition"},
        "actions": {"key": "properties.actions", "type": "ActivityLogAlertActionList"},
        "description": {"key": "properties.description", "type": "str"},
    }

    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
        scopes: Optional[List[str]] = None,
        enabled: bool = True,
        condition: Optional["_models.ActivityLogAlertAllOfCondition"] = None,
        actions: Optional["_models.ActivityLogAlertActionList"] = None,
        description: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword location: Resource location. Required.
        :paramtype location: str
        :keyword tags: Resource tags.
        :paramtype tags: dict[str, str]
        :keyword scopes: A list of resourceIds that will be used as prefixes. The alert will only apply
         to activityLogs with resourceIds that fall under one of these prefixes. This list must include
         at least one item.
        :paramtype scopes: list[str]
        :keyword enabled: Indicates whether this activity log alert is enabled. If an activity log
         alert is not enabled, then none of its actions will be activated.
        :paramtype enabled: bool
        :keyword condition: The condition that will cause this alert to activate.
        :paramtype condition:
         ~azure.mgmt.monitor.v2017_03_01_preview.models.ActivityLogAlertAllOfCondition
        :keyword actions: The actions that will activate when the condition is met.
        :paramtype actions: ~azure.mgmt.monitor.v2017_03_01_preview.models.ActivityLogAlertActionList
        :keyword description: A description of this activity log alert.
        :paramtype description: str
        """
        super().__init__(location=location, tags=tags, **kwargs)
        self.scopes = scopes
        self.enabled = enabled
        self.condition = condition
        self.actions = actions
        self.description = description


class ActivityLogAlertResourcePatch(Resource):
    """An activity log alert resource for patch operations.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Azure resource Id.
    :vartype id: str
    :ivar name: Azure resource name.
    :vartype name: str
    :ivar type: Azure resource type.
    :vartype type: str
    :ivar location: Resource location. Required.
    :vartype location: str
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar enabled: Indicates whether this activity log alert is enabled. If an activity log alert
     is not enabled, then none of its actions will be activated.
    :vartype enabled: bool
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "location": {"required": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "location": {"key": "location", "type": "str"},
        "tags": {"key": "tags", "type": "{str}"},
        "enabled": {"key": "properties.enabled", "type": "bool"},
    }

    def __init__(
        self, *, location: str, tags: Optional[Dict[str, str]] = None, enabled: bool = True, **kwargs: Any
    ) -> None:
        """
        :keyword location: Resource location. Required.
        :paramtype location: str
        :keyword tags: Resource tags.
        :paramtype tags: dict[str, str]
        :keyword enabled: Indicates whether this activity log alert is enabled. If an activity log
         alert is not enabled, then none of its actions will be activated.
        :paramtype enabled: bool
        """
        super().__init__(location=location, tags=tags, **kwargs)
        self.enabled = enabled


class ErrorResponse(_serialization.Model):
    """Describes the format of Error response.

    :ivar code: Error code.
    :vartype code: str
    :ivar message: Error message indicating why the operation failed.
    :vartype message: str
    """

    _attribute_map = {
        "code": {"key": "code", "type": "str"},
        "message": {"key": "message", "type": "str"},
    }

    def __init__(self, *, code: Optional[str] = None, message: Optional[str] = None, **kwargs: Any) -> None:
        """
        :keyword code: Error code.
        :paramtype code: str
        :keyword message: Error message indicating why the operation failed.
        :paramtype message: str
        """
        super().__init__(**kwargs)
        self.code = code
        self.message = message
