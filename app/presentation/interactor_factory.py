from abc import ABC, abstractmethod
from typing import ContextManager

from app.application.create_form_populations_from_table import (
    CreateFormPopulationsFromTable,
)
from app.application.gateway import UserProvider
from app.application.match_form_population import MatchFormPopulations


class InteractorFactory(ABC):
    @abstractmethod
    async def match_form_populations(
        self, user_provider: UserProvider
    ) -> ContextManager[MatchFormPopulations]:
        raise NotImplementedError

    @abstractmethod
    async def create_form_populations_from_table(
        self,
    ) -> ContextManager[CreateFormPopulationsFromTable]:
        raise NotImplementedError
