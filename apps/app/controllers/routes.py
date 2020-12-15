from libs.logger import logger
from controllers import app, templates
from fastapi import Request
from fastapi.responses import HTMLResponse


# helloworld index
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    logger.debug("index ->")

    return templates.TemplateResponse("index.html", {
        "request": request,
        "title": "sample"
    })


# helloworld page
@app.get("/{name}", response_class=HTMLResponse)
async def page(request: Request, name: str):
    logger.debug("page ->")

    return templates.TemplateResponse("page.html", {
        "request": request,
        "title": "sample",
        "name": name
    })
