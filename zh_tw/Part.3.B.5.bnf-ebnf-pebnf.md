
# BNF 以及 EBNF

通常情況下，你很少會在入門書籍里讀到關於 Backus-Naur Form（BNF，巴科斯-諾爾範式）和 Extended Backus-Naur Form（EBNF）的話題 —— 它們都被普遍認為是“非專業人士無需瞭解的話題”，隱含的另外一層含義是“反正就算給他們講他們也無論如何看不懂”……

然而，在我眼裡，這事兒非講不可 —— 這是這本“書”的設計目標決定的。

嚴格意義上來講，在《自學是門手藝》中，以自學編程為例，我完全沒必要自己動手耗時費力寫那麼多東西 —— 如果僅僅是為了讓讀者“入門”的話。編程入門書籍，或者 Python 編程入門書籍，都已經太多太多了，其中質量過硬的書籍也多得去了 —— 並且，如果你沒有英文閱讀障礙，那你就會發現網上有太多非常優質的免費教程…… 真的輪不到李笑來同學再寫一次。

我寫這本書的目標是：

> 讓讀者從認知自學能力開始，通過自學編程作為第一個實踐，逐步完整掌握自學能力，進而在隨後漫長的人生中，需要什麼就去學什麼，

…… 不用非得找人教、找人帶 —— 只有這樣，**前途**這兩個字才會變得實在。

於是，我最希望能做到的是，從這裡瞭解了自學方法論，也瞭解了編程以及 Python 編程的基礎概念之後，《自學是門手藝》的讀者能夠**自顧自地踏上徵程，一路走下去** —— 至於走到哪裡，能走到哪裡，不是我一個作者一廂情願能夠決定的，是吧？

當然，會自學的人運氣一定不會差。

於是，這本“書”的核心目標之一，換個說法就是：

