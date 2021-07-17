
# フォトモザイクの作り方
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