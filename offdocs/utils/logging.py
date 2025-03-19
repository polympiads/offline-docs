
from collections import deque


class LoggingWindow:
    def __init__ (self):
        self.lines = 0
    def clear (self):
        print("\033[F" * self.lines, end="")
        self.lines = 0
    def full_clear (self):
        print("\033[F" * self.lines, end="")
        print("\033[K\n" * self.lines, end="")
        print("\033[F" * self.lines, end="")
        self.lines = 0
    def show (self, *args, **kwargs):
        print("\033[K", end="")
        print(*args, **kwargs)
        self.lines += 1
    
    def hide_cursor (self):
        print("\033[?25l", end="")
    def show_cursor (self):
        print("\033[?25h", end="")

class LoggingQueue:
    def __init__(self, size: int):
        self.size  = size
        self.deque = deque()

        self.window = LoggingWindow()
    def clear (self):
        self.deque.clear()
        self.window.clear()
    def full_clear (self):
        self.deque.clear()
        self.window.full_clear()
    def show (self, *args, **kwargs):
        self.deque.append((args, kwargs))
        
        if len(self.deque) <= self.size:
            self.window.show(*args, **kwargs)
            return
        
        while len(self.deque) > self.size:
            self.deque.popleft()
        
        self.window.hide_cursor()
        self.window.clear()

        for _args, _kwargs in self.deque:
            self.window.show(*_args, *_kwargs)
        self.window.show_cursor()
