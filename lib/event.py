class Event:
    def __init__(self, value):
        self.value = value

    @staticmethod
    def completed():
        return CompletedEvent


class CompletedEvent(Event):
    pass
