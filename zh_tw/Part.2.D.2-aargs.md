
# 關於參數（下）

## 可以接收一系列值的位置參數

如果你在定義參數的時候，在一個_位置參數_（Positional Arguments）前面標註了星號，`*`，那麼，這個位置參數可以接收一系列值，在函數內部可以對這一系列值用 `for ... in ...` 循環進行逐一的處理。

帶一個星號的參數，英文名稱是 “Arbitrary Positional Arguments”，姑且翻譯為 “隨意的位置參數”。

還有帶兩個星號的參數，一會兒會講到，英文名稱是 “Arbitrary Keyword Arguments”，姑且翻譯為 “隨意的關鍵字參數”。

> 有些中文書籍把 “Arbitrary Positional Arguments” 翻譯成 “可變位置參數”。事實上，在這樣的地方，無論怎樣的中文翻譯都是令人覺得非常吃力的。前面的這個翻譯還好了，我還見過把 “Arbitrary Keyword Arguments” 翻譯成 “武斷的關鍵字參數” 的 —— 我覺得這樣的翻譯肯定會使讀者產生說不明道不白的疑惑。
>
> 所以，**入門之後就儘量只用英文**是個好策略。雖然剛開始有點吃力，但後面會很省心，很長壽 —— 是呀，少浪費時間、少浪費生命，其實就相當於更長壽了呀！
```python
def say_hi(*names):
    for name in names:
        print(f'Hi, {name}!')
say_hi()
say_hi('ann')
say_hi('mike', 'john', 'zeo')
```
    Hi, ann!
    Hi, mike!
    Hi, john!
    Hi, zeo!


`say_hi()` 這一行沒有任何輸出。因為你在調用函數的時候，沒有給它傳遞任何值，於是，在函數內部代碼執行的時候，`name in names` 的值是 `False`，所以，`for` 循環內部的代碼沒有被執行。

在函數內部，是把 `names` 這個參數當作容器處理的 —— 否則也沒辦法用 `for ... in ...` 來處理。而在調用函數的時候，我們是可以將一個容器傳遞給函數的 Arbitrary Positional Arugments 的 —— 做法是，在調用函數的時候，在參數前面加上星號 `*`： 
```python
def say_hi(*names):
    for name in names:
        print(f'Hi, {name}!')

names = ('mike', 'john', 'zeo')
say_hi(*names)
```
    Hi, mike!
    Hi, john!
    Hi, zeo!


實際上，因為以上的 `say_hi(*names)` 函數內部就是把接收到的參數當作容器處理的，於是，在調用這個函數的時候，向它傳遞任何容器都會被同樣處理：
```python
def say_hi(*names):
    for name in names:
        print(f'Hi, {name}!')

a_string = 'Python'
say_hi(*a_string)

a_range = range(10)
say_hi(*a_range)

a_list = list(range(10, 0, -1))
say_hi(*a_list)

a_dictionary = {'ann':2321, 'mike':8712, 'joe': 7610}
say_hi(*a_dictionary)
```
    Hi, P!
    Hi, y!
    Hi, t!
    Hi, h!
    Hi, o!
    Hi, n!
    Hi, 0!
    Hi, 1!
    Hi, 2!
    Hi, 3!
    Hi, 4!
    Hi, 5!
    Hi, 6!
    Hi, 7!
    Hi, 8!
    Hi, 9!
    Hi, 10!
    Hi, 9!
    Hi, 8!
    Hi, 7!
    Hi, 6!
    Hi, 5!
    Hi, 4!
    Hi, 3!
    Hi, 2!
    Hi, 1!
    Hi, ann!
    Hi, mike!
    Hi, joe!


_在定義可以接收一系列值的位置參數時，建議在函數內部為該變量命名時總是用**複數**_，因為函數內部，總是需要 `for` 循環去迭代元組中的元素，這樣的時候，名稱的複數形式對代碼的可讀性很有幫助 —— 註意以上程序第二行。以中文為母語的人，在這個細節上常常感覺 “不堪重負” —— 因為中文的名詞沒有複數 —— 但必須習慣。（同樣的道理，若是用拼音命名變量，就肯定是為將來挖坑……）

**註意**：一個函數中，可以接收一系列值的位置參數只能有一個；並且若是還有其它位置參數存在，那就必須把這個可以接收一系列值的位置參數排在所有其它位置參數之後。
```python
def say_hi(greeting, *names):
    for name in names:
        print(f'{greeting}, {name.capitalize()}!')

say_hi('Hello', 'mike', 'john', 'zeo')
```
    Hello, Mike!
    Hello, John!
    Hello, Zeo!


## 為函數的某些參數設定默認值

可以在定義函數的時候，為某些參數設定默認值，這些有默認值的參數，又被稱作關鍵字參數（Keyword Arguments）。從這個函數的 “用戶” 角度來看，這些設定了默認值的參數，就成了 “可選參數”。
```python
def say_hi(greeting, *names, capitalized=False):
    for name in names:
        if capitalized:
            name = name.capitalize()
        print(f'{greeting}, {name}!')

say_hi('Hello', 'mike', 'john', 'zeo')
say_hi('Hello', 'mike', 'john', 'zeo', capitalized=True)
```
    Hello, mike!
    Hello, john!
    Hello, zeo!
    Hello, Mike!
    Hello, John!
    Hello, Zeo!


