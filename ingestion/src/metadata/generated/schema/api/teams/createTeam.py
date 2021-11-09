# generated by datamodel-codegen:
#   filename:  schema/api/teams/createTeam.json
#   timestamp: 2021-11-09T16:16:34+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field

from ...entity.teams import team
from ...type import basic, profile


class CreateTeamEntityRequest(BaseModel):
    name: team.TeamName
    displayName: Optional[str] = Field(
        None,
        description="Optional name used for display purposes. Example 'Marketing Team'",
    )
    description: Optional[str] = Field(
        None, description='Optional description of the team'
    )
    profile: Optional[profile.Profile] = Field(
        None, description='Optional team profile information'
    )
    users: Optional[List[basic.Uuid]] = Field(
        None, description='Optional IDs of users that are part of the team'
    )
