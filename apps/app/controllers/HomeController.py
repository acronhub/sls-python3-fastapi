from libs.logger import create_logger
from fastapi import Request
from fastapi.responses import HTMLResponse


class HomeController():
    def __init__(self, app, templates):
        logger = create_logger()

        # helloworld index
        @app.get("/", response_class=HTMLResponse)
        async def index(request: Request):
            logger.debug("index ->")

            return templates.TemplateResponse("index.html", {
                "request": request,
                "title": "sample"
            })
