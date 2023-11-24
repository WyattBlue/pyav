class FilterContext:
    name: str | None

    def init(self, args=None, **kwargs) -> None: ...
    def link_to(self, input_, output_idx: int = 0, input_idx: int = 0) -> None: ...
    def push(self, frame) -> None: ...
