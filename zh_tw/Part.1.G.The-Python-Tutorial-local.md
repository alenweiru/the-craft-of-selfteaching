
# 官方教程：The Python Tutorial

雖然，第一部分總計七章關於編程內容的編排是非常特別且相當有效的：

> * 它並沒有像其它教程那樣，從 “Hello world!” 入手；
> * 它也沒有使用與市面上所有編程教材一樣的內容先後順序；
> * 它一上來就讓你明白了程序的靈魂：布爾運算；
> * 它很快就讓你明白有意義的程序其實只有兩個核心構成：運算和流程控制；
> * 它讓你很快理解函數從另外一個角度看只不過是 “程序員作為用戶所使用的產品”；
> * 它讓你重點掌握了最初級卻最重要的數據類型，字符串；
> * 它讓你從容器的角度瞭解了 Python 中絕大多數 “重要的數據類型”；
> * 最重要的是，它不承諾你 “速成”，但承諾 “領你入門”…… 顯然，它做到了。

但是，第一部分的內容核心目標是讓你 “**脫盲**” —— 它的作用還做不到讓你 “已然學會編程”，它更多是讓你從此開始有能力去閱讀更多的重要資源，比如，官方的教程和參考。第一部分的內容更像地圖上的 “**圖例**”，而不是地圖本身。

第一部分反覆讀過之後，最重要的結果就是：

> 現在你有能力自己查詢官方文檔了……

