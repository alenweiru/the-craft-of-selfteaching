
# 值及其相應的運算

從結構上來看，一切的計算機程序，都由且只由兩個最基本的成分構成：

> * **運算**（Evaluation）
> * **流程控制**（Control Flow）

沒有流程控制的是計算器而已；有流程控制的才是可編程設備。

看看之前我們見過的計算質數的程序：（按一下 `⎋`，即 `ESC`，確保已經進入命令模式，`⇧ L` 可以切換是否顯示代碼行號）
```python
def is_prime(n):            # 定義 is_prime()，接收一個參數
    if n < 2:              # 開始使用接收到的那個參數（值）開始計算……
        return False       # 不再是返回給人，而是返回給調用它的代碼……
    if n == 2:
        return True
    for m in range(2, int(n**0.5)+1):
        if (n % m) == 0:
            return False
    else:
        return True

for i in range(80, 110):
    if is_prime(i):          # 調用 is_prime() 函數，
        print(i)            # 如果返回值為 True，則向屏幕輸出 i
```
    83
    89
    97
    101
    103
    107
    109


`if...`，`for...` 在控制流程：在什麼情況下運算什麼，在什麼情況下重覆運算什麼；

第 13 行 `is_prime()` 這個函數的調用，也是在控制流程 —— 所以我們可以**把函數看作是 “子程序”**；

一旦這個函數被調用，流程就轉向開始執行在第 1 行中定義的 `is_prime()` 函數內部的代碼，而這段代碼內部還是_計算_和_流程控制_，決定一個返回值 —— 返回值是布爾值；再回到第 13 行，將返回值交給 `if` 判斷，決定是否執行第 14 行……

而計算機這種可編程設備之所以可以做流程控制，是因為它可以做**布爾運算**，即，它可以_對布爾值_進行_操作_，而後將布爾值交給_分支_和_循環_語句，構成了程序中的流程控制。

## 值

從本質上看，程序里的絕大多數語句包含著**運算**（Evaluation），即，在對某個值進行**評價**。這裡的 “評價”，不是 “判斷某人某事的好壞”，而是 “_計算出某個值究竟是什麼_” —— 所以，我們用中文的 “**運算**” 翻譯這個 “_Evaluation_” 可能表達得更準確一些。

在程序中，被運算的可分為**常量**（Literals）和**變量**（Variables）。
```python
a = 1 + 2 * 3
a += 1
print(a)
```
在以上代碼中，

`1`、`2`、`3`，都是**常量**。_Literal_ 的意思是是 “字面的”，顧名思義，常量的_值_就是它字面上的值。`1` 的值，就是 `1`。

`a` 是**變量**。顧名思義，它的值將來是可變的。比如，在第 2 句中，這個變量的_值_發生了改變，之前是 `7`，之後變成了 `8`。

第 1 句中的 `+`、`*`，是**操作符**（Operators），它用來對其左右的值進行相應的_運算_而後得到一個值。先是由操作符 `*` 對 `2` 和 `3` 進行運算，
生成一個值，`6`；然後再由操作符 `+` 對 `1` 和 `6` 進行運算，生成一個值 `7`。先算乘除後算加減，這是操作符的**優先級**決定的。

`=` 是賦值符號，它的作用是將它右邊的值保存到左邊的變量中。


_值_是程序的基礎成分（Building blocks），它就好像蓋房子用的磚塊一樣，無論什麼樣的房子，到最後都主要是由磚塊構成。

_常量_，當然有個_值_ —— 就是它們字面所表達的值。

_變量_必須先_賦值_才能使用，也就是說，要先把一個_值_保存到變量中，它才能在其後被運算。

在 Python 中每個函數都有_返回值_，即便你在定義一個函數的時候沒有設定返回值，它也會加上默認的返回值 `None`……（請註意 `None` 的
大小寫！）
```python
def f():
    pass
print(f())        # 輸出 f() 這個函數被調用後的返回值，None
print(print(f())) # 這一行最外圍的 print() 調用了一次 print(f())，所以輸出一個 None，
                  # 而後再輸出這次調用的返回值，所以又輸出一次 None
```
    None
    None
    None


當我們調用一個函數的時候，本質上來看，就相當於：

> 我們把一個值交給某個函數，請函數根據它內部的運算和流程控制對其進行操作而後返回另外一個值。

比如，`abs()` 函數，就會返回傳遞給它的_值_的*絕對值*；`int()` 函數，會將傳遞給它的值的小數部分砍掉；`float()` 接到整數參數之後，會返回這個整數的浮點數形式：
```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

abs(-3.14159)
int(abs(-3.14159))
float(int(abs(-3.14159)))
```
    3.14159



