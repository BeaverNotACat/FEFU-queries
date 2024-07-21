from litestar import Litestar
from litestar.config.cors import CORSConfig


cors_config = CORSConfig(allow_origins=["*"])
app = Litestar(
    cors_config=cors_config,
)
