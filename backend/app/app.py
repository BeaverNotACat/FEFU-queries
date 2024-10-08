from litestar import Litestar
from litestar.config.cors import CORSConfig

from app.presentation.authentication.api import api_auth
from app.presentation.routes import (Authentication, CreateFormPopulations,
                                     ListFormPopulations)
from app.state import ioc_manager

cors_config = CORSConfig(allow_origins=["*"])
app = Litestar(
    cors_config=cors_config,
    lifespan=[ioc_manager],
    on_app_init=[api_auth.on_app_init],
    route_handlers=[ListFormPopulations, CreateFormPopulations, Authentication],
)
