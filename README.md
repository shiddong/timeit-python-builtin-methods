# list 内置操作的时间复杂度(List Operations)
Operation           |   Big-O Efficiency    |   Desc
--------------------|-----------------------|-------------
index[]             |   O(1)
index assignment    |   O(1)
append              |   O(1)
pop                 |   O(1)
pop(i)              |   O(n)
insert(i, item)     |   O(n)
del operator        |   O(n)
iteration           |   O(n)
contains(in操作符)   |   O(n)
get slice(x:y)      |   O(k)                | 与x和y有关
del slice           |   O(n)
set slice           |   O(n+k)              | lis[:3] = [1, 2, 3, 4, 5]
reverse             |   O(n)
concatenate(+)      |   O(k)                | lis += [1, 2, 3] 添加k个元素
sort                |   O(nlogn)
multiply(*)         |   O(nk)               | lis * 10 即 k == 10

# dict 内置操作的时间复杂度(Dictionary Operations)
Operation           |   Big-O Efficiency    |   Desc
--------------------|-----------------------|-------------
copy                |   O(n)
get item            |   O(1)
set item            |   O(1)
del item            |   O(1)
contains(in)        |   O(1)
iteration           |   O(n)
