class LightModeNotAllowed(Exception):
    """
    Exception raised when user tries to use light mode on graph.
    """

    def __init__(self):
        self.message = "Light mode? You call yourself a programmer?"
        super().__init__(self.message)
