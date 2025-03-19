
import os


class BaseLanguage:
    def __init__ (self, name: str):
        self.name = name

    @property
    def cache (self):
        raise NotImplementedError()

    def get_static_file (self, name: str = None):
        if name is None:
            return os.path.join("./_build/_static", self.name)
        return os.path.join("./_build/_static", self.name, name)    
    def get_cache_file (self, name: str):
        return os.path.join("./_build/_cache", self.cache, name)
    def build (self):
        raise NotImplementedError()
