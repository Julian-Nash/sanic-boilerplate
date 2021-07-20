from sanic import Blueprint

from .feed import feed

ws = Blueprint("ws", url_prefix="/ws")

ws.add_websocket_route(feed, "/feed", name="feed")
