# ベースイメージを指定
FROM python:3.9-slim-buster

# 作業ディレクトリを作成
WORKDIR /app

# requirements.txtからパッケージをインストール
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# アプリケーションのソースコードをコピー
COPY . .

# 実行するコマンドを指定
CMD ["python", "janken.py"]