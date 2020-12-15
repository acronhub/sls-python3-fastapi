# AWS Lambda for FastAPI

> Serverless(ApiGateway + Lambda(FastAPI))

## 説明

FastAPIで、Helloworldページを返します

## 必須環境

* [Docker](https://www.docker.com/) をインストール済み

## セットアップ

1. クレデンシャル情報を設置

    ```bash
    cp -a .env.example .env
    vim .env

    以下を書き換えます
    AWS_ACCESS_KEY_ID=XXXXXXXXXXXXXXXXXXXX
    AWS_SECRET_ACCESS_KEY=YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
    ```

2. Dockerイメージの作成

    ```bash
    docker-compose build
    ```

3. パッケージのインストール

    ```bash
    docker-compose run --rm app yarn install
    ```

## ローカルPCで確認

1. Dockerコンテナの起動

    ```bash
    docker-compose up
    ```

2. ブラウザで確認

    ```bash
    http://localhost:8000/hello
    ```

## デプロイ

### ステージング環境

```bash
docker-compose run --rm app yarn run deploy -s dev
```

### 本番環境

```bash
docker-compose run --rm app yarn run deploy -s prod
```

## Author

* acronhub(https://github.com/acronhub)

## ライセンス

[MIT license](https://en.wikipedia.org/wiki/MIT_License).
