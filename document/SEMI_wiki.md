# B3ゼミWiki

<details>
<summary> <b>目次をクリックで展開</b> </summary>
<div>

+ [講義資料の開発環境について](#anchor1)

+ [環境構築について](#anchor2)

+ [Markdownの記述について](#anchor3)

+ [TeXの記述について](#anchor4)
</dev>
</details>

<a id="anchor1"></a>

## 講義資料の開発環境について

開発環境は以下のとおりです。

| 使用環境 |  |
|------|-----|
|CPU |Intel(R) Core(TM) i7-1165G7 @ 2.80GHz   2.80 GHz|
|メモリ|16.00GB|
|OS|Windows 11 (10) |
|使用言語| Python 3|

<a id="anchor2"></a>

## 環境構築について

想定する環境構築の流れを大雑把に説明するので、あくまで参考程度にお願いします。

VSCodeのインストール\[[2]\]を行ないます。完了している方は飛ばしてください。

[2]: https://code.visualstudio.com/download


インストールが完了したら、VSCodeを開きます。

講義資料をcloneします。
```
$ git clone https://github.com/SajiLab/2024B3semi.git
```

これでゼミ用の環境構築は終了です。

最後に動作をテストします。
cloneしたフォルダを開き、main.pyを選択してください。
ターミナルに以下を入力して
```
$ python main.py 
```

"Hello, World"がターミナルに出力されればOKです。

<a id="anchor3"></a>

## Markdownの記述について

Markdownの記述で使いやすそうなqiitaの記事です．リンク切れてたらすみません．

[リンク1](https://qiita.com/toyokky/items/47a5a56c20ad99e1784c)

[リンク2](https://qiita.com/kamorits/items/6f342da395ad57468ae3)

<a id="anchor4"></a>

## Texでの記述について
ローカルでの環境構築が面倒な場合はオンラインエディタでの作成をおすすめしています．
OverleafやCloudLaTeX等でアカウント作成して使用してください．

特にCloudLaTeXはローカルのVisualStudioCodeにオンライン上の編集データをダウンロードして使用できます．環境構築等はググってみてください．

Texでのレポート作成時にまた説明します。

