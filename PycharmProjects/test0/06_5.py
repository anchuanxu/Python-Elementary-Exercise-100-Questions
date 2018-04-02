from functools import lru_cache

def f(n):
    assert n >=0
    return n if n <=1 else f(n-1)+f(n-2)

print(f(10))

#不是很懂这段代码的算法.