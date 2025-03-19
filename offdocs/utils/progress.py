
import progressbar

class ProgressBar:
    def __init__ (self):
        self.pbar = None
    
    def set_value (self, value: int, max_value: int = 1):
        if self.pbar is None:
            self.pbar = progressbar.ProgressBar( max_value = max_value )
            self.pbar.start()
        
        if value < max_value:
            self.pbar.update(value)
        else:
            self.pbar.finish()
