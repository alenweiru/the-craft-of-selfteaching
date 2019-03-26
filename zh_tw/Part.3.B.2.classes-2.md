
# 類 —— Python 的實現

既然已經在不碰代碼的情況下，把 OOP 中的主要概念梳理清楚了，以下的行文中，那些概念就直接用英文罷，省得理解上還得再繞個彎……

## Defining Class

Class 使用 `class` 關鍵字進行定義。

與函數定義不同的地方在於，Class 接收參數不是在 `class Classname():` 的括號里完成 —— 那個圓括號有另外的用處。

讓我們先看看代碼，而後再逐一解釋：
```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
import datetime

class Golem:
    
    def __init__(self, name=None):
        self.name = name
        self.built_year = datetime.date.today().year
    
    def say_hi(self):
        print('Hi!')
        
g = Golem('Clay')
g.name
g.built_year
g.say_hi
g.say_hi()
type(g)
type(g.name)
type(g.built_year)
type(g.__init__)
type(g.say_hi)
```
    'Clay'
    2019
    <bound method Golem.say_hi of <__main__.Golem object at 0x107bac278>>
    Hi!
    __main__.Golem
    str
    int
    method
    method



以上，我們創建了一個 Class:
```python
class Golem:
    
    def __init__(self, name=None):
        self.name = name
        self.built_year = datetime.date.today().year
```
其中定義了當我們根據這個 Class 創建一個實例的時候，那個 Object 的初始化過程，即 `__init__()` 函數 —— 又由於這個函數是在 Class 中定義的，我們稱它為 Class 的一個 Method。

這裡的 `self` 就是個變量，跟程序中其它變量的區別在於，它是一個系統默認可以識別的變量，用來指代將來用這個 Class 創建的 Instance。

比如，我們創建了 Golem 這個 Class 的一個 Instance，`g = Golem('Clay')` 之後，我們寫 `g.name`，那麼解析器就去找 `g` 這個實例所在的 Scope 里有沒有 `self.name`…… 

註意：`self` 這個變量的定義，是在 `def __init__(self, ...)` 這一句里完成的。對於這個變量的名稱取名沒有強制要求，你實際上可以隨便用什麼名字，很多 C 程序員會習慣於將這個變量命名為 `this` —— 但根據慣例，你最好還是只用 `self` 這個變量名，省得給別人造成誤會。

在 Class 的代碼中，如果定義了 `__init__()` 函數，那麼系統就會將它當作用來 Instance 在創建後被初始化的函數。這個函數名稱是強制指定的，初始化函數必須使用這個名稱；註意 `init` 兩端各有兩個下劃線 `_`。

當我們用 `g = Golem('Clay')` 這一句創建了一個 Golam 的 Instance 的時候，以下一連串的事情發生了：

> * `g` 從此之後就是一個根據 Golem 這個 Class 創建的 Instance，對使用者來說，它就是個 Object；
> * 因為 Golem 這個 Class 的代碼中有 `__init__()`，所以，當 `g` 被創建的時候，`g` 就需要被初始化……
> * 在 `g` 所在的變量目錄中，出現了一個叫做 `self` 的用來指代 `g` 本身的變量；
> * self.name 接收了一個參數，`'Clay'`，並將其保存了下來；
> * 生成了一個叫做 `self.built_year` 的變量，其中保存的是 `g` 這個 Object 被創建時的年份……

對了，Golem 和 Robot 一樣，都是機器人的意思；Golem 的本義來自於猶太神話，一個被賦予了生命的泥人……

## Inheritance

我們剛剛創建了一個 Golem Class，如果我們想用它 Inherite 一個新的 Class，比如，`Running_Golem`，一個能跑的機器人，那就像以下的代碼那樣做 —— 註意 `class Running_Golem` 之後的圓括號：
```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
import datetime

class Golem:
    
    def __init__(self, name=None):
        self.name = name
        self.built_year = datetime.date.today().year
    
    def say_hi(self):
        print('Hi!')

class Running_Golem(Golem):      # 剛剛就說，這個圓括號另有用途……
    
    def run(self):
        print("Can't you see? I'm running...")

rg = Running_Golem('Clay')
rg.run
rg.run()
rg.name
rg.built_year
rg.say_hi()
```
    Can't you see? I'm running...
    Hi!


