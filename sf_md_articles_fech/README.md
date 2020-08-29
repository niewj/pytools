[TOC]

---

# sf_md_articles_fetch工具

python tools sf_md_articles_fetch

# 1. 工具功能简介

>  拉取segmentfault网站里的个人博客文章, 其中的markdown文本

python tools sf_md_articles_fetch



# 2. python依赖的安装

## 2.1 requests模块

## 2.2 bs4模块

## 2.3 js2xml模块

## 2.4 lxml模块

安装命令:

```
pip install requests
pip install BeautifulSoup4
pip install js2xml
pip install lxml
```

# 3. 使用前准备工作-参数配置 
## 3.1. 配置参数: account

```python
# 你登录账户的账号id: 注意这里是你的博客地址里的 account
account = 'niewj'
```

## 3.2. 配置参数: myCookie

### 3.2.1 前提是你本地浏览器登录过sf

### 3.2.2 在浏览器 devtools(chrome浏览器里 F12)

### 3.2.3 "Network"->"Doc"->"Name" 找到请求url: "Headers"标签里->"Request Headers"中找到 **cookie**

### 3.2.4 copy出来作为myCookie的值;

示例: 

```python
# ======== 2.cookie(配置项)需要自己修改 ============== ###
myCookie = 'XXXXXXXXX=XXXX~XXXXXXXXXXXXXXXXXXXXXXXXXX; _XX=XXX.X.XXXXXXXXXX.XXXXXXXXXX; __XXXX=XX=XXXXXXXXXXXXXXXX:X=XXXXXXXXXX:X=XXXX_XXXXXXXXXXXXXXXXXXXXXXXXXXX_X; _XXX=XXX.X.XXXXXXXXX.XXXXXXXXXX; XX_XXXXXXXX=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX; XX_XXX_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX=XXXXXXXXXX,XXXXXXXXXX,XXXXXXXXXX,XXXXXXXXXX; _XXX_XXXX_XX_XXXXXX_X=X; XX_XXXX_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX=XXXXXXXXXX; XX=XXXXXXXXXXXXXXXXXXXX'

```

## 3.3 配置参数: local_dir 

本地要保存结果markdown文档的目录, 可以自己先创建好

```python
# ======== 3. 本地保存markdown目录, 提前创建好(配置项)
local_dir = 'C:/Users/niewj/Desktop/html/sf_markdowns/'
```

## 3.4 配置参数: pages 

你自己的文章的页数, 因为是一页一页遍历的(sf一页展示不完所有文章), 所以需要配置总页数

可以去自己的主页, 看自己的文章分页, 比如我的, 目前是8页:

https://segmentfault.com/u/niewj/articles

```python
# ======== 4. 提前看好总共的页数(配置项)
pages = 8
```

# 4. 拷贝sf_md_articles_fetch.py到你本地然后执行即可

```python
#命令行打开执行
python sf_md_articles_fetch.py
```



# 5. 注意事项

模块里有几个地方是对markdown里的文章做了修改的, 可以注意下:

## 5.1 文章的标题替换

由于生成的markdown文件, 文件名是文章的标题; 但是文章标题里有些字符是不能作为文件名的, 代码中对这个做了替换:

```python
md_title = re.sub(r'[\/\\\:\*\?\"\<\>\|]', '-', md_title)
```

全替换为连字符了 **-**

## 5.2 文章内容的修改

我这里为了生成的文章会被 Typora 打开时, 自动索引目录, 都在第一行加了 [TOC], 如果不希望替换, 可以注释掉代码中这块(92行):

```python
    ### 对文本做处理, 如果需要的话
    md_text = do_filter(md_text)
```

## 5.3 图片路径的修改

由于在博客中的图片地址都是短地址, 保存到本地后打不开, 所以, 在每个图片的路径中追加了前面的域名:

```python
/img ---> https://segmentfault.com/img
```



Over!
