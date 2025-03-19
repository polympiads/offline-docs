
import os
import time
import argparse
from typing import List

from offdocs.language.base import BaseLanguage
from offdocs.language.python import PythonLanguage
from offdocs.utils.copy import Copy
from offdocs.utils.download import Download
from offdocs.utils.progress import ProgressBar
from offdocs.utils.unzip import Unzipper

import json

def main ():
    parser = argparse.ArgumentParser("offdocs", description="Offline Documentation Builder")
    parser.add_argument("config")
    
    args = parser.parse_args()

    with open(args.config) as file:
        conf = json.loads(file.read())

    langs: List[BaseLanguage] = []
    for data in conf:
        target = data["target"]
        path   = data["path"]

        if target == "Python":
            langs.append( PythonLanguage( path, data["version"] ) )

    def _mkdir (path: str):
        if os.path.exists(path): return
        os.mkdir(path)
    
    _mkdir("./_build")
    _mkdir("./_build/_cache")
    _mkdir("./_build/_static")
    for lang in langs:
        _mkdir(f"./_build/_cache/{lang.cache}")
    
    for lang in langs:
        lang.build()

if __name__ == "__main__":
    main()
