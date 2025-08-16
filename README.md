
# CommandoFreaks

コマンドー（1985年映画）の名台詞をランダムに表示する Django 超小型 PoC（Proof of Concept）アプリです。

## 概要

- Django 5.2.5 + Python 3.12.3 で作成
- POST リクエスト時にランダムな名台詞を表示
- 学習用の小型プロジェクトとして設計

## 環境

- OS: Windows 11 + WSL/Ubuntu
- Python: 3.12.3
- Django: 5.2.5
- mypy: 1.17.1

## セットアップ

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install django mypy
```

## 開発サーバー起動

```bash
python manage.py runserver
```

## 使用方法

- POST リクエストで名台詞をランダム表示
- フォームやボタンは `quotes/templates/quotes/quote.html` に実装

## テスト

```bash
python manage.py test quotes
mypy quotes
```

## 動作イメージ

![Image](https://github.com/user-attachments/assets/9bccfca3-4c25-4533-8067-dbeb9f9d6b12)


## 学習ポイント

- Django のビュー（FBV）とテンプレート連携
- ユニットテスト（TestCase）の基礎
- mypy による型チェック
- シンプルな PoC アプリの構成方法