##  可以接收一系列值的關鍵字參數

之前我們看到，可以設定一個位置參數（Positional Argument），接收一系列的值，被稱作 “Arbitrary Positional Argument”；

同樣地，我們也可以設定一個可以接收很多值的關鍵字參數（Arbitrary Keyword Argument）。
```python
def say_hi(**names_greetings):
    for name, greeting in names_greetings.items():
        print(f'{greeting}, {name}!')
        
say_hi(mike='Hello', ann='Oh, my darling', john='Hi')
```
    Hello, mike!
    Oh, my darling, ann!
    Hi, john!


既然在函數內部，我們在處理接收到的 Arbitrary Keyword Argument 時，用的是對字典的迭代方式，那麼，在調用函數的時候，也可以直接使用字典的形式：
```python
def say_hi(**names_greetings):
    for name, greeting in names_greetings.items():
        print(f'{greeting}, {name}!')
        
a_dictionary = {'mike':'Hello', 'ann':'Oh, my darling', 'john':'Hi'}
say_hi(**a_dictionary)

say_hi(**{'mike':'Hello', 'ann':'Oh, my darling', 'john':'Hi'})
```
    Hello, mike!
    Oh, my darling, ann!
    Hi, john!
    Hello, mike!
    Oh, my darling, ann!
    Hi, john!


至於在函數內部，你用什麼樣的迭代方式去處理這個字典，是你自己的選擇：
```python
def say_hi_2(**names_greetings):
    for name in names_greetings:
        print(f'{names_greetings[name]}, {name}!')
say_hi_2(mike='Hello', ann='Oh, my darling', john='Hi')
```
    Hello, mike!
    Oh, my darling, ann!
    Hi, john!


## 函數定義時各種參數的排列順序

在定義函數的時候，各種不同類型的參數應該按什麼順序擺放呢？對於之前寫過的 `say_hi()` 這個函數，
```python
def say_hi(greeting, *names, capitalized=False):
    for name in names:
        if capitalized:
            name = name.capitalize()
        print(f'{greeting}, {name}!')

say_hi('Hi', 'mike', 'john', 'zeo')
say_hi('Welcome', 'mike', 'john', 'zeo', capitalized=True)
```
    Hi, mike!
    Hi, john!
    Hi, zeo!
    Welcome, Mike!
    Welcome, John!
    Welcome, Zeo!


如果，你想給其中的 `greeting` 參數也設定個默認值怎麼辦？寫成這樣好像可以：
```python
def say_hi(greeting='Hello', *names, capitalized=False):
    for name in names:
        if capitalized:
            name = name.capitalize()
        print(f'{greeting}, {name}!')

say_hi('Hi', 'mike', 'john', 'zeo')
say_hi('Welcome', 'mike', 'john', 'zeo', capitalized=True)
```
    Hi, mike!
    Hi, john!
    Hi, zeo!
    
    Welcome, Mike!
    Welcome, John!
    Welcome, Zeo!


但 `greeting` 這個參數雖然有默認值，可這個函數在被調用的時候，還是必須要給出這個參數，否則輸出結果出乎你的想象：
```python
def say_hi(greeting='Hello', *names, capitalized=False):
    for name in names:
        if capitalized:
            name = name.capitalize()
        print(f'{greeting}, {name}!')

say_hi('mike', 'john', 'zeo')
```
    mike, john!
    mike, zeo!


設定了默認值的 `greeting`，竟然不像你想象的那樣是 “可選參數”！所以，你得這樣寫：
```python
def say_hi(*names, greeting='Hello', capitalized=False):
    for name in names:
        if capitalized:
            name = name.capitalize()
        print(f'{greeting}, {name}!')

say_hi('mike', 'john', 'zeo')
say_hi('mike', 'john', 'zeo', greeting='Hi')
```
    Hello, mike!
    Hello, john!
    Hello, zeo!
    Hi, mike!
    Hi, john!
    Hi, zeo!


這是因為函數被調用時，面對許多參數，Python 需要按照既定的規則（即，順序）判定每個參數究竟是哪一類型的參數：

> **Order of Arguments**
> 1. Positional
> 1. Arbitrary Positional
> 1. Keyword
> 1. Arbitrary Keyword

所以，即便你在定義里寫成
```python
def say_hi(greeting='Hello', *names, capitalized=False):
    ...
```
在調用該函數的時候，無論你寫的是
```python
say_hi('Hi', 'mike', 'john', 'zeo')
```
還是
```python
say_hi('mike', 'john', 'zeo')
```
Python 都會認為接收到的第一個值是 Positional Argument —— 因為在定義中，`greeting` 被放到了 Arbitrary Positional Arguments 之前。
