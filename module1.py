from random import *
s=pos=neg=nol=[]
def arvud_loendis():
    print("Данные:")
    n=abs(int(input("Сколько целых чисел генерируем в список? => ")))
    mini=int(input("Введите минимальное число диапазона => "))
    maxi=int(input("Введите максимальное число диапазона => "))
    if mini>=maxi:
        mini,maxi=vahetus(mini,maxi)
    generaator(n,s,mini,maxi)
    print()
    print("Результаты:")
    print("Полученный список от",mini,"до",maxi,s)
    s.sort()
    print("Отсортированный список",s)
    jagamine(s,pos,neg,nol)
    print("Список положительных элементов",pos)
    print("Список отрицательных элементов",neg)
    print("Список нулевых элементов",nol)
    kesk=keskmine(pos)
    lisamine(s,kesk)
    print("Среднее положительных:",kesk)
    kesk=keskmine(neg)
    lisamine(s,kesk)
    print("Среднее отрицательных:",kesk)
    print("Добавляем средние в изначалный массив:")
    print(s)

def vahetus(a:int,b:int):
    """Kui min suurem kui max, siis vahetame neid omavahel
    :parem int a: minimaalne arv, mis on suurem kui max
    :parem int b: maximaalne arv, mis on väiksem kui min
    :rtype int,int:
    """
    abi=a
    a=b
    b=abi
    return a,b

def generaator(n:int,loend:list,a:int,b:int):
    """Genereerib juhusliku arvu
    :parem int n:Numbri number
    :parem list loend:
    :parem int a:Minimaalne arv
    :parem int b:Maksimaalne arv
    """
    for i in range (n):
        loend.append(randint(a,b))
    

def jagamine(loend:list,p:list,n:list,nol:list):
    """leiab positiivsete, negatiivsete, nullide loendeid
    :parem list loend:Nimekiri
    :parem list p:Nimekiri
    :parem list n:Nimekiri
    :parem list nol:Nimekiri
    :rtype list
    """
    for el in loend:
        if el>0:
            p.append(el)
        elif el<0:
            n.append(el)
        else:
            nol.append(el)

def keskmine(loend):
    """leiab positiivse keskmise
    :rtype int n:
    :rtype int
    """
    n=len(loend)
    if n==0:
        kesk=0
    else:
        sum=0
        for i in loend:
            sum+=i
        kesk=round(sum/n,2)
    return kesk

def lisamine(loend:list,el:float):
    """lisab ja sorteerib loendit
    :rtype float
    """
    loend.append(el)
    loend.sort()

arvud_loendis()