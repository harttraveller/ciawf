class Interface:
    def __init__(self, cache_refresh_period_seconds: int = 86_400) -> None:
        self.__crps = cache_refresh_period_seconds
        self.__cache: dict = dict()

    def get_state_names(self):
        pass

    def get_state_codes(self):
        pass

    def get_state_name_code_pairs(self):
        pass
