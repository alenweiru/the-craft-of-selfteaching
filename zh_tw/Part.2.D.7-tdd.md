
# 測試驅動的開發

寫一個函數，或者寫一個程序，換一種說法，其實就是 “實現一個算法” —— 而所謂的 “算法”，Wikipedia 上的定義是這樣的：

> In mathematics and computer science, an **algorithm** is an unambiguous specification of how to solve a class of problems. Algorithms can perform *calculation*, _data processing_, and *automated reasoning tasks*.

“算法”，其實沒多神秘，就是 “解決問題的步驟” 而已。

在第二部分的第一章里，我們看過一個判斷是否為閏年的函數：

> 讓我們寫個判斷閏年年份的函數，取名為 is_leap()，它接收一個年份為參數，若是閏年，則返回 True，否則返回 False。
> 
> 根據閏年的定義：
> 
> > * 年份應該是 4 的倍數；
> > * 年份能被 100 整除但不能被 400 整除的，不是閏年。
> > * 所以，相當於要在能被 4 整除的年份中，排除那些能被 100 整除卻不能被 400 整除的年份。

不要往回翻！現在自己動手嘗試著寫出這個函數？你會發現其實並不容易的……
```python
def is_leap(year):
    pass
```
第一步，跟很多人想象得不一樣，第一步不是上來就開始寫……

第一步是先假定這個函數寫完了，我們需要驗證它返回的結果對不對……

這種 “通過先想辦法驗證結果而後從結果倒推” 的開發方式，是一種很有效的方法論，叫做 “Test Driven Development”，以測試為驅動的開發。

如果我寫的 `is_leap(year)` 是正確的，那麼：

> * `is_leap(4)` 的返回值應該是 `True`
> * `is_leap(200)` 的返回值應該是 `False`
> * `is_leap(220)` 的返回值應該是 `True`
> * `is_leap(400)` 的返回值應該是 `True`

能夠羅列出以上四種情況，其實只不過是根據算法 “考慮全面” 之後的結果 —— 但你自己試試就知道了，無論多簡單的事，想要 “考慮全面” 好像並不容易……

所以，在寫 `def is_leap(year)` 中的內容之前，我只是用 `pass` 先把位置占上，而後在後面添加了四個用來測試結果的語句 ——  它們的值，現在當然都是 `False`…… 等我把整個函數寫完了，寫正確了，那麼它們的值就都應該變成 `True`。
```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

def is_leap(year):
    pass

is_leap(4) is True
is_leap(200) is False
is_leap(220) is True
is_leap(400) is True
```
    False
    False
    False
    False



考慮到更多的年份不是閏年，所以，排除順序大抵上應該是這樣：
> * 先假定都不是閏年；
> * 再看看是否能被 `4` 整除；
> * 再剔除那些能被 `100` 整除但不能被 `400` 整除的年份……

於是，先實現第一句：“先假定都不是閏年”：
```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

def is_leap(year):
    r = False
    return r

is_leap(4) is True
is_leap(200) is False
is_leap(220) is True
is_leap(400) is True
```
    False
    True
    False
    False



然後再實現這部分：“年份應該是 4 的倍數”：
```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

def is_leap(year):
    r = False
    if year % 4 == 0:
        r = True
    return r

is_leap(4) is True
is_leap(200) is False
is_leap(220) is True
is_leap(400) is True
```
    True
    False
    True
    True



現在剩下最後一條了：“剔除那些能被 `100` 整除但不能被 `400` 整除的年份”…… 拿一個參數值，比如，`200` 為例，

> * 因為它能被 `4` 整除，所以，使 `r = True`，
> * 然後再看它是否能被 `100` 整除 —— 能 —— 既然如此再看它能不能被 `400` 整除，
>   * 如果不能，那就讓 `r = False`；
>   * 如果能，就保留 `r` 的值…… 
> 如此這般，`200` 肯定使得 `r = False`。
```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

def is_leap(year):
    r = False
    if year % 4 == 0:
        r = True
        if year % 100 == 0:
            if year % 400 !=0:
                r = False
    return r

is_leap(4) is True
is_leap(200) is False
is_leap(220) is True
is_leap(400) is True
```
    True
    True
    True
    True



儘管整個過程讀起來很直觀，但真的要自己從頭到尾操作，就可能四處出錯，不信你就試試 —— 這一頁最下麵添加一個單元格，自己動手從頭寫到尾試試……

當然，Python 內建庫中的 `datetime.py` 模塊里的代碼更簡潔，之前給你看過：
```python
# cpython/Lib/datetime.py
def _is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
_is_leap(300)
```
    False



你自己動手，從寫測試開始，逐步把它實現出來試試？—— 肯定不能允許你拷貝粘貼，哈哈。

在 Python 語言中，有專門用來 “試錯” 的流程控制 —— 今天的絕大多數編程語言都有這種 “試錯語句”。

當一個程序開始執行的時候，有兩種錯誤可能會導致程序執行失敗：

> * 語法錯誤（Syntax Errors）
> * 意外（Exceptions）

比如，在 Python3 中，你寫 `print i`，而沒有寫 `print(i)`，那麼你犯的是語法錯誤，於是，解析器會直接提醒你，你在第幾行犯了什麼樣的語法錯誤。語法錯誤存在的時候，程序無法啟動執行。

