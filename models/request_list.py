from pydantic import BaseModel
from typing import Optional

from .common import RequestLoginPass, RequestInfo


class RequestListFilter(RequestInfo):
    HideArchived: Optional[bool]


class RequestInfoExt(RequestInfo):
    statusId: int
    status: str


class RequestListRequest(RequestLoginPass):
    filter: RequestListFilter


class RequestListResponse(BaseModel):
    info: list[RequestInfoExt]
