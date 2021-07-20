from app.handlers import BaseHTTPView


class IndexView(BaseHTTPView):

    async def get(self, request):
        return self.render_template("index.html", request=request)
