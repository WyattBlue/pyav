from av.packet import Packet
from av.stream import Stream

from .frame import VideoFrame

class VideoStream(Stream):
    def encode(self, frame: VideoFrame | None = None) -> list[Packet]: ...
    def decode(self, packet: Packet | None = None) -> list[VideoFrame]: ...
