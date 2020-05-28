FizzBuzz Kata
==================

## Run tests

`python fizzbuzz/FizzBuzzTest.py`

## Unittest framework

https://docs.python.org/3/library/unittest.html#module-unittest


## Wymagania

FizzBuzz to gra w której gracze liczą po kolei: 1, 2... Ale gdy liczba jest podzielna przez 3, zamiast tej liczby należy powiedzieć "Fizz". Natomiast gdy liczba jest podzielna przez 5 trzeba powiedzieć "Buzz". Gdy liczba jest podzielna zarówno przez 3 jak i przez 5, trzeba powiedzieć "FizzBuzz".

Twoje zadanie to:

1. Utwórz funkcję, która przyjmuje liczbę naturalną większą od 0 i zwraca dla niej reprezentację, będący odpowiedzią w grze Fizz Buzz.
   Np. dla liczby `3` powinna zwrócić `"Fizz"`.

2. Utwórz program, który wypisuje na konsolę odpowiedzi dla liczb od 1 do 100 oddzielone przecinkami.
   Np. dla liczby `3` progam powinien wyświetlić na ekranie `"1,2,Fizz"` (bez przecinka na końcu).


#### Dodatkowe opcjonalne wymagania:

1. Fizz odpowiadamy również wtedy, gdy liczba zawiera cyfrę 3. Np. `"Fizz"` dla `31`. Ale nadal `"FizzBuzz"` dla `30`,
   ponieważ jest także podzielne przez 5.
    
2. Podobnie dla Buzz - także, gdy liczba zawiera cyfrę 5.

3. Wprowadzamy nową zasadę: dla liczb podzielnych przez/zawierających 7 mówimy `Bar`. 
   Czyli na przykład: 14 - `Bar`, 21 - `FizzBar` 

4. Od teraz Fizz, Buzz i Bar mówimy dla podzielności przez/zawierania cyfr 5, 7 i 9 (zamiast 3, 5 i 7).



## Requirements

In this games players count one after another: 1,2,3... But for multiples of 3 they need to say "Fizz" instead of the number. For the multiples of 5 say "Buzz" instead of the number. For numbers which are multiples of both 3 and 5 players need to say "FizzBuzz" instead of the number

You task is to:

1. Write a function that takes one number (larger than 0) and return its representation in FizzBuzz game
   For instance, for number `3` is should return `"Fizz"`.
2. Write a program that prints on console answers for numbers from 1 to 100, comma separated
   For instance, for number `3` the application should print `"1,2,Fizz"` (notice no comma at the end).


* Optional requirements:

1. "Fizz" returned also when number contains digit 3
2. "Buzz" returned also when number contains digit 5.
3. "Fizz" and "Buzz" when number is multiple or contains digit: 7 i 9.
