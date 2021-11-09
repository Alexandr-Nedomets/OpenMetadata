# generated by datamodel-codegen:
#   filename:  schema/api/setOwner.json
#   timestamp: 2021-11-09T16:16:34+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field

from ..type import basic


class SetOwnershipForAGivenEntity(BaseModel):
    id: Optional[basic.Uuid] = Field(None, description='Id of the owner of the entity')
    type: Optional[str] = Field(
        None, description="Entity type of the owner typically either 'user' or 'team'"
    )
