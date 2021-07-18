
# フォトモザイクの作り方
![capture2](https://user-images.githubusercontent.com/58985013/126052510-f43b0329-752d-4dd0-837c-07e9b1d5c6f5.jpg)

https://youtu.be/plWa7k7WG_I


東海オンエアのサムネイル画像を使ってヒカキンの画像を作ります。

## 東海オンエアのサムネイル画像を用意

youtubeのWebページからのスクレイピングが難しそう。

```
$$("#video-title").map(function(e){
  return e.href;
});
```
なのでChrome Developer ToolのconsoleからJavascriptを用いて取得。

このVideo IDをテキストファイルにいったん保存しておく。

## ヒカキンの画像を用意
こちらのサイトを使います。

https://html-css-javascript.com/youtube-thumb/


## フォトモザイクのプログラムを用意

https://github.com/codebox/mosaic


## プログラムを実行
フォトモザイク画像を作成します

# 注意

このレポジトリには東海オンエアとヒカキンの画像はアップロードしていません。自分でダウンロードして追加してください。
