#!/usr/bin/python3
import timeit

NUM_RANGE = 10000
NUM_TIMEIT = 1000

def test_append():
    lis = []
    for i in range(NUM_RANGE):
        lis.append(i)
def test_concat():
    lis = []
    for i in range(NUM_RANGE):
        lis += [i]
def test_comprehension():
    lis = [i for i in range(NUM_RANGE)]
def test_list_range():
    lis = list(range(NUM_RANGE))
def test_extend():
    lis = []
    for i in range(NUM_RANGE):
        lis.extend([i])
def test_insert():
    lis = []
    for i in range(NUM_RANGE):
        lis.insert(0, i)


timer_append = timeit.Timer("test_append()", "from __main__ import test_append")
print("append:", timer_append.timeit(NUM_TIMEIT), "seconds")

timer_concat = timeit.Timer("test_concat()", "from __main__ import test_concat")
print("concat:", timer_concat.timeit(NUM_TIMEIT), "seconds")

timer_comprehension = timeit.Timer("test_comprehension()", "from __main__ import test_comprehension")
print("comprehension:", timer_comprehension.timeit(NUM_TIMEIT), "seconds")

timer_list_range = timeit.Timer("test_list_range()", "from __main__ import test_list_range")
print("list range:", timer_list_range.timeit(NUM_TIMEIT), "seconds")

timer_extend = timeit.Timer("test_extend()", "from __main__ import test_extend")
print("extend:", timer_extend.timeit(NUM_TIMEIT), "seconds")

timer_insert = timeit.Timer("test_insert()", "from __main__ import test_insert")
print("insert(0):", timer_insert.timeit(NUM_TIMEIT), "seconds")


'''
append: 0.843514164 seconds
concat: 0.9529310910000001 seconds
comprehension: 0.4078549840000001 seconds
list range: 0.21328822800000014 seconds
extend: 1.3336434440000002 seconds
insert(0): 22.048957903 seconds


由此可见：insert/extend/append/使用 + 号的效率都比较差。而list range与列表生成式的方式效率相对比较高。
以及往尾部添加数据比往头部添加数据要慢的多，因为list是一种数组形式的数据结构，往头部添加数据时，需要移动后续的所有元素。
'''

