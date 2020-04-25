# 错误处理

## try...except...语句
```python
try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')
```
从输出可以看到，当错误发生时，后续语句print('result:', r)不会被执行，except由于捕获到ZeroDivisionError，因此被执行。最后，finally语句被执行。然后程序继续按照流程往下走。没有错误发生，所以except语句块不会被执行，但是finally如果有，则一定会被执行（可以没有finally语句）。

如果发生了不同类型的错误，应该由不同的except语句块处理。没错，可以有多个except来捕获不同类型的错误。如果没有错误发生，可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句：

```python
try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')
```
Python的错误其实也是class，所有的错误类型都继承自BaseException，所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”。比如：

```python
try:
    foo()
except ValueError as e:
    print('ValueError')
except UnicodeError as e:
    print('UnicodeError')
```

第二个`except`永远也捕获不到`UnicodeError`，因为`UnicodeError`是`ValueError`的子类，如果有，也被第一个`except`给捕获了。
Python所有的错误都是从`BaseException`类派生的，常见的错误类型和继承关系看这里:https://docs.python.org/3/library/exceptions.html#exception-hierarchy

## 调用栈

如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出。来看看`err.py`：
```python
# err.py:
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    bar('0')

main()
```
执行，结果如下：
``` bash
$ python3 err.py
Traceback (most recent call last):
  File "err.py", line 11, in <module>
    main()
  File "err.py", line 9, in main
    bar('0')
  File "err.py", line 6, in bar
    return foo(s) * 2
  File "err.py", line 3, in foo
    return 10 / int(s)
ZeroDivisionError: division by zero
```
出错并不可怕，可怕的是不知道哪里出错了。解读错误信息是定位错误的关键。我们从上往下可以看到整个错误的调用函数链：

错误信息第1行：

Traceback (most recent call last):
告诉我们这是错误的跟踪信息。

第2~3行：
```bash
  File "err.py", line 11, in <module>
    main()
```
调用main()出错了，在代码文件err.py的第11行代码，但原因是第9行：
```bash
  File "err.py", line 9, in main
    bar('0')
```
调用bar('0')出错了，在代码文件err.py的第9行代码，但原因是第6行：
```bash
  File "err.py", line 6, in bar
    return foo(s) * 2
```
原因是return foo(s) * 2这个语句出错了，但这还不是最终原因，继续往下看：
```bash
  File "err.py", line 3, in foo
    return 10 / int(s)
```
原因是return 10 / int(s)这个语句出错了，这是错误产生的源头，因为下面打印了：
```bash
ZeroDivisionError: integer division or modulo by zero
```
根据错误类型`ZeroDivisionError`，我们判断，`int(s)`本身并没有出错，但是`int(s)`返回0，在计算`10 / 0`时出错，至此，找到错误源头。

## 抛出错误
因为错误是class，捕获一个错误就是捕获到该class的一个实例。因此，错误并不是凭空产生的，而是有意创建并抛出的。Python的内置函数会抛出很多类型的错误，我们自己编写的函数也可以抛出错误。

如果要抛出错误，首先根据需要，可以定义一个错误的class，选择好继承关系，然后，用raise语句抛出一个错误的实例：

```python
# err_raise.py
class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

foo('0')
```
执行，可以最后跟踪到我们自己定义的错误：
```bash
$ python3 err_raise.py 
Traceback (most recent call last):
  File "err_throw.py", line 11, in <module>
    foo('0')
  File "err_throw.py", line 8, in foo
    raise FooError('invalid value: %s' % s)
__main__.FooError: invalid value: 0
```
只有在必要的时候才定义我们自己的错误类型。如果可以选择Python已有的内置的错误类型（比如ValueError，TypeError），尽量使用Python内置的错误类型。

最后，我们来看另一种错误处理的方式：

```python
# err_reraise.py

def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise

bar()
```

在bar()函数中，我们明明已经捕获了错误，但是，打印一个ValueError!后，又把错误通过raise语句抛出去了，这不有病么？

其实这种错误处理方式不但没病，而且相当常见。捕获错误目的只是记录一下，便于后续追踪。但是，由于当前函数不知道应该怎么处理该错误，所以，最恰当的方式是继续往上抛，让顶层调用者去处理。好比一个员工处理不了一个问题时，就把问题抛给他的老板，如果他的老板也处理不了，就一直往上抛，最终会抛给CEO去处理。

