# ベースイメージ（例: Python 3.11）
FROM python:3.11-slim

# 作業ディレクトリを作成
WORKDIR /app

# 依存関係ファイルをコピー（必要なら requirements.txt）
COPY requirements.txt ./

# パッケージインストール（requirements.txtがない場合はスキップ可）
RUN pip install --no-cache-dir -r requirements.txt || true

# ソースコードをコンテナ内にコピー（後述のvolumeマウントでも可）
COPY ./app /app

# デフォルトコマンド
CMD ["python", "main.py"]
