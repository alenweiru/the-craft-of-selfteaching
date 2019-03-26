
# Jupyterlab 的安裝與配置

## 下載並安裝 Anaconda

[Anaconda](https://www.anaconda.com) 是目前最方便的 Python 發行版，搭載了很多我們終將必用的軟件包，除了 Python 之外，還有 [R 語言](https://www.r-project.org/)，還包括 [Pandoc](https://pandoc.org/)， [NumPy](http://www.numpy.org/)，[SciPy](https://www.scipy.org/)，[Matplotlib](https://matplotlib.org/)…… 等等。

無論是圖形化界面安裝，還是命令行界面安裝，建議都把 Anaconda 安裝在本地用戶目錄內，`~/`。請下載並安裝 Python 3.x 的版本。

圖形化界面安裝的教程，官方的很詳細，各個操作平臺的說明都有：

> https://docs.anaconda.com/anaconda/install/

在 MacOS 的 Terminal 命令行下，可以直接下載並安裝：
```bash
cd ~/Downloads/
wget https://repo.anaconda.com/archive/Anaconda3-2018.12-MacOSX-x86_64.sh
./Anaconda3-2018.12-MacOSX-x86_64.sh
```
安裝到最後一步，會問你是否要安裝微軟出品的 [Visual Studio Code](https://code.visualstudio.com)，選擇 `yes` —— 反正以後你的電腦上會不止一個文本編輯器…… 以後你可能還會安裝的文本編輯器包括 [SublimeText](https://www.sublimetext.com), [Atom](https://atom.io) 等等。

安裝完畢之後，打開 Terminal(Windows 系統需要打開之前安裝的 Anaconda Prompt 輸入)，繼續安裝幾個組件：
```bash
conda update conda
conda update anaconda
conda install -c conda-forge nodejs
conda install -c conda-forge jupyterlab # 這是用來升級 jupyter lab 到最新版的方法
```
安裝完畢之後，可以看看各個你將要用到的可執行命令都在什麼地方，用 `which` 命令（windows下用 `where` 命令）：
```bash
which python
python --version
which node
node -v
which jupyter
jupyter lab --version
jupyter notebook --version
which pip
pip --version
```
## 第一次啟動 Jupyter lab

打開 Terminal，`cd` 到你想打開 Jupyter lab 的目錄（就是你保存 `ipynb` 文件的地方，以便在 Jupyter lab 中打開、瀏覽、編輯 `ipynb` 文件），在這裡以用戶根目錄為例 `~/`：
```bash
cd ~
jupyter lab
```
此時的 Terminal 窗口不能關閉，否則 Jupyter lab 就停止運行了 —— 就將它放在那裡。

隨後會有個瀏覽器打開，指向 [http://localhost:8888/lab?](http://localhost:8888/lab?) —— 你就看到 Jupyter lab 的操作界面了。

目前，Jupyter lab 和 Jupyter notebook 是並存的，雖然前者是後者的下一步替代者。如果你依然習慣於使用 Jupyter notebook，那麼，在瀏覽器中指向 [http://localhost:8888/tree?](http://localhost:8888/tree?) 看到的就是 Jupyter notebook.

## 配置 Jupyter lab

打開 Terminal，輸入以下命令：
```bash
jupyter lab --generate-config
```
這會在 `~/.jupyter/` 目錄下生成一個 `jupyter_notebook_config.py` 文件。
```bash
cd ~/.jupyter
code jupyter_notebook_config.py
```
上面的 code 命令，需要你已經安裝 Visual Studio Code，並且在已經在其中設置了 `Install 'code' command in PATH`。參見附錄 [Visual Studio Code 的安裝與配置](T-appendix.editor.vscode.md)

事實上，你可以用你喜歡的任何編輯器打開 `~/.jupyter/jupyter_notebook_config.py` 文件。

文件內容很長，有空可以仔細看。可以直接將以下內容拷貝粘貼到文件底部，根據需求修改：
```json
#c.NotebookApp.token = ''
#c.NotebookApp.open_browser = False
#c.NotebookApp.notebook_dir = '~/'
#c.NotebookApp.default_url = '/tree'
```
逐條解釋一下：

> `c.NotebookApp.token = ''`

每次打開 Jupter，它都會給你生成一個新的 Token —— 這是安全策略。但是，如果你只是在自己的電腦上使用，那麼，這就給你製造了麻煩，因為若是你想同時用另外一個瀏覽器打開它，那你就需要從 Terminal 里拷貝那個 Token 出來。所以，你可以在配置文件里直接把它設置為空。

> `c.NotebookApp.open_browser = False`

每次你執行 `jupyter lab` 或者 `jupyter notebook` 命令的時候，它都會使用系統默認瀏覽器。

每個人的習慣不一樣。比如我，會想到用一個平時不怎麼用的瀏覽器專門用在 Jupyter 上，這樣會防止自己在關閉其它網頁的時候不小心把 Jupyter 關掉…… 那我就會把這項設定為 `False`。

> `c.NotebookApp.notebook_dir = '~/'`

在 Terminal 中執行 `jupyter` 命令的時候，它默認是在你當前所在的工作目錄打開 `jupyter`，這同樣是出於安全考慮。但是，如果你只是在自己的電腦上使用，且只有自己在使用，那麼莫不如直接把它設置成 `~/`，即，你的用戶根目錄，這樣會很方便地訪問各種地方的文件……

> `c.NotebookApp.default_url = '/tree'`

這一項留給那些依然習慣於使用 jupter notebook 的人，這樣設置之後，即便是輸入 `jupyter lab` 命令，打開的還是 jupyter notebook。

在 Terminal 里常用的與 Jupyter 有關的命令有：
```bash
jupyter lab
jupyter lab --version
conda install -c conda-forge jupyterlab # 這是用來升級 jupyter lab 到最新版的方法
jupyter notebook list                   # 查看正在運行的 jupyter lab/notebook
jupyter notebook stop                   # 停止 jupyter lab/notebook 服務
```
## 將 Jupyter lab 配置成系統服務

如果，你厭煩每次都要跑到 Terminal 里啟動 Jupyter lab，可以把它配置成系統服務，每次開機啟動它就自動運行。而你需要做的只不過是直接從瀏覽器中訪問 [http://localhost:8888/](http://localhost:8888/)。
```bash
code ~/Library/LaunchAgents/com.jupyter.lab.plist
```
這條命令會讓 Visual Studio Code 創建 `~/Library/LaunchAgents/com.jupyter.lab.plist` 文件並打開。

在其中拷貝粘貼以下內容，註意，要把其中的 `your_username` 修改為你的用戶名：
``` xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>Label</key>
	<string>local.job</string>
	<key>ProgramArguments</key>
	<array>
		<string>/Users/your_username/anaconda3/bin/jupyter</string>
		<string>lab</string>
		<string>--no-browser</string>
		<string>--notebook-dir=/Users/your_username/</string>
	</array>
	<key>RunAtLoad</key>
	<true/>
	<key>StandardErrorPath</key>
	<string>/tmp/local.job.err</string>
	<key>StandardOutPath</key>
	<string>/tmp/local.job.out</string>
</dict>
</plist>
```
如果之前在 `jupyter_notebook_config.py` 文件里已經設置過
```json
c.NotebookApp.open_browser = False
c.NotebookApp.notebook_dir = '~/'
```
那麼這兩行就可以不要了：
```xml
		<string>--no-browser</string>
		<string>--notebook-dir=/Users/your_username/</string>
```
而後在 Terminal 里執行：
```bash
launchctl load ~/Library/LaunchAgents/com.jupyter.lab.plist
```
如果你想重新啟動這個服務，那麼執行：
```bash
launchctl unload ~/Library/LaunchAgents/com.jupyter.lab.plist
launchctl load ~/Library/LaunchAgents/com.jupyter.lab.plist
```
## 關於 Jupyter lab themes

對中文用戶來說，Jupyter 的默認字號有點過小，閱讀起來不是很舒適。但最佳的方案不是去尋找合適的 themes，而是直接使用支持 [Stylus](https://github.com/openstyles/stylus) 這類終端 CSS 定製插件的瀏覽器，Chrome/Firefox/Opera 都支持 Stylus 插件。

我用的 Stylus 定製 CSS 是這樣的：
```css
a {color: #2456A4 !important;}
strong {color:#6392BF;}
em {color: #A9312A; font-style: normal !important;}
table {font-size: 90% !important;}

#jp-main-dock-panel {background-color: #f9f9f9;}
.jp-RenderedHTMLCommon {font-family: "Yuanti SC"; font-size: 100%;}
.jp-Notebook {background-color: #fbfafa;}
.CodeMirror, .jp-RenderedHTMLCommon pre {font-size: 90%;}
.jp-RenderedHTMLCommon pre {
    padding: 10px 25px;
    background-color: #fafafa;
    border-left: 4px solid #dadada;
    border-radius: 10px;
}

.jp-RenderedHTMLCommon pre code {
    background-color: #fafafa;
}

.jp-RenderedHTMLCommon h1 code,
.jp-RenderedHTMLCommon h2 code,
.jp-RenderedHTMLCommon h3 code,
.jp-RenderedHTMLCommon h4 code,
.jp-RenderedHTMLCommon p code, 
.jp-RenderedHTMLCommon li code,
.jp-RenderedHTMLCommon blockquote p code, 
.jp-RenderedHTMLCommon blockquote li code,
.jp-RenderedHTMLCommon td code {
    background-color: #f6f6f6;
    font-size: 90%;
    color:#2e2e2e;
    padding: 4px 4px;
    margin: 0 8px;
    box-shadow: 0px 1px 2px 0px rgba(0,0,0,0.2);
    border-radius: 4px;
}
```
這樣就相當於我把 JupyterLab Light 這個 Theme 稍微 Tweak 了一下。

另，我寫的內容里，為了重點突出，特別定製了 `strong` 和 `em` 兩個元素的顯示，讓它們以不同的顏色展示；又因為中文並不適合斜體展示，所以，把 `em` 的 `font-style` 設定為 `normal`……

## 安裝插件

Jupyter notebook 經過很多年的發展，現在有很多擴展插件，但也有其中一些並不兼容最新的 Jupyter lab。不過，剛開始的時候用不著那麼多插件，你只用其中的兩個就足夠開始了：

> * [@jupyterlab/toc](https://github.com/jupyterlab/jupyterlab-toc)
> * [ryantam626/jupyterlab_sublime](https://github.com/ryantam626/jupyterlab_sublime)

首先在用快捷鍵 `⌘ ,` 打開 Jupter lab 的 Advanced Settings，在 Extension Manager 中，添加 User Overrides：
```json
{
    "enabled": true
}
```
而後在 Terminal 執行以下命令安裝插件：
```bash 
jupyter labextension install @jupyterlab/toc
jupyter labextension install @ryantam626/jupyterlab_sublime
jupyter lab build
```
toc 插件，自動將 ipynb 文件中的標題轉換成目錄。

![](https://github.com/jupyterlab/jupyterlab-toc/raw/master/toc.gif)

jupyterlab_sublime 則可以讓你在 Jupyter lab 的 cell 中，使用跟 SublimeText 一樣的快捷鍵，比如 `⌘ D` 能夠多選其它與當前選中內容一樣的內容；比如 `⌘` 加鼠標點擊，可以生成多個可編輯點……

![](http://blog.rtwilson.com/wp-content/uploads/2016/03/IPyNbSublime.gif)

## 常用快捷鍵

以下是 MacOS 下 Jupyter lab 最常用的快捷鍵。快捷鍵在兩種模式下執行，進入編輯模式用 `⏎`，回到命令模式用 `⎋`（ESC）。

另外，代碼編輯過程中需要安裝 Jupyterlab 插件 [@ryantam626/jupyterlab_sublime](https://github.com/ryantam626/jupyterlab_sublime) 之後才能使用 “多行同時編輯功能”。


| 快捷鍵                                  | 說明                                                         | 模式   |
| --------------------------------------- | ------------------------------------------------------------ | ------ |
| `ESC`                                   | 從編輯模式回到命令模式                                       | 命令   |
| `A`                                     | 在當前 Cell 之前插入一個 Cell                                |        |
| `B`                                     | 在當前 Cell 之後插入一個 Cell                                |        |
| `D`, `D`                                   | 連續按兩次 `d` 鍵，刪除當前 Cell                                                |        |
| `Y`                                     | 將當前 Cell 設置為 Code Cell                                 |        |
| `M`                                     | 將當前 Cell 設置為 Markdown Cell                             |        |
| `^ ⇧ - `                                | 將當前 Cell 拆分為兩個                                       | 編輯    |
| `⇧ M`                                   | 合併選中的 Cells                                             |        |
| `⇧ J` or `⇧ ↓`                          | 連續向下選中 Cells                                           |        |
| `⇧ K` or `⇧ ↑`                          | 連續向上選中 Cells                                           |        |
| `⇧ ⏎` or `^ ⏎`                          | 運行當前 Cell 中的代碼                                       |        |
| `⇧ L`                                   | 顯示/隱藏代碼行號                                            |        |
| `⏎`                                     | 當前 Cell 進入編輯模式                                       | 編輯   |
| `⇥`                                   | 自動補全代碼                               |        |
| `⇧ ⇥`                                   | 呼出當前光標下詞彙的 Docstring                               |        |
| `⌘ D`                                   | Sublime Keymap: 選中下一個相同字符串                         |        |
| `⇧ ⌘ L`                                 | Sublime Keymap: 在選中的行內啟動多行同時編輯                 |        |
| `⌘ + Mouse Click`                       | 生成下一個可同時編輯的光標點                                 |        |

## 增加一些必要的快捷鍵

在 Settings > Keyboard Shortcuts 中，可以設定一些常用但系統並未給出的快捷鍵：
```json
{
	"notebook:move-cells-down-down": {
		"command": "notebook:move-cell-down",
		"keys": [
		"Alt J"
		],
		"selector": ".jp-Notebook:focus",
		"title": "Move Cells Down",
		"category": "Notebook Cell Operations"
	},
	"notebook:move-cells-down-up": {
		"command": "notebook:move-cell-up",
		"keys": [
		"Alt K"
		],
		"selector": ".jp-Notebook:focus",
		"title": "Move Cells Down",
		"category": "Notebook Cell Operations"
	},
	"notebook:enable-output-scrolling": {
		"command": "notebook:enable-output-scrolling",
		"keys": [
		"S"
		],
		"selector": ".jp-Notebook:focus",
		"title": "Enable output scrolling",
		"category": "Notebook Cell Operations"
	},
	"notebook:disable-output-scrolling": {
		"command": "notebook:disable-output-scrolling",
		"keys": [
		"Alt S"
		],
		"selector": ".jp-Notebook:focus",
		"title": "Enable output scrolling",
		"category": "Notebook Cell Operations"
	}
}
```
這樣就添加了 4 個快捷鍵：
> * `⌥ J`: Move selected cells up
> * `⌥ K`: Move selected cells down
> * `S`: Enable output scrolling
> * `⌥ S`: Disable output scrolling

比如 Move Selected cells up：

![](https://user-images.githubusercontent.com/86304/37438938-b5bc4994-27b2-11e8-8f58-184a58b33ba4.gif)

## 輸出所有變量內容

默認情況下，Code Cell 只輸出最後一個可以被 evaluate 的值，用 `_` 代表之前剛剛被 evaluate 的值。
```python
[1, 2, 3]
```
    [1, 2, 3]


```python
_ # 執行完上面的 Cell，試試這個 Cell; 而後執行完下麵的 Cell 之後再重新執行一次當前這個 Cell
```
    [1, 2, 3]


```python
(1, 2, 3)
{1, 2, 3}
```
    {1, 2, 3}



於是，為了顯示最近 evaluate 的多個值，我們總是不得不使用很多的 `print()`……

如果覺得這事兒比較煩的話，可以在 Cell 最上面寫上：
```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
```
如果還想更省事兒一點，就把這個設置寫入配置文件：
```python
c.InteractiveShell.ast_node_interactivity = "all"
```
```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

(1, 2, 3)
{1, 2, 3}
```
    (1, 2, 3)
    {1, 2, 3}



## 魔法函數

在 Code Cell 里，可以運行一些 “魔法函數”（Magic Functions），這是秉承了 IPython 的特性。絕大多數在 IPython 里能夠使用的魔法函數在 Jupyterlab 里都可以直接使用。完整的 IPython 魔法函數請參照：

> https://ipython.readthedocs.io/en/stable/interactive/magics.html

Jupyterlab 里較為常用的魔法函數整理如下：

| 魔法函數             | 說明                                                         |
| -------------------- | ------------------------------------------------------------ |
| `%lsmagic`           | 列出所有可被使用的 Jupyter lab 魔法函數                      |
| `%run`               | 在 Cell 中運行 `.py` 文件：`%run file_name`                  |
| `%who`               | 列出所有當前 Global Scope 中的變量；類似的還有：`%who df`，`%whos` |
| `%env`               | 列出當前的環境變量                                           |
| `%load`              | 將其他文件內容導入 Cell，`%load source`，`source` 可以是文件名，也可以是 URL。 |
| `%time`              | 返回 Cell 內代碼執行的時間，相關的還有 `%timeit`             |
| `%writefile`         | 把 Cell 的內容寫入文件，`%write file_name`；%write -a file_name，`-a` 是追加 |
| `%matplotlib inline` | 行內展示 matplotlib 的結果                                   |
| `%%bash`             | 運行隨後的 shell 命令，比如 %%bash ls；與之類似的還有 `%%HTML`， `%%python2`， `%%python3`， `%%ruby`， `%%perl`……                      |

## 桌面版 Jupyter App

### Nteract

支持各個操作系統，很好看、很好用。有一個小缺點是，不支持 `input()` 函數的調用。

> https://nteract.io/desktop

![https://cloud.githubusercontent.com/assets/836375/18421299/d95ad398-783b-11e6-8b23-d54cf7caad1e.png](https://cloud.githubusercontent.com/assets/836375/18421299/d95ad398-783b-11e6-8b23-d54cf7caad1e.png)

### Pineapple

只支持 MacOS，也很好用 —— 缺點就是很難看……

> https://nwhitehead.github.io/pineapple/

![https://nwhitehead.github.io/pineapple/images/sshots.png](https://nwhitehead.github.io/pineapple/images/sshots.png)
