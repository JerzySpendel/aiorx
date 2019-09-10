class Action:
    def __init__(self, value=None):
        self.value = value

    @staticmethod
    def completed():
        return CompletedAction


class CompletedAction(Action):
    pass
