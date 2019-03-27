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
        lis = lis + [i]
def test_concat_optimize():
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

timer_concat_optimize = timeit.Timer("test_concat_optimize()", "from __main__ import test_concat_optimize")
print("concat_optimize:", timer_concat_optimize.timeit(NUM_TIMEIT), "seconds")

timer_comprehension = timeit.Timer("test_comprehension()", "from __main__ import test_comprehension")
print("comprehension:", timer_comprehension.timeit(NUM_TIMEIT), "seconds")

timer_list_range = timeit.Timer("test_list_range()", "from __main__ import test_list_range")
print("list range:", timer_list_range.timeit(NUM_TIMEIT), "seconds")

timer_extend = timeit.Timer("test_extend()", "from __main__ import test_extend")
print("extend:", timer_extend.timeit(NUM_TIMEIT), "seconds")

timer_insert = timeit.Timer("test_insert()", "from __main__ import test_insert")
print("insert(0):", timer_insert.timeit(NUM_TIMEIT), "seconds")


'''
append: 0.833000661 seconds（一般）
concat: 155.785993012 seconds（差）
concat_optimize: 0.9081458340000097 seconds（一般）
comprehension: 0.36562661900001103 seconds（好）
list range: 0.22507090700000276 seconds（好）
extend: 1.2832709179999995 seconds（一般）
insert(0): 21.524639981999997 seconds（差）


由此可见：insert/+ 直接计算效率太差；extend/append/+= 的效率也比较差；而list range与列表生成式的方式效率相对比较高。

往尾部添加数据比往头部添加数据要慢的多，因为list是一种数组形式的数据结构，往头部添加数据时，需要移动后续的所有元素。
使用 append 和 += 是在处理上是接近的，+= 是直接在lis列表上处理，而 + 则是新开辟空间进行处理，在效率上慢太多。 
'''

