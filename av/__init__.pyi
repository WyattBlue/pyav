from fractions import Fraction
from numbers import Real
from pathlib import Path
from typing import Any, Iterator, Literal, overload

from av import error, logging

class Codec:
    name: str
    mode: Literal["r", "w"]

    frame_rates: list[Fraction] | None
    audio_rates: list[int] | None

class CodecContext:
    name: str
    bit_rate: int | None
    width: int
    height: int
    pix_fmt: str | None
    sample_aspect_ratio: Fraction | None
    sample_rate: int | None
    channels: int
    extradata_size: int
    is_open: Literal[0, 1]
    is_encoder: Literal[0, 1]
    is_decoder: Literal[0, 1]

class Stream:
    thread_type: Literal["NONE", "FRAME", "SLICE", "AUTO"]

    id: int
    profile: str | None
    codec_context: CodecContext

    index: int
    time_base: Fraction | None
    average_rate: Fraction | None
    base_rate: Fraction | None
    guessed_rate: Fraction | None

    start_time: int | None
    duration: int | None
    frames: int
    language: str | None

    # Defined by `av_get_media_type_string` at
    # https://ffmpeg.org/doxygen/6.0/libavutil_2utils_8c_source.html
    type: Literal["video", "audio", "data", "subtitle", "attachment"]

    # From `codec_context`
    name: str
    bit_rate: int | None
    width: int
    height: int
    pix_fmt: str | None
    sample_aspect_ratio: Fraction | None
    sample_rate: int | None
    channels: int
    extradata_size: int
    is_open: Literal[0, 1]
    is_encoder: Literal[0, 1]
    is_decoder: Literal[0, 1]

    def decode(self, packet=None): ...
    def encode(self, frame=None): ...

class ContainerFormat: ...

class StreamContainer:
    video: tuple[Stream, ...]
    audio: tuple[Stream, ...]
    subtitles: tuple[Stream, ...]
    data: tuple[Stream, ...]
    other: tuple[Stream, ...]

    def __init__(self) -> None: ...
    def add_stream(self, stream: Stream) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[Stream]: ...
    @overload
    def __getitem__(self, index: int) -> Stream: ...
    @overload
    def __getitem__(self, index: slice) -> list[Stream]: ...
    @overload
    def __getitem__(self, index: int | slice) -> Stream | list[Stream]: ...
    def get(
        self,
        *args: int | Stream | dict[str, int | tuple[int, ...]],
        **kwargs: int | tuple[int, ...],
    ) -> list[Stream]: ...

class Container:
    writeable: bool
    name: str
    metadata_encoding: str
    metadata_errors: str
    file: Any
    buffer_size: int
    input_was_opened: bool
    io_open: Any
    open_files: Any
    format: ContainerFormat
    options: dict[str, str]
    container_options: dict[str, str]
    stream_options: list[str]
    streams: StreamContainer
    duration: int | None
    metadata: dict[str, str]
    open_timeout: Real | None
    read_timeout: Real | None

    def __enter__(self) -> Container: ...
    def __exit__(self, exc_type, exc_val, exc_tb): ...
    def err_check(self, value: int) -> int: ...
    def set_timeout(self, timeout: Real | None) -> None: ...
    def start_timeout(self) -> None: ...

class InputContainer(Container):
    bit_rate: int
    size: int

    def demux(self, *args, **kwargs): ...
    def decode(self, *args, **kwargs): ...

class OutputContainer(Container):
    def start_encoding(self) -> None: ...
