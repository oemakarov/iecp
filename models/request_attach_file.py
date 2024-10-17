from typing import Union

from .common import (
    RequestLoginPass,
)


class RequestAttachFileRequest(RequestLoginPass):
    fileName: str
    file: Union[str, bytes]
    fileType: int
    requestId: int
