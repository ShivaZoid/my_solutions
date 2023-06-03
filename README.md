# Решение задач

## 1) [__Добрый, добрый Python - обучающий курс от Сергея Балакирева__](https://stepik.org/course/100707/syllabus) на сайте Stepik

## Решения начинаются с 3 темы

## __3. Постижение строк и списков__
* 3.1 Введение в строки. Операции над строками
    <details>
    <summary>Подвиг 5.</summary>
    Напишите программу ввода двух строк (каждая вводится с новой строки) и их объединения в одну
    строку через пробел. Результат выведите на экран.

    ### Sample Input
    hello python
    i love you

    ### Sample Output
    hello python i love you

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/3_topic/3_1/5.py)

    </details>
    <details>
    <summary>Подвиг 7.</summary>
    Напишите программу ввода двух слов через пробел. Сформируйте новую строку, продублировав первое
    слово дважды, а второе - трижды (все слова в результирующей строке должны идти через пробел).
    Результат выведите на экран.

    Программу следует реализовать без использования F-строк, а с применением оператора дублирования
    строк.

    ### Sample Input
    hello python

    ### Sample Output
    hello hello python python python

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/3_topic/3_1/7.py)

    </details>
    <details>
    <summary>Подвиг 8.</summary>
    Выполняется считывание двух целочисленных значений в переменные a и b (вводятся в одну строчку
    через пробел). Необходимо сформировать строку вида: "Переменная a = <значение>, переменная b =
    <значение>", используя оператор конкатенации (соединения) строк. Результат выведите на экран.

    P. S. F-строки в программе не использовать.

    ### Sample Input
    2 -5

    ### Sample Output
    Переменная a = 2, переменная b = -5

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/3_topic/3_1/8.py)

    </details>
    <details>
    <summary>Подвиг 9.</summary>
    Написать программу ввода строки и формирования новой строчки вида: "Строка: <введенная строка>.
    Длина: <длина строки>". Результат сформированной строки вывести на экран.

    P. S. В программе F-строки не использовать.

    ### Sample Input
    hello Balakirev

    ### Sample Output
    Строка: hello Balakirev. Длина: 15

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/3_topic/3_1/9.py)

    </details>
    <details>
    <summary>Подвиг 10.</summary>
    Написать программу ввода двух слов (через пробел в одну строчку). Определить булевы значения для
    оператора in проверки вхождения первого слова во второе. А также для операторов ==, >, <. Все
    булевы значения объединить в одну строку через пробел и вывести на экран.

    ### Sample Input
    hello python

    ### Sample Output
    False False False True

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/3_topic/3_1/10.py)

    </details>
    <details>
    <summary>Подвиг 11.</summary>
    С клавиатуры вводятся две буквы (в одну строку через пробел). Вывести на экран следующую строку:
    "Коды: <буква1> = <код буквы1>, <буква2> = <код буквы2>"

    ### Sample Input
    a z

    ### Sample Output
    Коды: a = 97, z = 122

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/3_topic/3_1/11.py)

    </details>

* 3.2 Индексы и срезы строк
	<details>
    <summary>Подвиг 1.</summary>
    Напишите программу ввода строки и отображения на экране ее первого и последнего символа в виде
    одной строки.

    ### Sample Input
    I love Python

    ### Sample Output
    In

    [__Решение__]()

    </details>
    <details>
    <summary>Подвиг 4.</summary>
    Напишите программу отображения первых четырех символов из введенной строки. Будем полагать, что
    строка гарантированно длиной не менее четырех символов.

    ### Sample Input
    panda

    ### Sample Output
    pand

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/3_topic/3_2/4.py)

    </details>
    <details>
    <summary>Подвиг 5.</summary>
    Напишите программу отображения последних трех символов из введенной строки. Будем полагать, что
    строка гарантированно длиной не менее трех символов.

    ### Sample Input
    Balakirev

    ### Sample Output
    rev

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/3_topic/3_2/5.py)

    </details>
    <details>
    <summary>Подвиг 6.</summary>
    Напишите программу отображения всех символов с нечетными индексами из введенной строки.

    ### Sample Input
    Balakirev

    ### Sample Output
    aaie

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/3_topic/3_2/6.py)

    </details>
    <details>
    <summary>Подвиг 7.</summary>
    Вводятся две строки (каждая с новой строчки). Из первой строки выделить все символы с четными
    индексами, а из второй - с нечетными. Объединить строки через пробел и вывести на экран.

    ### Sample Input
    Hello

    Python

    ### Sample Output
    Hlo yhn

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/3_topic/3_2/7.py)

    </details>
    <details>
    <summary>Подвиг 8.</summary>
    Из введенной строки отобразить первые пять символов в обратном порядке. Полагается, что введенная
    строка имеет минимум пять символов.

    ### Sample Input
    abrakadabra

    ### Sample Output
    karba

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/3_topic/3_2/8.py)

    </details>
    <details>
    <summary>Подвиг 9.</summary>
    Вводятся два слова (через пробел в одной строке). Длина первого слова меньше второго. Необходимо
    обрезать второе слово до длины первого и отобразить обрезанное слово на экране.

    ### Sample Input
    Hello Balakirev

    ### Sample Output
    Balak

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/3_topic/3_2/9.py)

    </details>
    <details>
    <summary>Подвиг 10.</summary>
    Вводятся два слова (через пробел в одной строке). Длина второго слова меньше первого. Из этих слов
    выделить символы с нечетными индексами с обрезкой первого слова до длины второго. Сравнить
    полученные строки между собой на равенство и результат (True или False) вывести на экран. Задачу
    выполнять без использования условного оператора.

    ### Sample Input
    Hello Hell

    ### Sample Output
    True

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/3_topic/3_2/10.py)

    </details>