raise语句如果不带参数，就会把当前错误原样抛出。此外，在except中raise一个Error，还可以把一种类型的错误转化成另一种类型：

```python
try:
    10 / 0
except ZeroDivisionError:
    raise ValueError('input error!')
```
只要是合理的转换逻辑就可以，但是，决不应该把一个`IOError`转换成毫不相干的`ValueError`。

## traceback

使用traceback追踪异常的时候，需要import traceback模块。traceback模块可以有效的帮助查看异常的详细信息。 

**注意**：若希望获取异常的详细信息，却又不会终止程序的执行，可以在except子句中使用`tarceback.print_exc()`函数。

## print_exc

```python
import sys
import traceback
 
def func1():
  raise NameError("--func1 exception--")
 
def func2():
  func1()
 
def main():
  try:
    func2()
  except Exception as e:
    traceback.print_exc(limit=1, file=sys.stdout)
```

输出（由于limit=1，因此只有一个层级被打印出来）：

```
Traceback (most recent call last):
  File "<ipython-input-25-a1f5c73b97c4>", line 13, in main
    func2()
NameError: --func1 exception--
```

### format_exc
`print_exc()`会将异常信息直接打印出来，但有些时候我们需要将这些错误信息输入到文件或者仅仅获取字符串，这时候就需要调用`format_exc()`，它输出的信息和`print_exc`相同，不同的是它只是返回字符串并不会将其打印出来。

```python
import logging
import sys
import traceback
logger = logging.getLogger("traceback_test")
 
def func1():
  raise NameError("--func1 exception--")
 
def func2():
  func1()
 
def main():
  try:
    func2()
  except Exception as e:
    logger.error(traceback.format_exc(limit=1, file=sys.stdout))
```

从这个例子可以看出有时候我们想得到的是一个字符串，比如我们想通过logger将异常记录在log里，这个时候就需要format_exc了，这个也是最常用的一个函数，它跟print_exc用法相同，只是不直接打印而是返回了字符串。

## 传递异常 re-raise Exception
捕捉到了异常，但是又想重新抛出它（传递异常），使用不带参数的raise语句即可：

```python
def f1():
    print(1/0)

def f2():
    try:
        f1()
    except Exception as e:
        raise  # don't raise e !!!

f2()
```

在`Python2`中，为了保持异常的完整信息，那么你捕获后再次抛出时千万不能在`raise`后面加上异常对象，否则你的`trace`信息就会从此处截断。以上是最简单的重新抛出异常的做法，也是推荐的做法。

还有一些技巧可以考虑，比如抛出异常前你希望对异常的信息进行更新。

```python
def f2():
    try:
        f1()
    except Exception as e:
        e.args += ('more info',)
        raise
```

如果你有兴趣了解更多，建议阅读这篇博客:[http://www.ianbicking.org/blog/2007/09/re-raising-exceptions.html](http://www.ianbicking.org/blog/2007/09/re-raising-exceptions.html)

`Python3`对重复传递异常有所改进，你可以自己尝试一下，不过建议还是遵循以上规则。

## Exception 和 BaseException
当我们要捕获一个通用异常时，应该用`Exception`还是`BaseException`？我建议你还是看一下 官方文档说明，这两个异常到底有啥区别呢？ 请看它们之间的继承关系。

```
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration...
      +-- StandardError...
      +-- Warning...
```

从Exception的层级结构来看，`BaseException`是最基础的异常类，`Exception`继承了它。`BaseException`除了包含所有的`Exception`外还包含了`SystemExit`，`KeyboardInterrupt`和`GeneratorExit`三个异常。

由此看来你的程序在捕获所有异常时更应该使用`Exception`而不是`BaseException`，因为被排除的三个异常属于更高级别的异常，合理的做法应该是交给`Python`的解释器处理。

## `except Exception as e`和 `except Exception, e`

代码示例如下：
```python
try:
    do_something()
except NameError as e:  # should
    pass
except KeyError, e:  # should not
    pass
```

在P`ython2`的时代，你可以使用以上两种写法中的任意一种。在`Python3`中你只能使用第一种写法，第二种写法已经不再支持。第一个种写法可读性更好，而且为了程序的兼容性和后期移植的成本，请你果断抛弃第二种写法。