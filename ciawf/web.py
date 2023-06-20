from ciawf.urls import COUNTRIES


class Interface:
    def __init__(self, cache_refresh_period_seconds: int = 86_400) -> None:
        self.__crps = cache_refresh_period_seconds
        self.__cache: dict = dict()

    @property
    def cache(self) -> dict[str, str]:
        return self.__cache

    def check(self, key: str) -> bool:
        return key in self.cache.keys()

    def get_state_names(self):
        pass

    def get_state_codes(self):
        pass

    def get_state_name_code_pairs(self):
        pass
