from typing import Optional

from .common import (
        RequestLoginPass,
        RequestInfo,
)


class RequestChangeRequest(RequestLoginPass):
    requestId: int
    requestArchived: Optional[bool]
    info: Optional[RequestInfo]


