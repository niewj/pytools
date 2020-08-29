# sf个人博客markdown内容批量爬到本地
import requests
from bs4 import BeautifulSoup
import js2xml
from lxml import etree
import re


'''
    需要配置的参数一共4个:
    1. account 你登录账户的账号id, 其实是你编辑时博客地址栏里显示的用户id, 比如我是"niewj"
    2. myCookie 当然前提是你本地浏览器登录过, 在浏览器 devtools(chrome浏览器里 F12)里找到cookie
    3. local_dir 本地要保存结果markdown文档的目录, 可以自己先创建好
    4. pages 你自己的文章的页数, 因为是一页一页遍历的, 所以需要配置总页数
'''
# ======== 1. account 用户名 ======================= ###
account = 'niewj'
# ======== 2.cookie(配置项)需要自己修改 ============== ###
myCookie = 'XXXXXXXXX=XXXX~XXXXXXXXXXXXXXXXXXXXXXXXXX; _XX=XXX.X.XXXXXXXXXX.XXXXXXXXXX; __XXXX=XX=XXXXXXXXXXXXXXXX:X=XXXXXXXXXX:X=XXXX_XXXXXXXXXXXXXXXXXXXXXXXXXXX_X; _XXX=XXX.X.XXXXXXXXX.XXXXXXXXXX; XX_XXXXXXXX=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX; XX_XXX_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX=XXXXXXXXXX,XXXXXXXXXX,XXXXXXXXXX,XXXXXXXXXX; _XXX_XXXX_XX_XXXXXX_X=X; XX_XXXX_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX=XXXXXXXXXX; XX=XXXXXXXXXXXXXXXXXXXX'
# ======== 3. 本地保存markdown目录, 提前创建好(配置项)
local_dir = 'C:/Users/niewj/Desktop/html/sf_markdowns/'
# ======== 4. 提前看好总共的页数(配置项)
pages = 8

# 用于存储所有的文章id
article_ids = []
# 登录用
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
    'cookie': myCookie
}

### ========================================================== ###
### =====遍历所有页码, 获取所有文章id, 存入article_ids列表=== ###
### ========================================================= ###
def iterate_pages():
    print('总页数为:' + str(pages))
    for page_no in range(1, pages + 1):
        fetch_articles(page_no)
        print("解析完成一页了, 页码是:[" + str(page_no) + "]")


### ===> 抓取一页, 获取当前页的所有文章id, 存入article_ids列表 ===###
def fetch_articles(page_no):
    pageUrl = 'https://segmentfault.com/u/' + account + '/articles?page=' + str(page_no)
    ### ======1. 获取markdown文本内容, 作为文件内容=== ###
    ### ===>发起 GET的 requests 得到结果 res === ###
    res = requests.get(pageUrl, headers=headers)
    res.encoding = 'utf-8'

    ### ===> bs解析结果 得到 md_text 文本 === ###
    soup = BeautifulSoup(res.text, 'html.parser')
    page_list_articles = soup.select('div.profile-mine__content--title-warp')
    for article_ul in page_list_articles:
        article_ids.append(article_ul.a['href'].replace('/a/', ''))


### ==================================== ###
### =====读取一篇文章, 写入到本地目录=== ###
### ==================================== ###
def fetch_and_save_article(article_id):
    editUrl = 'https://segmentfault.com/a/' + article_id + '/edit'
    ### ======1. 获取markdown文本内容, 作为文件内容=== ###
    ### ===>发起 GET的 requests 得到结果 res === ###
    res = requests.get(editUrl, headers=headers)
    res.encoding = 'utf-8'

    ### ===> bs解析结果 得到 md_text 文本 === ###
    soup = BeautifulSoup(res.text, 'html.parser')
    md_text = soup.select('input#text-hidden')[0]['value']

    # 这里
    md_text = md_text.replace("![image.png](/img", "![image.png](https://segmentfault.com/img")

    ### =====2.获取 script中的title === ###
    ### ===> 2.1 拿到 <script>中的文本 === ###
    titleScript = soup.select("body script")[0].string

    ### ===> 2.2 <script>中的文本转为 js, 并用js2xml解析为xml === ###
    src_text = js2xml.parse(titleScript, debug=False)
    src_tree = js2xml.pretty_print(src_text)

    ### ===> 解析xml使用xpath:  建立xpath树 === ###
    parsed_tree = etree.HTML(src_tree)
    # 通过xpath获取数据
    md_title = parsed_tree.xpath("//property[@name='title']/string//text()")[0]
    ## 替换不能作为文件名的字符: 模式:==> r'[\/\\\:\*\?\"\<\>\|]'
    md_title = re.sub(r'[\/\\\:\*\?\"\<\>\|]', '-', md_title)
    print(md_title)

    ### 对文本做处理, 如果需要的话
    md_text = do_filter(md_text)

    ### ============3. 写入文件====== ###
    with open(local_dir + md_title + '.md', 'w', encoding='utf-8') as f:
        f.write(md_text)


### ==================================== ###
### =====读取一篇文章, 写入到本地目录=== ###
### ==================================== ###
def do_filter(md_text):
    # return md_text
    line_list = md_text.split('\n')
    if line_list[0].startswith('上一篇:'):
        line_list.pop(0)
    for i in range(len(line_list)):
        if line_list[i] == '* * *':
            line_list[i] = '---'
    if not line_list[0].startswith('---'):
        line_list.insert(0, '---')
    line_list.insert(0, '[TOC]')
    md_text = '\n'.join(line_list)
    return md_text


# 1. 初始化 article_ids
iterate_pages()
# 2. 打印 所有文章id
print(article_ids)
# 3. 遍历所有文章id, 写入到本地目录下, 标题就是文章标题
for article_id in article_ids:
    fetch_and_save_article(article_id)