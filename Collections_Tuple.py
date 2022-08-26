# import collections

# n = int(input())
# scol = ','.join(input().split())
# Student = collections.namedtuple('Student',scol)

# sum = 0
# for i in range(n):
#     row = input().split()
#     student = Student(*row)
#     sum += int(student.MARKS)

# print(sum/n)


from collections import namedtuple
x = int(input())
scol = ','.join(input().split())
Person = namedtuple('Person',scol)
sum = 0
for i in range(x):
    row = input().split()
    Persons = Person(*row)
    sum += int(Persons.MARKS)
print(sum/x)
