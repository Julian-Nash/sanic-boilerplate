from sanic import Blueprint

from .index import IndexView

view = Blueprint("view")

view.add_route(IndexView.as_view(), "/", name="index")
