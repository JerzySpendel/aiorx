from lib.subject import Subject


def first():

    class S(Subject.proxy()):
        async def queue_value(self, value):
            await super().proxy(value)

    return S()