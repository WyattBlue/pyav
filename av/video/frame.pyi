from typing import Any

from PIL import Image

from av.enum import EnumItem

from .plane import VideoPlane

class PictureType(EnumItem):
    NONE: int
    I: int
    P: int
    B: int
    S: int
    SI: int
    SP: int
    BI: int

class VideoFrame:
    planes: tuple[VideoPlane]
    width: int
    height: int
    key_frame: bool
    interlaced_frame: bool
    pict_type: Any

    def from_image(self, img: Image.Image) -> VideoFrame: ...
    def to_image(self, **kwargs) -> Image.Image: ...
    def __init__(
        self, name: str, width: int = 0, height: int = 0, format: str = "yuv420p"
    ): ...
