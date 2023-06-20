from ciawf.exception import LightModeNotAllowed


class Graph:
    def __init__(self, dark_mode: bool = True) -> None:
        if not dark_mode:
            raise LightModeNotAllowed()
