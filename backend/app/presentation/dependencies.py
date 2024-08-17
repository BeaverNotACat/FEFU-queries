from litestar.datastructures import State

from app.presentation.interactor_factory import InteractorFactory


async def interactor_dependency(state: State) -> InteractorFactory:
    return getattr(state, "ioc")
