# generated by datamodel-codegen:
#   filename:  schema/entity/data/pipeline.json
#   timestamp: 2021-11-09T16:16:34+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import AnyUrl, BaseModel, Field, constr

from ...type import basic, entityHistory, entityReference, tagLabel


class Task(BaseModel):
    name: constr(min_length=1, max_length=64) = Field(
        ..., description='Name that identifies this task instance uniquely.'
    )
    displayName: Optional[str] = Field(
        None,
        description='Display Name that identifies this Task. It could be title or label from the pipeline services.',
    )
    fullyQualifiedName: Optional[constr(min_length=1, max_length=64)] = Field(
        None,
        description="A unique name that identifies a pipeline in the format 'ServiceName.PipelineName.TaskName'.",
    )
    description: Optional[str] = Field(None, description='Description of this Task.')
    taskUrl: Optional[AnyUrl] = Field(
        None,
        description='Task URL to visit/manage. This URL points to respective pipeline service UI.',
    )
    downstreamTasks: Optional[List[constr(min_length=1, max_length=64)]] = Field(
        None, description='All the tasks that are downstream of this task.'
    )
    taskType: Optional[str] = Field(
        None, description='Type of the Task. Usually refers to the class it implements.'
    )
    taskSQL: Optional[basic.SqlQuery] = Field(
        None, description='SQL used in the task. Can be used to determine the lineage.'
    )
    tags: Optional[List[tagLabel.TagLabel]] = Field(
        None, description='Tags for this task.'
    )


class Pipeline(BaseModel):
    id: basic.Uuid = Field(
        ..., description='Unique identifier that identifies a pipeline instance.'
    )
    name: constr(min_length=1, max_length=64) = Field(
        ..., description='Name that identifies this pipeline instance uniquely.'
    )
    displayName: Optional[str] = Field(
        None,
        description='Display Name that identifies this Pipeline. It could be title or label from the source services.',
    )
    fullyQualifiedName: Optional[constr(min_length=1, max_length=64)] = Field(
        None,
        description="A unique name that identifies a pipeline in the format 'ServiceName.PipelineName'.",
    )
    description: Optional[str] = Field(
        None, description='Description of this Pipeline.'
    )
    version: Optional[entityHistory.EntityVersion] = Field(
        None, description='Metadata version of the entity.'
    )
    updatedAt: Optional[basic.DateTime] = Field(
        None,
        description='Last update time corresponding to the new version of the entity.',
    )
    updatedBy: Optional[str] = Field(None, description='User who made the update.')
    pipelineUrl: Optional[AnyUrl] = Field(
        None,
        description='Pipeline  URL to visit/manage. This URL points to respective pipeline service UI.',
    )
    concurrency: Optional[int] = Field(None, description='Concurrency of the Pipeline.')
    pipelineLocation: Optional[str] = Field(None, description='Pipeline Code Location.')
    startDate: Optional[basic.DateTime] = Field(
        None, description='Start date of the workflow.'
    )
    tasks: Optional[List[Task]] = Field(
        None, description='All the tasks that are part of pipeline.'
    )
    followers: Optional[entityReference.EntityReferenceList] = Field(
        None, description='Followers of this Pipeline.'
    )
    tags: Optional[List[tagLabel.TagLabel]] = Field(
        None, description='Tags for this Pipeline.'
    )
    href: Optional[basic.Href] = Field(
        None, description='Link to the resource corresponding to this entity.'
    )
    owner: Optional[entityReference.EntityReference] = Field(
        None, description='Owner of this pipeline.'
    )
    service: entityReference.EntityReference = Field(
        ..., description='Link to service where this pipeline is hosted in.'
    )
    changeDescription: Optional[entityHistory.ChangeDescription] = Field(
        None, description='Change that lead to this version of the entity.'
    )
