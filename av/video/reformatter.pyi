from av.enum import EnumItem

from .format import VideoFormat
from .frame import VideoFrame

class Interpolation(EnumItem):
    FAST_BILINEAER: int
    BILINEAR: int
    BICUBIC: int
    X: int
    POINT: int
    AREA: int
    BICUBLIN: int
    GAUSS: int
    SINC: int
    LANCZOS: int
    SPLINE: int

class ColorRange(EnumItem):
    UNSPECIFIED: int
    MPEG: int
    JPEG: int
    NB: int

class VideoReformatter:
    def reformat(
        self,
        frame: VideoFrame,
        width: int | None = None,
        height: int | None = None,
        format: str | None = None,
        src_colorspace=None,
        dst_colorspace=None,
        interpolation: int | str | None = None,
        src_color_range: int | str | None = None,
        dst_color_range: int | str | None = None,
    ) -> VideoFrame: ...
