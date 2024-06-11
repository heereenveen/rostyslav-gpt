from aiogram import BaseMiddleware
from aiogram.types import Message
from typing import Callable, Dict, Any, Awaitable
from cachetools import TTLCache


class ThrottlingMiddleware(BaseMiddleware):
    def __init__(self, limit: int=2):
        self.limit = TTLCache(maxsize=10_000, ttl=limit)

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]], 
        event: Message, 
        data: Dict[str, Any]
        ) -> Any:
            if event.chat.id in self.limit:
                 return
            else:
                 self.limit[event.chat.id] = None
            return await handler(event, data)