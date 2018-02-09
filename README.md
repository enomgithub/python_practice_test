# 概要

Pythonでの単体テストの練習。


## prac_doctest.py

doctest モジュールを用いた単体テストの例


## prac_unittest.py

unittest モジュールを用いた単体テストの例。


## as_unittest_and_doc.ipynb

Jupyter notebook を単体テストを兼ねたドキュメントとしてみた例。


## coverage モジュールを用いたカバレッジの計測例

カバレッジ (コードの網羅率) を簡単に計測できる [coverage](https://coverage.readthedocs.io/en/coverage-4.5/) モジュールでカバレッジを計測した例。
pip 等でインストールする必要がある。

### htmlconv(prac_doctest.py)/index.html

prac_doctest.py をメインモジュールとして実行した際のカバレッジを html 形式でまとめたもの。
コンソールで下記を実行すると作成される (ディレクトリ名は `htmlconv`)。

```
$ coverage run prac_doctest.py
$ coverage html
```


### htmlconv(prac_unittest.py)/index.html

prac_unittest.py をメインモジュールとして実行した際のカバレッジを html 形式でまとめたもの。
コンソールで下記を実行すると作成される (ディレクトリ名は `htmlconv`)。

```
$ coverage run prac_unittest.py
$ coverage html
```