如此這般，我們根據 Golem 這個 Class 創造了一個 Subclass —— `Running_Golem`，既然它是 Golem 的 Inheritance，那麼 Golem 有的 Attributes 和 Methods 它都有，並且還多了一個 Method —— `self.run`。

## Overrides

當我們創建一個 Inherited Class 的時候，可以重寫（Overriding）Parent Class 中的 Methods。比如這樣：
```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
import datetime

class Golem:
    
    def __init__(self, name=None):
        self.name = name
        self.built_year = datetime.date.today().year
    
    def say_hi(self):
        print('Hi!')

class runningGolem(Golem):
    
    def run(self):
        print("Can't you see? I'm running...")
    
    def say_hi(self):                            # 不再使用 Parent Class 中的定義，而是新的……
        print('Hey! Nice day, Huh?')

rg = runningGolem('Clay')
rg.run
rg.run()
rg.name
rg.built_year
rg.say_hi()
```
    <bound method runningGolem.run of <__main__.runningGolem object at 0x1056f9358>>
    Can't you see? I'm running...
    'Clay'
    2019
    Hey! Nice day, Huh?


## Inspecting A Class

當我們作為用戶想瞭解一個 Class 的 Interface，即，它的 Attributes 和 Methods 的時候，常用的有三種方式：
```python
1. help(object)
2. dir(object)
3. object.__dict__
```
```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
import datetime

class Golem:
    
    def __init__(self, name=None):
        self.name = name
        self.built_year = datetime.date.today().year
    
    def say_hi(self):
        print('Hi!')

class runningGolem(Golem):
    
    def run(self):
        print('Can\'t you see? I\'m running...')
    
    def say_hi(self):                            # 不再使用 Parent Class 中的定義，而是新的……
        print('Hey! Nice day, Huh?')

rg = runningGolem('Clay')
help(rg)
dir(rg)
rg.__dict__
hasattr(rg, 'built_year')
```
    Help on runningGolem in module __main__ object:
    
    class runningGolem(Golem)
     |  runningGolem(name=None)
     |  
     |  Method resolution order:
     |      runningGolem
     |      Golem
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  run(self)
     |  
     |  say_hi(self)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from Golem:
     |  
     |  __init__(self, name=None)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from Golem:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    
    ['__class__',
     '__delattr__',
     '__dict__',
     '__dir__',
     '__doc__',
     '__eq__',
     '__format__',
     '__ge__',
     '__getattribute__',
     '__gt__',
     '__hash__',
     '__init__',
     '__init_subclass__',
     '__le__',
     '__lt__',
     '__module__',
     '__ne__',
     '__new__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__setattr__',
     '__sizeof__',
     '__str__',
     '__subclasshook__',
     '__weakref__',
     'built_year',
     'name',
     'run',
     'say_hi']
    {'name': 'Clay', 'built_year': 2019}
    True



## Scope

每個變量都屬於某一個 **Scope**（變量的作用域），在同一個 Scope 中，變量可以被引用被操作…… 這麼說非常抽象，難以理解 —— 只能通過例子說明。

我們先給 Golem 這個 Class 增加一點功能 —— 我們需要隨時知道究竟有多少個 Golem 處於活躍狀態…… 也因此順帶給 Golem 加上一個 Method： `cease()` —— 哈！機器人麽，想關掉它，說關掉它，就能關掉它；

另外，我們還要給機器人設置個使用年限，比如 10 年；

…… 而外部會每隔一段時間，用 `Golem.is_active()` 去檢查所有的機器人，所以，不需要外部額外操作，到了年頭，它能應該關掉自己。—— 當然，又由於以下代碼是簡化書寫的，核心目的是為了講解 Scope，所以並沒有專門寫模擬 10 年後某些機器人自動關閉的情形……

在運行以下代碼之前，需要先介紹三個 Python 的內建函數：

> * `hasattr(object, attr)` 查詢這個 `object` 中有沒有這個 `attr`，返回布爾值
> * `getattr(object, attr)` 獲取這個 `object` 中這個 `attr` 的值
> * `setattr(object, attr, value)` 將這個 `object` 中的 `attr` 值設置為 `value`

