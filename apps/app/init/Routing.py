from fastapi.templating import Jinja2Templates


def register_routes(app):
    # テンプレートフォルダ読み込み
    templates = Jinja2Templates(directory="templates")

    from controllers.HomeController import HomeController
    HomeController(app, templates)

    from controllers.PageController import PageController
    PageController(app, templates)
