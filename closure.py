def dev():
    pass


def jiali():
    pass
# def foo():
#     x = 10
#     y = 20
#
#     def inner():
#         print(x, y)
#
#     return inner
#
#
# func = foo()
#
# for i in func.__closure__:
#     print(i.cell_contents)


# print(func.__closure__)

def foo(func):
    def inner():
        print("haha")
        print("devvvvvvvv")
        func()

    return inner


# index = foo(index)
@foo
def index():
    print("this is index")


index()


def fun_time(func):
    def inner():
        import time
        s1 = time.time()
        func()
        print('函数执行时间:%s' % str(time.time() - s1))

    return inner


@fun_time
def add():
    ret = 1
    for i in range(100000000):
        ret += i
    print(ret)

add()
