import datetime
from pydantic import BaseModel
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
    statusId: int
    status: str
    requestId: int
    list: list[RequestViewResponseList]
    smevChecks: list[RequestViewResponceSmevCheck]


