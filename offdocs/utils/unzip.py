
import time
from offdocs.utils.logging import LoggingQueue

from zipfile import ZipFile

class Unzipper:
    def __init__ (self, zipsrc: str, target: str):
        self.zipsrc = zipsrc
        self.target = target
    
    def do_unzip (self):
        print(f" [+] Unzipping {self.zipsrc} into {self.target}")
        queue = LoggingQueue(8)

        with ZipFile(self.zipsrc, "r") as file:
            infolist = file.infolist()

            for idx, x in enumerate( infolist ):
                file.extract(x, self.target)

                queue.show(f"   [-] ({str(idx).ljust(len(str(len(infolist))))}/{len(infolist)}) Extracting {x.filename}")

        queue.full_clear()
