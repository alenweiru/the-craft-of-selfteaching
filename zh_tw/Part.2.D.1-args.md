
# 關於參數（上）

之前就提到過，從結構上來看，每個函數都是一個完整的程序，因為一個程序，核心構成部分就是輸入、處理、輸出：

> * 它可以有**輸入** —— 即，它能接收外部通過參數傳遞的值；
> * 它可以有**處理** —— 即，內部有能夠完成某一特定任務的代碼；尤其是，它可以根據 “輸入” 得到 “輸出”；
> * 它可以有**輸出** —— 即，它能向外部輸送返回值……

所以，在我看來，有了一點基礎知識之後，最早應該學習的是 “如何寫函數” —— 這個起點會更好一些。

這一章的內容，看起來會感覺與[Part1 F4 函數那一章](Part.1.F.4.functions.md)部分重合。但這兩章的出發點不一樣：

> * [Part1.E.4 函數那一章](Part.1.E.4.functions.md)，只是為了讓讀者有 “閱讀” 函數說明文檔的能力；
> * 這一章，是為了讓讀者能夠開始動手寫函數給自己或別人用……

## 為函數取名

哪怕一個函數內部什麼都不乾，它也得有個名字，然後名字後面要加上圓括號 `()`，以明示它是個函數，而不是某個變量。

定義一個函數的關鍵字是 `def`，以下代碼定義了一個什麼都不乾的函數：
```python
def do_nothing():
    pass

do_nothing()
```
為函數取名（為變量取名也一樣）有些基本的註意事項：

