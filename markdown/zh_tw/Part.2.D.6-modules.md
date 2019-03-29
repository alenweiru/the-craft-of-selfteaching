
# 保存到文件的函數

寫好的函數，當然最好保存起來，以便將來隨時調用。

## 模塊

我們可以將以下內容保存到一個名為 `mycode.py` 的文件中 —— 這樣可以被外部調用的 `.py` 文件，有個專門的稱呼，**模塊**（Module）—— 於是，其實任何一個 `.py` 文件都可以被稱為_模塊_：
```python
# %load mycode.py
# 當前這個 Code Cell 中的代碼，保存在當前文件夾中的 mycode.py 文件中
# 以下的代碼，是使用 Jupyter 命令 %load mycode.py 導入到當前 Code Cell 中的：

def is_prime(n):
    """
    Return a boolean value based upon
    whether the argument n is a prime number.
    """
    if n < 2:
        return False
    if n == 2:
        return True
    for m in range(2, int(n**0.5)+1):
        if (n % m) == 0:
            return False
    else:
        return True

def say_hi(*names, greeting='Hello', capitalized=False):
    """
    Print a string, with a greeting to everyone.
    :param *names: tuple of names to be greeted.
    :param greeting: 'Hello' as default.
    :param capitalized: Whether name should be converted to capitalzed before print. False as default.
    :returns: None
    """
    for name in names:
        if capitalized:
            name = name.capitalize()
        print(f'{greeting}, {name}!')
```
而後，我們就可以在其它地方這樣使用（以上代碼現在已經保存在當前工作目錄中的 `mycode.py`）：
```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

import mycode

help(mycode.is_prime)
help(mycode.say_hi)

mycode.__name__
mycode.is_prime(3)
mycode.say_hi('mike', 'zoe')
```
    Help on function is_prime in module mycode:
    
    is_prime(n)
        Return a boolean value based upon
        whether the argument n is a prime number.
    
    Help on function say_hi in module mycode:
    
    say_hi(*names, greeting='Hello', capitalized=False)
        Print a string, with a greeting to everyone.
        :param *names: tuple of names to be greeted.
        :param greeting: 'Hello' as default.
        :param capitalized: Whether name should be converted to capitalzed before print. False as default.
        :returns: None
    
    Hello, mike!
    Hello, zoe!


