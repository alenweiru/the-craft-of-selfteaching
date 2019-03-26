
# 函數的文檔

你在調用函數的時候，你像是函數這個產品的用戶。

而你寫一個函數，像是做一個產品，這個產品將來可能會被很多用戶使用 —— 包括你自己。

產品，就應該有產品說明書，別人用得著，你自己也用得著 —— 很久之後的你，很可能把當初的各種來龍去脈忘得一干二凈，所以也同樣需要產品說明書，別看那產品曾經是你自己設計的。

Python 在這方面很用功，把函數的 “產品說明書” 當作語言內部的功能，這也是為什麼 Python 有 [Sphinx](http://www.sphinx-doc.org) 這種工具，而絕大多數其他語言沒有的原因之一罷。

## Docstring

在函數定義內部，我們可以加上 **Docstring**；將來函數的 “用戶” 就可以通過 `help()` 這個內建函數，或者 `.__doc__` 這個 Method 去查看這個 Docstring，即，該函數的 “產品說明書”。

先看一個 Docstring 以及如何查看某個函數的 Docstring 的例子：
```python
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


help(is_prime)
print(is_prime.__doc__)
is_prime.__doc__
```
    Help on function is_prime in module __main__:
    
    is_prime(n)
        Return a boolean value based upon
        whether the argument n is a prime number.
    
    
        Return a boolean value based upon
        whether the argument n is a prime number.
        
    '\n    Return a boolean value based upon\n    whether the argument n is a prime number.\n    '



Docstring 可以是多行字符串，也可以是單行字符串：
```python
def is_prime(n):
    """Return a boolean value based upon whether the argument n is a prime number."""
    
    if n < 2:
        return False
    if n == 2:
        return True
    for m in range(2, int(n**0.5)+1):
        if (n % m) == 0:
            return False
    else:
        return True


help(is_prime)
print(is_prime.__doc__)
is_prime.__doc__
```
    Help on function is_prime in module __main__:
    
    is_prime(n)
        Return a boolean value based upon whether the argument n is a prime number.
    
    Return a boolean value based upon whether the argument n is a prime number.
    'Return a boolean value based upon whether the argument n is a prime number.'



Docstring 如若存在，必須在函數定義的內部語句塊的開頭，也必須與其它語句一樣保持相應的縮進（Indention）。Docstring 放在其它地方不起作用：
```python
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for m in range(2, int(n**0.5)+1):
        if (n % m) == 0:
            return False
    else:
        return True
    """
    Return a boolean value based upon
    whether the argument n is a prime number.
    """

help(is_prime)
print(is_prime.__doc__)
is_prime.__doc__
```
    Help on function is_prime in module __main__:
    
    is_prime(n)
    
    None


## 書寫 Docstring 的規範

規範，雖然是人們最好遵守的，但其實通常是很多人並不遵守的東西。

既然學，就要**像樣** —— 這真的很重要。所以，非常有必要認真閱讀 Python [PEP 257](https://www.python.org/dev/peps/pep-0257/) 關於 Docstring 的規範。

簡要總結一下 PEP 257 中必須掌握的規範：

> 1. 無論是單行還是多行的 Docstring，一概使用三個雙引號擴起；
> 2. 在 Docstring 內部，文字開始之前，以及文字結束之後，都不要有空行；
> 3. 多行 Docstring，第一行是概要，隨後空一行，再寫其它部分；
> 4. 完善的 Docstring，應該概括清楚以下內容：參數、返回值、可能觸發的錯誤類型、可能的副作用，以及函數的使用限制等等；
> 5. 每個參數的說明都使用單獨的一行……

由於我們還沒有開始研究 Class，所以，關於 Class 的 Docstring 應該遵守什麼樣的規範就暫時略過了。然而，這種規範你總是要反覆去閱讀參照的。關於 Docstring，有兩個規範文件：

> * [PEP 257: Docstring Convensions](https://www.python.org/dev/peps/pep-0257/)
> * [PEP 258: Docutils Design Specification](https://www.python.org/dev/peps/pep-0258/)

需要**格外註意**的是：

> Docstring 是**寫給人看的**，所以，在複雜代碼的 Docstring 中，寫 **Why** 要遠比寫 _What_ 更重要 —— 你先記住這點，以後的體會自然會不斷加深。

## Sphinx 版本的 Docstring 規範

Sphinx 可以從 `.py` 文件里提取所有 Docstring，而後生成完整的 Documentation。將來若是你寫大型的項目，需要生成完善的文檔的時候，你就會發現 Sphinx 是個 “救命” 的家伙，省時、省力、省心、省命……

在這裡，沒辦法一下子講清楚 Sphinx 的使用，尤其是它還用它自己的一種標記語言，reStructureText，文件尾綴使用 `.rst`……

但是，可以看一個例子：
```python
class Vehicle(object):
    '''
    The Vehicle object contains lots of vehicles
    :param arg: The arg is used for ...
    :type arg: str
    :param `*args`: The variable arguments are used for ...
    :param `**kwargs`: The keyword arguments are used for ...
    :ivar arg: This is where we store arg
    :vartype arg: str
    '''
    def __init__(self, arg, *args, **kwargs):
        self.arg = arg
    def cars(self, distance, destination):
        '''We can't travel a certain distance in vehicles without fuels, so here's the fuels
        :param distance: The amount of distance traveled
        :type amount: int
        :param bool destinationReached: Should the fuels be refilled to cover required distance?
        :raises: :class:`RuntimeError`: Out of fuel
        :returns: A Car mileage
        :rtype: Cars
        '''  
        pass

help(Vehicle)
```
    Help on class Vehicle in module __main__:
    
    class Vehicle(builtins.object)
     |  Vehicle(arg, *args, **kwargs)
     |  
     |  The Vehicle object contains lots of vehicles
     |  :param arg: The arg is used for ...
     |  :type arg: str
     |  :param `*args`: The variable arguments are used for ...
     |  :param `**kwargs`: The keyword arguments are used for ...
     |  :ivar arg: This is where we store arg
     |  :vartype arg: str
     |  
     |  Methods defined here:
     |  
     |  __init__(self, arg, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  cars(self, distance, destination)
     |      We can't travel a certain distance in vehicles without fuels, so here's the fuels
     |      
     |      :param distance: The amount of distance traveled
     |      :type amount: int
     |      :param bool destinationReached: Should the fuels be refilled to cover required distance?
     |      :raises: :class:`RuntimeError`: Out of fuel
     |      
     |      :returns: A Car mileage
     |      :rtype: Cars
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    


通過插件，Sphinx 也能支持 Google Style Docstring 和 Numpy Style Docstring。

以下兩個鏈接，放在這裡，以便你將來查詢：

> * [sphinx.ext.napoleon – Support for NumPy and Google style docstrings](http://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html)
> * [sphinx.ext.autodoc – Include documentation from docstrings](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html)
