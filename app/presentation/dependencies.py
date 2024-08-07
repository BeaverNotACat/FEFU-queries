from app.presentation.interactor_factory import InteractorFactory

from litestar.datastructures import State


async def interactor_dependency(state: State) -> InteractorFactory:
    return getattr(state, "ioc")

