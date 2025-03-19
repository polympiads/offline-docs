from shutil import copytree

class Copy:
    def __init__ (self, src: str, target: str, exists_ok: bool = False):
        self.src, self.tar = src, target
        self.exists_ok = exists_ok
    def do_copy (self):
        print(f" [+] Attempting copy from {self.src} to {self.tar}")
        copytree(self.src, self.tar, dirs_exist_ok=self.exists_ok)