現在的你，應該一眼望過去，就已經能掌握這三個內建函數的用法 —— 還記得之前的你嗎？眼睜睜看著，那些字母放在那裡對你來說沒任何意義…… 這才多久啊！
```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
import datetime

class Golem:
    population = 0
    __life_span = 10
    
    def __init__(self, name=None):
        self.name = name
        self.built_year = datetime.date.today().year
        self.__active = True
        Golem.population += 1
    
    def say_hi(self):
        print('Hi!')
    
    def cease(self):
        self.__active = False
        Golem.population -= 1          # 執行一遍之後，試試把這句改成 population += 1
    
    def is_active(self):
        if datetime.date.today().year - self.built_year >= Golem.__life_span:
            self.cease()
        return self.__active

g = Golem()
hasattr(Golem, 'population')      # True
hasattr(g, 'population')          # True
hasattr(Golem, '__life_span')     # False
hasattr(g, '__life_span')         # False
hasattr(g, '__active')            # False
Golem.population                  # 1
setattr(Golem, 'population', 10) 
Golem.population                  # 10
x = Golem()
Golem.population                  # 11
x.cease()
Golem.population                  # 10
getattr(g, 'population')          # 10
g.is_active()
```
    True
    True
    False
    False
    False
    1
    10
    11
    10
    10
    True



如果你試過把第 13 行的 `Golem.population += 1` 改成 `population += 1`，你會被如下信息提醒：
```python
     12         self.__active = True
---> 13         population += 1
UnboundLocalError: local variable 'population' referenced before assignment
```
—— 本地變量 `population` 尚未賦值，就已經提前被引用…… 為什麼會這樣呢？因為在你所創建 `g` 之後，馬上執行的是 `__init()__` 這個初始化函數，而 `population` 是在這個函數之外定義的……

如果你足夠細心，你會發現這個版本中，有些變量前面有兩個下劃線 `__`，比如，`__life_span` 和 `self.__active`。這是 Python 的定義，變量名前面加上一個以上下劃線（Underscore） `_` 的話，那麼該變量是 “私有變量”（Private Variables），不能被外部引用。而按照 Python 的慣例，我們會使用兩個下劃線起始，去命名私有變量，如： `__life_span`。你可以回去試試，把所有的 `__life_span` 改成 `_life_span`（即，變量名開頭只有一個 `_`，那麼，`hasattr(Golem, '_life_span')` 和 `hasattr(g, '_life_span')` 的返回值就都變成了 `True`。

看看下麵的圖示，理解起來更為直觀一些：

![](../images/class-variables-scope.png)

整個代碼啟動之後，總計有 4 個 Scopes 如圖所示：

> * ① `class Golem` 之外；
> * ② `class Golem` 之內；
> * ③ `__init__(self, name=None)` 之內；
> * ④ `cease(self)` 之內；

在 Scope ① 中，可以引用 `Golem.population`，在生成一個 Golem 的實例 `g` 之後，也可以引用 `g.population`；但 `Golem.__life_span` 和 `g.__active` 在 Scope ① 是不存在的；

在 Scope ② 中，存在兩個變量，`population` 和 `__life_span`；而 `__life_span` 是 Private（私有變量，因為它的變量名中前兩個字符是下劃線 `__`；於是，在 Scope ① 中，不存在 `Golem.__life_span` —— `hasattr(Golem, '__life_span')` 的值為 `False`；

在 Scope ③ 中和 Scope ④ 中，由於都給它們傳遞了 `self` 這個參數，於是，在這兩個 Scope 里，都可以引用 `self.xxx`，比如 `self.population`，比如 `self.__life_span`；

在 Scope ③ 中，`population` 是不存在的，如果需要引用這個值，可以用 `Golem.population`，也可以用 `self.population`。同樣的道理，在 Scope ③ 中 `__life_span` 也不存在，如果想用這個值，可以用 `Golem.__life_span` 或者 `self.__life_span`；

Scope ④ 與 Scope ③ 平行存在。所以在這裡，`population` 和 `__life_span` 也同樣並不存在。


## Encapsulation

