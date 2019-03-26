
# 遞歸函數

## 遞歸（Recursion）

在函數中有個理解門檻比較高的概念：**遞歸函數**（Recursive Functions）—— 那些**在自身內部調用自身的函數**。說起來都比較拗口。

先看一個例子，我們想要有個能夠計算 `n` 的_階乘_（factorial） `n!` 的函數，`f()`，規則如下：

> - `n! = n × (n-1) × (n-2)... × 1`
> - 即，`n! = n × (n-1)!`
> - 且，`n >= 1`
>
> **註意**：以上是數學表達，不是程序，所以，`=` 在這一小段中是 “_等於_” 的意思，**不是程序語言中的賦值符號**。

於是，計算 `f(n)` 的 Python 程序如下：

```python
def f(n):
    if n == 1:
        return 1
    else:
        return n * f(n-1)
    
print(f(5))
```
    120


## 遞歸函數的執行過程

以 factorial(5) 為例，讓我們看看程序的流程（註意，圖片里的諸如 `n=5>1` 之類的標註，並不是程序語言表達式，只是對讀者的說明）:

![](../images/recursive-function-call.png)



當 f(5) 被調用之後，函數開始運行……
* 因為 `5 > 1`，所以，在計算 `n * f(n-1)` 的時候要再次調用自己 `f(4)`；所以必須等待 `f(4)` 的值返回；
* 因為 `4 > 1`，所以，在計算 `n * f(n-1)` 的時候要再次調用自己 `f(3)`；所以必須等待 `f(3)` 的值返回；
* 因為 `3 > 1`，所以，在計算 `n * f(n-1)` 的時候要再次調用自己 `f(2)`；所以必須等待 `f(2)` 的值返回；
* 因為 `2 > 1`，所以，在計算 `n * f(n-1)` 的時候要再次調用自己 `f(1)`；所以必須等待 `f(1)` 的值返回；
* 因為 `1 == 1`，所以，這時候不會再次調用 `f()` 了，於是遞歸結束，開始返回，這次返回的是 `1`；
* 下一步返回的是 `2 * 1`；
* 下一步返回的是 `3 * 2`；
* 下一步返回的是 `4 * 6`；
* 下一步返回的是 `5 * 24` ——至此，外部調用 `f(5)` 的最終返回值是 `120`……

加上一些輸出語句之後，能更清楚地看到大概的執行流程：
```python
def f(n):
    print('\tn =', n)
    if n == 1:
        print('Returning...')
        print('\tn =', n, 'return:', 1)
        return 1
    else:
        r = n * f(n-1)
        print('\tn =', n, 'return:', r)
        return r
    
print('Call f(5)...')
print('Get out of f(n), and f(5) =', f(5))
```
    Call f(5)...
    	n = 5
    	n = 4
    	n = 3
    	n = 2
    	n = 1
    Returning...
    	n = 1 return: 1
    	n = 2 return: 2
    	n = 3 return: 6
    	n = 4 return: 24
    	n = 5 return: 120
    Get out of f(n), and f(5) = 120


有點燒腦…… 不過，分為幾個層面去逐個突破，你會發現它真的很好玩。

## 遞歸的終點

遞歸函數在內部必須有一個能夠讓自己停止調用自己的方式，否則永遠循環下去了……

其實，我們所有人很小就見過遞歸應用，只不過，那時候不知道那就是遞歸而已。聽過那個無聊的故事罷？

> 山上有座廟，廟裡有個和尚，和尚講故事，說……
> > 山上有座廟，廟裡有個和尚，和尚講故事，說……
> > > 山上有座廟，廟裡有個和尚，和尚講故事，說……

寫成 Python 程序大概是這樣：
```python
def a_monk_telling_story():
    print('山上有座廟，廟裡有個和尚，和尚講故事，他說……')
    return a_monk_telling_story()

a_monk_telling_story()
```
這是個_無限循環_的遞歸，因為這個函數里_沒有設置中止自我調用的條件_。無限循環還有個不好聽的名字，叫做 “死循環”。