起碼，在此之後，再去閱讀 [The Python Tutorial](https://docs.python.org/3/tutorial/index.html)，不那麼費力了，最起碼，可以靠自己理解絕大多數內容……

在繼續閱讀本書內容的同時，有空就要反覆翻 The Python Tutorial。

## 官方文檔中最重要的鏈接

Python 也許是目前所有編程語言中在文檔建設（Documenting）方面做得最好的（好像真的不需要在這句話後面加上 “之一”）。Python 社區為了建設完善的文檔，甚至有專門的文檔製作工具 —— 得益於 Python 社區從一開始就非常重視[文檔規範](https://devguide.python.org/documenting/) —— [Sphinx](http://www.sphinx-doc.org/en/master/)。你在網絡上最經常看到的計算機類文檔，很可能都在這個網站上：[Read the Docs](https://readthedocs.org)……

Python 的官方文檔網址是：

> https://docs.python.org/3/

其中對初學者最重要的兩個鏈接是：

> * **[Tutorial](https://docs.python.org/3/tutorial/index.html)**: https://docs.python.org/3/tutorial/index.html
> * **[Library Reference](https://docs.python.org/3/library/index.html)**: https://docs.python.org/3/library/index.html

理論上來講，只要有了基礎的概念，自己反覆閱讀官方的 The Python Tutorial 是最好的，沒什麼入門書籍比它更好 —— 因為它的作者是 Python 的作者，那個被稱為 “善意獨裁者” 的 [Guido van Rossum](https://en.wikipedia.org/wiki/Guido_van_Rossum)。

此人很帥，但更帥的是他的車牌（摘自 Guido van Rossume 的[個人主頁](https://gvanrossum.github.io)）：

![](https://gvanrossum.github.io/images/license.jpg)

## 為什麼一定要閱讀官方文檔

買一兩本 Python 教程是不可能完整掌握 Python 的 —— 其實，這句話里的 Python 替換成任何一種語言也是一樣的。

教程和官方文檔的各種屬性是非常不一樣的，比如，針對讀者群，組織方式，語言表達…… 最不一樣的地方在 “全面性”。任何一本單獨的教程，都不可能像官方文檔那樣全面。各種單獨教程的優勢在於，它們更多地針對初學者、入門者設計，但與此同時，在全面性、深入性上做了妥協。

比如，在當前這本書里，不會涉及 [Bytes Object](https://docs.python.org/3/library/stdtypes.html#bytes-objects) —— 並非只有我一個人這麼做，著名的 Python 教程《[Think Python: How to Think Like a Computer Scientist](http://greenteapress.com/thinkpython2/html/index.html)》、《[Dive into Python](https://linux.die.net/diveintopython/html/toc/index.html)》等等都沒有涉及 Bytes Object 這個話題。

由於官方文檔實際上沒辦法對入門者、初學者過分友好 —— 畢竟，全面、權威、準確才是它更應該做到的事情 —— 所以，很多人在剛開始的時候求助於各類非官方的教材、教程。原本應該是入門以後就理應 “只讀官方文檔”，或者 “第一查詢對象只能是官方文檔”，但在很多人那裡竟然變成了 “從一開始到最後都在迴避官方文檔（或者說 ‘最專業的說明文字’），這就不好了，真的很吃虧，且自己都無法知道自己究竟吃了多少虧 —— 總以為自己已經學完了，但實際上從一開始就一點都不全面。

請牢記且遵守這個原則：

> **第一查詢對象只能是官方文檔**。

所以，當我用 Google 查詢的時候，經常使用這樣的格式：

> `<querries> site:python.org`

有時甚至會指定在那個目錄里搜索：
    
> `bytes site:python.org/3/library`，你試試這個連接：[bytes site:python.org/3/library](https://www.google.com/search?q=byte+site%3Apython.org%2F3%2Flibrary) 

這個原則對任何語言都適用。將來你在學習任何新軟件包（庫）、語言更新後的新特性、甚至另外一個新語言的時候，都要這麼做。所謂的超強自學能力，基本上就是由一些類似這樣的小習慣和另外一些特別基礎的方法構成的強大能力。

## 將官方文檔拉回本地

把 The Python Tutorial 拉回本地閱讀，可能更為方便，尤其是可以用 Sphinx 重新製作之後，頁面左側可以總是顯示完整的目錄：

![](../images/local-tutorial.png)

也可以把這個教程轉換成 epub 格式，以便在移動設備上閱讀；甚至可以把這些個頁面的 `.rst` 源文件轉換成 `.ipynb` 文件，以便用 Jupyter Lab 瀏覽時可以直接執行其中的代碼……

**註意**

> 此頁的 Code Cell 中都是可執行的 bash 命令……

在此頁執行它們對你來說是沒意義的 —— 因為它們的執行結果在服務器上；這其中的命令，應該在你本地計算機上的 Terminal 中執行，你才能在本地計算機上獲取結果。

### 安裝 git
```bash
%%bash
which git
git --version

# 沒有的話就執行以下命令安裝 git
# conda install -c anaconda git
```
### 下載源文件

The Python Tutorial 的源文件位置在：

> https://github.com/python/cpython/tree/master/Doc/tutorial

repo 地址是：

> https://github.com/python/cpython.git

使用 git 將 repo 下載到 `~/Download/` 目錄：
```bash
%%bash
cd ~/Downloads
# 總計 241 M，所以需要一點時間
git clone https://github.com/python/cpython.git
cd cpython/Doc/tutorial
ls
```
### 安裝 rst2ipynb
```bash
%%bash
# rst2ipynb needs pandoc and notedown...
which pandoc
which notedown
# 沒有這兩樣東西的話，需要執行下麵兩行進行安裝……
# conda install -c conda-forge pandoc
# conda install -c conda-forge notedown

# install rst2ipynb
cd ~/Downloads
git clone https://github.com/nthiery/rst-to-ipynb.git
cd rst-to-ipynb
pip install .
which rst2ipynb
```
### 批量轉換 rst 至 ipynb

這個 rst2ipynb 的程序有點討厭，一次只能處理一個文件…… 下麵是一個 bash 程序，其實將來學起來也不難，看著跟 Python 差不多…… 下麵的代碼執行過後會出現很多 “警告” —— 沒關係，文件會正常轉換的。
```bash
%%bash
cd ~/Downloads/cpython/Doc/tutorial/ 
for f in *.rst
    do
        rst2ipynb $f -o "${f/%.rst/.ipynb}"
    done
mkdir ipynbs
mv *.ipynb ipynbs/
```
如此這般，你就把 rst 文件都轉換成 ipynb 文件，保存在 `~/Downloads/cpython/Doc/tutorial/ipynbs/` 之中了。隨便把它挪到你喜歡的什麼地方。用本地的 Jupyterlab 瀏覽，或者用 [Nteract](https://nteract.io) App 瀏覽。

如果以後你經常需要批量轉換某個目錄內的 `rst` 文件，那就把 bash function 放在 `~/.bash_profile` 文件里，在最後面追加以下代碼：
```bash
function rsti {
    for f in *.rst
    do
    rst2ipynb $f -o "${f/%.rst/.ipynb}"
    done
}
```
而後在 Terminal 里執行一遍：
```bash
source ~/.bash_profile
```
而後，在有 `.rst` 文件的目錄下輸入 `rsti` 執行即可……

### 用 Sphinx 生成 html/epub 版本
```bash
%%bash 
which sphinx-quickstart
# 沒有的話就執行下一行：
# conda install -c anaconda sphinx
sphinx-quickstart --version
sphinx-quickstart --help
```
生成 html 版本和 epub 版本：
```bash
%%bash
cd ~/Downloads/cpython/Doc/tutorial/ 
sphinx-quickstart -q output --sep -p 'The Python Tutorial' -a 'Guido van Rossum' -r '1.0' -v '1.0' -l 'en' --suffix '.rst' --master 'index' --ext-autodoc --ext-doctest --ext-intersphinx --ext-todo --ext-coverage --ext-imgmath --ext-mathjax --ext-ifconfig --ext-viewcode --makefile --no-batchfile --no-use-make-mode
cp -f *.rst output/source/
cd output
make html
make epub

# 生成的 html 版本應該在 output/build/html 目錄下；
# 生成的 epub 版本應該在 output/build/epub 目錄下。

# sphinx-quickstart -q output \
# --sep \
# -p 'The Python Tutorial' \
# -a 'Guido van Rossum' \
# -v '1.0'
# -r '1.0' \
# -l 'en' \
# --suffix '.rst' \
# --master 'index' \
# --ext-autodoc \
# --ext-doctest \
# --ext-intersphinx \
# --ext-todo \
# --ext-coverage \
# --ext-imgmath \
# --ext-mathjax \
# --ext-ifconfig \
# --ext-viewcode \
# --makefile \
# --no-batchfile \
# --no-use-make-mode
```
用 Sphinx 這樣生成的版本，支持本地目錄內搜索，也確實比在網站上看更方便一點：

![](../images/search-generated-by-sphinx.png)

### 下載已經轉換好的版本

萬一有什麼情況中間出錯又搞不定的話，就直接下載已經轉換好的版本：
```bash
%%bash
cd ~/Downloads
git clone https://github.com/xiaolai/the-python-tutorial-in-other-formats.git
```
### 完整的 Python Doc 製作

其實，Python 的整個文檔，已經是做好了製作文件的文檔庫：

> `cpython/Doc/Makefile`

只不過，將所有文件編譯到一個 epub 里，在 iPad 之類的移動設備上打開有點費勁 —— 在我的設備上顯示有 7701 頁，翻頁都要頓一頓……

想要使用這個官方的 `Makefile` 的話，首先確認自己已經安裝過 Sphinx，其次需要補充安裝一個包：
```bash
pip install blurb
```
而後在 Terminal 中轉到 Doc 所在目錄，執行以下命令：
```bash
make html
make epub
```
