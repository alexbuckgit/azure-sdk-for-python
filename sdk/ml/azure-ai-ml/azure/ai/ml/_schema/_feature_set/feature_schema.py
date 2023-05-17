# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

# pylint: disable=unused-argument,no-self-use

from marshmallow import fields, post_load

from azure.ai.ml._schema.core.schema import PatchedSchemaMeta
from azure.ai.ml.entities._feature_store_entity.data_column_type import DataColumnType

class FeatureSchema(metaclass=PatchedSchemaMeta):
    name = fields.Str(
        required=True,
        allow_none=False,
    )
    data_type = fields.Enum(
        DataColumnType,
        required=True,
        allow_none=False
    )
    description = fields.Str(required=False)
    tags = fields.Dict(keys=fields.Str(), values=fields.Str(), required=False)

    @post_load
    def make(self, data, **kwargs):
        from azure.ai.ml.entities._feature_set.feature import Feature

        return Feature(description=data.pop("description", None), **data)
