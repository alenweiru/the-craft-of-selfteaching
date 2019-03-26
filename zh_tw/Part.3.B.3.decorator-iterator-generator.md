
# 函數工具

這一章要講的是迭代器、生成器，和裝飾器，這些都是函數工具。有人把它們稱為 **DIG**（Decorator, Iterator，Generator）—— 它們都是真正掌握 Python 的關鍵。

## 迭代器（Iterator）

我們已經見過 Python 中的所有容器，都是可迭代的 —— 準確地講，是可以通過迭代遍歷每一個元素：
```python
string = "this is a string."
list = ['item 1', 'item 2', 3, 5]
set = (1, 2, 3, 4, 5)
for c in string:
    print(c, end=', ')
print()
for L in list:
    print(L, end=', ')
print()
for s in set:
    print(s, end=', ')
print()
```
    t, h, i, s,  , i, s,  , a,  , s, t, r, i, n, g, ., 
    item 1, item 2, 3, 5, 
    1, 2, 3, 4, 5, 


有個內建函數，就是用來把一個對象轉換成 “可迭代對象” 的 —— `iter()`。
```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

i = iter("Python")
type(i)
s = iter((1, 2, 3, 4, 5))
type(s)
L = iter(['item 1', 'item 2', 3, 5])
type(L)
```
    str_iterator
    tuple_iterator
    list_iterator



可迭代對象如何使用呢？有個 `next()` 函數：
```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

i = iter("Python")
next(i)
next(i)
next(i)
next(i)
next(i)
next(i)
# next(i) 前面已經到 'n' 了，再調用就會有 StopIteration 錯誤提示。
```
    'P'
    'y'
    't'
    'h'
    'o'
    'n'



在 `i` 這個迭代器里一共有 6 個元素，所以，`next(i)` 在被調用 6 次之後，就不能再被調用了，一旦再被調用，就會觸發 StopIteration 錯誤。

那我們怎麼自己寫一個迭代器呢？

迭代器是個 Object，所以，寫迭代器的時候寫的是 Class，比如，我們寫一個數數的迭代器，Counter：
```python
class Counter(object):
    def __init__(self, start, stop):
        self.current = start
        self.stop = stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.current > self.stop:
            raise StopIteration
        else:
            c = self.current
            self.current += 1
        return c

c = Counter(11, 20)
next(c)
next(c)
next(c)
for c in Counter(101, 105):
    print(c, sep=', ')
type(Counter)
```
    11
    12
    13
    101
    102
    103
    104
    105
    type



這裡的重點在於兩個函數的存在，`__iter__(self)` 和 `__next__(self)`。
```python
    def __iter__(self):
        return self
```
這兩句是約定俗成的寫法，寫上它們，`Counter` 這個類就被會被識別為 Iterator 類型。而後再有 `__next__(self)` 的話，它就是個完整的迭代器了。除了可以用 `for loop` 之外，也可以用 `while loop` 去遍歷迭代器中的所有元素：
```python
class Counter(object):
    def __init__(self, start, stop):
        self.current = start
        self.stop = stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.current > self.stop:
            raise StopIteration
        else:
            c = self.current
            self.current += 1
        return c


for c in Counter(101, 103):
    print(c, sep=', ')

c = Counter(201, 203)
while True:
    try:
        print(next(c), sep=', ')
    except StopIteration:
        break
```
    101
    102
    103
    201
    202
    203


## 生成器（Generator）

那用函數（而不是 Class）能不能寫一個 Counter 呢？答案是能，用生成器（Generator）就行。
```python
def counter(start, stop):
    while start <= stop:
        yield start
        start += 1
for i in counter(101, 105):
    print(i)
```
    101
    102
    103
    104
    105


哎呀！怎麼感覺這個簡潔很多呢？

不過，是否簡潔並不是問題，這次看起來用生成器更簡單，無非是因為當前的例子更適合用生成器而已。在不同的情況下，用迭代器和用生成器各有各的優勢。

這裡的關鍵在於 `yield` 這個語句。它和 `return` 最明顯的不同在於，在它之後的語句依然會被執行 —— 而 `return` 之後的語句就被忽略了。

但正因為這個不同，在寫生成器的時候，只能用 `yield`，而沒辦法使用 `return` —— 你現在可以回去把上面代碼中的 `yield` 改成 `return` 看看，然後體會一下它們之間的不同。

生成器函數被 `next()` 調用後，執行到 `yield` 生成一個值返回（然後繼續執行剩餘的語句）；下次再被 `next()` 調用的時候，從上次生成返回值的 `yield` 語句處繼續執行…… 如果感覺費解，就多讀幾遍 —— 而後再想想若是生成器中有多個 `yield` 語句會是什麼情況？

還有一種東西，叫做生成器表達式。先看個例子：
```python
even = (e for e in range(10) if not e % 2)
# odd = (o for o in range(10) if o % 2)
print(even)
for e in even:
    print(e)
```
    <generator object <genexpr> at 0x107cc0048>
    0
    2
    4
    6
    8


其實，這種表達式我們早就在 List Comprehension 里見過 —— 那就是通過生成器表達式完成的。

