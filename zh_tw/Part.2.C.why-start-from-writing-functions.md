
# 為什麼從函數開始？

讀完第一部分之後，你多多少少已經 “寫” 了一些程序，雖然我們總是說，“這就是讓你脫盲”；也就是說，從此之後，你多多少少能夠讀懂程序，這就已經很好了。

可是你無論如何都避免不了已經寫了一些，雖然，那所謂的 “寫”，不過是 “改” 而已 —— 但畢竟也是一大步。

絕大多數編程書籍並不區分學習者的 “讀” 與 “寫” 這兩個實際上應該分離的階段 —— 雖然現實中這兩個階段總是多多少少重疊一部分。

在一個比較自然的過程中，我們總是先學會閱讀，而後才開始練習寫作；並且，最終，閱讀的量一定遠遠大於寫作的量 —— 即，輸入遠遠大於輸出。當然，貌似也有例外。據說，香港作家倪匡，他自己後來很少讀書，每天咣當咣當地像是打掃陳年舊物倒垃圾一樣寫作 —— 他幾乎是全球最具產量的暢銷小說作家，貌似地球另外一端的史蒂芬·金都不如他多。又當然，他的主要輸入來自於他早年豐富的人生經歷，人家讀書，他閱世，所以，實際上並不是輸入很少，恰恰相反，是輸入太多……

所以，正常情況下，輸入多於輸出，或者，輸入遠遠多於輸出，不僅是自然現象，也是無法改變的規則。

於是，我在安排內容的時候，也刻意如此安排。

第一部分，主要在於啟動讀者在編程領域中的 “閱讀能力”，到第二部分，才開始逐步啟動讀者在編程領域中的 “寫作能力”。

在第二部分啟動之前，有時間有耐心的讀者可以多做一件事情。

Python 的代碼是開源的，它的代碼倉庫在 Github 上：

> https://github.com/python/

在這個代碼倉庫中，有一個目錄下，保存著若干 Python Demo 程序：

> https://github.com/python/cpython/tree/master/Tools/demo

這個目錄下的 README 中有說明：

> This directory contains a collection of demonstration scripts for
> various aspects of Python programming.
>
> * beer.py        Well-known programming example: Bottles of beer.
> * eiffel.py      Python advanced magic: A metaclass for Eiffel post/preconditions.
> * hanoi.py       Well-known programming example: Towers of Hanoi.
> * life.py        Curses programming: Simple game-of-life.
> * markov.py      Algorithms: Markov chain simulation.
> * mcast.py       Network programming: Send and receive UDP multicast packets.
> * queens.py      Well-known programming example: N-Queens problem.
> * redemo.py      Regular Expressions: GUI script to test regexes.
> * rpython.py     Network programming: Small client for remote code execution.
> * rpythond.py    Network programming: Small server for remote code execution.
> * sortvisu.py    GUI programming: Visualization of different sort algorithms.
> * ss1.py         GUI/Application programming: A simple spreadsheet application.
> * vector.py      Python basics: A vector class with demonstrating special methods.

最起碼把這其中的以下幾個程序都精讀一下，看看自己的理解能力：

> * [beer.py](https://github.com/python/cpython/blob/master/Tools/demo/beer.py)        Well-known programming example: Bottles of beer.
> * [eiffel.py](https://github.com/python/cpython/blob/master/Tools/demo/eiffel.py)      Python advanced magic: A metaclass for Eiffel post/preconditions.
> * [hanoi.py](https://github.com/python/cpython/blob/master/Tools/demo/hanoi.py)       Well-known programming example: Towers of Hanoi.
> * [life.py](https://github.com/python/cpython/blob/master/Tools/demo/life.py)        Curses programming: Simple game-of-life.
> * [markov.py](https://github.com/python/cpython/blob/master/Tools/demo/markov.py)      Algorithms: Markov chain simulation.
> * [queens.py](https://github.com/python/cpython/blob/master/Tools/demo/queens.py)      Well-known programming example: N-Queens problem.

就算讀不懂也沒關係，把讀不懂的部分標記下來，接下來就可以 “帶著問題學習”……

在未來的時間里，一個好的習慣就是，有空了去讀讀別人寫的代碼 —— 理解能力的提高，就靠這個了。你會發現這事兒跟其他領域的學習沒什麼區別。你學英語也一樣，讀多了，自然就讀得快了，理解得快了，並且在那過程中自然而然地習得了很多 “句式”，甚至很多 “說理的方法”、“講故事的策略”…… 然後就自然而然地會寫了，從能寫一點開始，慢慢到 “很能寫”！

為了順利啟動第一部分的 “閱讀”，特意找了個不一樣的入口，“布爾運算”；第二部分，從 “閱讀” 過渡到 “寫作”，我也同樣特意尋找了一個不一樣的入口：**從函數開始寫起**。

從小入手，從來都是自學的好方法。我們沒有想著一上來就寫程序，而是寫 “子程序”、“小程序”、“短程序”。從結構化編程的角度來看，寫函數的一個基本要求就是：

> - 完成一個功能；
> - 只完成一個功能；
> - 沒有任何錯誤地只完成一個功能……

然而，即便是從小入手，任務也沒有變得過分簡單。其中涉及的話題理解起來並不容易，儘管我們儘量用最簡單的例子。涉及的話題有：

> - 參數的傳遞
> - 多參數的傳遞
> - 匿名函數以及函數的別稱
> - 遞歸函數
> - 函數文檔
> - 模塊
> - 測試驅動編程
> - 可執行程序

這些都是你未來寫自己的工程時所必須仰仗的基礎，馬虎不得，疏漏不得。

另外，這一部分與第一部分有一個刻意不同的編排，這一部分的每一章之後，**沒有寫總結** —— 那個總結需要讀者自己動手完成。你需要做的不僅僅是每一個章節的總結，整個第二部分讀完之後，還要做針對整個 “深入瞭解函數”（甚至應該包括第一部分已經讀過的關於函數的內容）的總結…… 並且，關於函數，這一章並未完全講完呢，第三部分還有生成器、迭代器、以及裝飾器要補充 —— 因為它們多多少少都涉及到下一部分才能深入的內容，所以，在這一部分就暫時沒有涉及。

你要習慣，歸納、總結、整理的工作，從來都不是一次就能完成的，都需要反覆多次之後才能徹底完成。必須習慣這種流程 —— 而不是像那些從未自學過的人一樣，對這種東西想當然地全不瞭解。

另外，從現代編程方法論來看，“寫作” 部分一上來就從函數入手也的確是 “更正確” 的，因為結構化編程的核心就是拆分任務，把任務拆分到不能再拆分為止 —— 什麼時候不能再拆分了呢？就是當一個函數只完成一個功能的時候……
