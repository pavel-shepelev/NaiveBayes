#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from collections import Counter

trainsize=50
testsize=10

fname="news_train.txt"
category=[]
content=[]
with open(fname, encoding='utf-8') as f:
    articles = f.readlines()
    for article in articles:
        category.append(article.split("\t", 1)[0])
        content.append(article.split("\t", 1)[1])
        
content = [x.strip() for x in content]

def Main():
    names=list(set(category))
    
    def IndexSelect(name):
        I=[]
        for i in range(trainsize):
            if (category[i]== name):
                I.append(i)
        return I

    testdic= dict(Counter(testcontent.split()))
    traindic = dict(Counter(content[1].split()))
    
    def CommonWords(categ):
        testcounts=dict.fromkeys(testdic, 0)
        totalwords=0
        voc=[]
        #commonwords = {k:testdic[k] for k in some_dict if k in traindic}
        for i in IndexSelect(categ):
            traindic = dict(Counter(content[i].split()))
            totalwords+=len(traindic.keys())
            voc=list(set(voc+list(traindic.keys())))
            for key in traindic:
                if key in testdic:
                    testcounts[key]+=traindic[key]
        return (testcounts, totalwords, voc)
    
    def Prior (categ):
        return (len(IndexSelect(categ))/len(category))
    
    #total vocabulary length
    def VocLength():
        voc=[]
        for categ in names:
            voc= list(set(CommonWords(categ)[2]+voc))
        return len(voc)

    probs=[]
    for categ in names:
        testcounts, totalwords, voc = CommonWords(categ)
        condprob=dict.fromkeys(testcounts, 0)
        p=1
        for word in testcounts:
            condprob[word]=10000*(testcounts[word]+1)/(totalwords +VocLength())
            if condprob[word] ==0.0:
                print("oops")
            p*=condprob[word]
        p*=Prior(categ)
        probs.append(p)
        #print(categ)
        #print(p)
    val,idx=max((val, idx) for (idx, val) in enumerate(probs))
    return (names[idx])

answer= open('answer.txt', 'w', encoding="utf8")
#test data
#testcategory='media'
#testcontent= 'CNN оказался самым непопулярным новостным каналом в США	CNN занял последнее место среди американских кабельных новостных каналов по размеру аудитории в прайм-тайм. Об этом сообщает издание The New York Times.По данным газеты, в октябре среднее число зрителей 25-54 лет, которые смотрели передачи канала с семи до 11 часов вечера, составило 202 тысячи человек. Аналогичные показатели его конкурентов - Fox News, MSNBC и HLN - составили 689 тысяч, 250 тысяч и 221 тысячу человек соответственно.В частности, отмечает издание, самыми непопулярными оказались три из четырех передач канала, которые транслировались в вечернем эфире. Единственной программой, которая заняла не последнее, а предпоследнее место, стало шоу Ларри Кинга.По мнению The NY Times, низкие результаты CNN объясняются большей по сравнению с конкурентами ориентированностью канала на исключительно новостные передачи. Подобной версии придерживаются и на самом телеканале, представитель которой заявил о сильной зависимости CNN от новостной конъюнктуры.Между тем, как пишет издание New York Post, в рейтинге, который замеряет среднесуточную аудиторию не только в прайм-тайм, а в течение всего дня, CNN проигрывает лишь Fox News.Ранее в интервью Bloomberg TV основатель CNN Тед Тернер выразил неудовольствие политикой канала, отметив, что ему следует давать в эфир "меньше разговоров и больше новостей".Круглосуточный новостной канал CNN был создан в 1980 году, став первым подобным проектом в США. В 1996 году он вошел в состав медиа-корпорации Time Warner, которую в 2001 году приобрела America Online. Созданному в результате сделки конгломерату, сохранившему название Time Warner, также принадлежит канал HLN, ранее известный как CNN-2.Владельцем Fox News является News Corp. Руперта Мердока, MSNBC принадлежит компаниям NBC Universal и Microsoft.'
testfname="news_test.txt"
tcategory=[]
tcontent=[]
with open(fname, encoding='utf-8') as f:
    tarticles = f.readlines()
    for article in tarticles:
        tcategory.append(article.split("\t", 1)[0])
        tcontent.append(article.split("\t", 1)[1])
for i in range(testsize):
    testcategory= tcategory[i]
    testcontent= tcontent[i]
    answer.write(Main()+'\n')