在著名的電影**盜夢空間**（_2010_）里，從整體結構上來看，“入夢” 也是個 “遞歸函數”。只不過，這個函數和 a_monk_telling_story() 不一樣，它並不是死循環 —— 因為它設定了_中止自我調用的條件_：

> 在電影里，醒過來的條件有兩個
>> * 一個是在夢裡死掉；
>> * 一個是在夢裡被 kicked 到……
>
> 如果這兩個條件一直不被滿足，那就進入 limbo 狀態 —— 其實就跟死循環一樣，出不來了……  

為了演示，我把故事情節改變成這樣：
> * 入夢， `in_dream()` ，是個遞歸函數；
> * 入夢之後醒過來的條件有兩個：
>> * 一個是在夢裡死掉， `dead is True`；
>> * 一個是在夢裡被 kicked， `kicked is True`……
>>
>> 以上兩個條件中任意一個被滿足，就蘇醒……

至於為什麼會死掉，如何被 kick，我偷懶了一下：管它怎樣，管它如何，反正，每個條件被滿足的概率是 1/10…… (也只有這樣，我才能寫出一個簡短的，能夠運行的 “_盜夢空間程序_”。）

把這個很抽象的故事寫成 Python 程序，看看一次入夢之後能睡多少天，大概是這樣：
```python
import random

def in_dream(day=0, dead=False, kicked=False):
    dead = not random.randrange(0,10) # 1/10 probability to be dead
    kicked = not random.randrange(0,10) # 1/10 probability to be kicked
    day += 1
    print('dead:', dead, 'kicked:', kicked)
    
    if dead:
        print((f"I slept {day} days, and was dead to wake up..."))
        return day
    elif kicked:
        print(f"I slept {day} days, and was kicked to wake up...")
        return day
    
    return in_dream(day)
    
print('The in_dream() function returns:', in_dream())
```
    dead: False kicked: False
    dead: False kicked: False
    dead: False kicked: False
    dead: False kicked: False
    dead: False kicked: False
    dead: False kicked: False
    dead: False kicked: False
    dead: True kicked: True
    I slept 8 days, and was dead to wake up...
    The in_dream() function returns: 8


如果疑惑為什麼 `random.randrange(0,10)` 能表示 1/10 的概率，請返回去重新閱讀[第一部分中關於布爾值的內容](Part.1.E.2.values-and-their-operators.md)。

另外，在 Python 中，若是需要將某個值於 True 或者 False 進行比較，尤其是在條件語句中，推薦寫法是（參見 [PEP8](https://www.python.org/dev/peps/pep-0008/)）：
```python
if condition:
    pass
```
就好像上面代碼中的 `if dead:` 一樣。

而不是（雖然這麼寫通常也並不妨礙程序正常運行<a href='#fn1' name='fn1b'><sup>[1]</sup></a>）：
```python
if condition is True:
    pass
```
抑或：
```python
if condition == True:
    pass
```
讓我們再返回來接著講遞歸函數。正常的**遞歸函數一定有個退出條件**。否則的話，就_無限循環_下去了…… 下麵的程序在執行一會兒之後就會告訴你：`RecursionError: maximum recursion depth exceeded`（上面那個 “山上廟裡講故事的和尚說” 的程序，真要跑起來，也是這樣）：
```python
def x(n):
    return n * x(n-1)
x(5)
```
    ---------------------------------------------------------------------------
    RecursionError                            Traceback (most recent call last)
    <ipython-input-3-daa4d33fb39b> in <module>
          1 def x(n):
          2     return n * x(n-1)
    ----> 3 x(5)
    
    <ipython-input-3-daa4d33fb39b> in x(n)
          1 def x(n):
    ----> 2     return n * x(n-1)
          3 x(5)
    ... last 1 frames repeated, from the frame below ...
    <ipython-input-3-daa4d33fb39b> in x(n)
          1 def x(n):
    ----> 2     return n * x(n-1)
          3 x(5)
    RecursionError: maximum recursion depth exceeded


不用深究上面盜夢空間這個程序的其它細節，不過，通過以上三個遞歸程序 —— 兩個很扯淡的例子，一個正經例子 —— 你已經看到了遞歸函數的共同特征：

> 1. 在 `return` 語句中返回的是_自身的調用_（或者是_含有自身的表達式_）
> 2. 為了避免死循環，_一定要有至少一個條件_下返回的不再是自身調用……

## 變量的作用域

再回來看計算階乘的程序 —— 這是正經程序。這次我們把程序名寫完整，`factorial()`:
```python
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))
```
    120


最初的時候，這個函數的執行流程之所以令人迷惑，是因為初學者對_變量_的**作用域**把握得不夠充分。

變量根據作用域，可以分為兩種：全局變量（Global Variables）和局部變量（Local Variables）。

可以這樣簡化理解：

> * 在函數內部被賦值而後使用的，都是*局部變量*，它們的作用域是_局部_，無法被函數外的代碼調用；
> * 在所有函數之外被賦值而後開始使用的，是*全局變量*，它們的作用域是_全局_，在函數內外都可以被調用。

定義如此，但通常程序員們會嚴格地遵守一條原則：

> 在函數內部絕對不調用全局變量。即便是必須改變全局變量，也只能通過函數的返回值在函數外改變全局變量。

你也必須遵守同樣的原則。而這個原則同樣可以在日常的工作生活中 “調用”：

> 做事的原則：自己的事兒自己做，別人的事兒，最多通過自己的產出讓他們自己去搞……

再仔細觀察一下以下代碼。當一個變量被當做參數傳遞給一個函數的時候，這個變量本身並不會被函數所改變。比如，`a = 5`，而後，再把 `a` 當作參數傳遞給 `f(a)` 的時候，這個函數當然應該返回它內部任務完成之後應該傳遞迴來的值，但 `a` 本身不會被改變。
```python
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
a = 5
b = factorial(a)   # a 並不會因此改變；
print(a, b)
a = factorial(a)   # 這是你主動為 a 再一次賦值……
print(a, b)
```
    5 120
    120 120


理解了這一點之後，再看 `factorial()` 這個遞歸函數的遞歸執行過程，你就能明白這個事實：

> 在每一次 factorial(n) 被調用的時候，它都會形成一個作用域，`n` 這個變量作為參數把它的值傳遞給了函數，*但是*，`n` 這個變量本身並不會被改變。

我們再修改一下上面的代碼：
```python
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
n = 5              # 這一次，這個變量名稱是 n
m = factorial(n)   # n 並不會因此改變；
print(n, m)
```
    5 120


在 `m = factorial(n)` 這一句中，`n` 被 `factorial()` 當做參數調用了，但無論函數內部如何操作，並不會改變變量 `n` 的值。

關鍵的地方在這裡：在函數內部出現的變量 `n`，和函數外部的變量 `n` 不是一回事兒 —— **它們只是名稱恰好相同而已**，函數參數定義的時候，用別的名稱也沒什麼區別：
```python
def factorial(x): # 在這個語句塊中出現的變量，都是局部變量
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)
    
n = 5           # 這一次，這個變量名稱是 n
m = factorial(n)   # n 並不會因此改變；
print(n, m)
# 這個例子和之前再之前的示例代碼有什麼區別嗎？
# 本質上沒區別，就是變量名稱換了而已……
```
    5 120


函數開始執行的時候，`x` 的值，是由外部代碼（即，函數被調用的那一句）傳遞進來的。即便函數內部的變量名稱與外部的變量名稱相同，它們也不是同一個變量。
```python
# 觀察一下名稱相同的一個全局變量和局部變量的不同內存地址
def f(n):
    return id(n)
    
n = 5
print(id(n))    # 全局變量 n 的內存地址
print(id(f(n))) # 局部變量 n 的內存地址。
```
    4430918896
    4467206608


## 遞歸函數三原則

現在可以小小總結一下了。

一個遞歸函數，之所以是一個有用、有效的遞歸函數，因為它要遵守遞歸三原則。正如，一個機器人之所以是個合格的機器人，因為它遵循[阿莫西夫三鐵律](https://zh.wikipedia.org/wiki/%E6%9C%BA%E5%99%A8%E4%BA%BA%E4%B8%89%E5%AE%9A%E5%BE%8B)（Three Laws of Robotics）一樣<a href='#fn2' name='fn2b'><sup>[2]</sup></a>。

> 1. 根據定義，遞歸函數必須在內部調用自己；
> 2. 必須設定一個退出條件；
> 3. 遞歸過程中必須能夠逐步達到退出條件……

從這個三原則望過去， `factorial()` 是個合格有效的遞歸函數，滿足第一條，滿足第二條，尤其還滿足第三條中的 “*逐步達到*”！

而那個扯淡的盜夢空間遞歸程序，說實話，不太合格，雖然它滿足第一條，也滿足第二條，第三條差點矇混過關：它不是*逐步達到*，而是*不管怎樣肯定能達到* —— 這明顯是兩回事兒…… 原諒它罷，它的作用就是當例子，一次正面的，一次負面的，作為例子算是功成圓滿了！

剛開始的時候，初學者好不容易搞明白遞歸函數究竟是怎麼回事兒之後，就不由自主地想 “我如何才能學會遞歸式思考呢？” —— 其實吧，這種想法本身可能並不是太正確或者準確。

準確地講，遞歸是一種解決問題的方式。當我們需要解決的問題，可以被逐步拆分成很多越來越小的模塊，然後每個小模塊還都能用同一種算法處理的時候，用遞歸函數最簡潔有效。所以，只不過是在遇到可以用遞歸函數解決問題的時候，才需要去寫遞歸函數。

從這個意義上來看，遞歸函數是程序員為了自己方便而使用的，並不是為了計算機方便而使用 —— 計算機麽，你給它的任務多一點或者少一點，對它來講無所謂，反正有電就能運轉，它自己又不付電費……

理論上來講，所有用遞歸函數能完成的任務，不用遞歸函數也能完成，只不過代碼多一點，啰嗦一點，看起來沒有那麼優美而已。

還有，遞歸，不像 “序列類型” 那樣，是某個編程語言的特有屬性。它其實是一種特殊算法，也是一種編程技巧，任何編程語言，都可以使用遞歸算法，都可以通過編寫遞歸函數巧妙地解決問題。

但是，學習遞歸函數本身就很燒腦啊！這才是最大的好事兒。從迷惑，到不太迷惑，到清楚，到很清楚，再到特別清楚 —— 這是個非常有趣，非常有成就感的過程。

這種過程鍛煉的是腦力 —— 在此之後，再遇到大多數人難以理解的東西，你就可以使用這一次積累的經驗，應用你已經磨煉過的腦力。有意思。

至此，封面上的那個 “偽代碼” 應該很好理解了：
```python
def teach_yourself(anything):
    while not create(something):
        learn()
        practice()
    return teach_yourself(another)

teach_yourself(coding)
```
自學還真的就是遞歸函數呢……

## 思考與練習

普林斯頓大學的一個網頁，有很多遞歸的例子

https://introcs.cs.princeton.edu/java/23recursion/
    

-----
**腳註**

<a name='fn1'>[1]</a>：參見 Stackoverflow 上的討論：[Boolean identity == True vs is True](https://stackoverflow.com/questions/27276610/boolean-identity-true-vs-is-true)

<a href='#fn1b'><small>↑Back to Content↑</small></a>


<a name='fn2'>[2]</a>：關於[阿莫西夫三鐵律](https://zh.wikipedia.org/wiki/%E6%9C%BA%E5%99%A8%E4%BA%BA%E4%B8%89%E5%AE%9A%E5%BE%8B)（Three Laws of Robotics）的類比，來自著名的 Python 教程，[Think Python: How to Think Like a Computer Scientist](http://greenteapress.com/thinkpython2/html/index.html)

<a href='#fn2b'><small>↑Back to Content↑</small>
