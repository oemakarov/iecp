from typing import Union

from .common import (
        RequestLoginPass,
)

# class RequestAttachFileResponse(BaseModel):
#     requestId: Optional[int]


class RequestAttachFileRequest(RequestLoginPass):
    fileName: str
    file: Union[str, bytes]
    fileType: int
    requestId: int

