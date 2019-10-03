import asyncio
import types

from lib.disposable import Disposable
from lib.observer import Observer
from lib.utils import ObservableTools
from lib import base


class Observable(base.Observable, ObservableTools):
    def __init__(self, on_subscribe=None):
        self.on_subscribe = on_subscribe or self.on_subscribe

    async def on_subscribe(self, observer: base.Observer):
        pass

    def subscribe(self, observer) -> Disposable:
        if isinstance(observer, types.FunctionType) or isinstance(observer, types.BuiltinFunctionType):
            observer = Observer.from_function(observer)

        task = asyncio.ensure_future(self.on_subscribe(observer))
        return Disposable(callback=task.cancel)

