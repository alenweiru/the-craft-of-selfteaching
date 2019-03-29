# Github進行fork後如何與原倉庫同步

實在是……有太多人同時在幫忙修訂錯別字或優化 xiaolai 的 `the-craft-of-selfteaching` 了。如果你提交的 pull request 未被接受且得到回复說：“重新fork”，其實是你遇到一個問題：

> - 在你 fork 之後， xiaolai 的倉庫又更新了；
> - 但 github 不會自動幫你把 xiaolai 的倉庫同步給你 fork 後的倉庫；
> - 導致你提交 pull request 時的版本和 xiaolai 的版本不一致。


這個問題，用顯得更“專業”的說法，叫做：`Github進行fork後如何與原倉庫同步`。那到底怎麼做呢？

這個問題，用顯得更“專業”的說法，叫做：`Github進行fork後如何與原倉庫同步 `。那到底怎麼做呢？


最省事的辦法可能是：

> - 在你fork的倉庫setting頁翻到最下方，然後delete這個倉庫；
> - 然後重新fork xiaolai 的倉庫，並 git clone 到你的本地。

有時候，你需要用到這個省事的辦法，比如xiaolai 的倉庫再次整理了commit ；或者你已經玩壞了自己fork的倉庫，又或者你所提交的大量內容僅是個人練習，但對xiaolai 並無幫助—— 於是如果你就這樣提交pull request 會有大量無效內容吖，只能刪了重來。

但在更多情況下，刪掉自己fork的庫，應該是你的最後選擇，而不應該是首選。

和很多人一起向 xiaolai 提交 pull request，這實在是一個反复練習 `merge` （中文說法：合併，或版本合併）的機會。毫不誇張地講，版本管理是軟件工程極其重要的規範，也是極其基礎的必備技能。而 `merge` 則是版本管理中最必須也最常用的場景。

那要不然，就多練練？以下是傻瓜版操作步驟，還細心配了截圖，保管你從 0 也能上手。至於原理嘛，慢慢再搞懂吧。

### merge前的設定

step 1、進入到本地倉庫的目錄。



![image](https://user-images.githubusercontent.com/31027645/54422899-6938e880-474a-11e9-8768-27ac24673e28.png)

step 2、執行命令 `git remote -v` 查看你的遠程倉庫的路徑：

![image](https://user-images.githubusercontent.com/31027645/54422975-95ed0000-474a-11e9-96bf-1018d6bc06f2.png)

如果只有上面2行，說明你未設置 `upstream` （中文叫：上游代碼庫）。一般情況下，設置好一次 `upstream` 後就無需重複設置。

step 3、執行命令 `git remote add upstream https://github.com/selfteaching/the-craft-of-selfteaching.git` 把 xiaolai 的倉庫設置為你的 `upstream` 。這個命令執行後，沒有任何返回信息；所以再次執行命令 `git remote -v` 檢查是否成功。

![image](https://user-images.githubusercontent.com/31027645/54423107-d8aed800-474a-11e9-9ab8-7bb901181283.png)

step 4、執行命令 `git status` 檢查本地是否有未提交的修改。如果有，則把你本地的有效修改，先從本地倉庫推送到你的github倉庫。最後再執行一次 `git status` 檢查本地已無未提交的修改。

`git add -A` 或者 `git add filename`
`git commit -m "your note"`
`git push origin master`
`git status`

注1：作為新手，這一步建議嚴格執行，是為了避免大量無效修改或文本衝突帶來的更複雜局面。

注2：如果你已經在fork後的倉庫提交了大量對 xiaolai 的倉庫並沒有價值的修改，那麼想要pull request，還是重新回到本文最初的“最省事辦法”吧。

### merge 的關鍵命令

以下操作緊接著上面的步驟。

step 5、執行命令 `git fetch upstream` 抓取 xiaolai 原倉庫的更新：

![image](https://user-images.githubusercontent.com/31027645/54448734-60b2d300-4787-11e9-9fdf-90fcc2e66052.png)

step 6、執行命令 `git checkout master` 切換到 master 分支：

![image](https://user-images.githubusercontent.com/31027645/54448759-6dcfc200-4787-11e9-8bbc-a5beef23ea88.png)

step 7、執行命令 `git merge upstream/master` 合併遠程的master分支：

![image](https://user-images.githubusercontent.com/31027645/54449526-47128b00-4789-11e9-9add-09217eb91a68.png)

step 8、執行命令 `git push ` 把本地倉庫向github倉庫（你fork到自己名下的倉庫）推送修改

如果擔心自己不小心改了哪裡，可以再次執行命令 `git status` 檢查哪些文件有變化。這個操作僅是檢查，不會改變任何狀態，放心用。

![image](https://user-images.githubusercontent.com/31027645/54449665-a07aba00-4789-11e9-9181-bdcc814fffe6.png)

現在你已經解決了fork的倉庫和原倉庫版本不一致的問題。可以放心向 xiaolai 發起 pull request 了。如果以上操作你花了不少時間，而 xiaolai 的倉庫又恰好更新了。很好，一次新的練習機會來了……gi