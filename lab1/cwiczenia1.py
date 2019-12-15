#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
zad. 1
Przejrzyj plik podstawy.py. Zawiera on kopię materiałów z części wykładowej.
"""

"""
zad. 2
Stwórz zmienną o nazwie `PI` i wartości 3.14. Wykorzystaj ją do obliczenia pola koła o promieniu 12.
Wynik wyświetl na ekran.
"""

pi=3.14
P = pi*(12**2)
print("Pole kołoa wynosi ", P)

"""
zad. 3
 * Stwórz dwie zmienne imie i nazwisko i przypisz do dowolne wartości (nie muszą
być prawdziwe).
 * wypisz obie zmienne na ekran.
 * Połącznie obie zmienne spacją i wynik zapisz do zmiennej dane.
"""
imie = "Tomasz"
nazwisko = "Szymanski"
print(imie)
print(nazwisko)
dane = imie + " " + nazwisko
print(dane)

"""
zad. 4
Przekonwertuj wartość b na int, a następnie oblicz średnią z a, b i c.
"""
a = 314
b = "500"
c = 4.5

b= int(b)
srednia = (a+b+c)/3
print(srednia)

"""
zad. 5
Wczytaj z klawiatury 3 liczby, skonwertuj je na dowolny typ liczbowy, a
wynik zapisz do zmiennej suma. Wyświetl zawartość tej funkcji na ekran.
"""
a = input('Podaj a:  ')
b = input('Podaj b:  ')
c = input('Podaj c:  ')

sum = int(a) + int(b) + int(c)
sum2 = float(a) + float(b) + float(c)
print("suma wynosi:  ", sum)
print("suma wynosi:  ", sum2)
"""
zad. 6
Stwórz 3 elementową listę, która zawiera nazwy 3 Twoich ulubionych owoców.
Wynik przypisz do zmiennej `owoce`.
"""

owoce = ["czeresnie", "gruszki", "winogrona"]

print(owoce)

"""
zad. 7
Dodaj do powyższej listy jako nowy element "pomidor".
"""
owoce.append("pomidor")
print(owoce)
"""
zad. 8
Usuń z powyższej listy drugi element.
"""
#owoce.remove('gruszki')

usuniety = owoce.pop(1)

print(owoce)
print("element usuniety: ",usuniety)

"""
zad. 9
Rozszerz listę o tablice ['Jabłko', "Gruszka"].
"""

#owoce.append('Jabłko')
#owoce.append( "Gruszka")

owoce.extend(['Jabłko',"Gruszka"])
print(owoce)

"""
zad. 10
Wyświetl listę owoce, ale bez pierwszego i ostatniego elementu.
"""
print(owoce[1:len(owoce)-1])
"""
zad. 11
Wyświetl co trzeci element z listy owoce.
"""
print(owoce[1:len(owoce):3])
"""
zad. 7
Stwórz pusty słownik i przypisz go do zmiennej magazyn.
"""

magazyn ={}

"""
zad. 8
Dodaj do słownika magazyn owoce z listy owoce, tak, aby owoce były kluczami,
zaś wartościami były równe 5.
"""
 for item in owoce:
        magazyn[item] = 5

print(magazyn)

"""
zad. 9
 * Stwórz listę składającą się z parzystych elementów listy l (l. parzystych)
 * Stwórz listę z elementów l o nieparzystych indeksach
"""
l = [4, 5, 8, 9, 0, 3]

"""
zad. 10
Lista `zad10` zawiera 2 elementy - listy. Stwórz nową listę `zad10_flat`,
która będzie składać się z elementów każdej z tych listy.
"""

zad10 = [[9, 8, 12, 7], [12, 33, 8, 7]]
zad10_flat = zad10[0] + zad10[1]
print(zad10_flat)

"""
zad. 11
Stwórz listę zad11out, która powstanie z <zad11> poprzez usunięcie 
powtarzających się wartości.
"""

zad11 = [3, 2, 2, 6, 9, 10, 1, 3]

"""
zad. 12
Wyświetl sumę liczb od 1 do 256.
"""
n = 257
sum = 0
for i in range(n):
    sum +=i

print('sum', sum)
"""
zad. 13
Wyświetl sumę liczb parzystych od 1 do 256.
"""

"""
zad. 14
Poniżej znajdują się 2 słowniki z danymi o liczbie przejazdów rowerami miejskimi w Montrealu w 2018 z podziałem na miesiące.
Pierwszy słownik zawiera informacje o przejazdach wykonanych przez posiadaczy abonamentu, a drugi przez ludzi, który
nie mają wykupionego abonamentu. Dane pochodzą ze strony https://montreal.bixi.com/en/open-data. 

