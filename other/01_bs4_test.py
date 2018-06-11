# coding:utf-8
from bs4 import BeautifulSoup
import re


def bs4_test():
    html_doc = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title"><b>The Dormouse's story</b></p>
    <p class="story">Once upon a time there were three little sisters; and their names were
        <a href="http://example.com/elsie" class="sister" id="link1"><!--Elsie--></a>,
        <a href="http://example.com/lacie" class="sister" id="link2"><img src="xxxx"><h2>Lacie</h2></a> and
        <a href="http://example.com/tillie" class="sister" id="link3"><h2>Tillie</h2></a>;
        and they lived at the bottom of a well.
    </p>
    <p class="story">...</p>
    </body>
    """
    # 创建 Beautiful Soup 对象
    # soup = BeautifulSoup(open("index.html"))
    # soup = BeautifulSoup(html_doc)

    # 我们可以通过以下方式指定lxml解析器。
    soup = BeautifulSoup(html_doc,"lxml")

    # 格式化输出 soup 对象的内容
    # print (soup.prettify())


    """
    Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象,所有对象可以归纳为4种:
    1、Tag
    2、NavigableString
    3、BeautifulSoup
    4、Comment
    """
##################################################################################
    print ("*"*20+"  1  "+"*"*10)

    # 1、Tag ：Tag 通俗点讲就是 HTML 中的一个个标签,我们可以利用 soup 加标签名轻松地获取这些标签的内容
    # 它查找的是在所有内容中的第一个符合要求的标签
    """
    <Tag>.name : Name 表示标签的名字 
    <Tag>.attrs : Attributes 表示标签的属性，返回字典形式组织， 
    <Tag>.string : NavigableString 表示标签内非属性字符串 
    <Tag>.string : Comment 表示标签内的注释部分
    """
    print (soup.title)
    print (soup.a)
    print (type(soup.p))
    print (soup.name) # soup 对象本身比较特殊，它的 name 即为 [document]
    print (soup.head.name) # 对于其他内部标签，输出的值便为标签本身的名称

    # 在这里，我们把第一个 a 标签的所有属性打印输出了出来，得到的类型是一个字典。
    print (soup.a.attrs)

    # 还可以利用get方法，传入属性的名称，二者是等价的
    print (soup.p['class'])
    # print (soup.p.get('class'))

    # 可以对这些属性和内容等等进行修改/删除
    soup.p['class'] = "newClass"
    print (soup.p)
    del soup.p['class']
    print (soup.p)

########################################################################################
    print ("*" * 20 + "  2  " + "*" * 10)

    # 2.NavigableString  :　用 .string 即可获取标签内部的文字
    print (soup.p.string)
    print (type(soup.p.string))

########################################################################################
    print ("*" * 20 + "  3  " + "*" * 10)

    #  3.Comment : Comment 对象是一个特殊类型的 NavigableString 对象，其输出的内容不包括注释符号。
    print (soup.a)
    print (soup.a.string)
    print (type(soup.a.string))


    print ("############################### 遍历文档树 #######################################")

    # 1. 直接子节点 ：.contents .children 属性
    """
    tag 的 .content 属性可以将tag的子节点以列表的方式输出,我们可以用列表索引来获取它的某一个元素
    """
    print (soup.head.contents)
    print (soup.head.contents[0])

    """
    tag 的.children它返回的不是一个 list，不过我们可以通过遍历获取所有子节点。它是一个 list 生成器对象
    """
    print (soup.body.children)
    for i in soup.body.children:
        print (i)

    """
    .contents 和 .children 属性仅包含tag的直接子节点，
    .descendants 属性可以对所有tag的子孙节点进行递归循环，和 children类似，我们也需要遍历获取其中的内容。
    """
    #for child in soup.descendants:
     #   print child

    """ .string
    如果一个标签里面没有标签了，那么 .string 就会返回标签里面的内容。
    如果标签里面只有唯一的一个标签了，那么 .string 也会返回最里面的内容。
    """
    print (soup.head.string)
    print (soup.title.string)

    print ("############################### 遍历文档树的方法 ##################################")
    """
    find_all(name, attrs, recursive, text, **kwargs)
    find( name , attrs , recursive , text , **kwargs )
    使用 find_all 方法并设置 limit=1 参数不如直接使用 find() 方法
    """
    # 1、name参数 ： name参数可以查找所有名字为name的tag, 字符串对象会被自动忽略掉

    """A.传字符串"""
    print (soup.find_all("b"))

    """
    B.传正则表达式
    如果传入正则表达式作为参数, BeautifulSoup会通过正则表达式的match()来匹配内容.
    下面例子中找出所有以b开头的标签, 这表示 < body > 和 < b > 标签都应该被找到
    """
    for tag in soup.find_all(re.compile("^b")):
        print(tag.name,tag.string)

    """
    C.传列表
    如果传入列表参数,Beautiful Soup会将与列表中任一元素匹配的内容返回.
    下面代码找到文档中所有<t>标签和<b>标签:
    """
    print (soup.find_all(["t","b"]))


    # 2）keyword 参数
    print (soup.find_all(id='link2'))

    #3）text 参数通过 text 参数可以搜搜文档中的字符串内容，
    # 与 name 参数的可选值一样, text 参数接受 字符串 , 正则表达式 , 列表
    print (soup.find_all(text="Elsie"))
    print (soup.find_all(text=["Tillie", "Elsie", "Lacie"]))
    print (soup.find_all(text=re.compile("Dormouse")))

    # 查找所有包含 id 属性的tag,无论 id 的值是什么
    print (soup.find_all(id=True))

    print ("############################### CSS选择器 ##################################")
    """
    CSS选择器
    这就是另一种与 find_all 方法有异曲同工之妙的查找方法.
    写 CSS 时，标签名不加任何修饰，类名前加.，id名前加#
    在这里我们也可以利用类似的方法来筛选元素，用到的方法是 soup.select()，返回类型是 list
    """
    # （1）通过标签名查找
    print soup.select('title')

    #（2）通过类名查找
    print soup.select('.sister')

    #（3）通过 id 名查找
    print soup.select('#link1')

    #　（4）组合查找
    """
    组合查找即和写 class 文件时，标签名与类名、id名进行的组合原理是一样的，
    例如查找 p 标签中，id 等于 link２的内容，二者需要用空格分开
    """

    print soup.select('p #link2')
    #　直接子标签查找，则使用 > 分隔
    print soup.select("head > title")

    #（5）属性查找
    """查找时还可以加入属性元素，属性需要用中括号括起来，注意属性和标签属于同一节点，
    所以中间不能加空格，否则会无法匹配到。
    不在同一节点的空格隔开，同一节点的不加空格
    """
    print soup.select('a[class="sister"]')
    print soup.select('p a[href="http://example.com/elsie"]')

    # (6) 获取内容
    """以上的 select 方法返回的结果都是列表形式，可以遍历形式输出，
    然后用 get_text() 方法来获取它的内容。"""
    print (soup.select('a[class="sister"]')[1].get_text())

    # 获取src属性的值
    print soup.select('a img')[0].get("src")

    for title in soup.select('title'):
        print title.get_text()

if __name__ == '__main__':
    bs4_test()