#!/usr/bin/env python
# coding: utf-8

# In[1]:


def hours():
    print('Open 9-5 daily')


# In[2]:


import zoo
zoo.hours()


# In[3]:


import zoo as menagerie
menagerie.hours()


# In[4]:


import sqlalchemy
conn = sqlalchemy.create_engine('sqlite3:///books.db')
sql = 'select title from book or by title asc'
rows = conn.execute(sql)
for row in rows:
    print(row)


# In[ ]:




