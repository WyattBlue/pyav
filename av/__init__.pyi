from typing import overload, Literal, Any, Iterator
from numbers import Real
from pathlib import Path
from fractions import Fraction

class FFmpegError(Exception):
    def __init__(self, code, message, filename=None, log=None): ...


class Codec:
    name: str
    mode: Literal["r", "w"]

    frame_rates: list[Fraction] | None
    audio_rates: list[int] | None


class CodecContext:
    extradata_size: bool
    is_open: bool
    is_encoder: bool
    is_decoder: bool

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
    def __getitem__(self, index: int | slice) -> Stream | list[Stream]: ...
    def get(
        self,
        *args: int | Stream | dict[str, int | tuple[int, ...]],
        **kwargs: int | tuple[int, ...]
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
    metadata: dict[str, str]
    open_timeout: Real | None
    read_timeout: Real | None

    def err_check(self, value: int) -> int: ...
    def set_timeout(self, timeout: Real | None) -> None: ...
    def start_timeout(self) -> None: ...

class InputContainer(Container): ...

class OutputContainer(Container):
    def start_encoding(self) -> None: ...

@overload
def open(
    file: Any,
    mode: Literal["r"] = None,
    format: str | None = None,
    options: dict[str, str] | None = None,
    container_options: dict[str, str] | None = None,
    stream_options: list[str] | None = None,
    metadata_encoding: str = "utf-8",
    metadata_errors: str = "strict",
    buffer_size: int = 32768,
    timeout=Real | None | tuple[Real | None, Real | None],
    io_open=None,
) -> InputContainer: ...
@overload
def open(
    file: str | Path,
    mode: Literal["r"] | None = None,
    format: str | None = None,
    options: dict[str, str] | None = None,
    container_options: dict[str, str] | None = None,
    stream_options: list[str] | None = None,
    metadata_encoding: str = "utf-8",
    metadata_errors: str = "strict",
    buffer_size: int = 32768,
    timeout=Real | None | tuple[Real | None, Real | None],
    io_open=None,
) -> InputContainer: ...
@overload
def open(
    file: Any,
    mode: Literal["w"],
    format: str | None = None,
    options: dict[str, str] | None = None,
    container_options: dict[str, str] | None = None,
    stream_options: list[str] | None = None,
    metadata_encoding: str = "utf-8",
    metadata_errors: str = "strict",
    buffer_size: int = 32768,
    timeout=Real | None | tuple[Real | None, Real | None],
    io_open=None,
) -> OutputContainer: ...
def open(
    file: Any,
    mode: Literal["r", "w"] | None = None,
    format: str | None = None,
    options: dict[str, str] | None = None,
    container_options: dict[str, str] | None = None,
    stream_options: list[str] | None = None,
    metadata_encoding: str = "utf-8",
    metadata_errors: str = "strict",
    buffer_size: int = 32768,
    timeout=Real | None | tuple[Real | None, Real | None],
    io_open=None,
) -> InputContainer | OutputContainer: ...