> - 首先，名稱不能以數字開頭。能用在名稱開頭的有，大小寫字母和下劃線 `_`；
> 
> - 其次，名稱中不能有空格，要麼使用下劃線連接詞彙，如，`do_nothing`，要麼使用 [Camel Case](https://en.wikipedia.org/wiki/Camel_case)，如 `doNothing` —— 更推薦使用下劃線；
> 
> - 再次，名稱不能與關鍵字重合 —— 以下是 Python 的 Keyword List：

| -  | Python     | Keyword    | List       |      -       |
| ------------ | ---------- | ---------- | ------------ | --------- |
| `and`      | `as`     | `assert` | `async`    | `await` |
| `continue` | `def`    | `del`    | `elif`     | `else`  |
| `finally`  | `for`    | `from`   | `global`   | `if`    |
| `is`       | `lambda` | `None`   | `nonlocal` | `not`   |
| `raise`    | `return` | `True`   | `try`      | `while` |
| `and`      | `as`     | `assert` | `async`    | `await` |

你隨時可以用以下代碼查詢關鍵字列表：
```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

import keyword
keyword.kwlist               # 列出所有關鍵字
keyword.iskeyword('if')      # 查詢某個詞是不是關鍵字
```
    ['False',
     'None',
     'True',
     'and',
     'as',
     'assert',
     'async',
     'await',
     'break',
     'class',
     'continue',
     'def',
     'del',
     'elif',
     'else',
     'except',
     'finally',
     'for',
     'from',
     'global',
     'if',
     'import',
     'in',
     'is',
     'lambda',
     'nonlocal',
     'not',
     'or',
     'pass',
     'raise',
     'return',
     'try',
     'while',
     'with',
     'yield']
    True



關於更多為函數、變量取名所需要的註意事項，請參閱：

> * [PEP 8 -- Style Guide for Python Code: Naming Conventions](https://www.python.org/dev/peps/pep-0008/#naming-conventions)
> * [PEP 526 -- Syntax for Variable Annotations](https://www.python.org/dev/peps/pep-0526/)
>
> 註：PEPs，是 Python Enhancement Proposals 的縮寫：https://www.python.org/dev/peps/

## 不接收任何參數的函數

在定義函數的時候，可以定義成不接收任何參數；但調用函數的時候，依然需要寫上函數名後面的圓括號 `()`：
```python
def do_something():
    print('This is a hello message from do_something().')

do_something()
```
    This is a hello message from do_something().


## 沒有 return 語句的函數

函數內部，不一定非要有 `return` 語句 —— 上面 `do_somthing()` 函數就沒有 `return` 語句。但如果函數內部並未定義返回值，那麼，該函數的返回值是 `None`，當 `None` 被當作布爾值對待的時候，相當於是 `False`。

這樣的設定，使得函數調用總是可以在條件語句中被當作判斷依據：
```python
def do_something():
    print('This is a hello message from do_something().')

if not do_something():                # 由於該函數名稱的緣故，這一句代碼的可讀性很差……
    print("The return value of 'do_something()' is None.")
```
    This is a hello message from do_something().
    The return value of 'do_something()' is None.


`if not do_something(): ` 翻譯成自然語言，應該是，“如果 `do_something()` 的返回值是 ‘非真’，那麼：……”

## 接收外部傳遞進來的值

讓我們寫個判斷閏年年份的函數，取名為 `is_leap()`，它接收一個年份為參數，若是閏年，則返回 `True`，否則返回 `False`。

根據閏年的定義：

> * 年份應該是 4 的倍數；
> * 年份能被 100 整除但不能被 400 整除的，不是閏年。

所以，相當於要在能被 4 整除的年份中，排除那些能被 100 整除卻不能被 400 整除的年份。
```python
def is_leap(year):
    leap = False
    if year % 4 == 0:
        leap = True
        if year % 100 == 0 and year % 400 != 0:
            leap = False
    return leap


is_leap(7)
is_leap(12)
is_leap(100)
is_leap(400)
```
    False
    True
    False
    True


```python
# 另外一個更為簡潔的版本，理解它還挺練腦子的
# cpython/Lib/datetime.py
def _is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
_is_leap(300)
```
    False



函數可以同時接收多個參數。比如，我們可以寫個函數，讓它輸出從大於某個數字到小於另外一個數字的斐波那契數列；那就需要定義兩個參數，調用它的時候也需要傳遞兩個參數：
```python
def fib_between(start, end):
    a, b = 0, 1
    while a < end:
        if a >= start:
            print(a, end=' ')
        a, b = b, a + b
        
fib_between(100, 10000)
```
    144 233 377 610 987 1597 2584 4181 6765 

當然可以把這個函數寫成返回值是一個列表：
```python
def fib_between(start, end):
    r = []
    a, b = 0, 1
    while a < end:
        if a >= start:
            r.append(a)
        a, b = b, a + b
    return r
        
fib_between(100, 10000)
```
    [144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]



## 變量的作用域

下麵的代碼，經常會讓初學者迷惑：
```python
def increase_one(n):
    n += 1
    return n

n = 1
print(increase_one(n))
# print(n)
```
    2


當 `increase_one(n)` 被調用之後，`n` 的值究竟是多少呢？或者更準確點問，隨後的 `print(n)` 的輸出結果應該是什麼呢？

輸出結果是 `1`。

在程序執行過程中，變量有**全局變量**（Global Variables）和**局域變量**（Local Variables）之分。

> 首先，每次某個函數被調用的時候，這個函數會開闢一個新的區域，這個函數內部所有的變量，都是局域變量。也就是說，即便那個函數內部某個變量的名稱與它外部的某個全局變量名稱相同，它們也不是同一個變量 —— 只是名稱相同而已。
> 
> 其次，更為重要的是，當外部調用一個函數的時候，準確地講，傳遞的不是變量，而是那個變量的*值*。也就是說，當 `increase_one(n)` 被調用的時候，被傳遞給那個恰好名稱也叫 `n` 的局域變量的，是全局變量 `n` 的值，`1`。
> 
> 而後，`increase_one()` 函數的代碼開始執行，局域變量 `n` 經過 `n += 1` 之後，其中存儲的值是 `2`，而後這個值被 `return` 語句返回，所以，`print(increase(n))` 所輸出的值是函數被調用之後的返回值，即，`2`。
> 
> 然而，全局變量 `n` 的值並沒有被改變，因為局部變量 `n`（它的值是 `2`） 和全局變量 `n`（它的值還是 `1`）只不過是名字相同而已，但它們並不是同一個變量。

以上的文字，可能需要反覆閱讀若干遍；幾遍下來，消除了疑惑，以後就徹底沒問題了；若是這個疑惑並未消除，或者關鍵點並未消化，以後則會反覆被這個疑惑所坑害，浪費無數時間。

不過，有一種情況要格外註意 —— 在函數內部處理被傳遞進來的值是可變容器（比如，列表）的時候：
```python
def be_careful(a, b):
    a = 2
    b[0] = 'What?!'

a = 1
b = [1, 2, 3]
be_careful(a, b)
a, b
```
    (1, ['What?!', 2, 3])



所以，一個比較好的習慣是，如果傳遞進來的值是列表，那麼在函數內部對其操作之前，先創建一個它的拷貝：
```python
def be_careful(a, b):
    a = 2
    b_copy = b.copy()
    b_copy[0] = 'What?!'

a = 1
b = [1, 2, 3]
be_careful(a, b)
a, b
```
    (1, [1, 2, 3])