## 值的類型

在編程語言中，總是包含最基本的三種數據類型：

> * 布爾值（Boolean Value)
> * 數字（Numbers）：整數（Int）、浮點數（Float）、複數（Complex Numbers）
> * 字符串（Strings）

既然有不同類型的數據，它們就分別對應著不同類型的值。

運算的一個默認法則就是，通常情況下應該是_相同類型的值才能相互運算_。

顯然，數字與數字之間的運算是合理的，但你讓 `+` 這個操作符對一個字符串和一個數字進行運算就不行：
```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

11 + 10 - 9 * 8 / 7 // 6 % 5
'3.14' + 3                  # 這一句會報錯
```
    20.0
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-4-e922b7565e53> in <module>
          3 
          4 11 + 10 - 9 * 8 / 7 // 6 % 5
    ----> 5 '3.14' + 3                  # 這一句會報錯
    
    TypeError: can only concatenate str (not "int") to str


所以，在不得不對不同類型的值進行運算之前，總是要事先做 **Type Casting**（類型轉換）。比如，

> * 將字符串轉換為數字用 `int()`、`float()`；
> * 將數字轉換成字符串用 `str()`；

另外，即便是在數字之間進行計算的時候，有時也需要將整數轉換成浮點數字，或者反之：
> * 將整數轉換成浮點數字用 `float()`；
> * 將浮點數字轉換成整數用 `int()`；

有個函數，`type()` ，可以用來查看某個值屬於什麼類型：
```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

type(3)
type(3.0)
type('3.14')
type(True)
type(range(10))
type([1,2,3])
type((1,2,3))
type({1,2,3})
type({'a':1, 'b':2, 'c':3})
```
## 操作符

針對不同類型的數據，有各自專用的**操作符**。

### 數值操作符

針對數字進行計算的操作符有加減乘除商餘冪：`+`、`-`、`*`、`/`、`//`、`%`、`**`。

其中 `+` 和 `-` 可以對單個值進行操作，`-3`；其它的操作符需要有兩個值才能操作。

從優先級來看，這些操作符中：

> * 對兩個值進行操作的 `+`、`-` 的優先級最低；
> * 稍高的是 `*`、`/`、`//`、`%`；
> * 更高的是對單個值進行操作的 `+`、`-`；
> * 優先級最高的是 `**`。

完整的操作符優先級列表，參見官方文檔：

> https://docs.python.org/3/reference/expressions.html#operator-precedence



### 布爾值操作符

針對布爾值，操作符有與或非： `and`、`or`、`not`。

它們之中，優先級最低的是或 `or`，然後是與 `and`, 優先級最高的是非 `not`：
```python
True and False or not True
```
最先操作的是 `not`，因為它優先級最高。所以，上面的表達式相當於 `True and False or (not True)`， 即相當於 `True and False or False`；

然後是 `and`，所以，`True and False or False` 相當於是 `(True and False) or False`，即相當於 `False or False`；

於是，最終的值是 `False`。

### 邏輯操作符

數值之間還可以使用邏輯操作符，`1 > 2` 返回布爾值 `False`。邏輯操作符有：`<`（小於）、`<=`（小於等於）、`>`（大於）、`>=`（大於等於）、`!=`（不等於）、`==`（等於）。

邏輯操作符的優先級，高於布爾值的操作符，低於數值計算的操作符。
即：數值計算的操作符優先級最高，其次是邏輯操作符，布爾值的操作符優先級最低。
```python
n = -95
n < 0 and (n + 1) % 2 == 0
```
### 字符串操作符

針對字符串，有三種操作：

> * 拼接：`+` 和 `' '`（後者是空格）
> * 拷貝：`*`
> * 邏輯運算：`in`、 `not in`；以及， `<`、`<=`、`>`、`>=`、`!=`、`==` 
```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

'Awesome' + 'Python'
'Awesome' 'Python'
'Python, ' + 'Awesome! ' * 3
'o' in 'Awesome' and 'o' not in 'Python'
```
字符之間，字符串之間，除了 `==` 和 `!=` 之外，也都可以被邏輯操作符 `<`、`<=`、`>`、`>=` 運算：
```python
'a' < 'b'
```
這是因為字符對應著 Unicode 碼，字符在被比較的時候，被比較的是對應的 Unicode 碼。
```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

'A' > 'a'
ord('A')
ord('a')
```
當字符串被比較的時候，將從兩個字符串各自的第一個字符開始逐個比較，“一旦決出勝負馬上停止”：
```python
'PYTHON' > 'Python 3'
```
### 列表的操作符

