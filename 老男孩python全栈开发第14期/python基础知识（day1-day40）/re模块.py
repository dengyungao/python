"""
re模块
匹配字符串
re.findall()    返回值类型：列表 返回值个数：1 返回值内容：所有匹配上的项
                常用

re.search()     返回值类型：正则匹配结果的对象 返回值个数：1 返回值内容：如果匹配上了就返回一个对象
                再通过返回的对象.group()方法获取匹配到的第一个结果
                常用
                
re.match()      返回值类型：正则匹配结果的对象 返回值个数：1 返回值内容：如果匹配上了就返回一个对象
                再通过返回的对象.group()方法获取匹配到的第一个结果
                与search()的使用方法相同，区别在于match()只从字符串首字符开始匹配，如果首字符不匹配则匹配失败。search()则能匹配任意位置。
                不常用
                
替换
re.sub()        等效于str.replace()
re.subn()       用法等效于re.sub()，只是会额外返回正则表达式匹配到的字符个数。

切割
re.split()      等效于str.split()


进阶
re.compile()    预编译，提前编译正则表达式，多次使用同一个正则表达式进行匹配时能提高效率。
                ret=re.compile(正则表达式)
                ret.findall()
                ret.search().group()
                ret.match().group()
                
re.finditer()  作用与re.findall()相同，只是能节省内存和减少时间，且返回一个迭代器，但findall()直接返回一个列表。
                ret=re.finditer()
                resultList=[key.group() for key in ret]
                

正则表达式中的分组（）
re.findall()       优先显示分组中的内容，取消分组优先：?:正则表达式

re.split()         遇到分组时只返回分组内的内容，其余内容不返回，并且返回的列表首末各有一个空字符。

re.search()        如果search()中有分组的话，会通过group(n)拿到group中匹配到的内容，groups()方法会以元组形式返回所有匹配到的分组。

分组练习：
re.search(r"<(\w)>(\w)<\\(\w+)>","<a>deng<\a>")
"""