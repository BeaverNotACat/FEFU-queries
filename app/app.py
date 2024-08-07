from pathlib import Path

from litestar import Litestar
from litestar.config.cors import CORSConfig
from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.template import TemplateConfig

from app.presentation.routes import ListFormPopulations
from app.state import ioc_manager


cors_config = CORSConfig(allow_origins=["*"])
app = Litestar(
    cors_config=cors_config,
    template_config=TemplateConfig(
        directory=Path(__file__).parent / "templates",
        engine=JinjaTemplateEngine,
    ),
    lifespan=[ioc_manager],
    route_handlers=[ListFormPopulations],
)