**註意**

仔細看 `even = (e for e in range(10) if not e % 2)` 中最外面那層括號，用了圓括號，`even` 就是用生成器創造的迭代器（Iterator），若是用了方括號，那就是用生成器創造的列表（List）—— 當然用花括號 `{}` 生成的就是集合（Set）……
```python
# even = (e for e in range(10) if not e % 2)
odd = [o for o in range(10) if o % 2]
print(odd)
for o in odd:
    print(o)
```
    [1, 3, 5, 7, 9]
    1
    3
    5
    7
    9

```python
# even = (e for e in range(10) if not e % 2)
odd = {o for o in range(10) if o % 2}
print(odd)
for o in odd:
    print(o)
```
    {1, 3, 5, 7, 9}
    1
    3
    5
    7
    9


**生成器表達式必須在括號內使用**（參見官方 [HOWTOS](https://docs.python.org/3/howto/functional.html#generator-expressions-and-list-comprehensions)），包括函數的參數括號，比如：
```python
sum_of_even = sum(e for e in range(10) if not e % 2)
print(sum_of_even)
```
    20

```python
```
函數內部當然可以包含其它的函數，以下就是一個函數中包含著其它函數的結構示例：
```python
def a_func():
    def b_func():
        pass
    def c_func():
        pass
        def d_func():
            pass
        b_func()
    return True
```
想象一下，如果，我們讓一個函數返回的是另外一個函數呢？我們一步一步來：
```python
def a_func():
    def b_func():
        print("Hi, I'm b_func!")
    print("Hi, I'm a_func!")
a_func()
```
    Hi, I'm a_func!

```python
def a_func():
    def b_func():
        print("Hi, I'm b_func!")
    print("Hi, I'm a_func!")
    b_func()
a_func()
```
    Hi, I'm a_func!
    Hi, I'm b_func!


上一個代碼，我們可以寫成這樣 —— 讓 `a_func()` 將它內部的 `b_func()` 作為它的返回值：
```python
def a_func():
    def b_func():
       print("Hi, I'm b_func!")
    print("Hi, I'm a_func!")
    return b_func()
a_func()
```
    Hi, I'm a_func!
    Hi, I'm b_func!


如果我們在 `return` 語句里只寫函數名呢？好像這樣：
```python
def a_func():
    def b_func():
        print("Hi, I'm b_func!")
    print("Hi, I'm a_func!")
    return b_func
a_func()
```
    Hi, I'm a_func!
    <function __main__.a_func.<locals>.b_func()>



這次返回的不是調用 `b_func()` 這個函數的執行結果，返回的是 `b_func` 這個_函數本身_。

## 裝飾器（Decorator）

### 函數也是對象

這是關鍵：

> 函數本身也是對象（即，Python 定義的某個 Class 的一個 Instance）。

於是，函數本身其實可以與其它的數據類型一樣，作為其它函數的參數或者返回值。

讓我們分步走 —— 註意，在以下代碼中，`a_decorator` 返回的一個函數的調用 `wrapper()` 而不是 `wrapper` 這個函數本身：
```python
def a_decorator(func):
    def wrapper():
        print('We can do sth. before a func is called...')
        func()
        print('... and we can do sth. after it is called...')
    return wrapper()

def a_func():
    print("Hi, I'm a_func!")
    
a_func()
a_decorator(a_func)
```
    Hi, I'm a_func!
    We can do sth. before a func is called...
    Hi, I'm a_func!
    ... and we can do sth. after it is called...


如果返回的是函數本身，`wrapper`，輸出結果跟你想的並不一樣：
```python
def a_decorator(func):
    def wrapper():
        print('We can do sth. before a func is called...')
        func()
        print('... and we can do sth. after it is called...')
    return wrapper  # 

def a_func():
    print("Hi, I'm a_func!")
    
a_func()
a_decorator(a_func)
```
    Hi, I'm a_func!
    <function __main__.a_decorator.<locals>.wrapper()>



### 裝飾器操作符

不過，Python 提供了一個針對函數的操作符 `@`，它的作用是…… 很難一下子說清楚，先看看以下代碼：
```python
def a_decorator(func):
    def wrapper():
        print('We can do sth. before calling a_func...')
        func()
        print('... and we can do sth. after it was called...')
    return wrapper

@a_decorator
def a_func():
    print("Hi, I'm a_func!")
    
a_func()
```
    We can do sth. before calling a_func...
    Hi, I'm a_func!
    ... and we can do sth. after it was called...


註意：以上的代碼中， `a_decorator(func)` 返回的是 `wrapper` 這個函數本身。

在我們定義 `a_func()` 的時候，在它之前，加上了一句 `@a_decorator`；這麼做的結果是：

> 每次 `a_func()` 在被調用的時候，因為它之前有一句 `@a_decorator`，所以它會先被當作參數傳遞到 `a_decorator(func)` 這個函數中…… 而後，真正的執行，是在 `a_decorator()` 里被完成的。

—— 被 `@` 調用的函數，叫做 “裝飾器”（Decorator），比如，以上代碼中的 `a_decorator(func)`。

現在可以很簡單直接地說清楚裝飾器的作用了：
```python
@a_decorator
def a_func():
    ...
```
等價於
```python
def a_func():
    ...
a_func = a_decorator(a_func)
```
就是用 `a_decorator` 的調用結果替換掉原來的函數。`a_decorator` 返回值是什麼，以後調用 `a_func` 時就是在調用這個返回值，而 `a_decorator` 本身此時已經執行完畢了。

### 裝飾器的用途

Decorator 最常用的場景是什麼呢？最常用的場景就是用來改變其它函數的行為。
```python
def an_output():
    return 'The quick brown fox jumps over the lazy dog.'
print(an_output())
```
    The quick brown fox jumps over the lazy dog.

```python
def uppercase(func):
    def wrapper():
        original_result = func()
        modified_restult = original_result.upper()
        return modified_restult
    return wrapper

@uppercase
def an_output():
    return 'The quick brown fox jumps over the lazy dog.'
print(an_output())
```
    THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.


你還可以給一個函數加上一個以上的裝飾器：
```python
def uppercase(func):
    def wrapper():
        original_result = func()
        modified_restult = original_result.upper()
        return modified_restult
    return wrapper
def strong(func):
    def wrapper():
        original_result = func()
        modified_restult = '<strong>'+original_result+'</strong>'
        return modified_restult
    return wrapper

@strong
@uppercase
def an_output():
    return 'The quick brown fox jumps over the lazy dog.'
print(an_output())
```
    <strong>THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.</strong>


你把兩個裝飾器的順序調換一下寫成下麵這樣試試：
```python
@uppercase
@strong
def an_output():
...
```
裝飾器的執行順序是 “自下而上” —— 其實是 “由里到外” 更為準確。體會一下。


### 裝飾帶有參數函數

到現在我們見到的使用裝飾器的函數都是沒有參數的：`an_output` 以及之前的 `a_func`。

如果被裝飾的函數有參數怎麼辦？裝飾器自身內部又應該怎麼寫？

這時候，Python 的 `*args` and `**kwargs` 的威力就顯現出來了 —— 之前怕麻煩沒有通過仔細反覆閱讀搞定這 “一個星號、兩個星號、直接暈倒” 的知識點的人，現在恐怕要吃虧了……

裝飾器函數本身這麼寫：
```python
def a_decorator(func):
    def wrapper(*args, **kwargs):
        return original_result
    # ...   
    return wrapper
```
在這裡，`(*args, **kwargs)` 非常強大，它可以匹配所有函數傳進來的所有參數…… 準確地講，`*args` 接收並處理所有傳遞進來的位置參數，`**kwargs` 接收並處理所有傳遞進來的關鍵字參數。

假設我們有這麼個函數：
```python
def say_hi(greeting, name=None):
    return greeting + '! ' + name + '.'

print(say_hi('Hello', 'Jack'))
```
    Hello! Jack.


如果我們想在裝飾器里對函數名、參數，都做些事情 —— 比如，我們寫個 `@trace` 用來告訴用戶調用一個函數的時候都發生了什麼……
```python
def trace(func):
    def wrapper(*args, **kwargs):
        print(f"Trace: You've called a function: {func.__name__}(),",
              f"with args: {args}; kwargs: {kwargs}")
    
        orginal_result = func(*args, *kwargs)
        print(f"Trace: {func.__name__}{args} returned: {orginal_result}")
        return orginal_result
    return wrapper

@trace
def say_hi(greeting, name=None):
    return greeting + '! ' + name + '.'

print(say_hi('Hello', 'Jack'))
```
    Trace: You've called a function: say_hi(), with args: ('Hello', 'Jack'); kwargs: {}
    Trace: say_hi('Hello', 'Jack') returned: Hello! Jack.
    Hello! Jack.


有了以上的基礎知識之後，再去閱讀 Python Decorator Library 的 Wiki 頁面就會輕鬆許多：

> https://wiki.python.org/moin/PythonDecoratorLibrary

### 學會裝飾器究竟有多重要？

裝飾器一定要學會 —— 因為很多人就是不會。

Oreilly.com 上有篇文章，《5 reasons you need to learn to write Python decorators》中，其中的第五條竟然是：**Boosting your career**!

> Writing decorators isn’t easy at first. It’s not rocket science, but takes enough effort to learn, and to grok the nuances involved, that many developers will never go to the trouble to master it. And that works to your advantage. When you become the person on your team who learns to write decorators well, and write decorators that solve real problems, other developers will use them. Because once the hard work of writing them is done, decorators are so easy to use. This can massively magnify the positive impact of the code you write. And it just might make you a hero, too.
> 
> As I’ve traveled far and wide, training hundreds of working software engineers to use Python more effectively, teams have consistently reported writing decorators to be one of the most valuable and important tools they’ve learned in my advanced Python programming workshops. 

為什麼有那麼多人就是學不會呢？—— 只不過是因為在此之前，遇到 `*args` `**kwargs` 的時候，“一個星號、兩個星號、直接暈倒”…… 而後並未再多掙扎一下。
