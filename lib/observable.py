import asyncio
import types

from lib.disposable import Disposable
from lib.observer import Observer
from lib.utils import ObservableTools
from lib import base


class Observable(base.Observable, ObservableTools):
    """
    Every class has to derive from this.
    """
    def __init__(self, on_subscribe=None):
        self.on_subscribe = on_subscribe or self.on_subscribe

    async def on_subscribe(self, observer: base.Observer):
        """
        :param observer:
        :return:
        """
        pass

    def subscribe(self, observer, loop=None) -> Disposable:
        loop = loop or asyncio.get_event_loop()

        if isinstance(observer, (types.FunctionType, types.BuiltinFunctionType)):
            observer = Observer.from_function(observer)

        task = asyncio.ensure_future(self.on_subscribe(observer), loop=loop)
        return Disposable(callback=task.cancel)
