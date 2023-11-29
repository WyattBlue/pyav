from fractions import Fraction
from typing import Literal

from av.codec.context import CodecContext

class VideoCodecContext(CodecContext):
    width: int
    height: int
    bits_per_codec_sample: int
    pix_fmt: str
    framerate: Fraction
    rate: Fraction
    gop_size: int
    sample_aspect_ratio: Fraction
    display_aspect_ratio: Fraction
    has_b_frames: bool
    coded_width: int
    coded_height: int
    color_range: int
    type: Literal["video"]
