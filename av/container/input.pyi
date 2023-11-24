from .core import Container
from .streams import Stream

class InputContainer(Container):
    bit_rate: int
    size: int

    def demux(self, *args, **kwargs): ...
    def decode(self, *args, **kwargs): ...
    def seek(
        self,
        offset: int,
        *,
        whence: str = "time",
        backward: bool = True,
        any_frame: bool = False,
        stream: Stream | None = None,
        unsupported_frame_offset: bool = False,
        unsupported_byte_offset: bool = False,
    ) -> None: ...
