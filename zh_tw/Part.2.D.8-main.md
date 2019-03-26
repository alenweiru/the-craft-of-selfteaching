
# 可執行的 Python 文件

理論上來講，你最終可以把任何一個程序，無論大小，都封裝（或者囊括）到僅僅一個函數之中。按照慣例（Convention），這個函數的名稱叫做 `main()`：
```python
def routine_1():
    print('Routine 1 done.')

def routine_2():
    sub_routine_1()
    sub_routine_2()
    print('Routine 2 done.')
    
def sub_routine_1():
    print('Sub-routine 1 done.')

def sub_routine_2():
    print('Sub-routine 2 done.')

def main():
    routine_1()
    routine_2()
    print('This is the end of the program.')
    
if __name__ == '__main__':
    main()
```
    Routine 1 done.
    Sub-routine 1 done.
    Sub-routine 2 done.
    Routine 2 done.
    This is the end of the program.


當一個模塊（其實就是存有 Python 代碼的 `.py` 文件）被導入，或者被執行的時候，這個模塊的 `__name__` 被設定為 `__main__`。

把一個程序整個封裝到 `main()` 之中，而後在模塊代碼裡加上：
```python
if __name__ == '__main__':
    main()
```
這麼做的結果是：

> 1. 當 Python 文件被當作模塊，被 `import` 語句導入時，`main()` 函數不被直接運行；
> 2. 當 Python 文件被 `python -m` 執行的時候，`main()` 才被執行。

還記得那個 Python 的彩蛋吧？`this.py` 的代碼如下：
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
所以，只要 `import this`，`this.py` 中的代碼就被執行：
```python
import this
```
我在當前目錄下，保存了一個文件 `that.py`，它的內容如下 —— 其實就是把 `this.py` 之中的代碼封裝到 `main()` 函數中了：
```python
# %load that.py
def main():
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


if __name__ == '__main__':
    main()
```
於是，當你在其它地方導入它的時候，`import that`，`main()` 函數的內容不會被執行：
```python
import that
```
但是，你在命令行中，用 `python that.py`，或者 `python -m that` 將 `that.py` 當作可執行模塊運行的時候，`main()` 就會被執行 —— 註意，不要寫錯，`python -m that.py` 會報錯的 —— 有 `-m` 參數，就不要寫文件尾綴 `.py`：
```bash
%%bash
python that.py
```
```bash
%%bash
python -m that
```
像 `that.py` 那樣把整個程序放進 `main()` 函數之後，`import that` 不會自動執行 main 函數里的代碼。不過，你可以調用 that.main() ：
```python
import that
that.main()
```
當然，`that.py` 之中沒有任何 Docstring，所以 `help(that)` 的結果是這樣的：
```python
import that
help(that)
```
所以，之前那個從 37 萬個詞彙中挑出 3700 個字母加起來等於 100 的詞彙的程序，也可以寫成以下形式：
```python
#!/usr/bin/env python

def sum_of_word(word):
    sum = 0
    for char in word:
        sum += ord(char) - 96
    return sum
def main(wordlist, result):
    with open(result, 'w') as result:
        with open(wordlist, 'r') as file:
            for word in file.readlines():
                if sum_of_word(word.strip()) == 100:
                    result.write(word)

if __name__ == '__main__':
    main('words_alpha.txt', 'results.txt')
```
至於以上代碼中的第一行，`#!/usr/bin/env python` 是怎麼回事兒，建議你自己動手解決一下，去 Google：

> [`python3 script executable`](https://www.google.com/search?q=python3+script+executable)

你會很快弄明白的……

另外，再搜索一下：

> [`python3 script executable parameters retrieving`](https://www.google.com/search?q=python3+script+executable+parameters+retrieving)

你就可以把以上程序改成在命令行下能夠接收指定參數的 Python 可執行文件……

順帶說，`import this` 的彩蛋有更好玩的玩法：
```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

import this
love = this
this is love                            # True
love is True                            # False
love is False                           # False
love is not True or False               # True
love is not True or False; love is love # True True
```
    True
    False
    False
    True
    True
    True



在 Terminal 里輸入 `python ⏎` 而後在 Interactive Shell 里逐句輸入試試。`love = this` 後面的每一句，都是布爾運算，想想看為什麼是那樣的結果？
```python
import this
love = this

this is love      
# True, 試試看，id(this) 和 id(love) 是同一個值
# 即，它們的內存地址相同

love is True       
# False, id(love) 和 id(True) 不是同一個值  
love is False      
# 同上


love is not True or False  
# is not 的優先級比 or 高；所以相當於是：
# (love is not True) or False，於是返回 True

love is not True or False; love is love  
# 重覆一次上一句 —— `;` 是語句分隔符
# 而後 love is love 當然是 True
```
註意以下代碼中，`id()` 函數的輸出結果：
```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

import this
love = this
this is love
love is True
love is False
love is not True or False
love is not True or False; love is love
id(love)
id(this)
id(True)
id(False)
love is not True
```
    True
    False
    False
    True
    True
    True
    4345330968
    4345330968
    4308348176
    4308349120
    True



Python 的操作符優先級，完整表格在這裡：

> [Operator precedence](https://docs.python.org/3/reference/expressions.html#operator-precedence)

Python 的更多彩蛋：

> [Python Easter Eggs](https://github.com/OrkoHunter/python-easter-eggs)
