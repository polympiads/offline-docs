
import os
from offdocs.language.base import BaseLanguage
from offdocs.utils.copy import Copy
from offdocs.utils.download import Download
from offdocs.utils.unzip import Unzipper


class PythonLanguage(BaseLanguage):
    def __init__(self, name: str, version: str):
        super().__init__(name)
        
        self.major, self.minor = list(map(int, version.split(".")))

    @property
    def cache (self):
        return f"_py_{self.major}_{self.minor}"
    @property
    def version (self):
        return f"{self.major}.{self.minor}"
    
    @property
    def archive_target (self):
        return f"https://docs.python.org/{self.major}/archives/python-{self.version}-docs-html.zip"
    def build(self):
        print(f" [+] Building documentation for Python {self.major}.{self.minor}")

        cached_zip      = self.get_cache_file("cache.zip")
        cached_unzipped = self.get_cache_file("unzipped")

        cached_target = self.get_cache_file(f"unzipped/python-{self.version}-docs-html")
        static_target = self.get_static_file()

        if not os.path.exists(cached_zip):
            bar = Download("https://docs.python.org/3/archives/python-3.13-docs-html.zip", self.get_cache_file("cache.zip"))
            bar.do_download()
        else:
            print(f" [+] Using cached file {cached_zip}")

        if not os.path.exists(cached_unzipped):
            zip = Unzipper(self.get_cache_file("cache.zip"), self.get_cache_file("unzipped"))
            zip.do_unzip()
        else:
            print(f" [+] Using cached folder {cached_unzipped}")

        if not os.path.exists(static_target):
            copy = Copy( self.get_cache_file(f"unzipped/python-{self.version}-docs-html"), "_build/_static/python", True )
            copy.do_copy()
        else:
            print(f" [+] Target is already ready at {static_target}")