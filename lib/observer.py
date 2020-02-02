class Observer:
    async def on_next(self, value):
        pass

    async def on_error(self, err):
        pass

    async def on_completed(self):
        pass

    @classmethod
    def from_function(cls, f):
        class O(cls):
            async def on_next(self, value):
                f(value)

            async def on_completed(self):
                pass

        return O()
