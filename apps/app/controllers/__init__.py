import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# テンプレートフォルダ読み込み
templates = Jinja2Templates(directory="templates")

# 定数 環境変数
ENV = os.getenv("ENV", "local")

# FastAPI application
app = FastAPI(
    title='Sample',
    description='HTMLページ',
    version='0.1',
    docs_url="/docs" if ENV != 'prod' else None,
    redoc_url="/redoc" if ENV != 'prod' else None,
)

# 開発環境のみ
if ENV == 'local':
    app.mount("/static", StaticFiles(directory="static"), name="static")
