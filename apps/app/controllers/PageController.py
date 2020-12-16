from libs.logger import create_logger
from fastapi import Request
from fastapi.responses import HTMLResponse


class PageController():
    def __init__(self, app, templates):
        logger = create_logger()

        # helloworld page
        @app.get("/{name}", response_class=HTMLResponse)
        async def page(request: Request, name: str):
            logger.debug("page ->")

            return templates.TemplateResponse("page.html", {
                "request": request,
                "title": "sample",
                "name": name
            })
