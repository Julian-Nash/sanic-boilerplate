from sanic.views import HTTPMethodView
from sanic.response import text, html
from jinja2 import Environment, PackageLoader, select_autoescape


env = Environment(loader=PackageLoader("app", "templates"), autoescape=select_autoescape(["html", "xml"]))


class BaseHTTPView(HTTPMethodView):
    """ Base handler for all HTTP views """

    def render_template(self, template: str, request, **kwargs) -> html:
        template = env.get_template(template)
        rendered = template.render(request=request, app=request.app, **kwargs)
        return html(rendered)

    @property
    def text(self):
        return text
