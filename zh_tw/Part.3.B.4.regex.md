
# 正則表達式

正則表達式本質上是個獨立的語言，短小卻格外強悍 —— 乃至於，如果你竟然沒學會它的話，你的之前學的編程技能幹脆與殘疾無異。

Wikipedia 上對正則表達式的說明如下：

> **正則表達式**（英語：Regular Expression，在代碼中常簡寫為 regex、regexp 或 RE），又稱_正規表示式_、_正規表示法_、_正規運算式_、_規則運算式_、_常規表示法_，是計算機科學的一個概念。正則表達式使用單個字符串來描述、匹配一系列符合某個句法規則的字符串。在很多文本編輯器里，正則表達式通常被用來檢索、替換那些符合某個模式的文本。許多程序設計語言都支持利用正則表達式進行字符串操作。例如，在 Perl 中就內建了一個功能強大的正則表達式引擎。正則表達式這個概念最初是由 Unix 中的工具軟件（例如 sed 和 grep）普及開的。

以下是絕大多數翻譯成中文的教程中對正則表達式進行講解時所使用的描述：

> 一個正則表達式（Regular Expression）通常被稱為一個模式（Pattern）。

我常常覺得當初要是它被翻譯成 “規則表達式”，那麼很可能初學者不會感到那麼大的壓力 —— 誰都一樣，看著由 “每個都認識的字構成的詞組” 卻不能直觀地想到它究竟是什麼東西，都會感到莫名的壓力。

**Regular**，其實在它的眾多語義中，取以下釋義最符合 Regular Expression 的原意<a href='#fn1' name='fn1b'><sup>[1]</sup></a>：

> ⑭ Linguistics 規則的 ▸ regular verbs 規則動詞

而 **Pattern** 這個詞，在詞典里有好幾個對應的中文詞彙：

> ① 圖案；② 式樣；③ 圖樣；④ 榜樣；⑤ 模式；⑥ 樣品；⑦ 模子

在當前語境之下，把 Pattern 翻譯成 “模式”，顯然不如 “模子” 更好（甚至連 “樣品” 感覺都比 “模式” 更恰當）—— “模子” 這個詞很直觀啊，拿著一個模子去找與它一致的字符串…… “與規則一致”，英文用的是 **Match**，一般被翻譯作 “匹配”。

在自學編程的過程中，處處都是這種語言翻譯帶來的迷惑、障礙，或者耽誤。既然應該把 Regular Expression 理解為 “規則表達式” 更好，那其實吧，把 Pattern 直接理解為中文的 “*規則*”，可能更直觀更準確，理解上更是毫無障礙：

> 一個規則表達式（Regular Expression）通常被稱為一個規則（Pattern）。

那麼，**規則表達式**里寫的是什麼呢？只能是**規則**了…… 到最後好像也就 “捕獲”（Capture）這個詞沒什麼歧義。

現在，我們已經把術語全部 “解密” 了，然後再看看下麵的表述：

> 我們可以用書寫特定的規則，用來在文本中捕獲與規則一致的字符串，而後對其進行操作……

理解起來相當順暢。

以下的 Python 代碼中，[`\wo\w`](https://regexper.com#%5Cwo%5Cw) 就是一個_規則表達式_（或稱為_規則_）；

而 `re.findall(pttn, str)` 的作用就是，在 `str` 里找到所有與這個**規則**（Pattern，模式）**一致**（Match，匹配）的字符串：
```python
import re
str = 'The quick brown fox jumps over the lazy dog'
pttn = re.compile(r'\wo\w')
re.findall(pttn, str)
```
    ['row', 'fox', 'dog']



總結一下：

> **規則表達式**（Regular Expressions，通常縮寫為 Regex）是最強大且不可或缺的文本處理工具 —— 它的用處就是在文本中**掃描/搜索**（Scan/Search）與某一**規則**（Pattern）**匹配**（Match，即，與規則一致）的所有實例，並且還可以按照規則**捕獲**（Capture）其中的部分或者全部，對它們進行**替換**（Replace）。

接下來為了避免歧義，我們乾脆用 Regex 這個縮寫，以及與它相關的英文單詞：pattern, match, capture, replace(ment)……

有時，使用 Regex 並不是為了 Replace，而是為了檢查格式，比如，可以用 Regex 檢查用戶輸入的密碼是否過於簡單（比如，全部都由數字構成），比如可以用來驗證用戶輸入的電話號碼、證件號碼是否符合特定格式等等。

另外，在自學的過程中，想盡一切辦法把一切術語用簡單直白的 “人話” 重新表述，是特別有效的促進進步的行為模式。

## 視覺體驗

所謂百聞不如一見。

眼見為實 —— 想辦法讓一個陌生的概念視覺上直觀，是突破大多學習障礙的最簡單粗暴直接有效的方式。

我們最好先直接看看 Regex 的工作過程。以下，是用微軟發行的代碼編輯工具 Visual Studio Code 針對一小段文本使用若干條 Regex 進行匹配的過程：

![](../images/regex-test.gif)

Python 的項目代碼倉庫里有一個很簡短的 Demo 程序，叫 [`redemo.py`](https://github.com/python/cpython/blob/master/Tools/demo/redemo.py)，它使用 [Tcl/Tk](https://docs.python.org/3/library/tkinter.html) 作為圖形界面，也可以用來測試正則表達式。

它的代碼地址是：

> https://raw.githubusercontent.com/python/cpython/master/Tools/demo/redemo.py

它運行起來長成這樣：

![](../images/redemo.png)

目前（2019）網上最方便的 Regex 測試器，是 [regex101.com](https://regex101.com)：

以下，就是在一段文本中，找出所有首寫字母大寫的詞彙的_過程_，並將其先全部替換成小寫，再將其全部替換為大寫的過程；使用的正則表達式是 `([A-Z])\w+`，替換表達式分別是 `\L$1` 和 `\U$1`：

![](../images/regex101.gif)

這個網站太好了，所以，平日里我是用 [Nativefier](https://github.com/jiahaog/nativefier) 工具將這個網站打包為一個 Mac Desktop App 使用。不過，它也有局限，就是被搜索文件略微大點就報錯，說 `timeout`……

## 準備工作


我們需要個文本文件，用來當作練習使用正則表達式去搜索替換的目標。這個文件保存在當前的根目錄，文件名稱是：`regex-target-text-sample.txt`。

以下代碼中，`pttn = r'beg[iau]ns?'` 這一句中的 [`beg[iau]ns?`](https://regexper.com#beg[iau]ns?) 就是 Regex 的 Pattern。

**註意**：在 Python 代碼中，寫 Pattern 的時候，之所以要在字符串 `'...'` 之前加上 `r`，寫成 `r'...'`，是因為如果不用 raw string 的話，那麼，每個轉義符號都要寫成 `\\`；如果用 raw string，轉義符號就可以直接使用 `\` 本身了…… 當然，如果你想搜索 `\` 這個符號本身的話，那麼還是得寫 `\\`。

而 `re.findall(pttn, str)` 的意思是說，把 `str` 中所有與 `pttn` 這個規則一致的字符串都找出來：
```python
import re
with open('regex-target-text-sample.txt', 'r') as f:
    str = f.read()
pttn = r'beg[iau]ns?'
re.findall(pttn, str)
```
    ['begin', 'began', 'begun', 'begin']



文件 `regex-target-text-sample.txt` 中的內容如下：
```html
<ol>
    <li><pre>begin began begun bigins begining</pre></li>
    <li><pre>google gooogle goooogle goooooogle</pre></li>
    <li><pre>coloured color coloring  colouring colored</pre></li>
    <li><pre>never ever verb however everest</pre></li>
    <li><pre>520 52000 5200000 520000000 520000000000</pre></li>
    <li><pre>error wonderer achroiocythaemia achroiocythemia</pre></li>
    <li><pre>The white dog wears a black hat.</pre></li>
    <li><pre>Handel, Händel, Haendel</pre></li>
</ol>
<dl>(843) 542-4256</dl> <dl>(431) 270-9664</dl>
<dl>3336741162</dl> <dl>3454953965</dl>
<ul>
<li>peoplesr@live.com</li> <li>jaxweb@hotmail.com</li>
<li>dhwon@comcast.net</li> <li>krueger@me.com</li>
</ul>
<h3>URLs</h3>
https://docs.python.org/3/howto/regex.html
https://docs.python.org/3/library/re.html
<h3>passwords</h3>
Pasw0rd~
i*Eh,GF67E
a$4Bh9XE&E
<h3>duplicate words</h3>
<p>It's very very big.</p>
<p>Keep it simple, simple, simple!</p>
```
在以下的示例中，有時直接設定了 str 的值，而不是使用以上整個文本文件 —— 因為讀者在閱讀的時候，最好能直接看到被搜索的字符串。另外，如果使用整個文件，所得到的 Match 太多，也確實影響閱讀。

## 優先級

畢竟，你已經不是 “啥都不懂” 的人了。你已經知道一個事實：編程語言無非是用來運算的。

所謂的運算，就有操作符（Operators）和操作元（Operands）—— 而操作符肯定是有優先級的，不然的話，那麼多操作元和操作符放在一起，究竟先操作哪個呢？

Regex 也一樣，它本身就是個迷你語言（Mini Language）。在 Regex 中，操作符肯定也有優先級。它的操作元有個專門的名稱，**原子**（Atom）。

先大致看看它的操作符優先級，你就會對它有相當不錯的瞭解：

| 排列 |         原子與操作符優先級      | 從高到低 )  |   
|---|-----------------------------------|------------------------|
| 1 | 轉義符號 (Escaping Symbol)               | `\` |
| 2 | 分組、捕獲 (Grouping or Capturing)                          | `(...)` `(?:...)` `(?=...)` `(?!...)` `(?<=...)` `(?<!...)`     |
| 3 | 數量 (Quantifiers)      | `a*` `a+` `a?` `a{n, m}` |
| 4 | 序列與定位（Sequence and Anchor      | `abc` `^` `$` `\b` `\B`               |
| 5 | 或（Alternation）                       | `a\|b\|c`                   |
| 6 | 原子 (Atoms)                 | `a` `[^abc]` `\t` `\r` `\n` `\d` `\D` `\s` `\S` `\w` `\W` `.` |

當然，你若是在之前，沒有自學過、理解過 Python （或者任何其它編程語言）表達式中的操作符優先級，那麼一上來就看上面的表格不僅對你沒有幫助，只能讓你更迷惑。

—— 這就是理解能力逐步積累逐步加強的過程。

## 原子

在 Regex 的 Pattern 中，操作元，即，被運算的 “值”，被稱為**原子**（Atom）。

### 本義字符

最基本的原子，就是本義字符，它們都是單個字符。

本義字符包括從 `a` 到 `z`，`A` 到 `Z`，`0` 到 `9`，還有 `_` —— 它們所代表的就是它們的字面值。

即，相當於，`string.ascii_letters` 和 `string.digits` 以及 `_`。
```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

import string
string.ascii_letters
string.digits
```
    'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    '0123456789'



以下字符在 Regex 中都有特殊含義：

> `\` `+` `*` `.` `?` `-` `^` `$` `|` `(` `)` `[` `]` `{` `}` `<` `>` 

當你在寫 Regex 的時候，如果你需要搜索的字符不是本義字符，而是以上這些特殊字符時，_建議_都直接加上轉義符號 `\` 來表示，比如，你想搜索 `'`，那你就寫 `\'`，或者你想搜索 `#` 那你就寫 `\#`（事實上，`#` 並不是 Regex 的特殊符號，所以，它之前的轉義符號可有可無） —— 這對初學者來說可能是最安全的策略。

跟過往一樣，所有的細節都很重要，它們就是需要花時間逐步熟悉到牢記。

### 集合原子

集合原子還是原子。

標示集合原子，使用方括號 `[]`。`[abc]` 的意思是說，“`a` or `b` or `c`”，即，`abc` 中的任意一個字符。

比如，[`beg[iau]n`](https://regexper.com#beg[iau]n) 能夠代表 `begin`、`began`，以及 `begun`。
```python
import re

str = 'begin began begun bigins begining'
pttn = r'beg[iau]n'
re.findall(pttn, str)
```
    ['begin', 'began', 'begun', 'begin']



在方括號中，我們可以使用兩個操作符：`-`（區間）和 `^`（非）。

* `[a-z]` 表示從小寫字母 `a` 到小寫字母 `z` 中的任意一個字符。
* `[^abc]` 表示 `abc` 以外的其它任意字符，即，非 `[abc]` 。

註意，一個集合原子中，`^` 符號只能用一次，只能緊跟在 `[` 之後。否則不起作用。

### 類別原子

類別原子，是指那些能夠代表 “一類字符” 的原子，它們都得使用轉義符號再加上另外一個符號表達，包括：

`\d` 任意數字；等價於 `[0-9]`

`\D` 任意非數字；等價於 `[^0-9]`

`\w` 任意本義字符；等價於 `[a-zA-z0-9_]`

`\W` 任意非本義字符；等價於 `[^a-zA-z0-9_]`

`\s` 任意空白；相當於 `[ \f\n\r\t\v]` （註意，方括號內第一個字符是空格符號） 

`\S` 任意非空白；相當於 `[^ \f\n\r\t\v]` （註意，緊隨 `^` 之後的是一個空格符號） 

`.` 除 `\r` `\n` 之外的任意字符；相當於 `[^\r\n]`

類別原子挺好記憶的，如果你知道各個字母是哪個詞的首字母的話：

> * `d` 是 digits
> * `w` 是 word characters
> * `s` 是 spaces

另外，在空白的集合 `[ \f\n\r\t\v]` 中：`f` 是分頁符；`\n` `\r` 是換行符； `\t` 是製表符；`\v` 是縱向製表符（很少用到）。各種關於空白的轉義符也同樣挺好記憶的，如果你知道各個字母是那個詞的首字母的話：

> * `f` 是 flip
> * `n` 是 new line
> * `r` 是 return
> * `t` 是 tab
> * `v` 是 vertical tab
```python
import re

str = '<dl>(843) 542-4256</dl> <dl>(431) 270-9664</dl>'
pttn = r'\d\d\d\-'
re.findall(pttn, str)
```
    ['542-', '270-']



### 邊界原子

我們可以用邊界原子指定邊界。也可以稱作 “定位操作符”。

`^` 匹配被搜索字符串的開始位置；

`$` 匹配被搜索字符串的結束位置；

`\b` 匹配單詞的邊界；[`er\b`](https://regexper.com#er%5Cb)，能匹配 `coder` 中的 `er`，卻不能匹配 `error` 中的 `er`；

`\B` 匹配非單詞邊界；[`er\B`](https://regexper.com#er%5CB)，能匹配 `error` 中的 `er`，卻不能匹配 `coder` 中的 `er`。
```python
import re

str = 'never ever verb however everest'
pttn = r'er\b'
re.findall(pttn, str)
pttn = r'er\B'
re.findall(pttn, str)
```
    ['er', 'er', 'er']
    ['er', 'er']



**註意**：`^` 和 `$` 在 Python 語言中被 `\A` 和 `\Z` 替代。

事實上，每種語言或多或少都對 Regex 有自己的定製。不過，本章討論的絕大多數細節，都是通用的。

### 組合原子

我們可以用圓括號 `()` 將多個單字符原子組合成一個原子 —— 這麼做的結果是，`()` 內的字符串將被當作一整個原子，可以被隨後我們要講解的數量操作符操作。

另外，`()` 這個操作符，有兩個作用：**組合**（Grouping），就是我們剛剛講到的作用；而另外一個作用是**捕獲**（Capturing)，後面會講到。

註意區別， [`er`](https://regexper.com#er)、[`[er]`](https://regexper.com#[er]) 和 [`(er)`](https://regexper.com#(er)) 各不相同。

> * `er` 是兩個原子，`'e'` 和緊隨其後的 `'r'`
> * `[er]` 是一個原子，或者 `'e'` 或者 `'r'`；
> * `(er)` 是一個原子，`'er'`

下一節中講到數量操作符的時候，會再次強調這點。

## 數量操作符

數量操作符有： `+` `?` `*` `{n, m}`。

它們是用來限定位於它們之前的原子允許出現的個數；不加數量限定則代表出現一次且僅出現一次：

`+` 代表前面的原子必須至少出現一次，即：` 出現次數 ≧ 1`

> 例如，[`go+gle`](https://regexper.com#go+gle)可以匹配 `google` `gooogle` `goooogle` 等;

`?` 代表前面的原子最多只可以出現一次，即：`0 ≦ 出現次數 ≦ 1`

> 例如，[`colou?red`](https://regexper.com#colou?red)可以匹配 `colored` 或者 `coloured`;

`*` 代表前面的原子可以不出現，也可以出現一次或者多次，即：` 出現次數 ≧ 0`

> 例如，[`520*`](https://regexper.com#520*)可以匹配 `52` `520` `52000` `5200000` `520000000000` 等。

`{n}` 之前的原子出現確定的 `n` 次；

`{n,}` 之前的原子出現至少 `n` 次；

`{n, m}` 之前的原子出現至少 `n` 次，至多 `m` 次

> 例如，[`go{2,5}gle`](https://regexper.com#go%7B2,5%7Dgle)，能匹配 `google` `gooogle` `goooogle` 或 `gooooogle`，但不能匹配 `gogle` 和 `gooooooogle`
```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

import re
with open('regex-target-text-sample.txt', 'r') as f:
    str = f.read()

pttn = r'go+gle'
re.findall(pttn, str)

pttn = r'go{2,5}gle'
re.findall(pttn, str)

pttn = r'colou?red'
re.findall(pttn, str)

pttn = r'520*'
re.findall(pttn, str)
```
    ['google', 'gooogle', 'goooogle', 'goooooogle']
    ['google', 'gooogle', 'goooogle']
    ['coloured', 'colored']
    ['520', '52000', '5200000', '520000000', '520000000000']



數量操作符是對它之前的原子進行操作的，換言之，數量操作符的操作元是操作符之前的原子。

上一節提到，要註意區別：`er`、`[er]` 和 `(er)` 各不相同。

> * `er` 是兩個原子，`'e'` 之後 `'r'`
> * `[er]` 是一個原子，或者 `'e'` 或者 `'r'`；
> * `(er)` 是一個原子，`'er'`
```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

import re

str = 'error wonderer severeness'

pttn = r'er'
re.findall(pttn, str)

pttn = r'[er]'
re.findall(pttn, str)

pttn = r'(er)'
re.findall(pttn, str)
```
    ['er', 'er', 'er', 'er']
    ['e', 'r', 'r', 'r', 'e', 'r', 'e', 'r', 'e', 'e', 'r', 'e', 'e']
    ['er', 'er', 'er', 'er']



在以上的例子中，看不出 `er` 和 `(er)` 的區別，但是，加上數量操作符就不一樣了 —— 因為_數量操作符只對它之前的那一個原子進行操作_：
```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

str = 'error wonderer severeness'

pttn = r'er+'
re.findall(pttn, str)

pttn = r'[er]+'
re.findall(pttn, str)

pttn = r'(er)+'
re.findall(pttn, str)
```
    ['err', 'er', 'er', 'er']
    ['err', 'r', 'erer', 'e', 'ere', 'e']
    ['er', 'er', 'er']



## 或操作符 `|`

或操作符 `|` 是所有操作符中優先級最低的，數量操作符的優先級比它高，所以，在 `|` 前後的原子被數量操作符（如果有的話）操作之後才交給 `|` 操作。

於是，[`begin|began|begun`](https://regexper.com#begin%7Cbegan%7Cbegun) 能夠匹配 `begin` 或 `began` 或 `begun`。
```python
import re

str = 'begin began begun begins beginn'
pttn = r'begin|began|begun'
re.findall(pttn, str)
```
    ['begin', 'began', 'begun', 'begin', 'begin']



在集合原子中（即，`[]` 內的原子）各個原子之間的關係，只有 “或” —— 相當於方括號中的每個原子之間都有一個被省略的 `|`。

**註意**：中括號的 `|` 不被當作特殊符號，而是被當作 `|` 這個符號本身。在中括號中的圓括號，也被當作圓括號 `()` 本身，而無分組含義。

```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

import re

str = 'achroiocythaemia achroiocythemia a|e'
pttn = r'[a|ae]'
re.findall(pttn, str)

pttn = r'[a|e]'
re.findall(pttn, str)

pttn = r'[ae]'
re.findall(pttn, str)

pttn = r'[(ae)]'
re.findall(pttn, str)

pttn = r'[a|ae|(ae)]'
re.findall(pttn, str)
```
    ['a', 'a', 'e', 'a', 'a', 'e', 'a', 'a', '|', 'e']



## 匹配並捕獲

捕獲（Capture），使用的是圓括號 `()`。使用圓括號得到的匹配的值被暫存成一個帶有索引的列表，第一個是 `$1`，第二個是 `$2`…… 以此類推。隨後，我們可以在替換的過程中使用 `$1` `$2` 中所保存的值。

**註意**：在 Python 語言中調用 `re` 模塊之後，在 `re.sub()` 中調用被匹配的值，用的索引方法是 `\1`、`\2`…… 以此類推。
```python
import re
str = 'The white dog wears a black hat.'
pttn = r'The (white|black) dog wears a (white|black) hat.'
re.findall(pttn, str)

repl = r'The \2 dog wears a \1 hat.'
re.sub(pttn, repl, str)

repl = r'The \1 dog wears a \1 hat.'
re.sub(pttn, repl, str)
```
    [('white', 'black')]
    'The black dog wears a white hat.'
    'The white dog wears a white hat.'



## 非捕獲匹配

有時，你並不想捕獲圓括號中的內容，在那個地方你使用括號的目的只是分組，而非捕獲，那麼，你就在圓括號內最開頭加上 `?:` —— `(?:...)`：
```python
import re
str = 'The white dog wears a black hat.'
pttn = r'The (?:white|black) dog wears a (white|black) hat.'
re.findall(pttn, str)                   # 只捕獲了一處，也就是說只有一個值將來可以被引用

repl = r'The \1 dog wears a \1 hat.'    # 不過，可替換的位置卻有兩個（即便非捕獲匹配，也有可替換位置）
re.sub(pttn, repl, str)
```
    ['black']
    'The black dog wears a black hat.'



需要註意的是，雖然非匹配捕獲不將匹配值暫存以便隨後替換時調用，但匹配處依然是將來可被替換的位置。

在 Python 代碼中使用正則表達式，匹配和捕獲以及隨後的替換，有更靈活的方式，因為可以對那些值直接編程。`re.sub()` 中，`repl` 參數甚至可以接收另外一個函數作為參數 —— 以後你肯定會自行認真閱讀以下頁面中的所有內容：

> https://docs.python.org/3/library/re.html

非捕獲匹配，還有若干個操作符：

 `(?=pattern)`   
> 正向肯定預查（look ahead positive assert），在任何匹配規則的字符串開始處匹配查找字符串。這是一個非獲取匹配，也就是說，該匹配不需要獲取供以後使用。例如，[`Windows(?=95|98|NT|2000)`](https://regexper.com#%60Windows(?=95%7C98%7CNT%7C2000)%60)
能匹配 `Windows2000` 中的 `Windows`，但不能匹配 `Windows3.1` 中的 `Windows`。預查不消耗字符，也就是說，在一個匹配發生後，在最後一次匹配之後立即開始下一次匹配的搜索，而不是從包含預查的字符之後開始。 

`(?!pattern)`
> 正向否定預查（negative assert），在任何不匹配規則的字符串開始處匹配查找字符串。這是一個非獲取匹配，也就是說，該匹配不需要獲取供以後使用。例如[`Windows(?=95|98|NT|2000)`](https://regexper.com#Windows(?=95%7C98%7CNT%7C2000))
能匹配 `Windows3.1` 中的 `Windows`，但不能匹配 `Windows2000` 中的 `Windows`。預查不消耗字符，也就是說，在一個匹配發生後，在最後一次匹配之後立即開始下一次匹配的搜索，而不是從包含預查的字符之後開始。

`(?<=pattern)`
>反向（look behind）肯定預查，與正向肯定預查類似，只是方向相反。例如，[`(?<=95|98|NT|2000)Windows`](https://regexper.com#(?%3C=95%7C98%7CNT%7C2000)Windows)
能匹配 `2000Windows` 中的 `Windows`，但不能匹配 `3.1Windows` 中的 `Windows`。

 `(?<!pattern)`
 >反向否定預查，與正向否定預查類似，只是方向相反。例如 `(?<!95|98|NT|2000)Windows`
能匹配 `3.1Windows` 中的 `Windows`，但不能匹配 `2000Windows` 中的 `Windows`。 
 


## 控制標記

有幾個全局控制標記（Flag）需要瞭解，其中最常默認指定的有 `G` 和 `M`：
 
`A`/`ASCII`，默認為 `False` 

> * `\d`, `\D`, `\w`, `\W`, `\s`, `\S`, `\b`, 和 `\B` 等只限於 ASCII 字符 
> * 行內寫法：`(?a)`
> * Python re 模塊中的常量： `re.A` `re.ASCII`
 
`I`/`IGNORECASE` ，默認為 `False`

> * 忽略字母大小寫 
> * 行內寫法： `(?i)` 
> * Python re 模塊中的常量：`re.I` `re.IGNORECASE` 

`G`/`GLOBAL`，默認為 `True`
> * 找到第一個 match 之後不返回
> * 行內寫法： `(?g)` 
> * Python re 模塊中這個標記不能更改，默認為 TRUE
 
`L`/`LOCALE`，默認為 `False`

> * 由本地語言設置決定 `\d`, `\D`, `\w`, `\W`, `\s`, `\S`, `\b`, 和 `\B` 等等的內容
> * 行內寫法： `(?L)` 
> * Python re 模塊中的常量：`re.L` `re.LOCALE`
 
`M`/`MULTILINE`，默認為 `True`

> * 使用本標誌後， `^` 和 `$` 匹配行首和行尾時，會增加換行符之前和之後的位置。
> * 行內寫法： `(?m)`
> * Python re 模塊中的常量： `re.M` `re.MULTILINE`
 
`S`/`DOTALL`，默認為 `False`
> * 使 `.` 完全匹配任何字符，包括換行；沒有這個標誌， `.` 匹配除了 `n` `r` 之外的任何字符。 
> * 行內寫法： `(?s)`
> * Python re 模塊中的常量： `re.S` `re.DOTALL`
 
`X`/`VERBOSE`，默認為 `False` 
> * 當該標誌被指定時，Pattern 中的的空白符會被忽略，除非該空白符在圓括號或方括號中，或在反斜杠 `\ ` 之後。這樣做的結果是允許將註釋寫入 Pattern，這些註釋會被 Regex 解析引擎忽略。註釋用 `#` 號來標識，不過該符號不能在字符串或反斜杠之後。 
> * 行內寫法： `(?x)`
> * Python re 模塊中的常量： `re.X` `re.VERBOSE`


## 幾個最常用的 Regex

以下是幾個常用的 Regex<a href='#fn2' name='fn2b'><sup>[2]</sup></a>，值得保存：

* matching username
> [`/^[a-z0-9_-]{3,16}$/`](https://regexper.com#/%5E[a-z0-9_-]%7B3,16%7D$/)

* matching password<a href='#fn3' name='fn3b'><sup>[3]</sup></a>
> [`/^[a-z0-9_-]{6,18}$/`](https://regexper.com#/%5E[a-z0-9_-]%7B6,18%7D$/)

* matching a HEX value
> [`/^#?([a-f0-9]{6}|[a-f0-9]{3})$/`](https://regexper.com#/%5E#?([a-f0-9]%7B6%7D%7C[a-f0-9]%7B3%7D)$/)

* matching a slug
> [`/^[a-z0-9-]+$/`](https://regexper.com#/%5E[a-z0-9-]+$/)

* matching email address
> [`/^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$/`](https://regexper.com#/%5E([a-z0-9_%5C.-]+)@([%5Cda-z%5C.-]+)%5C.([a-z%5C.]%7B2,6%7D)$/)
 

* matching a URL
> [`/^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$/`](https://regexper.com#/%5E(https?:%5C/%5C/)?([%5Cda-z%5C.-]+)%5C.([a-z%5C.]%7B2,6%7D)([%5C/%5Cw%20%5C.-]*)*%5C/?$/)

* matching an IP address
> [`/^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/`](https://regexper.com/#%2F%5E%28%3F%3A%28%3F%3A25%5B0-5%5D%7C2%5B0-4%5D%5B0-9%5D%7C%5B01%5D%3F%5B0-9%5D%5B0-9%5D%3F%29%5C.%29%7B3%7D%28%3F%3A25%5B0-5%5D%7C2%5B0-4%5D%5B0-9%5D%7C%5B01%5D%3F%5B0-9%5D%5B0-9%5D%3F%29%24%2F)

* matching a HTML tag
> [`/^<([a-z]+)([^<]+)*(?:>(.*)<\/\1>|\s+\/>)$/`](https://regexper.com/#%2F%5E<%28%5Ba-z%5D%2B%29%28%5B%5E<%5D%2B%29*%28%3F%3A>%28.*%29<%5C%2F%5C1>%7C%5Cs%2B%5C%2F>%29%24%2F)

對了，告訴你一個小秘密：
> 以上的正則表達式，點擊都能連接到 [regexper.com](https://regexper.com)，在那裡你能查看這些正則表達式的圖形化示意圖。另外，本文中，處於 markdown cell 的絕大多數正則表達式都有這樣的連接…… 你可以重讀的時候試試。


寫 Regex 最燒腦的地方在於 “使其全面” —— 要考慮到各種意外情況。

當然，除非必要，也不要在 “全面” 這事兒上面花太多時間 —— 給你看一個據說是 “最大程度上能夠匹配所有 email 地址的 Regex”<a href='#fn4' name='fn4b'><sup>[4]</sup></a>，我都懶得測試的一個正則表達式：
```regex
(?:(?:\r\n)?[ \t])*(?:(?:(?:[^()<>@,;:\\".\[\] \000-\031]+(?:(?:(?:\r\n)?[ \t]
)+|\Z|(?=[\["()<>@,;:\\".\[\]]))|"(?:[^\"\r\\]|\\.|(?:(?:\r\n)?[ \t]))*"(?:(?:
\r\n)?[ \t])*)(?:\.(?:(?:\r\n)?[ \t])*(?:[^()<>@,;:\\".\[\] \000-\031]+(?:(?:(
?:\r\n)?[ \t])+|\Z|(?=[\["()<>@,;:\\".\[\]]))|"(?:[^\"\r\\]|\\.|(?:(?:\r\n)?[ 
\t]))*"(?:(?:\r\n)?[ \t])*))*@(?:(?:\r\n)?[ \t])*(?:[^()<>@,;:\\".\[\] \000-\0
31]+(?:(?:(?:\r\n)?[ \t])+|\Z|(?=[\["()<>@,;:\\".\[\]]))|\[([^\[\]\r\\]|\\.)*\
](?:(?:\r\n)?[ \t])*)(?:\.(?:(?:\r\n)?[ \t])*(?:[^()<>@,;:\\".\[\] \000-\031]+
(?:(?:(?:\r\n)?[ \t])+|\Z|(?=[\["()<>@,;:\\".\[\]]))|\[([^\[\]\r\\]|\\.)*\](?:
(?:\r\n)?[ \t])*))*|(?:[^()<>@,;:\\".\[\] \000-\031]+(?:(?:(?:\r\n)?[ \t])+|\Z
|(?=[\["()<>@,;:\\".\[\]]))|"(?:[^\"\r\\]|\\.|(?:(?:\r\n)?[ \t]))*"(?:(?:\r\n)
?[ \t])*)*\<(?:(?:\r\n)?[ \t])*(?:@(?:[^()<>@,;:\\".\[\] \000-\031]+(?:(?:(?:\
r\n)?[ \t])+|\Z|(?=[\["()<>@,;:\\".\[\]]))|\[([^\[\]\r\\]|\\.)*\](?:(?:\r\n)?[
 \t])*)(?:\.(?:(?:\r\n)?[ \t])*(?:[^()<>@,;:\\".\[\] \000-\031]+(?:(?:(?:\r\n)
?[ \t])+|\Z|(?=[\["()<>@,;:\\".\[\]]))|\[([^\[\]\r\\]|\\.)*\](?:(?:\r\n)?[ \t]
)*))*(?:,@(?:(?:\r\n)?[ \t])*(?:[^()<>@,;:\\".\[\] \000-\031]+(?:(?:(?:\r\n)?[
 \t])+|\Z|(?=[\["()<>@,;:\\".\[\]]))|\[([^\[\]\r\\]|\\.)*\](?:(?:\r\n)?[ \t])*
)(?:\.(?:(?:\r\n)?[ \t])*(?:[^()<>@,;:\\".\[\] \000-\031]+(?:(?:(?:\r\n)?[ \t]
)+|\Z|(?=[\["()<>@,;:\\".\[\]]))|\[([^\[\]\r\\]|\\.)*\](?:(?:\r\n)?[ \t])*))*)
*:(?:(?:\r\n)?[ \t])*)?(?:[^()<>@,;:\\".\[\] \000-\031]+(?:(?:(?:\r\n)?[ \t])+
|\Z|(?=[\["()<>@,;:\\".\[\]]))|"(?:[^\"\r\\]|\\.|(?:(?:\r\n)?[ \t]))*"(?:(?:\r
\n)?[ \t])*)(?:\.(?:(?:\r\n)?[ \t])*(?:[^()<>@,;:\\".\[\] \000-\031]+(?:(?:(?:
\r\n)?[ \t])+|\Z|(?=[\["()<>@,;:\\".\[\]]))|"(?:[^\"\r\\]|\\.|(?:(?:\r\n)?[ \t
]))*"(?:(?:\r\n)?[ \t])*))*@(?:(?:\r\n)?[ \t])*(?:[^()<>@,;:\\".\[\] \000-\031
]+(?:(?:(?:\r\n)?[ \t])+|\Z|(?=[\["()<>@,;:\\".\[\]]))|\[([^\[\]\r\\]|\\.)*\](
?:(?:\r\n)?[ \t])*)(?:\.(?:(?:\r\n)?[ \t])*(?:[^()<>@,;:\\".\[\] \000-\031]+(?
:(?:(?:\r\n)?[ \t])+|\Z|(?=[\["()<>@,;:\\".\[\]]))|\[([^\[\]\r\\]|\\.)*\](?:(?
:\r\n)?[ \t])*))*\>(?:(?:\r\n)?[ \t])*)|(?:[^()<>@,;:\\".\[\] \000-\031]+(?:(?
:(?:\r\n)?[ \t])+|\Z|(?=[\["()<>@,;:\\".\[\]]))|"(?:[^\"\r\\]|\\.|(?:(?:\r\n)?
[ \t]))*"(?:(?:\r\n)?[ \t])*)*:(?:(?:\r\n)?[ \t])*(?:(?:(?:[^()<>@,;:\\".\[\] 
\000-\031]+(?:(?:(?:\r\n)?[ \t])+|\Z|(?=[\["()<>@,;:\\".\[\]]))|"(?:[^\"\r\\]|
\\.|(?:(?:\r\n)?[ \t]))*"(?:(?:\r\n)?[ \t])*)(?:\.(?:(?:\r\n)?[ \t])*(?:[^()<>
@,;:\\".\[\] \000-\031]+(?:(?:(?:\r\n)?[ \t])+|\Z|(?=[\["()<>@,;:\\".\[\]]))|"
(?:[^\"\r\\]|\\.|(?:(?:\r\n)?[ \t]))*"(?:(?:\r\n)?[ \t])*))*@(?:(?:\r\n)?[ \t]
)*(?:[^()<>@,;:\\".\[\] \000-\031]+(?:(?:(?:\r\n)?[ \t])+|\Z|(?=[\["()<>@,;:\\
".\[\]]))|\[([^\[\]\r\\]|\\.)*\](?:(?:\r\n)?[ \t])*)(?:\.(?:(?:\r\n)?[ \t])*(?
:[^()<>@,;:\\".\[\] \000-\031]+(?:(?:(?:\r\n)?[ \t])+|\Z|(?=[\["()<>@,;:\\".\[
\]]))|\[([^\[\]\r\\]|\\.)*\](?:(?:\r\n)?[ \t])*))*|(?:[^()<>@,;:\\".\[\] \000-
\031]+(?:(?:(?:\r\n)?[ \t])+|\Z|(?=[\["()<>@,;:\\".\[\]]))|"(?:[^\"\r\\]|\\.|(
?:(?:\r\n)?[ \t]))*"(?:(?:\r\n)?[ \t])*)*\<(?:(?:\r\n)?[ \t])*(?:@(?:[^()<>@,;
:\\".\[\] \000-\031]+(?:(?:(?:\r\n)?[ \t])+|\Z|(?=[\["()<>@,;:\\".\[\]]))|\[([
^\[\]\r\\]|\\.)*\](?:(?:\r\n)?[ \t])*)(?:\.(?:(?:\r\n)?[ \t])*(?:[^()<>@,;:\\"
.\[\] \000-\031]+(?:(?:(?:\r\n)?[ \t])+|\Z|(?=[\["()<>@,;:\\".\[\]]))|\[([^\[\
]\r\\]|\\.)*\](?:(?:\r\n)?[ \t])*))*(?:,@(?:(?:\r\n)?[ \t])*(?:[^()<>@,;:\\".\
[\] \000-\031]+(?:(?:(?:\r\n)?[ \t])+|\Z|(?=[\["()<>@,;:\\".\[\]]))|\[([^\[\]\
r\\]|\\.)*\](?:(?:\r\n)?[ \t])*)(?:\.(?:(?:\r\n)?[ \t])*(?:[^()<>@,;:\\".\[\] 
\000-\031]+(?:(?:(?:\r\n)?[ \t])+|\Z|(?=[\["()<>@,;:\\".\[\]]))|\[([^\[\]\r\\]
|\\.)*\](?:(?:\r\n)?[ \t])*))*)*:(?:(?:\r\n)?[ \t])*)?(?:[^()<>@,;:\\".\[\] \0
00-\031]+(?:(?:(?:\r\n)?[ \t])+|\Z|(?=[\["()<>@,;:\\".\[\]]))|"(?:[^\"\r\\]|\\
.|(?:(?:\r\n)?[ \t]))*"(?:(?:\r\n)?[ \t])*)(?:\.(?:(?:\r\n)?[ \t])*(?:[^()<>@,
;:\\".\[\] \000-\031]+(?:(?:(?:\r\n)?[ \t])+|\Z|(?=[\["()<>@,;:\\".\[\]]))|"(?
:[^\"\r\\]|\\.|(?:(?:\r\n)?[ \t]))*"(?:(?:\r\n)?[ \t])*))*@(?:(?:\r\n)?[ \t])*
(?:[^()<>@,;:\\".\[\] \000-\031]+(?:(?:(?:\r\n)?[ \t])+|\Z|(?=[\["()<>@,;:\\".
\[\]]))|\[([^\[\]\r\\]|\\.)*\](?:(?:\r\n)?[ \t])*)(?:\.(?:(?:\r\n)?[ \t])*(?:[
^()<>@,;:\\".\[\] \000-\031]+(?:(?:(?:\r\n)?[ \t])+|\Z|(?=[\["()<>@,;:\\".\[\]
]))|\[([^\[\]\r\\]|\\.)*\](?:(?:\r\n)?[ \t])*))*\>(?:(?:\r\n)?[ \t])*)(?:,\s*(
?:(?:[^()<>@,;:\\".\[\] \000-\031]+(?:(?:(?:\r\n)?[ \t])+|\Z|(?=[\["()<>@,;:\\
".\[\]]))|"(?:[^\"\r\\]|\\.|(?:(?:\r\n)?[ \t]))*"(?:(?:\r\n)?[ \t])*)(?:\.(?:(
?:\r\n)?[ \t])*(?:[^()<>@,;:\\".\[\] \000-\031]+(?:(?:(?:\r\n)?[ \t])+|\Z|(?=[
\["()<>@,;:\\".\[\]]))|"(?:[^\"\r\\]|\\.|(?:(?:\r\n)?[ \t]))*"(?:(?:\r\n)?[ \t
])*))*@(?:(?:\r\n)?[ \t])*(?:[^()<>@,;:\\".\[\] \000-\031]+(?:(?:(?:\r\n)?[ \t
])+|\Z|(?=[\["()<>@,;:\\".\[\]]))|\[([^\[\]\r\\]|\\.)*\](?:(?:\r\n)?[ \t])*)(?
:\.(?:(?:\r\n)?[ \t])*(?:[^()<>@,;:\\".\[\] \000-\031]+(?:(?:(?:\r\n)?[ \t])+|
\Z|(?=[\["()<>@,;:\\".\[\]]))|\[([^\[\]\r\\]|\\.)*\](?:(?:\r\n)?[ \t])*))*|(?:
[^()<>@,;:\\".\[\] \000-\031]+(?:(?:(?:\r\n)?[ \t])+|\Z|(?=[\["()<>@,;:\\".\[\
]]))|"(?:[^\"\r\\]|\\.|(?:(?:\r\n)?[ \t]))*"(?:(?:\r\n)?[ \t])*)*\<(?:(?:\r\n)
?[ \t])*(?:@(?:[^()<>@,;:\\".\[\] \000-\031]+(?:(?:(?:\r\n)?[ \t])+|\Z|(?=[\["
()<>@,;:\\".\[\]]))|\[([^\[\]\r\\]|\\.)*\](?:(?:\r\n)?[ \t])*)(?:\.(?:(?:\r\n)
?[ \t])*(?:[^()<>@,;:\\".\[\] \000-\031]+(?:(?:(?:\r\n)?[ \t])+|\Z|(?=[\["()<>
@,;:\\".\[\]]))|\[([^\[\]\r\\]|\\.)*\](?:(?:\r\n)?[ \t])*))*(?:,@(?:(?:\r\n)?[
 \t])*(?:[^()<>@,;:\\".\[\] \000-\031]+(?:(?:(?:\r\n)?[ \t])+|\Z|(?=[\["()<>@,
;:\\".\[\]]))|\[([^\[\]\r\\]|\\.)*\](?:(?:\r\n)?[ \t])*)(?:\.(?:(?:\r\n)?[ \t]
)*(?:[^()<>@,;:\\".\[\] \000-\031]+(?:(?:(?:\r\n)?[ \t])+|\Z|(?=[\["()<>@,;:\\
".\[\]]))|\[([^\[\]\r\\]|\\.)*\](?:(?:\r\n)?[ \t])*))*)*:(?:(?:\r\n)?[ \t])*)?
(?:[^()<>@,;:\\".\[\] \000-\031]+(?:(?:(?:\r\n)?[ \t])+|\Z|(?=[\["()<>@,;:\\".
\[\]]))|"(?:[^\"\r\\]|\\.|(?:(?:\r\n)?[ \t]))*"(?:(?:\r\n)?[ \t])*)(?:\.(?:(?:
\r\n)?[ \t])*(?:[^()<>@,;:\\".\[\] \000-\031]+(?:(?:(?:\r\n)?[ \t])+|\Z|(?=[\[
"()<>@,;:\\".\[\]]))|"(?:[^\"\r\\]|\\.|(?:(?:\r\n)?[ \t]))*"(?:(?:\r\n)?[ \t])
*))*@(?:(?:\r\n)?[ \t])*(?:[^()<>@,;:\\".\[\] \000-\031]+(?:(?:(?:\r\n)?[ \t])
+|\Z|(?=[\["()<>@,;:\\".\[\]]))|\[([^\[\]\r\\]|\\.)*\](?:(?:\r\n)?[ \t])*)(?:\
.(?:(?:\r\n)?[ \t])*(?:[^()<>@,;:\\".\[\] \000-\031]+(?:(?:(?:\r\n)?[ \t])+|\Z
|(?=[\["()<>@,;:\\".\[\]]))|\[([^\[\]\r\\]|\\.)*\](?:(?:\r\n)?[ \t])*))*\>(?:(
?:\r\n)?[ \t])*))*)?;\s*)
```
## 趣事一則

[ELIZA](https://en.wikipedia.org/wiki/ELIZA) 是人類史上第一個 “聊天機器人” 程序，上個世紀六十年代，1966 年實現的。核心就是使用正則表達式匹配對方語句中的關鍵詞彙，再經過替換，形成看似有意義的 “回應” —— 事實上，ELIZA 完全不知道自己在說什麼……

幾年後，就是七十年代初，1972 年，另外一個聊天機器人 [Parry](https://en.wikipedia.org/wiki/PARRY) <a href='#fn5' name='fn5b'><sup>[5]</sup></a>被寫了出來…… 隨後第二年，這兩個聊天機器人在 ARPANET “碰面” 好好地聊了一下<a href='#fn6' name='fn6b'><sup>[6]</sup></a>：

> ELIZA: Good Evening. Tell me your problems. Please terminate input with a period or a question mark.
>
> PARRY: People get on my nerves sometimes.
>
> ELIZA: I am not sure I understand you fully.
>
> PARRY: You should pay more attention.
>
> ELIZA: Suppose you should pay more attention.
>
> PARRY: You're entitled to your own opinion.
>
> ELIZA: What makes you think I am entitled to my own opinion?
>
> PARRY: It bothers me just to be around people in general.
>
> ELIZA: Please go on.
>
> PARRY: I went to the track at Bay Meadows a while back.
>
> ELIZA: What does that suggest to you?
> 
> PARRY: I went to the races.
>
> ......

以下是後人用 Python 重新實現的 ELIZA 的程序代碼，你可以直接執行它，嘗試一下與 ELIZA 聊聊天：
```python
# %load https://raw.githubusercontent.com/jezhiggins/eliza.py/master/eliza.py
#----------------------------------------------------------------------
#  eliza.py
#
#  a cheezy little Eliza knock-off by Joe Strout
#  with some updates by Jeff Epler
#  hacked into a module and updated by Jez Higgins
#----------------------------------------------------------------------

import string
import re
import random

class eliza:
  def __init__(self):
    self.keys = list(map(lambda x:re.compile(x[0], re.IGNORECASE),gPats))
    self.values = list(map(lambda x:x[1],gPats))

  #----------------------------------------------------------------------
  # translate: take a string, replace any words found in dict.keys()
  #  with the corresponding dict.values()
  #----------------------------------------------------------------------
  def translate(self,str,dict):
    words = str.lower().split()
    keys = dict.keys();
    for i in range(0,len(words)):
      if words[i] in keys:
        words[i] = dict[words[i]]
    return ' '.join(words)

  #----------------------------------------------------------------------
  #  respond: take a string, a set of regexps, and a corresponding
  #    set of response lists; find a match, and return a randomly
  #    chosen response from the corresponding list.
  #----------------------------------------------------------------------
  def respond(self,str):
    # find a match among keys
    for i in range(0, len(self.keys)):
      match = self.keys[i].match(str)
      if match:
        # found a match ... stuff with corresponding value
        # chosen randomly from among the available options
        resp = random.choice(self.values[i])
        # we've got a response... stuff in reflected text where indicated
        pos = resp.find('%')
        while pos > -1:
          num = int(resp[pos+1:pos+2])
          resp = resp[:pos] + \
            self.translate(match.group(num),gReflections) + \
            resp[pos+2:]
          pos = resp.find('%')
        # fix munged punctuation at the end
        if resp[-2:] == '?.': resp = resp[:-2] + '.'
        if resp[-2:] == '??': resp = resp[:-2] + '?'
        return resp

#----------------------------------------------------------------------
# gReflections, a translation table used to convert things you say
#    into things the computer says back, e.g. "I am" --> "you are"
#----------------------------------------------------------------------
gReflections = {
  "am"   : "are",
  "was"  : "were",
  "i"    : "you",
  "i'd"  : "you would",
  "i've"  : "you have",
  "i'll"  : "you will",
  "my"  : "your",
  "are"  : "am",
  "you've": "I have",
  "you'll": "I will",
  "your"  : "my",
  "yours"  : "mine",
  "you"  : "me",
  "me"  : "you"
}

#----------------------------------------------------------------------
# gPats, the main response table.  Each element of the list is a
#  two-element list; the first is a regexp, and the second is a
#  list of possible responses, with group-macros labelled as
#  %1, %2, etc.
#----------------------------------------------------------------------
gPats = [
  [r'I need (.*)',
  [  "Why do you need %1?",
    "Would it really help you to get %1?",
    "Are you sure you need %1?"]],

  [r'Why don\'?t you ([^\?]*)\??',
  [  "Do you really think I don't %1?",
    "Perhaps eventually I will %1.",
    "Do you really want me to %1?"]],

  [r'Why can\'?t I ([^\?]*)\??',
  [  "Do you think you should be able to %1?",
    "If you could %1, what would you do?",
    "I don't know -- why can't you %1?",
    "Have you really tried?"]],

  [r'I can\'?t (.*)',
  [  "How do you know you can't %1?",
    "Perhaps you could %1 if you tried.",
    "What would it take for you to %1?"]],

  [r'I am (.*)',
  [  "Did you come to me because you are %1?",
    "How long have you been %1?",
    "How do you feel about being %1?"]],

  [r'I\'?m (.*)',
  [  "How does being %1 make you feel?",
    "Do you enjoy being %1?",
    "Why do you tell me you're %1?",
    "Why do you think you're %1?"]],

  [r'Are you ([^\?]*)\??',
  [  "Why does it matter whether I am %1?",
    "Would you prefer it if I were not %1?",
    "Perhaps you believe I am %1.",
    "I may be %1 -- what do you think?"]],

  [r'What (.*)',
  [  "Why do you ask?",
    "How would an answer to that help you?",
    "What do you think?"]],

  [r'How (.*)',
  [  "How do you suppose?",
    "Perhaps you can answer your own question.",
    "What is it you're really asking?"]],

  [r'Because (.*)',
  [  "Is that the real reason?",
    "What other reasons come to mind?",
    "Does that reason apply to anything else?",
    "If %1, what else must be true?"]],

  [r'(.*) sorry (.*)',
  [  "There are many times when no apology is needed.",
    "What feelings do you have when you apologize?"]],

  [r'Hello(.*)',
  [  "Hello... I'm glad you could drop by today.",
    "Hi there... how are you today?",
    "Hello, how are you feeling today?"]],

  [r'I think (.*)',
  [  "Do you doubt %1?",
    "Do you really think so?",
    "But you're not sure %1?"]],

  [r'(.*) friend (.*)',
  [  "Tell me more about your friends.",
    "When you think of a friend, what comes to mind?",
    "Why don't you tell me about a childhood friend?"]],

  [r'Yes',
  [  "You seem quite sure.",
    "OK, but can you elaborate a bit?"]],

  [r'(.*) computer(.*)',
  [  "Are you really talking about me?",
    "Does it seem strange to talk to a computer?",
    "How do computers make you feel?",
    "Do you feel threatened by computers?"]],

  [r'Is it (.*)',
  [  "Do you think it is %1?",
    "Perhaps it's %1 -- what do you think?",
    "If it were %1, what would you do?",
    "It could well be that %1."]],

  [r'It is (.*)',
  [  "You seem very certain.",
    "If I told you that it probably isn't %1, what would you feel?"]],

  [r'Can you ([^\?]*)\??',
  [  "What makes you think I can't %1?",
    "If I could %1, then what?",
    "Why do you ask if I can %1?"]],

  [r'Can I ([^\?]*)\??',
  [  "Perhaps you don't want to %1.",
    "Do you want to be able to %1?",
    "If you could %1, would you?"]],

  [r'You are (.*)',
  [  "Why do you think I am %1?",
    "Does it please you to think that I'm %1?",
    "Perhaps you would like me to be %1.",
    "Perhaps you're really talking about yourself?"]],

  [r'You\'?re (.*)',
  [  "Why do you say I am %1?",
    "Why do you think I am %1?",
    "Are we talking about you, or me?"]],

  [r'I don\'?t (.*)',
  [  "Don't you really %1?",
    "Why don't you %1?",
    "Do you want to %1?"]],

  [r'I feel (.*)',
  [  "Good, tell me more about these feelings.",
    "Do you often feel %1?",
    "When do you usually feel %1?",
    "When you feel %1, what do you do?"]],

  [r'I have (.*)',
  [  "Why do you tell me that you've %1?",
    "Have you really %1?",
    "Now that you have %1, what will you do next?"]],

  [r'I would (.*)',
  [  "Could you explain why you would %1?",
    "Why would you %1?",
    "Who else knows that you would %1?"]],

  [r'Is there (.*)',
  [  "Do you think there is %1?",
    "It's likely that there is %1.",
    "Would you like there to be %1?"]],

  [r'My (.*)',
  [  "I see, your %1.",
    "Why do you say that your %1?",
    "When your %1, how do you feel?"]],

  [r'You (.*)',
  [  "We should be discussing you, not me.",
    "Why do you say that about me?",
    "Why do you care whether I %1?"]],

  [r'Why (.*)',
  [  "Why don't you tell me the reason why %1?",
    "Why do you think %1?" ]],

  [r'I want (.*)',
  [  "What would it mean to you if you got %1?",
    "Why do you want %1?",
    "What would you do if you got %1?",
    "If you got %1, then what would you do?"]],

  [r'(.*) mother(.*)',
  [  "Tell me more about your mother.",
    "What was your relationship with your mother like?",
    "How do you feel about your mother?",
    "How does this relate to your feelings today?",
    "Good family relations are important."]],

  [r'(.*) father(.*)',
  [  "Tell me more about your father.",
    "How did your father make you feel?",
    "How do you feel about your father?",
    "Does your relationship with your father relate to your feelings today?",
    "Do you have trouble showing affection with your family?"]],

  [r'(.*) child(.*)',
  [  "Did you have close friends as a child?",
    "What is your favorite childhood memory?",
    "Do you remember any dreams or nightmares from childhood?",
    "Did the other children sometimes tease you?",
    "How do you think your childhood experiences relate to your feelings today?"]],

  [r'(.*)\?',
  [  "Why do you ask that?",
    "Please consider whether you can answer your own question.",
    "Perhaps the answer lies within yourself?",
    "Why don't you tell me?"]],

  [r'quit',
  [  "Thank you for talking with me.",
    "Good-bye.",
    "Thank you, that will be $150.  Have a good day!"]],

  [r'(.*)',
  [  "Please tell me more.",
    "Let's change focus a bit... Tell me about your family.",
    "Can you elaborate on that?",
    "Why do you say that %1?",
    "I see.",
    "Very interesting.",
    "%1.",
    "I see.  And what does that tell you?",
    "How does that make you feel?",
    "How do you feel when you say that?"]]
  ]

#----------------------------------------------------------------------
#  command_interface
#----------------------------------------------------------------------
def command_interface():
  print('Therapist\n---------')
  print('Talk to the program by typing in plain English, using normal upper-')
  print('and lower-case letters and punctuation.  Enter "quit" when done.')
  print('='*72)
  print('Hello.  How are you feeling today?')

  s = ''
  therapist = eliza();
  while s != 'quit':
    try:
      s = input('> ')
    except EOFError:
      s = 'quit'
    print(s)
    while s[-1] in '!.':
      s = s[:-1]
    print(therapist.respond(s))


if __name__ == "__main__":
  command_interface()
```
    Therapist
    ---------
    Talk to the program by typing in plain English, using normal upper-
    and lower-case letters and punctuation.  Enter "quit" when done.
    ========================================================================
    Hello.  How are you feeling today?


-----
**腳註**

<a name='fn1'>[1]</a>：釋義摘自蘋果電腦上系統內建的《牛津英漢雙解辭典》

<a href='#fn1b'><small>↑Back to Content↑</small></a>
    
<a name='fn2'>[2]</a>：[8 Regular Expressions You Should Know](https://bit.ly/2tz8v9n) by Vasili 

<a href='#fn2b'><small>↑Back to Content↑</small></a>

<a name='fn3'>[3]</a>：關於校驗密碼強度的正則表達式，往往需要設置更為複雜的規則，Stackoverflow 上的一則答覆中有很好的示例：https://stackoverflow.com/a/21456918

<a href='#fn3b'><small>↑Back to Content↑</small></a>

<a name='fn4'>[4]</a>：http://www.ex-parrot.com/pdw/Mail-RFC822-Address.html

<a href='#fn4b'><small>↑Back to Content↑</small></a>

<a name='fn5'>[5]</a>：Parry 的源代碼（用 Lisp 寫的）在這裡： http://www.cs.cmu.edu/afs/cs/project/ai-repository/ai/areas/classics/parry/</a>

<a href='#fn5b'><small>↑Back to Content↑</small></a>
    
<a name='fn6'>[6]</a>：ELIZA 和 Parry 的完整聊天記錄在這裡：https://tools.ietf.org/html/rfc439</a>

<a href='#fn6b'><small>↑Back to Content↑</small></a>
    
