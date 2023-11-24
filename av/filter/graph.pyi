from fractions import Fraction

from .context import FilterContext
from .filter import Filter

class Graph:
    def __init__(self): ...
    def configure(self, auto_buffer: bool = True, force: bool = False) -> None: ...
    def add(self, filter: str | Filter, args=None, **kwargs: str) -> FilterContext: ...
    def add_buffer(
        self,
        template=None,
        width: int | None = None,
        height: int | None = None,
        format=None,
        name: str | None = None,
        time_base: Fraction | None = None,
    ) -> FilterContext: ...
    def add_abuffer(
        self,
        template=None,
        sample_rate: int | None = None,
        format=None,
        layout=None,
        channels: int | None = None,
        name: str | None = None,
        time_base: Fraction | None = None,
    ) -> FilterContext: ...
    def push(self, frame) -> None: ...
    def pull(self): ...
