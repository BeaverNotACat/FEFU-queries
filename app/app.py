from pathlib import Path

from litestar import Litestar
from litestar.config.cors import CORSConfig
from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.template import TemplateConfig

cors_config = CORSConfig(allow_origins=["*"])
app = Litestar(
    cors_config=cors_config,
    template_config=TemplateConfig(
        directory=Path("templates"),
        engine=JinjaTemplateEngine,
    ),
)