以上這個**模塊**（[Module](https://docs.python.org/3/tutorial/modules.html)）的名稱，就是 `mycode`。

## 模塊文件系統目錄檢索順序

當你向 Python 說 `import ...` 的時候，它要去尋找你所指定的文件，那個文件應該是 `import` 語句後面引用的名稱，再加上 `.py` 構成的名字的文件。Python 會按照以下順序去尋找：

> * 先去看看內建模塊里有沒有你所指定的名稱；
> * 如果沒有，那麼就按照 `sys.path` 所返回的目錄列表順序去找。

你可以通過以下代碼查看你自己當前機器的 `sys.path`：
```python
import sys
sys.path
```
在 `sys.path` 所返回的目錄列表中，你當前的工作目錄排在第一位。

有時，你需要指定檢索目錄，因為你知道你要用的模塊文件在什麼位置，那麼可以用 `sys.path.append()` 添加一個搜索位置：
```python
import sys
sys.path.append("/My/Path/To/Module/Directory")
import my_module 
```
## 系統內建的模塊

你可以用以下代碼獲取系統內建模塊的列表：
```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

sys.builtin_module_names
"_sre" in sys.builtin_module_names # True
"math" in sys.builtin_module_names # True
```
    ('_abc',
     '_ast',
     '_codecs',
     '_collections',
     '_functools',
     '_imp',
     '_io',
     '_locale',
     '_operator',
     '_signal',
     '_sre',
     '_stat',
     '_string',
     '_symtable',
     '_thread',
     '_tracemalloc',
     '_warnings',
     '_weakref',
     'atexit',
     'builtins',
     'errno',
     'faulthandler',
     'gc',
     'itertools',
     'marshal',
     'posix',
     'pwd',
     'sys',
     'time',
     'xxsubtype',
     'zipimport')
    True
    False



跟變量名、函數名，不能與關鍵字重名一樣，你的模塊名稱也最好別與系統內建模塊名稱重合。

## 指定引入模塊中特定函數

當你使用 `import mycode` 的時候，你向當前工作空間引入了 `mycode` 文件中定義的所有函數，相當於：
```python
from mycode import *
```
你其實可以只引入當前需要的函數，比如，只引入 `is_prime()`
```python
from mycode import is_prime
```
這種情況下，你就不必使用 `mycode.is_prime()` 了；而是就好像這個函數就寫在當前工作空間一樣，直接寫 `is_prime()`：
```python
from mycode import is_prime
is_prime(3)
```
    True



註意，如果當前目錄中並沒有 `mycode.py` 這個文件，那麼，`mycode` 會被當作目錄名再被嘗試一次，如果當前目錄內，有個叫做 `mycode` 的目錄（或稱文件夾），那麼，`from mycode import *` 的作用就是把 `mycode` 這個文件夾中的所有 `.py` 文件全部導入……

如果我們想要導入 `foo` 這個目錄中的 `bar.py` 這個模塊文件，那麼，可以這麼寫：
```python
import foo.bar
```
或者
```python
from foo import bar
```
## 引入並使用化名

有的時候，或者為了避免混淆，或者為了避免輸入太多字符，我們可以為引入的函數設定 **化名**（alias），而後使用化名調用函數。比如：
```python
from mycode import is_prime as isp
isp(3)
```
    True



甚至乾脆給整個模塊取個化名：
```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

import mycode as m

m.is_prime(3)
m.say_hi('mike', 'zoe')
```
    True
    Hello, mike!
    Hello, zoe!


## 模塊中不一定只有函數

一個模塊文件中，不一定只包含函數；它也可以包含函數之外的可執行代碼。只不過，在 `import` 語句執行的時候，模塊中的非函數部分的可執行代碼，只執行一次。

有一個 Python 的彩蛋，恰好是可以用在此處的最佳例子 —— 這個模塊是 `this`，它的文件名是 [`this.py`](https://github.com/python/cpython/blob/master/Lib/this.py)：
```python
import this
```
    The Zen of Python, by Tim Peters
    
    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!


這個 `this` 模塊中的代碼如下：
```python
s = """Gur Mra bs Clguba, ol Gvz Crgref
Ornhgvshy vf orggre guna htyl.
Rkcyvpvg vf orggre guna vzcyvpvg.
Fvzcyr vf orggre guna pbzcyrk.
Pbzcyrk vf orggre guna pbzcyvpngrq.
Syng vf orggre guna arfgrq.
Fcnefr vf orggre guna qrafr.
Ernqnovyvgl pbhagf.
Fcrpvny pnfrf nera'g fcrpvny rabhtu gb oernx gur ehyrf.
Nygubhtu cenpgvpnyvgl orngf chevgl.
Reebef fubhyq arire cnff fvyragyl.
Hayrff rkcyvpvgyl fvyraprq.
Va gur snpr bs nzovthvgl, ershfr gur grzcgngvba gb thrff.
Gurer fubhyq or bar-- naq cersrenoyl bayl bar --boivbhf jnl gb qb vg.
Nygubhtu gung jnl znl abg or boivbhf ng svefg hayrff lbh'er Qhgpu.
Abj vf orggre guna arire.
Nygubhtu arire vf bsgra orggre guna *evtug* abj.
Vs gur vzcyrzragngvba vf uneq gb rkcynva, vg'f n onq vqrn.
Vs gur vzcyrzragngvba vf rnfl gb rkcynva, vg znl or n tbbq vqrn.
Anzrfcnprf ner bar ubaxvat terng vqrn -- yrg'f qb zber bs gubfr!"""

d = {}
for c in (65, 97):
    for i in range(26):
        d[chr(i+c)] = chr((i+13) % 26 + c)

print("".join([d.get(c, c) for c in s]))
```
這個 `this.py` 文件中也沒有什麼函數，但這個文件里所定義的變量，我們都可以在 `import this` 之後觸達：
```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

import this
this.d
this.s
```
    {'A': 'N',
     'B': 'O',
     'C': 'P',
     'D': 'Q',
     'E': 'R',
     'F': 'S',
     'G': 'T',
     'H': 'U',
     'I': 'V',
     'J': 'W',
     'K': 'X',
     'L': 'Y',
     'M': 'Z',
     'N': 'A',
     'O': 'B',
     'P': 'C',
     'Q': 'D',
     'R': 'E',
     'S': 'F',
     'T': 'G',
     'U': 'H',
     'V': 'I',
     'W': 'J',
     'X': 'K',
     'Y': 'L',
     'Z': 'M',
     'a': 'n',
     'b': 'o',
     'c': 'p',
     'd': 'q',
     'e': 'r',
     'f': 's',
     'g': 't',
     'h': 'u',
     'i': 'v',
     'j': 'w',
     'k': 'x',
     'l': 'y',
     'm': 'z',
     'n': 'a',
     'o': 'b',
     'p': 'c',
     'q': 'd',
     'r': 'e',
     's': 'f',
     't': 'g',
     'u': 'h',
     'v': 'i',
     'w': 'j',
     'x': 'k',
     'y': 'l',
     'z': 'm'}
    "Gur Mra bs Clguba, ol Gvz Crgref\n\nOrnhgvshy vf orggre guna htyl.\nRkcyvpvg vf orggre guna vzcyvpvg.\nFvzcyr vf orggre guna pbzcyrk.\nPbzcyrk vf orggre guna pbzcyvpngrq.\nSyng vf orggre guna arfgrq.\nFcnefr vf orggre guna qrafr.\nErnqnovyvgl pbhagf.\nFcrpvny pnfrf nera'g fcrpvny rabhtu gb oernx gur ehyrf.\nNygubhtu cenpgvpnyvgl orngf chevgl.\nReebef fubhyq arire cnff fvyragyl.\nHayrff rkcyvpvgyl fvyraprq.\nVa gur snpr bs nzovthvgl, ershfr gur grzcgngvba gb thrff.\nGurer fubhyq or bar-- naq cersrenoyl bayl bar --boivbhf jnl gb qb vg.\nNygubhtu gung jnl znl abg or boivbhf ng svefg hayrff lbh'er Qhgpu.\nAbj vf orggre guna arire.\nNygubhtu arire vf bsgra orggre guna *evtug* abj.\nVs gur vzcyrzragngvba vf uneq gb rkcynva, vg'f n onq vqrn.\nVs gur vzcyrzragngvba vf rnfl gb rkcynva, vg znl or n tbbq vqrn.\nAnzrfcnprf ner bar ubaxvat terng vqrn -- yrg'f qb zber bs gubfr!"



試試吧，試試能否獨立讀懂這個文件里的代碼 —— 對初學者來說，還是挺練腦子的呢！

它先是通過一個規則生成了一個密碼表，保存在 `d` 這個字典中；而後，將 `s` 這個變量中保存的 “密文” 翻譯成了英文……

或許，你可以試試，看看怎樣能寫個函數出來，給你一段英文，你可以把它加密成跟它一樣的 “密文”？

## dir() 函數

你的函數，保存在模塊里之後，這個函數的用戶（當然也包括你），可以用 `dir()` 函數查看模塊中可觸達的變量名稱和函數名稱：
```python
import mycode
dir(mycode)
```
    ['__builtins__',
     '__cached__',
     '__doc__',
     '__file__',
     '__loader__',
     '__name__',
     '__package__',
     '__spec__',
     'is_prime',
     'say_hi']


