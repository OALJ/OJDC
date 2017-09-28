# OJDC (Online-Judge Date Crawler)

An Online-Judge Date Crawler [OJDC](https://github.com/OALJ/OJDC) for Local Judge [OALJ](https://github.com/OALJ/OALJ) developed by [kZime](https://github.com/kZime) && [Margatroid](https://github.com/enter-tainer) with ❤❤

## 功能

从部分公开数据的Online-Judge 上扒取供OALJ使用的数据及其题目限定

## 使用方法

注意，暂时~~(未来八成也不会)~~不支持Windows系统。

### 安装:

执行`install.py`安照引导进行安装,**需要`sudo`权限。**

### 使用:

在需评测`cpp`文件目录下执行`cogs` 并输入题号来获取数据及`config.txt` 。

可以使用参数或者输入题号。

``` bash
$ cogs 1 # 获取cogs上题号为1的数据
$ cogs   # 获取cogs上题目的数据，根据引导使用
```

配合OALJ使用效果如图:

![cogs.gif](https://i.loli.net/2017/09/28/59cc8964c2589.gif)

```
TODO LIST:
  √ cogs.py 已经完成
  √ loj.py 已经完成
  √ syzoj 已经完成
  - codeforces
  - USACO
```
