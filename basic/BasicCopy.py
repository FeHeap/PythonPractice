# -*- coding = utf-8 -*-
# @Time: 2021/7/9 下午 10:06
# @Software: PyCharm

a = 10
b = a
print(a,id(a))
print(b,id(b))
a = 15
print(a,id(a))
print(b,id(b))
print()

num1 = [1,2,3]
num2 = num1 #copy the address of num1 to num2
num1.append(4)
print(num1,id(num1))
print(num2,id(num2))
print()

#shallow copy #only copy the first layer of list
num1 = [10,[2,3]]
num2 = num1.copy()
num1.append(4)
num1[0] = 8
num1[1].append(100)
print(num1,id(num1))
print(num2,id(num2))
print("num1[0]:",num1[0],id(num1[0]))
print("num2[0]:",num2[0],id(num2[0]))
print("num1[1]:",num1[1],id(num1[1]))
print("num2[1]:",num2[1],id(num2[1]))
print()


#deep copy #copy all the layers of list
import copy
num1 = [10,[2,3]]
num2 = copy.deepcopy(num1)
print(num1,id(num1))
print(num2,id(num2))
print("num1[0]:",num1[0],id(num1[0]))
print("num2[0]:",num2[0],id(num2[0]))
print("num1[1]:",num1[1],id(num1[1]))
print("num2[1]:",num2[1],id(num2[1]))
num1.append(4)
num1[0] = 8
num1[1].append(100)
print(num1,id(num1))
print(num2,id(num2))
print()


#practice
n1 = [1,2,3,[4,5]]
n2 = n1[:]
n1.append(6)
print(n1,id(n1)) #[1, 2, 3, [4, 5], 6] 2210222736960
print(n2,id(n2)) #[1, 2, 3, [4, 5]] 2210222736512
print(n1[3],id(n1[3])) #[4, 5] 2210222748544
print(n2[3],id(n2[3])) #[4, 5] 2210222748544
