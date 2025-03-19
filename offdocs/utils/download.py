
import urllib
import urllib.request

from offdocs.utils.progress import ProgressBar

class DownloadProgressBar(ProgressBar):
    def __call__(self, block_num, block_size, total_size):
        self.set_value( block_num * block_size, total_size )

class Download:
    def __init__ (self, url: str, storage: str):
        self.url = url
        self.storage = storage

        self.pbar = DownloadProgressBar()

    def do_download (self):
        print(f" [+] Starting download of {self.url}")
        print(f" [+] Opening storage at {self.storage}")
        urllib.request.urlretrieve( self.url, self.storage, self.pbar )
