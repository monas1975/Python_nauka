#!/usr/bin/env python
# coding: utf-8

# # Podstawy Pythona: cz. 1
#
# &nbsp;
#
# ##  15 grudnia 2019

# In[ ]:


print('Hello Python')


# In[4]:



print('Hello')
print('Python')
print('Hello', 'Python', '!')


# Typy podstawowe:
#  * liczby całkowite (`int`): `3`, `1000`, `-100`, `0`
#  * liczby rzeczywiste (`float`): `3.14`, `5.0`, `-0.001`
#  * napisy: (`str`): `"Python"`, `"Rock'n'Roll"`, `'zalicznie z przedmiotu'`
#  * logiczne (`bool`): `True`, `False`
#  * None: `None`

# In[1]:


print(10)
print(1000.0)
print (100, 100.0, 'Sto')
print('Zaokrąglenie PI:', 3.141519)
print(True, False)
print(None)


# ## Zmienne
#  * case sensitive,
#  * brak konieczności deklaracji typu,
#  * do zmiennej można przypisać wszystko.

# In[2]:


user = "t.dwojak"
domain = "amu.edu.pl"
email = user + "@" + domain
print("email:", email)


# Operacje arytmetyczne na liczbach:
#  * dodawanie `+`, np. `2 + 3`
#  * odejmowanie `-`, np. `10-9`
#  * mnożenie `*`, np. `2.0 * 3.0`
#  * dzielenie `/`, np. `3 / 4` ( == 0.75)
#  * dzielenie całkowite `//`, `3 / 4` ( == 0)
#  * potęgowanie `**`, np. `10 ** 3` ( == 1000)

# In[15]:


print(1 + 2 - 3)
print("2 ** 10", "=", 2 ** 10)
print(1 + 2 - 3 + (4 * 5) / 6 ** 2)


# In[4]:


imie = input('Przedstaw się')
print('Cześć', imie, '!')


# Konwersja typów:

# In[24]:


print(int("100"))
print(str(100))
print(float(100))
print(bool("Fałsz"))


# ## Komentarze
#  * Komentarze nie są interpretowane.
#  * Komentarze w Pythonie zaczynają się od znaku '#'
#  * Istnieją komentarze wielolinijkowe tagowane potrójnym ", czyli """ """
#

# In[ ]:


print("Bardzo ważna wiadomość") # A to jest komentarz
"""
Komentarz
wielo-
linijkowy
"""
# print("Nie chcę być wydrukowanym")
print("A teraz chcę")


# ## Listy
#  * W Pythonie nie ma tablic, są listy;
#  * Listy mogą przechowywać elementy różnych typów;
#  * Indeksowanie zaczyna się od 0.
#  * Funkcja `len` zwraca liczbę elementów listy

# In[32]:


x = [] # albo równoważnie pusta_lista = list()
oceny = [5, 4, 3, 5, 5]
roznosci = [3.14, "pi", ["pi"], 3]
list_0_9 = list(range(10))
print("Liczba elementów", len(oceny))


# In[33]:


print(oceny)
print(oceny[1])


# ## Dodawanie i usuwanie elementów z listy
#
# Istnieją dwie metody:
#  * `append(x)`: dodaje x na koniec listy
#  * `extend(x)`: rozszerza listę o każdy element z x

# In[13]:


engines = []
engines.append('duck-duck-go')
engines.append("yahoo")
print(engines)


# In[9]:


m = ["google", 'bing']
m.extend(l)
print(m)


# In[15]:


liczby = [1,2,3,2,3,1,2,4]
liczby.pop() # Domyślnie usuwa ostatni element z listy
liczby.remove(2)
print(liczby)


# Inne przydatne metody:
#  * `sort()`: sortuje listę rosnąco
#  * `count(x)`: zlicza wystąpienia x w  liście
#  * `index(x)`: zwraca indeks pierwszego wystąpienia x

# In[20]:


liczby = [1,2,3,2,3,1,2,4]
print(liczby.count(1))
print(liczby.index(4))
liczby.sort()
print(liczby)


# ## Indeksowanie

# In[21]:


oceny = [1, 3, 2, 3, 1, 2, 4]
print('pierwszy element:', oceny[0])
print('ostatni element:', oceny[-1])
print('5 pierwszych:', oceny[:5])
print('5 ostatnich', oceny[-5:])
print('od drugiego, do piątego', oceny[1:5])
print('parzyste:', oceny[1:6:2])
print('od tyłu', oceny[::-1])