數字和字符串（由字符構成的序列）是最基本的數據類型，而我們往往需要批量處理數字和字符串，這樣的時候，我們需要**數組**（Array）。不過，在 Python 語言中，它提供了一個**容器**（Container）的概念，用來容納批量的數據。

Python 的容器有很多種 —— 字符串，其實也是容器的一種，它的裡面容納著批量的字符。

我們先簡單接觸一下另外一種容器：**列表**（List）。

列表的標示，用方括號 `[]`；舉例來說，`[1, 2, 3, 4, 5]` 和 `['ann', 'bob', 'cindy', 'dude', 'eric']`，或者 `['a', 2, 'b', 32, 22, 12]` 都是一個列表。

因為列表和字符串一樣，都是_有序容器_（容器還有另外一種是無序容器），所以，它們可用的操作符其實相同：

> * 拼接：`+` 和 `' '`（後者是空格）
> * 拷貝：`*`
> * 邏輯運算：`in`、 `not in`；以及， `<`、`<=`、`>`、`>=`、`!=`、`==` 

兩個列表在比較時（前提是兩個列表中的數據元素類型相同），遵循的還是跟字符串比較相同的規則：“一旦決出勝負馬上停止”。但實際上，由於列表中可以包含不同類型的元素，所以，通常情況下沒有實際需求對他們進行 “大於、小於” 的比較。（比較時，類型不同會引發 `TypeError`……）
```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

a_list = [1, 2, 3, 4, 5]
b_list = [1, 2, 3, 5]
c_list = ['ann', 'bob', 'cindy', 'dude', 'eric']
a_list > b_list
10 not in a_list
'ann' in c_list
```
## 更複雜的運算

對於數字進行加、減、乘、除、商、餘、冪的操作，對於字符串進行拼接、拷貝、屬於的操作，對布爾值進行或、與、非的操作，這些都是相對簡單的運算。

更為複雜一點的，我們要通過調用函數來完成 —— 因為在函數內部，我們可以用比 “單個表達式” 更為複雜的程序針對傳遞進來的參數進行運算。換言之，函數就相當於各種事先寫好的子程序，給它傳遞一個值，它會對其進行運算，而後返回一個值（最起碼返回一個 `None`）。

以下是 Python 語言所有的內建函數（[Built-in Functions](https://docs.python.org/3/library/functions.html)）：

| ( | Python | Built-in  |  Functions   |  )  |
| --- | --- | --- | --- | --- |
| [abs()](https://docs.python.org/3/library/functions.html#abs) | [delattr()](https://docs.python.org/3/library/functions.html#delattr) | [hash()](https://docs.python.org/3/library/functions.html#hash) | [memoryview()](https://docs.python.org/3/library/functions.html#func-memoryview) | [set()](https://docs.python.org/3/library/functions.html#func-set) |
| [all()](https://docs.python.org/3/library/functions.html#all) | [dict()](https://docs.python.org/3/library/functions.html#func-dict) | [help()](https://docs.python.org/3/library/functions.html#help) | [min()](https://docs.python.org/3/library/functions.html#min) | [setattr()](https://docs.python.org/3/library/functions.html#setattr) |
| [any()](https://docs.python.org/3/library/functions.html#any) | [dir()](https://docs.python.org/3/library/functions.html#dir) | [hex()](https://docs.python.org/3/library/functions.html#hex) | [next()](https://docs.python.org/3/library/functions.html#next) | [slice()](https://docs.python.org/3/library/functions.html#slice) |
| [ascii()](https://docs.python.org/3/library/functions.html#ascii) | [divmod()](https://docs.python.org/3/library/functions.html#divmod) | [id()](https://docs.python.org/3/library/functions.html#id)  | [object()](https://docs.python.org/3/library/functions.html#object) | [sorted()](https://docs.python.org/3/library/functions.html#sorted) |
| [bin()](https://docs.python.org/3/library/functions.html#bin) | [enumerate()](https://docs.python.org/3/library/functions.html#enumerate) | [input()](https://docs.python.org/3/library/functions.html#input) | [oct()](https://docs.python.org/3/library/functions.html#oct) | [staticmethod()](https://docs.python.org/3/library/functions.html#staticmethod) |
| [bool()](https://docs.python.org/3/library/functions.html#bool) | [eval()](https://docs.python.org/3/library/functions.html#eval) | [int()](https://docs.python.org/3/library/functions.html#int) | [open()](https://docs.python.org/3/library/functions.html#open) | [str()](https://docs.python.org/3/library/functions.html#func-str) |
| [breakpoint()](https://docs.python.org/3/library/functions.html#breakpoint) | [exec()](https://docs.python.org/3/library/functions.html#exec) | [isinstance()](https://docs.python.org/3/library/functions.html#isinstance) | [ord()](https://docs.python.org/3/library/functions.html#ord) | [sum()](https://docs.python.org/3/library/functions.html#sum) |
| [bytearray()](https://docs.python.org/3/library/functions.html#func-bytearray) | [filter()](https://docs.python.org/3/library/functions.html#filter) | [issubclass()](https://docs.python.org/3/library/functions.html#issubclass) | [pow()](https://docs.python.org/3/library/functions.html#pow) | [super()](https://docs.python.org/3/library/functions.html#super) |
| [bytes()](https://docs.python.org/3/library/functions.html#func-bytes) | [float()](https://docs.python.org/3/library/functions.html#float) | [iter()](https://docs.python.org/3/library/functions.html#iter) | [print()](https://docs.python.org/3/library/functions.html#print) | [tuple()](https://docs.python.org/3/library/functions.html#func-tuple) |
| [callable()](https://docs.python.org/3/library/functions.html#callable) | [format()](https://docs.python.org/3/library/functions.html#format) | [len()](https://docs.python.org/3/library/functions.html#len) | [property()](https://docs.python.org/3/library/functions.html#property) | [type()](https://docs.python.org/3/library/functions.html#type) |
| [chr()](https://docs.python.org/3/library/functions.html#chr) | [frozenset()](https://docs.python.org/3/library/functions.html#func-frozenset) | [list()](https://docs.python.org/3/library/functions.html#func-list) | [range()](https://docs.python.org/3/library/functions.html#func-range) | [vars()](https://docs.python.org/3/library/functions.html#vars) |
| [classmethod()](https://docs.python.org/3/library/functions.html#classmethod) | [getattr()](https://docs.python.org/3/library/functions.html#getattr) | [locals()](https://docs.python.org/3/library/functions.html#locals) | [repr()](https://docs.python.org/3/library/functions.html#repr) | [zip()](https://docs.python.org/3/library/functions.html#zip) |
| [compile()](https://docs.python.org/3/library/functions.html#compile) | [globals()](https://docs.python.org/3/library/functions.html#globals) | [map()](https://docs.python.org/3/library/functions.html#map) | [reversed()](https://docs.python.org/3/library/functions.html#reversed) | [__import__()](https://docs.python.org/3/library/functions.html#__import__) |
| [complex()](https://docs.python.org/3/library/functions.html#complex) | [hasattr()](https://docs.python.org/3/library/functions.html#hasattr) | [max()](https://docs.python.org/3/library/functions.html#max) | [round()](https://docs.python.org/3/library/functions.html#round) |  |

現在倒不用著急一下子全部瞭解它們 —— 反正早晚都會的。

這其中，針對數字，有計算絕對值的函數 `abs()`，有計算商餘的函數 `divmod()` 等等。
```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

abs(-3.1415926)
divmod(11, 3)
```
這些內建函數也依然只能完成 “基本操作”，比如，對於數字，我們想計算三角函數的話，內建函數就幫不上忙了，於是，我們需要調用標準庫（Standard Library）中的 math 模塊（Module）：
```python
import math
math.sin(5)
```
代碼 `math.sin(5)` 這裡的 `.`，也可以被理解為 “操作符”，它的作用是：

> 從其它模塊中調用函數。

代碼 `math.sin(5)` 的作用是：

> 把 `5` 這個值，傳遞給 `math` 這個模塊里的 `sin()` 函數，讓 `sin()` 根據它內部的代碼對這個值進行運算，而後返回一個值（即，計算結果）。

類（Class）中定義的函數，也可以這樣被調用 —— 雖然你還不明白類（Class）究竟是什麼，但從結構上很容易理解，它實際上也是保存在其他文件中的一段代碼，於是，那段代碼內部定義的函數，也可以這樣調用。

比如，數字，其實屬於一個類，所以，我們可以調用那個類里所定義的函數，比如，`float.as_integer_ratio()`，它將返回兩個值，第一個值除以第二個值，恰好等於傳遞給它的那個浮點數字參數：
```python
3.1415926.as_integer_ratio()
```
## 關於布爾值的補充

當你看到以下這樣的表達式，而後再看看它的結果，你可能會多少有點迷惑：
```python
True or 'Python'
```
這是因為 Python 將 `True` 定義為：

> By default, an object is considered true unless its class defines either a \_\_bool\_\_() method that returns `False` or a \_\_len\_\_() method that returns zero, when called with the object.
>
> https://docs.python.org/3/library/stdtypes.html#truth-value-testing

這一段文字，初學者是看不懂的。但下一段就好理解了：

> Here are most of the built-in objects considered `False`:
> 
> > * constants defined to be false: `None` and `False`.
> > * zero of any numeric type: `0`, `0.0`, `0j`, `Decimal(0)`, `Fraction(0, 1)`
> > * empty sequences and collections: `''`, `()`, `[]`, `{}`, `set()`, `range(0)`

所以，`'Python'` 是個非空的字符串，即，不屬於是 `empty sequences` ，所以它不被認為是 `False`，即，它的布爾值是 `True`

於是，這麼理解就輕鬆了：

> 每個變量或者常量，除了它們的值之外，同時還相當於有一個對應的布爾值。


## 關於值的類型的補充

除了數字、布爾值、字符串，以及上一小節介紹的列表之外，還有若干數據類型，比如 `range()`（等差數列）、`tuple`（元組）、`set`（集合）、`dictionary`（字典），再比如 `Date Type`（日期）等等。

它們都是基礎數據類型的各種組合 —— 現實生活中，更多需要的是把基礎類型組合起來構成的數據。比如，一個通訊簿，裡面是一系列字符串分別對應著若干字符串和數字。
``` python
entry[3662] = {
    'first_name': 'Michael',
    'last_name': 'Willington',
    'birth_day': '12/07/1992',
    'mobile': {
        '+714612234', 
        '+716253923'
    }
    'id': 3662,
    ...
}
```

針對不同的類型，都有相對應的操作符，可以對其進行運算。

這些類型之間有時也有不得不相互運算的需求，於是，在相互運算之前同樣要 _Type Casting_，比如將 List 轉換為 Set，或者反之：
```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

a = [1, 2, 3, 4, 5, 6, 7]
b = set(a)
c = list(b)
a
b
c
```
## 總結

回到最開始：從結構上來看，一切的計算機程序，都由且只由兩個最基本的成分構成：

> * **運算**（Evaluation）
> * **流程控制**（Control Flow）

這一章主要介紹了基礎數據類型的運算細節。而除了基礎數據類型，我們需要由它們組合起來的更多複雜數據類型。但無論數據的類型是什麼，被操作符操作的總是該數據的**值**。所以，雖然絕大多數編程書籍按照慣例會講解 “數據類型”，但為了究其本質，我們在這裡關註的是 “值的類型”。雖然只是關註焦點上的一點點轉換，但實踐證明，這一點點的不同，對初學者更清楚地把握知識點有巨大的幫助。

針對每一種_值_的類型，無論簡單複雜，都有相應的操作方式：

> * **操作符**
>   * 值運算
>   * 邏輯運算
> *  **函數**
>   * 內建函數
>   * 其他模塊里的函數
>   * 其本身所屬類之中所定義的函數

所以，接下來要學習的，無非就是熟悉各種_數據類型_，及其相應的操作，包括能對它們的_值_進行操作的操作符和函數；無論是操作符還是函數，最終都會返回一個相應的**值**，及其相應的*布爾值* —— 這麼看來，編程知識結構沒多複雜。因為換句話講，

> 接下來你要學習的無非是各種_數據類型_的_運算_而已。

另外，雖然現在尚未來得及對**函數**進行深入講解，但最終你會發現它跟操作符一樣，在程序里無所不在。

## 備註

另外，以下幾個鏈接先放在這裡，未來你會返回來參考它們，還是不斷地參考它們：

> * 關於表達式：https://docs.python.org/3/reference/expressions.html
> * 關於所有操作的優先級：https://docs.python.org/3/reference/expressions.html#operator-precedence
> * 上一條鏈接不懂 BNF 的話根本讀不懂：https://en.wikipedia.org/wiki/Backus-Naur_form
> * Python 的內建函數：https://docs.python.org/3/library/functions.html
> * Python 的標準數據類型：https://docs.python.org/3/library/stdtypes.html

另外，其實所有的操作符，在 Python 內部也是調用函數完成的……

> https://docs.python.org/3.7/library/operator.html
