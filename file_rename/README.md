[TOC]

---

# rename 工具

python tools rename

# 1. 使用前准备工作: 
## 1.1. 将此文件放到需要批量替换文件名的目录下
## 1.2. old_str 修改为文件名中想要替换的字符串(替换前)
比如文件目录下文件名如下: 

`23、尚硅谷-SpringBoot-高级-检索-整合SpringDataElasticsearch.avi`

而且目录下大部分文件名都类似: 都有"尚硅谷-SpringBoot-", 我们想把这部分替换掉;

比如把 `old_str = '尚硅谷-SpringBoot-'`,  替换成`trim_str=''`

我们需要修改配置: 

```python
old_str = '尚硅谷-SpringBoot-'
```

## 1.3. trim_str 改为想替换成的字符串

我们需要修改配置: 

``` python
trim_str = ''
```

# 2. 执行步骤

## 2.1 安装python, 配置python环境变量(略)

## 2.2 rename.py文件拷到当前目录下

## 2.3 在当前目录下打开`cmd`窗口

>  (shift+右键->在此处打开power shell窗口)  
>
> 或者 打开命令行, 一路 cd 到目录下

## 2.4 执行脚本

```shell
python rename.py
```

Over!