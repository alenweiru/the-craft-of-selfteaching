
# 文件

我們需要處理的數據，一定是很多，所以才必須由計算機幫我們處理 —— 大量的數據保存、讀取、寫入，需要的就是文件（Files）。在這一章里，我們只介紹最簡單的文本文件。

## 創建文件

創建一個文件，最簡單的方式就是用 Python 的內建函數 `open()` 。

`open()` 函數的[官方文檔](https://docs.python.org/3/library/functions.html#open)很長，以下是個簡化版：

> `open(file, mode='r')`

第二個參數，`mode`，默認值是 `'r'`，可用的 `mode` 有以下幾種：

| 參數字符 | 意義                            |
| -------- | ------------------------------- |
| `'r'`    | 只讀模式                        |
| `'w'`    | 寫入模式（重建）                |
| `'x'`    | 排他模式 —— 如果文件已存在則打開失敗 |
| `'a'`    | 追加模式 —— 在已有文件末尾追加      |
| `'b'`    | 二進制文件模式                  |
| `'t'`    | 文本文件模式 (默認)             |
| `'+'`    | 讀寫模式（更新）                |

創建一個新文件，用這樣一個語句就可以：
```python
open('test-file.txt', 'w')
```
    <_io.TextIOWrapper name='test-file.txt' mode='w' encoding='UTF-8'>



當然，更多的時候，我們會把這個函數的返回值，一個所謂的 [file object](https://docs.python.org/3/glossary.html#term-file-object)，保存到一個變量中，以便後面調用這個 file object 的各種 Methods，比如獲取文件名 `file.name`，比如關閉文件 `file.close()`：
```python
f = open('test-file.txt', 'w')
print(f.name)
f.close()
```
    test-file.txt


## 刪除文件

刪除文件，就得調用 `os` 模塊了。刪除文件之前，要先確認文件是否存在，否則刪除命令會失敗。
```python
import os

f = open('test-file.txt', 'w')
print(f.name)

if os.path.exists(f.name):
    os.remove(f.name)
    print(f'{f.name} deleted.')
else:
    print(f'{f.name} does not exist')
```
    test-file.txt
    test-file.txt deleted.


## 讀寫文件

創建文件之後，我們可以用 `f.write()` 把數據寫入文件，也可以用 `f.read()` 讀取文件。
```python
f = open('test-file.txt', 'w')
f.write('first line\nsecond line\nthird line\n')
f.close()

f = open('test-file.txt', 'r')
s = f.read()
print(s)
f.close()
```
    first line
    second line
    third line



文件有很多行的時候，我們可以用 `file.readline()` 操作，這個 Method 每次調用，都會返迴文件中的新一行。
```python
f = open('test-file.txt', 'w')
f.write('first line\nsecond line\nthird line\n')
f.close()

f = open('test-file.txt', 'r')
s = f.readline()    # 返回的是 'first line\n'
print(s)
s = f.readline()    # 返回的是 'second line\n'
print(s)
f.close()
```
    first line
    
    second line



**註意**，返回結果好像跟你想的不太一樣。這時候，之前見過的 `str.strip()` 就派上用場了：
```python
f = open('test-file.txt', 'w')
f.write('first line\nsecond line\nthird line\n')
f.close()

f = open('test-file.txt', 'r')
s = f.readline().strip()    # 返回的是 'first line'，'\n' 被去掉了……
print(s)
s = f.readline().strip()    # 返回的是 'second line'，'\n' 被去掉了……
print(s)
f.close()
```
    first line
    second line


與之相對的，
```python
f = open('test-file.txt', 'w')
f.write('first line\nsecond line\nthird line\n')
f.close()

f = open('test-file.txt', 'r')
s = f.readlines()    # 返回的是一個列表，註意，readlines，最後的 's'
print(s)
f.close()
```
    ['first line\n', 'second line\n', 'third line\n']


既然返回的是列表，那麼就可以被迭代，逐一訪問每一行：
```python
f = open('test-file.txt', 'w')
f.write('first line\nsecond line\nthird line\n')
f.close()

f = open('test-file.txt', 'r')
for line in f.readlines():
    print(line)
f.close()
```
    first line
    
    second line
    
    third line



與之相對的，我們也可以用 `file.writelines()` 把一個列表寫入到一個文件中，按順序每一行寫入列表的對應元素：
```python
a_list = ['first line\n', 'second line\n', 'third line\n']
f = open('test-file.txt', 'w')
f.writelines(a_list)
f.close()

f = open('test-file.txt', 'r')
for line in f.readlines():
    print(line)
f.close()
```
    first line
    
    second line
    
    third line



## with 語句塊

針對文件操作，Python 有個另外的語句塊寫法，更便於閱讀：
```python
with open(...) as f:
    f.write(...)
    ...
```
這樣，就可以把針對當前以特定模式打開的某個文件的各種操作都寫入同一個語句塊了：
```python
import os

with open('test-file.txt', 'w') as f:
    f.write('first line\nsecond line\nthird line\n')
    
with open('test-file.txt', 'r') as f:
    for line in f.readlines():
        print(line)

if os.path.exists(f.name):
    os.remove(f.name)
    print(f'{f.name} deleted.')
else:
    print(f'{f.name} does not exist')    
```
    first line
    
    second line
    
    third line
    
    test-file.txt deleted.


另外，用 `with` 語句塊的另外一個附加好處就是不用寫 `file.close()` 了……

## 另一個完整的程序

若干年前，我在寫某本書的時候，需要一個例子 —— 用來說明 “**即便是結論正確，論證過程亂七八糟也不行！**” 

作者就是這樣，主要任務之一就是給論點找例子找論據。找得到不僅_恰當_且又_精彩_的例子和論據的，就是好作者。後面這個 “_精彩_” 二字要耗費很多時間精力，因為它意味著說 “要找到_很多_例子而後在裡面選出_最精彩_的那個！” —— 根本不像很多人以為的那樣，是所謂的 “信手拈來”。

找了很多例子都不滿意…… 終於有一天，我看到這麼個說法：

> 如果把字母 `a` 計為 `1`、`b` 計為 `2`、`c` 計為 `3` …… `z` 計為 `26`，那麼：
>
> - knowledge = 96
> - hardwork = 98
> - attitude = 100
>
> 所以結論是：
>
> - 知識（*knowledge*）與勤奮（*hardwork*）固然都很重要；
> - 但是，決定成敗的卻是態度（**attitude**）！

結論雖然有道理 —— 可這論證過程實在是太過分了罷…… 

我很高興，覺得這就是個_好例子_！並且，加工一下，會讓讀者覺得很精彩 —— 如果能找到一些按照同樣的計算方式能得到 100 的單詞，並且還是那種一看就是 “反例” 的單詞……

憑直覺，英文單詞幾十萬，如此這般等於 100 的單詞豈不是數不勝數？並且，一定會有很多負面意義的單詞如此計算也等於 100 罷？然而，這種事情憑直覺是不夠的，手工計算又會被累死…… 於是，面對如此荒謬的論證過程，我們竟然 “無話可說”。

幸虧我是會寫程序的人。所以，不會 “干著急沒辦法”，我有能力讓計算機幫我把活幹了。

很快就搞定了，找到很多很多個如此計算加起來等於 100 的英文單詞，其中包括：

> - connivance（縱容）
> - coyness（羞怯）
> - flurry (慌張)
> - impotence（陽痿）
> - stress（壓力）
> - tuppence（微不足道的東西）
> - ……

所以，決定成敗的可以是 “慌張”（flurry），甚至是 “陽痿”（impotence）？這不明顯是胡說八道嘛！

—— 精彩例子製作完畢，我把它放進了書里。

那，具體的過程是什麼樣的呢？

首先我得找到一個英文單詞列表，很全的那種。這事用不著寫程序，Google 一下就可以了。我搜索的關鍵字是 “[english word list](https://www.google.com/search?q=english+word+list)”，很直觀吧？然後就找到一個：[https://github.com/dwyl/english-words](https://github.com/dwyl/english-words)；這個鏈接里有一個 [words-alpha.txt](https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt) 文件，其中包含接近 370,101 個單詞，應該夠用了！下載下來用程序處理就可以了！

因為文件里每行一個單詞，所以，就讓程序打開文件，將文件讀入一個列表，而後迭代這個列表，逐一計算那個單詞每個字母所代表的數字，並加起來看看是否等於 100？如果是，就將它們輸出到屏幕…… 好像不是很難。
```python
with open('words_alpha.txt', 'r') as file:
    for word in file.readlines():
        pass # 先用 pass 占個位，一會兒再寫計算過程
```
按照上面那說法，把 `a` 記為 `1`，直至把 `z` 記為 `26`，這事並不難，因為有 `ord()` 函數啊 —— 這個函數返回字符的 Unicode 編碼：`ord('a')` 的值是 `97`，那按上面的說法，用 `ord('a') - 96` 就相當於得到了 `1` 這個數值…… 而 `ord('z') - 96` 就會得到 `26` 這個數值。
```python
ord('a')
```
    97



那麼，計算 `'knowledge'` 這個字符串的代碼很簡單：
```python
word = 'knowledge'
sum = 0
for char in word:
    sum += ord(char) - 96
print(sum)
```
    96


果然，得到的數值等於 `96` —— 不錯。把它寫成一個函數罷：`sum_of_word(word)`:
```python
def sum_of_word(word):
    sum = 0
    for char in word:
        sum += ord(char) - 96
    return sum

sum_of_word('attitude')
```
    100



那讓程序就算把幾十萬行都算一遍也好像很簡單了：
```python
def sum_of_word(word):
    sum = 0
    for char in word:
        sum += ord(char) - 96
    return sum

with open('words_alpha.txt', 'r') as file:
    for word in file.readlines():
        if sum_of_word(word) == 100:
            print(word)
```
    abstrusenesses
    acupuncturist
    adenochondrosarcoma
    
    ...
    
    worshipability
    zeuctocoelomatic
    zygapophysis



嗯？怎麼輸出結果跟想得不一樣？找到的詞怎麼都 “奇形怪狀” 的…… 而且，輸出結果中也沒有 `attitude` 這個詞。

插入個中止語句，`break`，把找到的第一個詞中的每個字符和它所對應的值都拿出來看看？
```python
def sum_of_word(word):
    sum = 0
    for char in word:
        sum += ord(char) - 96
    return sum

with open('words_alpha.txt', 'r') as file:
    for word in file.readlines():
        if sum_of_word(word) == 100:
            print(word)
            for c in word:        # 把字母和值都打出來，看看對不對？
                print(c, ord(c) - 96)
            break                 # 找到一個之後就停下來。
```
    abstrusenesses
    
    a 1
    b 2
    s 19
    t 20
    r 18
    u 21
    s 19
    e 5
    n 14
    e 5
    s 19
    s 19
    e 5
    s 19
    
     -86


怎麼有個 `-86`？！仔細看看輸出結果，看到每一行之間都被插入了一個空行，想到應該是從文件里讀出的行中，包含 `\n` 這種換行符…… 如果是那樣的話，那麼 `ord('\n') -96` 返回的結果是 `-86` 呢，怪不得找到的詞都 “奇形怪狀” 的……
```python
ord('\n') -96
```
    -86



改進一下唄 —— 倒也簡單，在計算前把讀入字符串前後的空白字符都給刪掉就好了，用 `str.strip()` 就可以了：
```python
def sum_of_word(word):
    sum = 0
    for char in word:
        sum += ord(char) - 96
    return sum

with open('words_alpha.txt', 'r') as file:
    for word in file.readlines():
        if sum_of_word(word.strip()) == 100:
            print(word)
```
    abactinally
    abatements
    abbreviatable
    
    ...
    
    zithern
    zoogleas
    zorgite



如果想把符合條件的詞保存到一個文件 `result.txt` 里的話，那麼：
```python
def sum_of_word(word):
    sum = 0
    for char in word:
        sum += ord(char) - 96
    return sum

with open('results.txt', 'w') as result:
    with open('words_alpha.txt', 'r') as file:
        for word in file.readlines():
            if sum_of_word(word.strip()) == 100:
                result.write(word)
```
竟然這麼簡單就搞定了？！

這 12 行的代碼，在幾秒鐘內從接近 370,101 個英文單詞中找到 3,771 個如此計算等於 100 的詞彙。

喝著咖啡翻一翻 `result.txt`，很快就找到了那些可以用來做反例格外恰當的詞彙。

真無法想象當年的自己若是不懂編程的話現在會是什麼樣子……

## 總結

這一章我們介紹了文本文件的基本操作：

> * 打開文件，直接用內建函數，`open()`，基本模式有 `r` 和 `w`；
> * 刪除文件，得調用 `os` 模塊，使用 `os.remove()`，刪除文件前最好確認文件確實存在……
> * 讀寫文件分別有 `file.read()`、`file.write()`、`file.readline()`、`file.readlines()`、`file.writelines()`；
> * 可以用 `with` 把相關操作都放入同一個語句塊……
