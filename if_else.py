'''
Python 3.10 中增加了一种新的构造分支结构的方式，通过使用match和case 关键字，我们可以轻松的构造出多分支结构。Python
的官方文档在介绍这个新语法时，举了一个 HTTP 响应状态码识别的例子（根据 HTTP 响应状态输出对应的描述），非常有意思。如果不知道什么是 HTTP
响应状态吗，可以看看 MDN 上面的文档。下面我们对官方文档上的示例稍作修改，为大家讲解这个语法，先看看下面用if-else结构实现的代码。
'''
status_code = int(404)
match status_code:
    case 400:
        description = 'Bad Request'
    case 401:
        description = 'Unauthorized'
    case 403:
        description = 'Forbidden'
    case 404:
        description = 'Not Found'
    case 405:
        description = 'Method Not Allowed'
    case 418:
        description = 'I am a teapot'
    case 429:
        description = 'Too many requests'
    case _:
        description = 'Unknown Status Code'
print('状态码描述:', description)

'''
match-case语法还有很多高级玩法，其中有一个合并模式可以先教给大家。例如，我们要将响应状态码401、403和404归入一个分支，400和405归入到一个分支，其他保持不变，代码还可以这么写。
'''
status_code = int(502)
match status_code:
    case 400 | 405:
        description = 'Invalid Request'
    case 401 | 403 | 404:
        description = 'Not Allowed'
    case 418:
        description = 'I am a teapot'
    case 429:
        description = 'Too many requests'
    case _:
        description = 'Unknown Status Code'
print('状态码描述:', description)


