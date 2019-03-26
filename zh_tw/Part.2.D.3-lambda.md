
# 化名與匿名

## 化名

在 Python 中，我們可以給一個函數取個**化名**（alias）。

以下的代碼，我們先是定義個了一個名為 `_is_leap` 的函數，而後為它另取了一個化名：
```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

def _is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

year_leap_bool = _is_leap
year_leap_bool              #<function __main__._is_leap(year)>
year_leap_bool(800)         # _is_leap(800) -> True

id(year_leap_bool)          # id() 這個函數可以查詢某對象的內存地址
id(_is_leap)                # year_leap_bool 和 _is_leap 其實保存在同一個地址中，也就是說，它們是同一個對象。

type(year_leap_bool)
type(_is_leap)              # 它們都是 function
```
    <function __main__._is_leap(year)>
    True
    4547071648
    4547071648
    function
    function



我們可以看到的是，`id(year_leap_bool)` 和 `id(_is_leap)` 的內存地址是一樣的 —— 它們是同一個對象，它們都是函數。所以，當你寫 `year_leap_bool = _is_leap` 的時候，相當於給 `_is_leap()` 這個函數取了個化名。

在什麼樣的情況下，要給一個函數取一個化名呢？

在任何一個工程里，為函數或者變量取名都是很簡單卻不容易的事情 —— 因為可能會重名（雖然已經儘量用變量的作用域隔離了），可能會因取名含混而令後來者費解…… 

所以，僅僅為了少敲幾下鍵盤而給一個函數取個更短的化名，實際上並不是好主意，更不是好習慣。尤其現在的編輯器都支持自動補全和多光標編輯的功能，變量名再長都不構成負擔。

更多的時候，為函數取一個化名，應該是為了提高代碼可讀性 —— 對自己或其他人都很重要。

## lambda

寫一個很短的函數可以用 `lambda` 關鍵字。

下麵是用 `def` 關鍵字寫函數：
```python
def add(x, y):
    return x + y
add(3, 5)
```
    8



下麵是用 `lambda` 關鍵字寫函數：
```python
add = lambda x, y: x + y
add(3, 5)
```
    8



lambda 的語法結構如下：

> `lambda_expr ::= "lambda" [parameter_list] ":" expression`

以上使用的是 BNF 標註。當然，BNF 是你目前並不熟悉的，所以，有疑惑別當回事兒。

反正你已經見到示例了： 
```python
lambda x, y: x + y
```
先寫上 `lambda` 這個關鍵字，其後分為兩個部分，`:` 之前是參數，之後是表達式；這個表達式的值，就是這個函數的返回值。

> **註意**：`lambda` 語句中，`:` 之後有且只能有一個表達式。

而這個函數呢，沒有名字，所以被稱為 “匿名函數”。

`add = lambda x, y: x + y`

就相當於是給一個沒有名字的函數取了個名字。

## lambda 的使用場景

那 lambda 這種匿名函數的用處在哪裡呢？

### 作為某函數的返回值

第一個常見的用處是*作為另外一個函數的返回值*。

讓我們看看 [The Python Tutorial](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions) 中的一個例子。
```python
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
f(0)

f(1)
```
    42
    43



這個例子乍看起來很令人迷惑。我們先看看 `f = make_incrementor(42)` 之後，`f` 究竟是什麼東西：
```python
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
f

id(make_incrementor)
id(f)
```
    <function __main__.make_incrementor.<locals>.<lambda>(x)>
    4428443296
    4428726888



首先，要註意，`f` 並不是 `make_incrementor()` 這個函數的化名，如果是給這個函數取個化名，寫法應該是：
```python
f = make_incrementor
```
那 `f` 是什麼呢？ 它是 `<function __main__.make_incrementor.<locals>.<lambda>(x)>` ：

> * `f = make_incrementor(42)` 是將 `make_incrementor(42)` 的返回值保存到 `f` 這個變量之中；
> * 而 `make_incrementor()` 這個函數接收到 `42` 這個參數之後，返回了一個函數：`lambda x: x + 42`；
> * 於是，`f` 中保存的函數是 `lambda x: x + 42`；
> * 所以，`f(0)` 是向這個匿名函數傳遞了 `0`，而後，它返回的是 `0 + 42`。

### 作為某函數的參數

可以拿一些可以接收函數為參數的內建函數做例子。比如，[`map()`](https://docs.python.org/3/library/functions.html#map)。

> `map`(*function*, *iterable*, *...*)
> 
> Return an iterator that applies *function* to every item of *iterable*, yielding the results. If additional *iterable* arguments are passed, *function* must take that many arguments and is applied to the items from all iterables in parallel. With multiple iterables, the iterator stops when the shortest iterable is exhausted. For cases where the function inputs are already arranged into argument tuples, see [`itertools.starmap()`](https://docs.python.org/3/library/itertools.html#itertools.starmap).

`map()` 這個函數的第一個參數，就是用來接收函數的。隨後的參數，是 `iterable` —— 就是可被迭代的對象，比如，各種容器，例如：列表、元組、字典什麼的。
```python
def double_it(n):
    return n * 2

a_list = [1, 2, 3, 4, 5, 6]

b_list = list(map(double_it, a_list))
b_list

c_list = list(map(lambda x: x * 2, a_list))
c_list
```
    [2, 4, 6, 8, 10, 12]
    [2, 4, 6, 8, 10, 12]



顯然用 `lambda` 更為簡潔。另外，類似完成 `double_it(n)` 這種簡單功能的函數，常常有 “用過即棄” 的必要。
```python
phonebook = [
    {
        'name': 'john',
        'phone': 9876
    },
    {
        'name': 'mike',
        'phone': 5603
    },
    {
        'name': 'stan',
        'phone': 6898
    },
    {
        'name': 'eric',
        'phone': 7898
    }
]

phonebook
list(map(lambda x: x['name'], phonebook))
list(map(lambda x: x['phone'], phonebook))
```
    [{'name': 'john', 'phone': 9876},
     {'name': 'mike', 'phone': 5603},
     {'name': 'stan', 'phone': 6898},
     {'name': 'eric', 'phone': 7898}]
    ['john', 'mike', 'stan', 'eric']
    [9876, 5603, 6898, 7898]



可以給 map() 傳遞若干個可被迭代對象：
```python
a_list = [1, 3, 5]
b_list = [2, 4, 6]

list(map(lambda x, y: x * y, a_list, b_list))
```
    [2, 12, 30]



以上的例子都弄明白了，再去看 [The Python Tutorial](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions) 中的例子，就不會有任何疑惑了：
```python
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda p: p[1])
pairs
```
    [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]


