class Observer:
    async def on_next(self, value):
        pass

    async def on_error(self, err):
        pass

    async def on_completed(self):
        pass

    @staticmethod
    def from_function(f):
        class O(Observer):
            async def on_next(self, value):
                f(value)

            async def on_completed(self):
                pass

        return O()
