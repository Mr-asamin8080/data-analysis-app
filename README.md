# data-analysis-app

## 概要
CSVファイルからデータを取得し、elasticsearchに登録する。
登録されているデータをkibanaで可視化する。

## 使い方
1.Dockerコンテナ起動する
```
# docker-compose up
```
2.ブラウザにてデータ登録画面にアクセスする
```
http://localhost:5000
```
3.登録したいデータを含んだCSVファイルを洗濯して送信する
