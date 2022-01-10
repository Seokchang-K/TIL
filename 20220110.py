#!/usr/bin/env python
# coding: utf-8

# In[ ]:


data = [1, 2, 3, 4, 5]

data


# In[ ]:


type(data)


# In[ ]:


data1 = []

data1


# In[ ]:


type (data1)


# In[ ]:


data2= list()

data2


# In[ ]:


type(data2)


# In[ ]:


strlist = ['I', 'love', 'you']

strlist


# In[ ]:


comlist = [1, 2, 'I', 'love', 'you']

comlist


# In[ ]:


comlist2 = [1, 2, ['I', 'love', 'you']]

comlist2


# In[ ]:


strlist = list('I love you')

strlist


# In[ ]:


type(strlist)


# In[ ]:


data


# In[ ]:


data[0]


# In[ ]:


data[0] + data[2]


# In[ ]:


data[-1]


# In[ ]:


str_list0001 = list("I'm a man")

str_list0001


# In[ ]:


str_list0001 [4]


# In[ ]:


str_list0001 [0] + str_list0001 [1] + str_list0001 [2]


# In[ ]:


comlist2


# In[ ]:


comlist2[0]


# In[ ]:


comlist2[-1]


# In[ ]:


comlist2[-1][-1]


# In[ ]:


comlist2[-1][-2]


# In[ ]:


comlist2[[1]]


# In[ ]:


comlist3 = [1, 2, ['a', 'b', ['life', 'is', 'good']]]

comlist3


# In[ ]:


comlist3 [-1][-1][0]


# In[ ]:


data


# In[ ]:


sData = data[:2]

sData


# In[ ]:


sData2 = data[2:]

sData2


# In[ ]:


data3 = [1, 2, 3, ['a', 'b', 'c'], 4, 5]

data3


# In[ ]:


data3[2:5]


# In[ ]:


data3[3][:2]


# In[ ]:


a = [1, 2, 3]
b = [4, 5, 6]

a + b


# In[ ]:


a*3


# In[ ]:


a


# In[ ]:


len(a)


# In[ ]:


a[2] + 'hahaha'


# In[ ]:


str(a[2]) + 'hahaha'


# In[ ]:


a


# In[ ]:


a[-1] = 5

a


# In[ ]:


del a[0]

a


# In[ ]:


a=[1, 2, 3, 4, 5]

del a[2:]

a


# In[ ]:


a = [1, 2, 3]

a


# In[ ]:


a[-1] = 5

a


# In[ ]:


del a[0]

a


# In[ ]:


a = [1,2,3]

a.append(4)

a


# In[ ]:


a


# In[ ]:


del a[-1]
a


# In[ ]:


a.append( [5, 6] )
a


# In[ ]:


del a[-1]

a


# In[ ]:


a


# In[ ]:


a.append([5,6])


# In[ ]:


a


# In[ ]:


help(list)


# In[ ]:


a = [1, 3, 4, 2]

a


# In[ ]:


a.sort()

a


# In[ ]:


b = ['a', 'd', 'b']

b


# In[ ]:


b.sort()

b


# In[ ]:


b = ['a', 'd', 'b']

b


# In[ ]:


b.reverse()

b


# In[ ]:


b.index('b')


# In[ ]:


b.index('c')


# In[ ]:


a = [1, 2, 3]

a


# In[ ]:


a.insert(4)


# In[ ]:


a.insert(0, 4)

a


# In[ ]:


a.insert(3, 5)

a


# In[ ]:


a = [1,2,3]
a = a * 3

a


# In[ ]:


a.remove(3)


# In[ ]:


a


# In[ ]:


a.remove(3)

a


# In[ ]:


a.remove(3)

a


# In[ ]:


a.remove(3)


# In[ ]:


a = [1, 2, 3, 1, 2, 3]

while True:
  try:
    a.remove(3)
    print(a)
  except Exception as e:
    print(e)
    break

a


# In[ ]:


a = [1, 2, 3]

a


# In[ ]:


val = a.pop()

val, a


# In[ ]:


a = [1,2,3]

a.remove(3)

a


# In[ ]:


a = [1,2,3]

val = a.pop()

val, a


# In[ ]:


a = [1,2,3]

a.pop(1)

a


# In[ ]:


a = [1,2,3,4,5,6,7]

val = a.pop()

val, a


# In[ ]:


a = [1,2,3,1,2]

a.count(1)


# In[ ]:


a.count(3)


# In[ ]:


a = [1,2,3]
b = [4,5,6]

