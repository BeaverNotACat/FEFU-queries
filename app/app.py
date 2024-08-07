from litestar import Litestar
from litestar.config.cors import CORSConfig

from app.presentation.routes import ListFormPopulations
from app.state import ioc_manager

cors_config = CORSConfig(allow_origins=["*"])
app = Litestar(
    cors_config=cors_config,
    lifespan=[ioc_manager],
    route_handlers=[ListFormPopulations],
)
