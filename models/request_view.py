import datetime
from pydantic import BaseModel, field_validator
from typing import Optional

from .common import (
        RequestInfo,
        RequestLoginPass,
)


class RequestViewResponceSmevCheck(BaseModel):
    status: int
    initialStatus: int
    requestType: int
    title: Optional[str]
    name: Optional[str]
    comment: Optional[str]
    launchDate: Optional[datetime.datetime]
    smevIntegrationId: Optional[int]


class RequestViewResponseList(BaseModel):
    typeId: int
    typeName: str


class RequestViewRequest(RequestLoginPass):
    requestId: int


class RequestViewResponse(BaseModel):
    info: RequestInfo
    statusId: str
    status: str
    requestId: str
    list: list[RequestViewResponseList]
    smevChecks: list[RequestViewResponceSmevCheck]

    @field_validator('statusId', 'requestId', mode='before')
    def parse_int_to_str(cls, value):
        return str(value)

