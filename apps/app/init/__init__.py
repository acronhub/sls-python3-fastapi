import os
from init.Routing import register_routes
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


def create_app():
    env = os.getenv("ENV", "local")

    # FastAPI application
    app = FastAPI(
        title='Sample',
        description='HTMLページ',
        version='0.1',
        docs_url="/docs" if env != 'prod' else None,
        redoc_url="/redoc" if env != 'prod' else None,
    )

    # 開発環境のみ
    if env == 'local':
        app.mount("/static", StaticFiles(directory="static"), name="static")

    register_routes(app)

    return app