> 我希望讀者在讀完《自學是門手藝》之後，有能力獨立地去全面研讀[官方文檔](https://docs.python.org/3/) —— 甚至是各種編程語言、各種軟件的相關的文檔（包括它們的官方文檔）。

自學編程，很像獨自一人沖入了一個叢林，裡面什麼動物都有…… 而且那個叢林很大很大，雖然叢林里有的地方很美，可若是沒有地圖和指南針，你就會迷失方向。

其實吧，地圖也不是沒有 —— 別說 Python 了，無論什麼編程語言（包括無論什麼軟件）都有很翔實的官方文檔…… 可是吧，絕大多數人無論買多少書、上多少課，就是不去用官方“地圖”，就不！

—— 其實倒不是說“第三方地圖”更好，實際的原因很不好意思說出來：

> * 這首先吧，覺得官方文檔閱讀量太大了……（嗯？那地圖不是越詳細越好嗎？）
> * 那還有吧…… 也不是沒去看過，**看不懂**……（嗯…… 這對初學者倒是個問題！）

所以，我要認為這本“書”的最重要工作是：

> 為讀者解讀清楚地圖上的“圖例”，從此之後讀者在任何需要的時候能夠徹底讀懂地圖。

在閱讀官方文檔的時候，很多人在 [The Python Tutorial](https://docs.python.org/3/tutorial/index.html) 上就已經覺得吃力了…… 如果到了 [Standard Libraries](https://docs.python.org/3/library/index.html) 和 [Language References](https://docs.python.org/3/reference/index.html) 的部分，就基本上完全放棄了，比如，以下這段摘自 [string — Common string operations](https://docs.python.org/3/library/string.html)：

> Format Specification Mini-Language
> ...
> The general form of a standard format specifier is:
```
format_spec     ::=  [[fill]align][sign][#][0][width][grouping_option][.precision][type]
fill            ::=  <any character>
align           ::=  "<" | ">" | "=" | "^"
sign            ::=  "+" | "-" | " "
width           ::=  digit+
grouping_option ::=  "_" | ","
precision       ::=  digit+
type            ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" |
                     "n" | "o" | "s" | "x" | "X" | "%"
```
> ...

讀到這，看著一大堆的 `::=` `[]` `|` 當場傻眼了……

這是 BNF 描述，還是 Python 自己定製的 EBNF…… 為了理解它們，以後當然最好有空研究一下“上下文無關文法”（[Context-free Grammar](https://en.wikipedia.org/wiki/Context-free_grammar)），沒準未來你一高興就會去玩一般人不敢玩的各種 Parser，甚至乾脆自己寫門編程語言啥的…… 不過，完全可以跳過那些複雜的東西的 —— 因為你當前的目標只不過是“能夠讀懂那些符號的含義”。

其實吧，真的不難的 —— 它就是語法描述的方法。

比如，什麼是符合語法的整數（Integer）呢？符合以下語法描述的是整數（使用 Python 的 EBNF）：
```
integer ::= [sign] digit +
sign    ::= "+" | "-"
digit   ::=  "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
``` 
以上的描述中，基本符號沒幾個，它們各自的含義是：

> * `::=` 表示定義；
> * `< >` 尖括號里的內容表示必選內容；
> * `[ ]` 中是可選項；
> * `" "` 雙引號里的內容表示字符；
> * ` | ` 豎線兩邊的是可選內容，相當於or；
> * ` * ` 表示零個或者多個……
> * ` + ` 表示一個或者多個……

於是：

> 1. `interger` 定義是：由“可選的 `sign`”和“一個或者多個 `digit` 的集合” 構成 —— 第一行末尾那個 `+` 的作用和正則表達式里的 `+` 一樣；
> 2. `sign` 的定義是什麼呢？要麼是 `+` 要麼是 `-；`
> 3. `digit` 的定義是什麼呢？從 `"0"` 到 `"9"` 中的任何一個值……

於是，`99`、`+99`、`-99`，都是符合以上語法描述的 `integer`；但 `99+` 和 `99-` 肯定不符合以上語法描述的 `integer`。

很簡單吧？反正就是在 `::=` 左邊逐行列出一個語法構成的所有要素，而後在右邊逐行逐一定義，直至全部要素定義完畢。

也許那些在此之前已經熟悉 BNF 範式的人會有點驚訝，“你怎麼連‘_終結符_’和‘_非終結符_’這種最基本的概念都跳過了？” —— 是呀，即便不講那倆概念也能把這事兒講清楚到“能馬上開始用”了的地步…… 這就是我經常說的，“人類有這個神奇的本領，擅長使用自己並不懂的東西……”

Python 對 BNF 的拓展，借鑒了正則表達式<a href='#fn1' name='fn1b'><sup>[1]</sup></a> —— 從最後兩個符號的使用（`*` `+`）你可以看得出來。順帶說，這也是為什麼這本“書”里非要講其他入門書籍里不講的正則表達式的原因之一。

又由於 Python 的社區文檔是二十來年長期積累的，有時標註方法並不一致。比如，在描述 [Python Full Grammar specification](https://docs.python.org/3/reference/grammar.html) 的時候，他們用的語法標註符號體系就跟上面描述 String 的語法不一樣了，是這樣的：

> * `:` 表示定義；
> * `[ ]` 中是可選項；
> * `' '` 雙引號里的內容表示字符；
> * ` | ` 豎線兩邊的是可選內容，相當於or；
> * ` * ` 表示零個或者多個……
> * ` + ` 表示一個或者多個……

—— 用冒號 `:` 替代了 `::=`，用單引號 `''` 替代了雙引號 `""`，而尖括號 `<>` 乾脆不用了：
``` python
# Grammar for Python

# NOTE WELL: You should also follow all the steps listed at
# https://devguide.python.org/grammar/

# Start symbols for the grammar:
#       single_input is a single interactive statement;
#       file_input is a module or sequence of commands read from an input file;
#       eval_input is the input for the eval() functions.
# NB: compound_stmt in single_input is followed by extra NEWLINE!
single_input: NEWLINE | simple_stmt | compound_stmt NEWLINE
file_input: (NEWLINE | stmt)* ENDMARKER
eval_input: testlist NEWLINE* ENDMARKER

decorator: '@' dotted_name [ '(' [arglist] ')' ] NEWLINE
decorators: decorator+
decorated: decorators (classdef | funcdef | async_funcdef)

async_funcdef: 'async' funcdef
funcdef: 'def' NAME parameters ['->' test] ':' suite

parameters: '(' [typedargslist] ')'
typedargslist: (tfpdef ['=' test] (',' tfpdef ['=' test])* [',' [
        '*' [tfpdef] (',' tfpdef ['=' test])* [',' ['**' tfpdef [',']]]
      | '**' tfpdef [',']]]
  | '*' [tfpdef] (',' tfpdef ['=' test])* [',' ['**' tfpdef [',']]]
  | '**' tfpdef [','])
tfpdef: NAME [':' test]
varargslist: (vfpdef ['=' test] (',' vfpdef ['=' test])* [',' [
        '*' [vfpdef] (',' vfpdef ['=' test])* [',' ['**' vfpdef [',']]]
      | '**' vfpdef [',']]]
  | '*' [vfpdef] (',' vfpdef ['=' test])* [',' ['**' vfpdef [',']]]
  | '**' vfpdef [',']
)
vfpdef: NAME

stmt: simple_stmt | compound_stmt
simple_stmt: small_stmt (';' small_stmt)* [';'] NEWLINE
small_stmt: (expr_stmt | del_stmt | pass_stmt | flow_stmt |
             import_stmt | global_stmt | nonlocal_stmt | assert_stmt)
expr_stmt: testlist_star_expr (annassign | augassign (yield_expr|testlist) |
                     ('=' (yield_expr|testlist_star_expr))*)
annassign: ':' test ['=' test]
testlist_star_expr: (test|star_expr) (',' (test|star_expr))* [',']
augassign: ('+=' | '-=' | '*=' | '@=' | '/=' | '%=' | '&=' | '|=' | '^=' |
            '<<=' | '>>=' | '**=' | '//=')
# For normal and annotated assignments, additional restrictions enforced by the interpreter
del_stmt: 'del' exprlist
pass_stmt: 'pass'
flow_stmt: break_stmt | continue_stmt | return_stmt | raise_stmt | yield_stmt
break_stmt: 'break'
continue_stmt: 'continue'
return_stmt: 'return' [testlist]
yield_stmt: yield_expr
raise_stmt: 'raise' [test ['from' test]]
import_stmt: import_name | import_from
import_name: 'import' dotted_as_names
# note below: the ('.' | '...') is necessary because '...' is tokenized as ELLIPSIS
import_from: ('from' (('.' | '...')* dotted_name | ('.' | '...')+)
              'import' ('*' | '(' import_as_names ')' | import_as_names))
import_as_name: NAME ['as' NAME]
dotted_as_name: dotted_name ['as' NAME]
import_as_names: import_as_name (',' import_as_name)* [',']
dotted_as_names: dotted_as_name (',' dotted_as_name)*
dotted_name: NAME ('.' NAME)*
global_stmt: 'global' NAME (',' NAME)*
nonlocal_stmt: 'nonlocal' NAME (',' NAME)*
assert_stmt: 'assert' test [',' test]

compound_stmt: if_stmt | while_stmt | for_stmt | try_stmt | with_stmt | funcdef | classdef | decorated | async_stmt
async_stmt: 'async' (funcdef | with_stmt | for_stmt)
if_stmt: 'if' test ':' suite ('elif' test ':' suite)* ['else' ':' suite]
while_stmt: 'while' test ':' suite ['else' ':' suite]
for_stmt: 'for' exprlist 'in' testlist ':' suite ['else' ':' suite]
try_stmt: ('try' ':' suite
           ((except_clause ':' suite)+
            ['else' ':' suite]
            ['finally' ':' suite] |
           'finally' ':' suite))
with_stmt: 'with' with_item (',' with_item)*  ':' suite
with_item: test ['as' expr]
# NB compile.c makes sure that the default except clause is last
except_clause: 'except' [test ['as' NAME]]
suite: simple_stmt | NEWLINE INDENT stmt+ DEDENT

test: or_test ['if' or_test 'else' test] | lambdef
test_nocond: or_test | lambdef_nocond
lambdef: 'lambda' [varargslist] ':' test
lambdef_nocond: 'lambda' [varargslist] ':' test_nocond
or_test: and_test ('or' and_test)*
and_test: not_test ('and' not_test)*
not_test: 'not' not_test | comparison
comparison: expr (comp_op expr)*
# <> isn't actually a valid comparison operator in Python. It's here for the
# sake of a __future__ import described in PEP 401 (which really works :-)
comp_op: '<'|'>'|'=='|'>='|'<='|'<>'|'!='|'in'|'not' 'in'|'is'|'is' 'not'
star_expr: '*' expr
expr: xor_expr ('|' xor_expr)*
xor_expr: and_expr ('^' and_expr)*
and_expr: shift_expr ('&' shift_expr)*
shift_expr: arith_expr (('<<'|'>>') arith_expr)*
arith_expr: term (('+'|'-') term)*
term: factor (('*'|'@'|'/'|'%'|'//') factor)*
factor: ('+'|'-'|'~') factor | power
power: atom_expr ['**' factor]
atom_expr: ['await'] atom trailer*
atom: ('(' [yield_expr|testlist_comp] ')' |
       '[' [testlist_comp] ']' |
       '{' [dictorsetmaker] '}' |
       NAME | NUMBER | STRING+ | '...' | 'None' | 'True' | 'False')
testlist_comp: (test|star_expr) ( comp_for | (',' (test|star_expr))* [','] )
trailer: '(' [arglist] ')' | '[' subscriptlist ']' | '.' NAME
subscriptlist: subscript (',' subscript)* [',']
subscript: test | [test] ':' [test] [sliceop]
sliceop: ':' [test]
exprlist: (expr|star_expr) (',' (expr|star_expr))* [',']
testlist: test (',' test)* [',']
dictorsetmaker: ( ((test ':' test | '**' expr)
                   (comp_for | (',' (test ':' test | '**' expr))* [','])) |
                  ((test | star_expr)
                   (comp_for | (',' (test | star_expr))* [','])) )

classdef: 'class' NAME ['(' [arglist] ')'] ':' suite

arglist: argument (',' argument)*  [',']

# The reason that keywords are test nodes instead of NAME is that using NAME
# results in an ambiguity. ast.c makes sure it's a NAME.
# "test '=' test" is really "keyword '=' test", but we have no such token.
# These need to be in a single rule to avoid grammar that is ambiguous
# to our LL(1) parser. Even though 'test' includes '*expr' in star_expr,
# we explicitly match '*' here, too, to give it proper precedence.
# Illegal combinations and orderings are blocked in ast.c:
# multiple (test comp_for) arguments are blocked; keyword unpackings
# that precede iterable unpackings are blocked; etc.
argument: ( test [comp_for] |
            test '=' test |
            '**' test |
            '*' test )

comp_iter: comp_for | comp_if
sync_comp_for: 'for' exprlist 'in' or_test [comp_iter]
comp_for: ['async'] sync_comp_for
comp_if: 'if' test_nocond [comp_iter]

# not used in grammar, but may appear in "node" passed from Parser to Compiler
encoding_decl: NAME

yield_expr: 'yield' [yield_arg]
yield_arg: 'from' test | testlist
```
現在你已經能讀懂 BNF 了，那麼，可以再讀讀用 BNF 描述的 Regex 語法<a href='#fn2' name='fn2b'><sup>[2]</sup></a>，就當複習了 —— 很短的：
```html
BNF grammar for Perl-style regular expressions

<RE>             ::=  <union> | <simple-RE>
<union>          ::=  <RE> "|" <simple-RE>
<simple-RE>      ::=  <concatenation> | <basic-RE>
<concatenation>  ::=  <simple-RE> <basic-RE>
<basic-RE>       ::=  <star> | <plus> | <elementary-RE>
<star>           ::=  <elementary-RE> "*"
<plus>           ::=  <elementary-RE> "+"
<elementary-RE>  ::=  <group> | <any> | <eos> | <char> | <set>
<group>          ::=  "(" <RE> ")"
<any>            ::=  "."
<eos>            ::=  "$"
<char>           ::=  any non metacharacter | "\" metacharacter
<set>            ::=  <positive-set> | <negative-set>
<positive-set>   ::=  "[" <set-items> "]"
<negative-set>   ::=  "[^" <set-items> "]"
<set-items>      ::=  <set-item> | <set-item> <set-items>
<set-items>      ::=  <range> | <char>
<range>          ::=  <char> "-" <char>
```
真的沒原來以為得那麼神秘，是不？<a href='#fn3' name='fn3b'><sup>[3]</sup></a>

都學到這兒了…… 順帶再自學個東西吧。

這個東西叫 `glob`，是 Global 的縮寫。你可以把它理解為“超級簡化版正則表達式” —— 它最初是 Unix/Posix 操作系統中用來匹配文件名的“通配符”。

先看一張 1971 的 Unix 操作系統中關於 glob 的截圖：
![](../images/Unix_Glob_Reference.png)
> A screenshot of the original 1971 Unix reference page for glob – note the owner is dmr, short for Dennis Ritchie.

glob 的主要符號只有這麼幾個：

> * `*`
> * `?`
> * `[abc]`
> * `[^abc]`

現在的你，打開 Wikipedia 上的關於 glob 和 Wildcard character 的頁面，肯定能做到“無障礙”理解：

> * https://en.wikipedia.org/wiki/Glob_(programming)
> * https://en.wikipedia.org/wiki/Wildcard_character

順帶說，現在你再去讀關於 Format String 的官方文檔，就不會再覺得“根本看不懂”了，恰恰相反，你會覺得“我怎麼之前連這個都看不懂呢？”

> https://docs.python.org/3/library/string.html#format-string-syntax

在自學這件事兒上，失敗者的死法看起來千變萬化，但其實都是一樣的…… 只不過是因為怕麻煩或者基礎知識不夠而不去讀最重要的文檔。

比如，學英語的時候死活不讀語法書。其實英文語法書也沒多難啊？再厚，不也是用來“查”的嗎？不就是多記幾個標記就可以讀懂的嗎？比如，詞性標記，`v.`, `n.`, `adj.`, `adv.`, `prep.`... 不就是相當於地圖上的圖例嗎？那語法書，和現在這裡提到的官方文檔，不都是“自學者地圖”嗎？

但就是這麼一點點簡單的東西，擋住了幾乎所有人，真是可怕。

-----
**腳註**

<a name='fn1'>[1]</a>：[The Python Language Reference » 1.2 Notation](https://docs.python.org/3/reference/introduction.html#notation) —— 這個鏈接必須去看一看……

<a href='#fn1b'><small>↑Back to Content↑</small></a>

<a name='fn2'>[2]</a>：[Perl Style Regular Expressions in Prolog](http://www.cs.sfu.ca/~cameron/Teaching/384/99-3/regexp-plg.html) CMPT 384 Lecture Notes
Robert D. Cameron November 29 - December 1, 1999

<a href='#fn2b'><small>↑Back to Content↑</small></a>

<a name='fn3'>[3]</a>：很少有人註意到：在很多編程語言的文法文檔中，`"$"` 被稱為 `<eos>` —— 2017 年 5 月我投資了一個初創公司，聽說他們的資產名稱叫做 `eos`…… 我當場就被這個梗逗樂了。

<a href='#fn3b'><small>↑Back to Content↑</small></a>

