from lib.subject import Subject


def first():

    class S(Subject.proxy()):
        async def queue_value(self, value):
            await super().queue_value(value)

    return S()