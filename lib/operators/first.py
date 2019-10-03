from lib.action import Action
from lib.subject import Subject


def first():

    class S(Subject.proxy()):
        async def queue_value(self, value):
            await super().queue_value(value)
            await super().queue_value(Action.completed())

    return S()