到目前為止，Golem 這個 Class 看起來不錯，但有個問題，它裡面的數據，外面是可以隨便改的 —— 雖然，我們已經通過給變量 life_span 前面加上兩個下劃線，變成 `__life_span`，使其成為私有變量，外部不能觸達（你不能引用 `Golem.__life_span`），可 Golem.population 就不一樣，外面隨時可以引用，還可以隨時修改它，只需要寫上一句：
```python
Golem.population = 1000000
```
我們乾脆把 `population` 這個變量也改成私有的罷：`__population`，而後需要從外界查看這個變量的話，就在 Class 裡面寫個函數，返回那個值好了：
```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
import datetime

class Golem:
    __population = 0
    __life_span = 10
    
    def __init__(self, name=None):
        self.name = name
        self.built_year = datetime.date.today().year
        self.__active = True
        Golem.__population += 1
    
    def say_hi(self):
        print('Hi!')
    
    def cease(self):
        self.__active = False
        Golem.__population -= 1
    
    def is_active(self):
        if datetime.date.today().year - self.built_year >= Golem.__life_span:
            self.cease
        return self.__active
    
    def population(self):
        return Golem.__population

g = Golem('Clay')
g.population
g.population()
```
    <bound method Golem.population of <__main__.Golem object at 0x1036f5cc0>>
    1



如果，你希望外部能夠像獲得 Class 的屬性那樣，直接寫 `g.population`，而不是必須加上一個括號 `g.population()` 傳遞參數（實際上傳遞了一個隱含的 `self` 參數），那麼可以在 `def population(self):` 之前的一行加上一句 `@property`：
```python
class Golem:
    __population = 0
    ...
    
    @property
    def population(self):
        return Golem.__population
```
如此這般之後，你就可以用 `g.population` 了：
```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
import datetime

class Golem:
    __population = 0
    __life_span = 10
    
    def __init__(self, name=None):
        self.name = name
        self.built_year = datetime.date.today().year
        self.__active = True
        Golem.__population += 1
    
    def say_hi(self):
        print('Hi!')
    
    def cease(self):
        self.__active = False
        Golem.__population -= 1
    
    def is_active(self):
        if datetime.date.today().year - self.built_year >= Golem.__life_span:
            self.cease
        return self.__active
    
    @property
    def population(self):
        return Golem.__population

g = Golem('Clay')
g.population
# g.population = 100
```
    1



如此這般之後，不僅你可以直接引用 `g.population`，並且，在外部不能再直接給 `g.population` 賦值了，否則會報錯：
```python
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-16-5d8c475304d3> in <module>
     26 g = Golem('Clay')
     27 g.population
---> 28 g.population = 100

AttributeError: can't set attribute
```
到此為止，Encapsulation 就做得不錯了。

如果你非得希望從外部可以設置這個值，那麼，你就得再寫個函數，並且在函數之前加上一句：
```python
    ...
    
    @property
    def population(self):
        return Golem.__population
    
    @population.setter
    def population(self, value):
        Golem.__population = value
```
這樣之後，`.population` 這個 Attribute 就可以從外部被設定其值了（雖然在當前的例子中顯得沒必要讓外部設定 `__population` 這個值…… 以下僅僅是為了舉例）：
```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
import datetime

class Golem:
    __population = 0
    __life_span = 10
    
    def __init__(self, name=None):
        self.name = name
        self.built_year = datetime.date.today().year
        self.__active = True
        Golem.__population += 1
    
    def say_hi(self):
        print('Hi!')
    
    def cease(self):
        self.__active = False
        Golem.__population -= 1
    
    def is_active(self):
        if datetime.date.today().year - self.built_year >= Golem.__life_span:
            self.cease
        return self.__active
    
    @property
    def population(self):
        return Golem.__population
    
    @population.setter
    def population(self, value):
        Golem.__population = value

g = Golem('Clay')
g.population
g.population = 100
ga = Golem('New')
g.population
ga.population
help(Golem)
Golem.__dict__
g.__dict__
hasattr(Golem, 'population')
getattr(Golem, 'population')
setattr(Golem, 'population', 10000)
g.population    # 所以，在很多的情況下，不把數據封裝在 Class 內部的話，後面會很有很多麻煩。
```
    Help on class Golem in module __main__:
    
    class Golem(builtins.object)
     |  Golem(name=None)
     |  
     |  Methods defined here:
     |  
     |  __init__(self, name=None)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  cease(self)
     |  
     |  is_active(self)
     |  
     |  say_hi(self)
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  population
    
    10000


