import requests
import json
from bs4 import BeautifulSoup
#Сначала надо получить исходный код сайта и обработать его в BeautifulSoup. Тут будет часто использоваться то, что BeautifulSoup готов обрабатывать строки, необязательно полученные 
#через метод request.get().Однако фаилы самого BeautifulSoup прямо опять обработать через BeautifulSoup нельзя. Поэтому для начала обрабатывается код сайта через BeautifulSoup, затем
# то, что получено, если нужно извлечь информацию оттуда, переводится str() в строки и заново по нужным идентификаторам находятся нужные данные через BeautifulSoup. И так делается
# столько, сколько нужно
url1="https://books.toscrape.com/"
url11="https://books.toscrape.com/catalogue"
text=requests.get(url1)
soup=BeautifulSoup(text.text,'html.parser')
# Дальше находим список ссылок на страницы списков книг разных жанров
ff=soup.find('ul', class_="nav nav-list")
ss=str(ff)
soup1=BeautifulSoup(ss,'html.parser')
ff1=soup1.findAll('a')
#Тут создаем на будущее несколько пустых списков и основной словарь, в котором будут заносится данные о книгах и который позже будет переведен в формат json
sss=[]
ssss=[]
FF={}
ssss1=[]
#Выделяем части ссылок и делаем из этого список
for x in ff1:
    s=x.get('href')
    sss.append(s)
# С помощью полученного из прошлого шага списка создаем новый список, состоящий из ссылок, полученных присоединением основной части ссылки на сайт и части, отвечающей за конкретный
# жанр
for x in sss:
    urll=url1+x
    ssss.append(urll)
#Теперь циклом нам нужно пройтись по списку ссылок, зайдя на них всех. Нулевым в списке является ненужная нам информация, поэтому рассматривается все сразу с первого 
# элемента списка
for x in range(1,len(ssss)):
# Для начала выделяем название жанра книг и
    textt=requests.get(ssss[x])
    soupp=BeautifulSoup(textt.text,'html.parser')
    headd=soupp.find('li',class_='active').text
    FF[headd]={}
#Создаем пустой список, в котором будут все данные по книгам отдельного жанра
    sf=[]
#Далее запускаем цикл, который будет заканчиваться при условии, если нет больше страниц с книгами определенного жанра. Это мы определяем тем, содержится ли что нибудь в 
# объекте nextt
    while True:
#Находим все ссылки на описания отдельных книг и заносим их в список sf
        fff4=soupp.find('ol',class_='row')
        fff4=str(fff4)
        fff4=BeautifulSoup(fff4,'html.parser')
        fff4=fff4.findAll('a')
        for g in fff4:
            s=g.get('href')
            sf.append(s)
#Так как ссылки там повторяются, переводим список сначала в множество, чтобы устранить повторения, а потом обратно в спискок (благо, порядок книг нам не важен)
        sf=list(set(sf))
#Далее находим объект nextt и проверяем,пустой ли он
        nextt=soupp.find('li',class_='next')
        if nextt is None:
            break
        else:
#В случае, если в объекте nextt что то есть (то есть страница не последняя), нам нужно переидти на следующую страницу, для этого сначала выделяем последний кусок будущей ссылки
            nextt=str(nextt)
            nextt=BeautifulSoup(nextt,'html.parser')
            nextt=nextt.find('a').get('href')
#Для получения ссылки на следующую страницу нам нужно соединить кусок ссылки на список книг отдельного жанра и nextt. Так как мы заранее, что ссылка на список книг заканчивается
# всегда одинаково - index.html, то при обозначении первой части ссылки используем слайс от 0 элемента до -11.
            soupp=requests.get(ssss[x][0:-11:1]+nextt)
            soupp=BeautifulSoup(soupp.text,'html.parser')
# Теперь нам нужно получить список полных ссылок на описания книг отдельного жанра. Для этого присоединяем вторую ссылку, которую мы задали далеко в самом начале и ссылку из
# списка sf и букву l. Дело в том, что мы не знаем точную длину слайса, однако мы знаем, что нужен слайс от 8 элемента до последнего, которого можно обозначить -1. Так как 
# Python при указании слайсов съедает последний элемент, в данном случае мы знаем, что это "l", то добавляем его искуственно
    for d in range(len(sf)):
        sf[d]=url11+sf[d][8:-1:1]+'l'
# Теперь самая легкая часть - нам нужно получить данные о цене, есть ли книга на складе и описание и заносим это все в словарь FF
    for l in sf:
        textt1=requests.get(l)
        textt1=BeautifulSoup(textt1.text,'html.parser')
        name1=textt1.find('h1').text
        price=textt1.find('p',class_='price_color').text
        instock=textt1.find('p',class_='instock availability').text.strip()
        descr=textt1.findAll('p')
        descr=descr[3].text
        FF[headd][name1]={}
        FF[headd][name1]['Цена']=price
        FF[headd][name1]["In stock"]=instock
        FF[headd][name1]['Description']=descr





#Сохраняем словарь FF в фаил json
with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(FF, file, ensure_ascii=False, indent=4)
