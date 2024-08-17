from contextlib import asynccontextmanager
from typing import AsyncGenerator

from litestar import Litestar

from app.ioc import IoC


@asynccontextmanager
async def ioc_manager(app: Litestar) -> AsyncGenerator[None, None]:
    interactor = getattr(app.state, "ioc", None)
    if interactor is None:
        app.state.ioc = IoC()
    yield
