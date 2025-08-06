# 强制固定位置参数，参数必须按照定义的顺序传递，/以前的都是强制位置参数
import functools


def static_pos_function(a, b, c, /, d, e):
    return a + b + c + d + e


print(static_pos_function(1, 2, 3, e=5, d=4))


# 强制命名参数，参数必须按照a=1,b=2,c=3的格式传递,*后面的都是强制命名参数
def static_name_function(a, b, c, *, d, e, f=0):
    return a + b + c + d + e + f


print(static_name_function(1, 2, 3, d=4, e=5, f=6))


# 可变参数
def static_var_function(a, b, c, *args):
    return a + b + c + sum(v for v in args if v in (int, float))


print(static_var_function(1, 2, 3, 4, '4', 0))


# 参数列表中的**kwargs可以接收0个或任意多个关键字参数
# 调用函数时传入的关键字参数会组装成一个字典（参数名是字典中的键，参数值是字典中的值）
# 如果一个关键字参数都没有传入，那么kwargs会是一个空字典
def foo(*args, **kwargs):
    print(args)
    print(kwargs)


foo(3, 2.1, True, name='骆昊', age=43, gpa=4.95)

# lambda表达式
# 用一行代码实现判断素数的函数
is_prime = lambda x: all(map(lambda f: x % f, range(2, int(x ** 0.5) + 1)))
print(is_prime(37))


# 装饰器：高阶函数
def log_func(func):
    def wrapper(*args, **kwargs):
        print('调用函数前log')
        result = func(*args, **kwargs)
        print('调用函数后log')
        return result

    return wrapper


# 这里是语法糖，这种写法等于get_sum=log_func(get_sum)
@log_func
def get_sum(*args):
    return sum(v for v in args if isinstance(v, (int, float)))


print(f'sum={get_sum(1, 2, 3)}')


# 带参数的装饰器
def log_param(param):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"调用函数前:{param}")
            result = func(*args, **kwargs)
            print(f"调用函数后:{param*2}")
            return result

        return wrapper

    return decorator


@log_param('hello')
def get_sum(*args):
    return sum(v for v in args if isinstance(v, (int, float)))


print(f'sum={get_sum(1, 2, 3)}')