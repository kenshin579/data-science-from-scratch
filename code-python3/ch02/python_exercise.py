import collections
import random

even_numbers = [x for x in range(5) if x % 2 == 0]
zeros = [0 for _ in even_numbers]
print(zeros)


def lazy_range(n):
    i = 0
    while i < n:
        yield i
        i += 1


def natural_numbers():
    n = 1
    while True:
        yield n
        n += 1


def do_something_with(i):
    print("i", i)


for i in lazy_range(10):
    do_something_with(i)

# todo: 아래는 key-value pairs를 return한다고 하는데 어떻게 써야 하나??
lazy_evens_below_20 = (i for i in lazy_range(20) if i % 2 == 0)

# 4번 random값을 선택하기때문에 중복이 있을 수 있음
four_with_replacement = [random.choice(range(10))
                         for _ in range(4)]
print("four_with_replacement", four_with_replacement)

# zip
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
print(list(zip(list1, list2)))  # [('a', 1), ('b', 2), ('c', 3)]

pairs = [('a', 1), ('b', 2), ('c', 3)]
print(list(zip(pairs)))  # [(('a', 1),), (('b', 2),), (('c', 3),)]
print(list(zip(*pairs)))  # [('a', 'b', 'c'), (1, 2, 3)]


def add(a, b): return a + b


print(add(1, 2))
# print(add([1, 2]))
print(add(*[1, 2]))

# Counter
print(collections.Counter(['a', 'b', 'c', 'a', 'b', 'b']))  # {'b': 3, 'a': 2, 'c': 1}
print(collections.Counter({'a': 2, 'b': 3, 'c': 1}))  #
print(collections.Counter(a=2, b=3, c=1))
