from pydantic import BaseModel, RootModel
from typing import Optional

from .common import (
        RequestLoginPass,
        Attachment,
)

class RequestResultRequest(RequestLoginPass):
    requestId: int


class RequestResultResponseAttacment(BaseModel, Attachment):
    name: str
    contentBase64: str
    mimeType: str
    type: Optional[int]


class RequestResultResponse(RootModel):
    root: list[RequestResultResponseAttacment]