a) Stwórz trzeci słownik `all_rides`, w którym zliczysz łączną liczbę przejazdów w każdym z miesięcy.
b) Wykorzystując listę `months` wyświetl ile w danym miesiącu odbyło się przejazdów. Załóż, że odbyło się 0 przejazdów 
w miesiącach, którycj brakuje w `all_rides`.
c) Oblicz jaki procent stanowią w ciągu roku przejazdy okazjonalne.
d) Czy obie grupy osiągają największą liczbę przejazdów w tym samym miesiącu? Spróbuj znaleźć odpowiedź bez patrzenia
na wartości w podanych słownikach.
"""

members = {'April': 211819, 'May': 682758, 'June': 737011, 'July': 779511, 'August': 673790,
           'September': 673790, 'October': 444177, 'November': 136791}

occasionals = {'April': 32058, 'May': 147898, 'June': 171494, 'July': 194316, 'August': 206809,
               'September': 140492, 'October': 53596, 'November': 10516}

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']

"""
zad. 15
 * Stwórz listę składającą się z dowolnych 100 elementów, np. może być
 to listę kwadratów liczb.
 * Sprawdź za pomocą funkcji len liczbę elementów tej listy.
 * Usuń trzeci, element.
 * Usuń przedostatni element.
 * Wyświetl pierwsze 10 elementów.
"""

"""
zad. 16
Znajdz najmniejsz element w poniższej liście.
"""
numbers = [0, 6, 9, -10, -5, 9, 8, -6]

"""
zad. 17
Wyświetl poniższy słownik, tak, aby każda para "klucz: wartość"
była w osobnej linii.
"""
s = {'Tomasz': [3, 4, 5, 4], 'Agata': [5, 5, 5, 4]}


"""
zad. 18
Poniżej jest podana lista liczby. Stwórz słownik <counter>, którego kluczami
będą wartości występujące w liście <liczby>, a wartościami ile dany element
wystąpił w liście <liczby>.
"""
liczby = [3, 4, 3, 3, 4, 7, 9]

"""
zad. 19
Poniższy słownik oceny dwóch osób. Stwórz nowy słownik z takimi samymi kluczami,
ale wartościami tego słownika będą średnie oceń.
"""
s = {'Tomasz': [3, 4, 5, 4], 'Agata': [5, 5, 5, 4]}


"""
zad. 20
Dla podanego poniże słownika S, stwórz nowy słownik, którego kluczami będą
wartości słownika S, a wartościami: odpowiadające im klucze z S.
"""
s = {'Klucz1': 'Wartosc1', 'Klucz2': 'Wartosc2', 'Klucz3': 'Wartosc3'}

"""
zad. 21
Napisz kod, który wypisze na ekran elementy, które występnują w obu poniżej
podanych funkcjach.
"""
l1 = [99, 8, 7, 55]
l2 = [55, 111, 11, 99, 8]

"""
zad. 22
Napisz kod, który znajdzie najdroższy produkt  w poniższym słowniku.
"""
zakupy = {'telefon': 1000, 'ładowarka': 35, 'chleb': 4.30, 'kawa': 55, 'gramofon': 240}

"""
zad. 23
Stwórz listę składającą się z wartości słownika zakupy.
"""
zakupy = {'telefon': 1000, 'ładowarka': 35, 'chleb': 4.30, 'kawa': 55, 'gramofon': 240}

"""
zad. 24
Wyświetl na ekranie poniższy wzór:
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""
