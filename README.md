# NaiveBayes
Вероятность, что новость прнадлежит теме: P(c|d) = P(d|c) * P(c)/P(d), d-новость, c-тема.
Нужно найти Сmax = argmax (P(c|d)), среди всех тем.
argmax (P(c|d))=argmax (P(d|c) * P(c)) [P(d)- константа, одинаковая для всех тем].
Пусть позиции слов не важны, и появления слов в новости- независимые события, тогда
P(d|c)=P(x1|c)* P(x2|c)*..* P(xn|c), где P(xi|c) - вероятность появления i - го слова в теме.
P(c)= Nc/N - вероятность появления темы (частота).
P(xi|c) = (N(xi|c) +1)/SUM (N(xi|c)+1)= [сумма для всех слов в теме, +1 для защиты от нулей в произведении] =
=(N(xi|c) +1)/SUM (N(xi|c))+V), где V- размер словаря , SUM (N(xi|c)) - общее число слов в теме .
