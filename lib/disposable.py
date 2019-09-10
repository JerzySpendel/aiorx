class Disposable:
    def __init__(self, callback):
        self.callback = callback

    def dispose(self):
        self.callback()

    @classmethod
    def dummy(cls):
        return cls(callback=lambda: print('disposed'))