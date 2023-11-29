from typing import Any

from .plane import VideoPlane

class VideoFrame:
    planes: tuple[VideoPlane]
    width: int
    height: int
    key_frame: bool
    interlaced_frame: bool
    pict_type: Any

    def from_image(self, img: Any) -> VideoFrame: ...
    def __init__(
        self, name: str, width: int = 0, height: int = 0, format: str = "yuv420p"
    ): ...