a + b


# In[ ]:


a.extend(b)

a


# In[ ]:


a = [1,2,3]
b = [4,5,6]

a = a + b

a


# In[ ]:


movie_titles = ['스파이더맨', '경관의 피', '씽2게더']

movie_titles


# In[ ]:


movie_titles.append('킹스맨')

movie_titles


# In[ ]:


movie_titles.insert(1, '매트릭스')


# In[ ]:


movie_titles


# In[ ]:


movie_titles.remove('매트릭스')

movie_titles


# In[ ]:


movie_titles = ['스파이더맨', '매트릭스', '경관의 피', '씽2게더', '킹스맨']

movie_titles.pop(1)

movie_titles


# In[ ]:


movie_titles = ['스파이더맨', '매트릭스', '경관의 피', '씽2게더', '킹스맨']

del movie_titles[1]

movie_titles


# In[ ]:


compile_lang = ['C', 'C++', 'Java']

interpret_lang = ['Python', 'Javascript']

languages = compile_lang + interpret_lang


# In[ ]:


languages


# In[ ]:


compile_lang


# In[ ]:


compile_lang = ['C', 'C++', 'Java']

interpret_lang = ['Python', 'Javascript']


# In[ ]:


languages = compile_lang.extend(interpret_lang)

languages


# In[ ]:


languages


# In[ ]:


languages


# In[ ]:


nums = [1, 2, 3, 4, 5, 6]

nums.max()


# In[ ]:


max(nums)


# In[ ]:


min(nums)


# In[ ]:


print(max(nums))


# In[ ]:


print(min(nums))


# In[ ]:


print(f'최대값 : {max(nums)}')
print(f'최소값 : {min(nums)}')


# In[ ]:


nums = [1, 2, 3, 4, 5, 6]

print(f'최대값 : {max(nums)}')
print(f'최소값 : {min(nums)}')
print(f'총합 : {sum(nums)}')
print(f'평균값 : {sum(nums)/len(nums)}')


# In[ ]:


import numpy as np

array = np.array(nums)
print(f'평균값 : {np.mean(array)}')


# In[ ]:


stock = [20220110, 124000, 124000, 123500, 12400,12400,124000,124500]

stock.pop(0)

stock


# In[ ]:


stock = [20220110, 124000, 124000, 123500, 12400,12400,124000,124500]

del stock[0]

stock


# In[ ]:


stock = [20220110, 124000, 124000, 123500, 12400,12400,124000,124500]

stock[1:]


# In[ ]:


stock = [20220110, 124000, 124000, 123500, 12400,12400,124000,124500]

stock.remove(20220110)
stock


# ## 슬라이싱은 원본에 영향 안미침 따라서 밑에 stock 쓸필요 x
# ## del,pop,reomve는 원본 영향 O stock써야 한다.

# In[ ]:


nums


# ## nums 에서 홀수 구하기 (슬라이싱 활용)
# ## (start:stop:step)

# In[ ]:


nums[::2]


# In[ ]:


nums[0:5:2]


# In[ ]:


nums[1::2]


# In[ ]:


nums


# In[ ]:


nums[::-1]


# In[ ]:


nums.reverse()
nums


# In[ ]:


nums[::-1]


# In[ ]:


nums.reverse()
nums


# In[ ]:


t1 = ()
t2 = (1, )
t3 = (1, 2, 3)
t4 = 1,2,3
t5 = ('a', 'b', ('ab', 'cd'))

t4


# In[ ]:


t1 = (1, 2, 'a', 'b')

del t1[0]


# 튜플은 데이터의 삭제가 불가하다.

# In[ ]:


t1[0] = 100


# 튜플은 데이터의 변조가 불가하다.

# In[ ]:


t1


# In[ ]:


t1[0]


# In[ ]:


t1[1:]


# In[ ]:


t2 = ('c', 'd')

t1 + t2


# In[ ]:


t2 * 4


# In[ ]:


len(t1)


# In[ ]:


t1.count(1)


# In[ ]:


tu1 = (1,2,1,1,1,3,4,5,5,6,7,8,10)


# In[ ]:


tu1.count(1)


# In[ ]:


tu1.pop()

tu1


# pop 메소드는 맨뒤의 숫자를 빼내는 것이기에 변조 시도. 따라서 튜플에서는 사용불가

# In[ ]:


tu1.index(5)


# In[ ]:


tu1.reverse()

tu1


# reverse도 마찬가지로 변조이기에 사용 불가!

# In[ ]:




