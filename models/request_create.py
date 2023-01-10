from pydantic import BaseModel
from typing import Optional

from .common import (
        RequestLoginPass,
        RequestInfo,
)


class RequestCreateResponse(BaseModel):
    requestId: Optional[int]


class RequestCreateRequest(RequestLoginPass):
    info: RequestInfo


