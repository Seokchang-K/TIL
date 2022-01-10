#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n=3
"I eat {0} apples" .format(n)


# In[ ]:


'I eat {0} apples' .format('five')


# In[ ]:


n=10
day = 'tree'

"I ate {0} apples. so I was sick for {1} days." .format(n, day)


# In[ ]:


"I ate {0} apples. so I was sick for {1} days" .format(n=100, day='first')


# In[ ]:


"I ate {n} apples. so I was sick for {day} days" .format(n=100, day='first')


# In[ ]:


"I ate {0} apples. so I was sick for {day} days" .format(100, day='first')


# In[ ]:


"{0:<10}" .format('hi')


# In[ ]:


"{0:>10}" .format('hi')


# In[ ]:


"{0:^10}" .format('hi')


# In[ ]:


"{0:=<10}" .format('hi')


# In[ ]:


"{0:!<10}" .format('hi')


# In[ ]:


"{0:0.4f}" .format(3.141569)


# In[ ]:


'{{and}}' .format()


# ## f-formatting

# In[ ]:


name = '홍길동'
age = 20

f'나의 이름은 {name} 입니다. 나이는 {age} 입니다.'


# In[ ]:


f'나는 올해 {age+1} 이 되었다.'


# In[104]:


d={ 'name' : '김철수' , 'age':20}
f'나의 이름은 {d["name"]} 입니다. 나이는 {d["age"]} 입니다.'


# In[ ]:


f'{"hi":<10}'


# In[ ]:


f'{"hi":>10}'


# In[ ]:


f'{"hi":^10}' 


# 
# '''{[인덱스/값]:[공백을 채울 문자][정령방식][자리수]}'''

# In[ ]:


f'{"hi":$^10}'


# In[ ]:


'{0},{1},{2}' .format('a','b','c')


# In[ ]:


'{},{},{}' .format('a','b','c')


# In[ ]:


'{2},{1},{0}' .format('a','b','c')


# In[ ]:


'{2},{1},{0}' .format(*'abc')


# In[ ]:


'{0}{1}{0}' .format('abra', 'cad')


# In[ ]:


'Coordinates: {latitude}, {longtitude}' .format(latitude='37.24N', longtitude='-115.81\')


# In[ ]:





# ### 문자열 함수

# In[ ]:


a = 'Hello World'

a.count('l')


# In[ ]:


a = 'Python is the best choice'

a. find('b')


# In[ ]:


a. find('k')


# In[ ]:


a= 'Life is too short'

a. index('t')


# In[ ]:


a. index('k')


# In[ ]:


',' .join('abcd')


# In[ ]:


',' .join(['a','b','c','d'])


# In[ ]:


a = 'Welcome'

a. upper()


# In[ ]:


a. lower()


# In[ ]:


a = '       hi'

a. lstrip()


# In[ ]:


a. strip()


# In[ ]:


a='Life is too short'

a. replace('Life', 'Your leg')


# In[ ]:


'Your leg' + a[4:]


# In[ ]:


a. split()


# In[ ]:


a= 'a:b:c:d'

a. split(':')


# ### 3.리스트

# In[ ]:


odd = [1,3,5,7,9]
odd


# In[ ]:


odd[0]


# In[ ]:


a = []

a


# In[ ]:


a = ['I','love','you']
a


# In[ ]:


a = [1,2,'I','love','you']

a


# In[ ]:


a = [1,2,['I','love','you']]

a


# In[ ]:


a = [1,2,3]
a


# In[ ]:


a[0]


# In[ ]:


a[0] + a[2]


# In[ ]:


a[-1]


# In[106]:


a=[1, 2, ['I', 'love', 'you']]

a[0]


# In[ ]:


a[-1]


# In[ ]:


a[-1][1]


# In[ ]:


a=[1,2, ['a','b',['life', 'is','good']]]

a


# In[108]:


a=[1,2,['a','b',['life', 'is', 'good', [3,4,5]]]]

a[2][2][0]


# In[109]:


a=[1, 2, ['I', 'love', 'you']]
a[-1][1]


# In[ ]:




