from pathlib import Path
import os

from sanic import Sanic

from app.config import get_config
from app.blueprints import view, ws


def create_app(config_name: str) -> Sanic:
    """ Creates and returns an instance of Sanic """

    config_class = get_config(config_name)

    app = Sanic("Sanic boilerplate with Jinja2 template rendering", config=config_class())

    app.static("/static", os.path.join(Path(__file__).parent.resolve(), "static"), name="static")

    for bp in (view, ws):
        app.blueprint(bp)

    return app
