#!/usr/bin/env python
# coding: utf-8

# In[25]:


from collections import Counter

trainsize=6000
testsize=len(tcategory)


# In[26]:


fname="news_train.txt"
category=[]
content=[]
with open(fname, encoding='utf-8') as f:
    articles = f.readlines()
    for article in articles:
        category.append(article.split("\t", 1)[0])
        content.append(article.split("\t", 1)[1])
        
content = [x.strip() for x in content]


# In[ ]:


names=list(set(category))


# In[28]:


#Выбираем индексы новостей данной темы из всех новостей
def IndexSelect(name):
    I=[]
    for i in range(trainsize):
        if (category[i]== name):
            I.append(i)
    return I


# In[31]:


# Общие слова тестовой новости и новостей данной темы
def CommonWords(categ, testdic):
    testcounts=dict.fromkeys(testdic, 0)
    for i in IndexSelect(categ):
        traindic = dict(Counter(content[i].split()))
        for key in traindic:
            if key in testdic:
                testcounts[key]+=traindic[key]
    return (testcounts)


# In[32]:


#Вероятность темы 
def Prior (categ):
    return (len(IndexSelect(categ))/len(category))


# In[33]:


#Считаем количество слов и формируем словарь темы
def WordsnVoc(categ):
    totalwords=0
    voc=[]
    for i in IndexSelect(categ):
        traindic = dict(Counter(content[i].split()))
        totalwords+=len(traindic.keys())
        voc=list(set(voc+list(traindic.keys())))
    return (totalwords, voc)


# In[34]:


values=[]
voc=[]
for categ in names:
    voc= list(set(WordsnVoc(categ)[1]+voc))
    values.append(WordsnVoc(categ)[0])
totalwords=dict(zip(names, values))
voclength=len(voc) 
print(voclength)  #Длина общего словаря
print(totalwords) #Число слов в каждой теме 


# In[35]:


def Main(testdic):
    probs=[]
    for categ in names:
        testcounts=CommonWords(categ, testdic)
        condprob=dict.fromkeys(testcounts, 0)
        p=1
        for word in testcounts:
            condprob[word]=10000*(testcounts[word]+1)/(totalwords[categ] +voclength) #вероятность что новость принадлежит
                                                                                     #данной теме, при условии, что в ней
                                                                                     #есть данное слово (+1 - защита от нулей
                                                                                     #в произведении) 
            p*=condprob[word]  #умножаем для каждого слова в тестовой новости   
        p*=Prior(categ)        #и на вероятность темы
        probs.append(p)
    val,idx=max((val, idx) for (idx, val) in enumerate(probs))
    return names[idx]


# In[ ]:


testfname="news_test.txt"
tcontent=[]
with open(testfname, encoding='utf-8') as f:
    tarticles = f.readlines()
    
answerfile= open('answer.txt', 'w', encoding="utf8")
answer=''

#Запись ответа в файл
for i in range(testsize):
    testdict=dict(Counter(tarticles[i].split()))
    answer=Main(testdict)
    answerfile.write(answer+'\n')
#Точность 0.7853