但是，有時會出現這種情況：語法上完全正確，但出現了**意外**。這種錯誤，都是程序已經執行之後才發生的（Runtime Errors） —— 因為只要沒有語法錯誤，程序就可以啟動。比如，你寫的是 `print(11/0)`：
```python
print(11/0)
```
    ---------------------------------------------------------------------------
    ZeroDivisionError                         Traceback (most recent call last)
    <ipython-input-2-5544d98276be> in <module>
    ----> 1 print(11/0)
    
    ZeroDivisionError: division by zero


雖然這個語句本身沒有語法錯誤，但這個表達式是不能被處理的。於是，它觸發了 `ZeroDivisionError`，這個 “意外” 使得程序不可能繼續執行下去。

在 Python 中，定義了大量的常見 “意外”，並且按層級分類：

> 在第三部分閱讀完畢之後，可以回來重新查看以下官方文檔：<br />
> https://docs.python.org/3/library/exceptions.html
``` bash
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- ResourceWarning
```
拿 `FileNotFoundError` 為例 —— 當我們想要打開一個文件之前，其實應該有個辦法提前驗證一下那個文件是否存在。如果那個文件並不存在，就會引發 “意外”。
```python
f = open('test_file.txt', 'r')
```
    ---------------------------------------------------------------------------
    FileNotFoundError                         Traceback (most recent call last)
    <ipython-input-3-5fac19176fe6> in <module>
    ----> 1 f = open('test_file.txt', 'r')
    
    FileNotFoundError: [Errno 2] No such file or directory: 'test_file.txt'


在 Python 中，我們可以用 `try` 語句塊去執行那些可能出現 “意外” 的語句，`try` 也可以配合 `except`、`else`、`finally` 使用。從另外一個角度看，`try` 語句塊也是一種特殊的流程控制，專註於 “當意外發生時應該怎麼辦？”
```python
try:
    f = open('test_file.txt', 'r')
except FileNotFoundError as fnf_error:
    print(fnf_error)
```
    [Errno 2] No such file or directory: 'test_file.txt'


如此這般的結果是：

> 當程序中的語句 `f = open('test_file.txt', 'r')` 因為 `test_file.txt` 不存在而引發意外之時，`except` 語句塊會接管流程；而後，又因為在 `except` 語句塊中我們指定了 `FileNotFoundError`，所以，若是 `FileNotFoundError` 真的發生了，那麼，`except` 語句塊中的代碼，即，`print(fnf_error)` 會被執行……

你可以用的試錯流程還有以下變種：
```python
try:
    do_something()
except built_in_error as name_of_error:
    do_something()
else:
    do_something()
```
或者：
```python
try:
    do_something()
except built_in_error as name_of_error:
    do_something()
else:
    do_something()
finally:
    do_something()
```
甚至可以嵌套：
```python
try:
    do_something()
except built_in_error as name_of_error:
    do_something()
else:
    try:
        do_something()
    except built_in_error as name_of_error:
        do_something()
...
```
更多關於錯誤處理的內容，請在閱讀完第三部分中與 Class 相關的內容之後，再去詳細閱讀以下官方文檔：

> * [Errors and Exceptions](docs.python.org/3/tutorial/errors.html)
> * [Built-in Exceptions](https://docs.python.org/3/library/exceptions.html)
> * [Handling Exceptions](https://wiki.python.org/moin/HandlingExceptions)

理論上，這一章不應該套上這麼大的標題：《測試驅動開發》，因為在實際開發過程中，所謂測試驅動開發要使用更為強大更為複雜的模塊、框架和工具，比如，起碼使用 Python 內建庫中的 [unittest](https://docs.python.org/3/library/unittest.html) 模塊。

在寫程序的過程中，為別人（和將來的自己）寫註釋、寫 Docstring；在寫程序的過程中，為了保障程序的結果全面正確而寫測試，或者乾脆在最初寫的時候就考慮到各種意外所以使用試錯語句塊 —— 這些明明是天經地義的事情，卻是絕大多數人不做的…… 因為感覺有點麻煩。

這裡是 “聰明反被聰明誤” 的最好示例長期堆積的地方。很多人真的是因為自己很聰明，所以才覺得 “沒必要麻煩” —— 這就好像當年蘇格拉底仗著自己記憶力無比強大甚至乾脆過目不忘於是鄙視一切記筆記的人一樣。

但是，隨著時間的推移，隨著工程量的放大，到最後，那些 “聰明人” 都被自己坑死了 —— 聰明本身搞不定工程，能搞定工程的是智慧。蘇格拉底自己並沒完成任何工程，是他的學生柏拉圖不顧他的嘲笑用紙筆記錄了一切；而後柏拉圖的學生亞里士多德才有機會受到蘇格拉底的啟發，寫了《前分析篇》，提出對人類影響至今的 “三段論”……

千萬不要因為這第二部分中所舉的例子太容易而把自己迷惑了。刻意選擇簡單的例子放在這裡，是為了讓讀者更容易集中精力去理解關於自己動手寫函數的方方面面 —— 可將來你自己真的動手去做，哪怕真的去閱讀真實的工程代碼，你就會發現，難度還是很高的。現在的輕敵，會造成以後的潰敗。

現在還不是時候，等你把整本書都完成之後，記得回來再看這個鏈接：

> * [doctest — Test interactive Python examples](https://docs.python.org/3/library/doctest.html)
> * [unittest — Unit testing framework](https://docs.python.org/3/library/unittest.html)