# ## Pętla typu ```for```
#  * W Pythonie pętla *for* działa jak pętla *for each* w innych językach;
#  * W Pythonie nie ma klamr, ani *begin* i *end*; jako ciało pętli musi być wcięte (najcześciej 4 spacje).

# In[22]:


n = 3

for i in range(n):
    print('element', i)


# In[23]:


l = ["jeden", "dwa", "trzy"]
for item in l:
    print(item)


# In[24]:


kwadraty = []

for i in range(10):
    kwadraty.append(i ** 2)

print(kwadraty)


# ## Słowniki: `dict`

# In[25]:


slownik = {}
s_oceny = {"Justyna" : [5,5,5], "Bartek" : [3,4,5], "Ola": [3,3,3]}
print(s_oceny)


# In[26]:


s_oceny["Jan"] = [3,4,5]
print(s_oceny)


# ## Iterowanie po słowniku

# In[27]:


for osoba in s_oceny:
    print(osoba,':', s_oceny[osoba])


# In[ ]:


for osoba, oceny in s_oceny.items():
    print(osoba,':', oceny)


# ## Instrukcja sterująca ```if ... else```

#  * działa tak samo, jak w innych języka;
#  * jest dodatkowa instrukcja następnego warunku *elif...*;

# In[30]:


zmienna = int(input("Podaj liczbe:\n"))

if zmienna < 0:
    print("Ujemna!")
elif zmienna > 0:
    print("Dodatnia")
else:
     print("Zero!")


# ## Przydatne warunki
#
#  * Porównanie za pomocą `==`
#  * znak różności: `!=`
#  * większe, mniejsze: `>`, `>=`, `<`, `<=`
#  * Sprawdzenie, czy coś jest w liście: `item in l`
#  * Do łączenia warunków służą słowa klucznowe `and` i `or`

# In[ ]:


if "Ala" in s_oceny:
    print("Ala jest w grupie!")
else:
    print("Niestety Ali nie ma  grupie!")


# # Łańcuchy znakowe

# In[ ]:


napis = "Wiadomość"
print(napis)


# Operacje na napisach:
#  * konkatenacja `+`, np. `"Tarnowo " + "Podgórne"`
#  * wielokrotność: `*`, np. `"O" * 6` ("OOOOOO")

# In[ ]:


for znak in napis:
    print(znak, ord(znak))


# In[ ]:


slowa = ['Bardzo' , 'ważna', 'wiadomość']
print(' '.join(slowa))


# In[ ]:


if 'dom' in napis:
    print(True)
else:
    print(False)


# In[ ]:


text = "Bardzo ważna wiadomość"
print(text.split(' '))


# In[ ]:


text = "Nie wszyscy lubią spacje na końcu linii.       "
print(text)
print(text.strip(' '))


# ## Funkcje

# ```python
# def nazwa_funkcji(arg_1, arg_2, arg_3):
#     instrukcja 1
#     instrukcja 2
#     return jakaś wartość
# ```

# In[5]:


def max2(a, b):
    if a >= b:
        return a
    return b
print(max2(56, 512))


# In[ ]:


def srednia(lista):
    s = 0
    for item in lista:
        s += item
    return s / len(lista)

print(srednia([7,8,9]))


# In[6]:


def count(lista, item):
    l = 0
    for i in lista:
        if i == item:
            l += 1
    return l


# In[9]:


count([5,5,5,4], 5)
count(lista=[5,5,5,4], item=5)
count(item=5, lista=[5,5,5,4])


# ## Korzystanie z bibliotek

# In[11]:


import os
print(os.name)

from os import getenv
print('Nazwa uzytkownika: {}'.format(getenv("USERNAME")))


# In[12]:


from collections import *
print(Counter("konstantynopolitańczykowianeczka"))


# In[15]:


import calendar as cal
cal.TextCalendar().prmonth(2019, 12)


# In[17]:


import math
math.cos(math.pi)


# Ważniejsze biblioteki:
#  * `os`, `sys`: obsługa rzeczy dt. systemu i środowiska
#  * `datetime`: wszystko co jest związane z czasem
#  * `collections`: zawiera `Counter` i `defaultdict`
#  * `typing`: poprawia anotacje typowania

# In[ ]:




