# Решение задач __Заброшено__

## 1) [__Добрый, добрый Python - обучающий курс от Сергея Балакирева__](https://stepik.org/course/100707/syllabus) на сайте Stepik 


[https://github.com/ShivaZoid/my_solutions/blob/main/stepik-certificate.pdf](https://github.com/ShivaZoid/my_solutions/blob/main/stepik-certificate.jpg)


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

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/3_topic/3_2/1.py)

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
* 3.3 Основные методы строк
    <details>
    <summary>Подвиг 2.</summary>
    Вводится слово. Необходимо первую букву этого слова сделать заглавной, а остальные - малыми.
    Результат отобразить на экране.

    ### Sample Input
    HELLO

    ### Sample Output
    Hello

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/3_topic/3_3/2.py)

    </details>
    <details>
    <summary>Подвиг 3.</summary>
    Вводится строка. Необходимо определить число вхождений дефисов (-) в этой строке. На экране
    отобразить полученное число.

    ### Sample Input
    osnovnye-metody-strok

    ### Sample Output
    2

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/3_topic/3_3/3.py)

    </details>
    <details>
    <summary>Подвиг 6.</summary>
    Вводится строка. С помощью метода String.find найдите в этой строке индекс первого вхождения
    фрагмента "ra". Полученное число выведите на экран.

    ### Sample Input
    abrakadabra

    ### Sample Output
    2

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/3_topic/3_3/6.py)

    </details>
    <details>
    <summary>Подвиг 7.</summary>
    Вводится строка (слаг). Замените в этой строке все двойные дефисы (--) и тройные (---) на одинарные
    (-). Подумайте, в какой последовательности следует выполнять эти замены. Результат преобразования
    выведите на экран.

    ### Sample Input
    dobavlyaem---slagi--slug-k--url---adresam

    ### Sample Output
    dobavlyaem-slagi-slug-k-url-adresam

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/3_topic/3_3/7.py)

    </details>
    <details>
    <summary>Подвиг 8.</summary>
    Вводятся три целых положительных числа (максимум трехзначные) через пробел в одну строчку. Для
    двухзначных и однозначных чисел нужно добавить слева незначащие нули так, чтобы все числа содержали
    по три цифры. Вывести на экран полученные числа в столбик.

    ### Sample Input
    8 11 123

    ### Sample Output
    008

    011

    123

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/3_topic/3_3/8.py)

    </details>
    <details>
    <summary>Подвиг 9.</summary>
    Вводится строка, состоящая из слов, разделенных пробелом. Необходимо подсчитать число слов в этой
    строке и результат (число) отобразить на экране.

    ### Sample Input
    I love Python

    ### Sample Output
    3

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/3_topic/3_3/9.py)

    </details>
    <details>
    <summary>Подвиг 10.</summary>
    Вводится строка, состоящая из названий городов, разделенных пробелом. Необходимо преобразовать эту
    строку, чтобы названия городов шли через точку с запятой. Результат отобразить на экране.

    ### Sample Input
    Москва Тверь Казань

    ### Sample Output
    Москва;Тверь;Казань

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/3_topic/3_3/10.py)

    </details>
* 3.4 Спецсимволы и экранирование символов
    <details>
    <summary>Подвиг 2.</summary>
    Необходимо задать строку со следующим содержимым: Тема занятия "спецсимволы". И отобразить ее на
    экране (кавычки у слова спецсимволы также должны быть отображены).

    ### Sample Input
     -

    ### Sample Output
    Тема занятия "спецсимволы"

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/3_topic/3_4/2.py)

    </details>
    <details>
    <summary>Подвиг 3.</summary>
    Вводится два слова в одну строку через пробел. Поставьте между этими словами символ обратного слеша
    (вместо пробела). Результирующую строку отобразите на экране.

    P. S. Задачу реализовать без применения F-строк.

    ### Sample Input
    Hello Balakirev!

    ### Sample Output
    Hello\Balakirev!

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/3_topic/3_4/3.py)

    </details>
    <details>
    <summary>Подвиг 4.</summary>
    Вводится строка со словами, разделенными пробелом. Необходимо первый пробел заменить на одинарную
    кавычку, а все остальные - на двойные. Результирующую строку отобразить на экране.

    ### Sample Input
    My best friend is Python!

    ### Sample Output
    My'best"friend"is"Python!

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/3_topic/3_4/4.py)

    </details>
    <details>
    <summary>Подвиг 5.</summary>
    Используя raw-строки, задайте строку, содержащую этот путь к файлу:
    C:\WINDOWS\System32\drivers\etc\hosts. Результат отобразите на экране.

    ### Sample Input
    -

    ### Sample Output
    C:\WINDOWS\System32\drivers\etc\hosts

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/3_topic/3_4/5.py)

    </details>
    <details>
    <summary>Подвиг 6.</summary>
    Вводится слово. Необходимо сформировать новую строку, где введенное слово будет заключено в двойные
    кавычки. Результат выведите на экран.

    ### Sample Input
    language

    ### Sample Output
    "language"

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/3_topic/3_4/6.py)

    </details>
* 3.5 Форматирование строк и F-строки
    <details>
    <summary>Подвиг 1.</summary>
    Вводятся: имя, фамилия и возраст (целое положительное число) каждое значение с новой строки.
    Используя метод строки format, через индексы переменных необходимо сформировать строку по шаблону:
    "Уважаемый <имя> <фамилия>! Поздравляем Вас с <возраст>-летием!"

    Результат вывести на экран (без кавычек).

    ### Sample Input
    Sergey

    Balakirev

    35

    ### Sample Output
    Уважаемый Sergey Balakirev! Поздравляем Вас с 35-летием!

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/3_topic/3_5/1.py)

    </details>
    <details>
    <summary>Подвиг 2.</summary>
    Вводятся: габариты изделия (целые числа): ширина, глубина, высота - в одну строчку через пробел. С
    помощью метода format, используя ключи в качестве имен переменных, сформировать строку: "Габариты:
    <ширина> x <глубина> x <высота>". Результат вывести на экран.

    ### Sample Input
    8 11 13

    ### Sample Output
    Габариты: 8 x 11 x 13

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/3_topic/3_5/2.py)

    </details>
    <details>
    <summary>Подвиг 3.</summary>
    Вводятся: два целых числа в одну строку через пробел. С помощью F-строки отобразить их по
    возрастанию в одну строку через пробел. Результат вывести на экран.
    P. S. Реализовать программу без использования условных операторов. Подумайте, как это можно
    сделать.

    ### Sample Input
    18 11

    ### Sample Output
    11 18

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/3_topic/3_5/3.py)

    </details>
    <details>
    <summary>Подвиг 4.</summary>
    Вводится адрес (каждое значение с новой строки) в формате: город, улица, номер дома (целое число),
    номер квартиры (целое число). Сформировать строку по шаблону: "г. <город>, ул. <улица>, д. <номер
    дома>, кв. <номер квартиры>", используя F-строку. Результат вывести на экран.

    ### Sample Input
    Москва

    Воздвиженка

    9

    1

    ### Sample Output
    г. Москва, ул. Воздвиженка, д. 9, кв. 1

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/3_topic/3_5/4.py)

    </details>
    <details>
    <summary>Подвиг 5.</summary>
    Вводятся (каждое с новой строки): курс доллара (вещественное значение) и число рублей (целое число)
    для обмена рублей на доллары. Вычислить целое количество получаемых долларов (с отбрасыванием
    дробной части) и сформировать строку, используя F-строку:

    "Вы можете получить <долларов>$ за <число рублей> рублей по курсу <курс доллара>".
    Вывести результат на экран (без кавычек).

    ### Sample Input
    73.54

    1000

    ### Sample Output
    Вы можете получить 13$ за 1000 рублей по курсу 73.54

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/3_topic/3_5/5.py)

    </details>
* 3.6 Списки и операции над ними
	<details>
    <summary>Подвиг 3.</summary>
    Вводятся три целых числа в одну строку через пробел. Сформируйте список lst, хранящий эти значения
    в порядке их ввода. Результат выведите на экран

    ### Sample Input
    8 11 3

    ### Sample Output
    [8, 11, 3]

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/3_topic/3_6/3.py)

    </details>
    <details>
    <summary>Подвиг 4.</summary>
    Вводятся названия городов в одну строчку через пробел. На основе этой строки формируется список с
    помощью команды: cities = input().split()
    Необходимо проверить, присутствует ли в этом списке город "Москва". Вывести на экран True, если
    присутствует и False - в противном случае. Решить эту задачу следует без использования условного
    оператора.

    ### Sample Input
    Тверь Уфа Москва Казань

    ### Sample Output
    True

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/3_topic/3_6/4.py)

    </details>
    <details>
    <summary>Подвиг 6.</summary>
    Вводятся названия городов в одну строчку через пробел. На основе этой строки формируется список с
    помощью команды: cities = input().split()
    Необходимо вывести значение последнего элемента этого списка на экран.

    ### Sample Input
    Москва Питер Уфа Казань Владимир

    ### Sample Output
    Владимир

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/3_topic/3_6/6.py)

    </details>
    <details>
    <summary>Подвиг 7.</summary>
    Вводятся оценки студента (целые числа от 2 до 5) в одну строчку через пробел. На основе введенной
    строки формируется список командой: marks = list(map(int, input().split()))
    Необходимо вычислить средний балл и вывести его на экран с точностью до десятых (один знак после
    запятой).

    ### Sample Input
    3 3 2 4 4 5 4 3 2

    ### Sample Output
    3.3

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/3_topic/3_6/7.py)

    </details>
    <details>
    <summary>Подвиг 8.</summary>
    Вводится информация по книге (каждое значение с новой строки): название, автор, число страниц
    (целое число), цена (вещественное число). На основе этих данных формируется список book с
    элементами в порядке их ввода. Затем, из этого списка необходимо удалить 3-й элемент (число
    страниц),в качестве автора записать "Пушкин" и цену увеличить в 2 раза. Результат вывести на экран.

    ### Sample Input
    Мастер и Маргарита

    Булгаков

    233

    435.45

    ### Sample Output
    ['Мастер и Маргарита', 'Пушкин', 870.9]

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/3_topic/3_6/8.py)

    </details>
    <details>
    <summary>Подвиг 9.</summary>
    Вводится число новых подписчиков канала по дням в одну строку через пробел. На основе введенной
    строки необходимо сформировать список из целых чисел. Затем, вывести на экран максимальное,
    минимальное и суммарное значения этого списка через пробел.

    ### Sample Input
    52 65 64 54 68 59 42 63

    ### Sample Output
    68 42 467

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/3_topic/3_6/9.py)

    </details>
    <details>
    <summary>Подвиг 10.</summary>
    Вводится число новых подписчиков канала по дням в одну строку через пробел. На основе введенной
    строки необходимо сформировать список lst из целых чисел. Требуется отсортировать элементы этого
    списка по убыванию и результат вывести на экран.

    ### Sample Input
    52 65 64 54 68 59 42 63

    ### Sample Output
    68 65 64 63 59 54 52 42

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/3_topic/3_6/10.py)

    </details>
    <details>
    <summary>Подвиг 12.</summary>
    Вводятся названия городов в одну строку через пробел. На основе этой строки необходимо создать
    список lst и добавить его в конец следующего списка: cities = ["Москва", "Тверь", "Вологда"]

    Вывести результат на экран

    ### Sample Input
    Уфа Казань Севастополь

    ### Sample Output
    Москва Тверь Вологда Уфа Казань Севастополь

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/3_topic/3_6/12.py)

    </details>
    <details>
    <summary>Подвиг 13.</summary>
    Вводятся названия городов в одну строку через пробел. На основе этой строки необходимо создать
    список lst и добавить его в начало другого списка: cities = ["Москва", "Тверь", "Вологда"]

    Вывести результат на экран

    ### Sample Input
    Уфа Казань Севастополь

    ### Sample Output
    Уфа Казань Севастополь Москва Тверь Вологда

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/3_topic/3_6/13.py)

    </details>
* 3.7 Срезы списков. Операторы сравнения списков
    <details>
    <summary>Подвиг 1.</summary>
    Имеется список числа просмотров видео по дням:
    v = [1205, 1101, 1434, 1320, 923, 874]

    Необходимо выбрать из него первые три значения (используя срезы) и вывести результат на экран.

    ### Sample Input
    -

    ### Sample Output
    [1205, 1101, 1434]

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/3_topic/3_7/1.py)

    </details>
    <details>
    <summary>Подвиг 2.</summary>
    Имеется список числа просмотров видео по дням:
    v = [1205, 1101, 1434, 1320, 923, 874]

    Необходимо выбрать из него последние четыре значения (используя срезы) и вывести результат на
    экран.

    ### Sample Input
    -

    ### Sample Output
    [1434, 1320, 923, 874]

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/3_topic/3_7/2.py)

    </details>
    <details>
    <summary>Подвиг 3.</summary>
    Имеется список городов:
    c = ["Москва", "Ульяновск", "Самара", "Тверь", "Вологда", "Омск", "Уфа"]

    Необходимо с помощью срезов выбрать из него города через один (начиная с первого) и результат
    вывести на экран.

    ### Sample Input
    -

    ### Sample Output
    ['Москва', 'Самара', 'Вологда', 'Уфа']

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/3_topic/3_7/3.py)

    </details>
    <details>
    <summary>Подвиг 4.</summary>
    Имеется список городов:
    c = ["Москва", "Ульяновск", "Самара", "Тверь", "Вологда", "Омск", "Уфа"]

    Необходимо с помощью срезов выбрать из него города через один (начиная со второго) и результат
    вывести на экран.

    ### Sample Input
    -

    ### Sample Output
    ['Ульяновск', 'Тверь', 'Омск']

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/3_topic/3_7/4.py)

    </details>
    <details>
    <summary>Подвиг 5.</summary>
    Имеется список с оценками студента:
    m = [2, 3, 5, 5, 2, 2, 3, 3, 4, 5, 4, 4]

    Необходимо с помощью срезов выбрать элементы с 3-го по 7-й (включительно) и вывести их на экран в
    обратном порядке.

    ### Sample Input
    -

    ### Sample Output
    [3, 2, 2, 5, 5]

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/3_topic/3_7/5.py)

    </details>
    <details>
    <summary>Подвиг 6.</summary>
    Имеется список с оценками студента:
    m = [2, 3, 5, 5, 2, 2, 3, 3, 4, 5, 4, 4]

    Необходимо с помощью срезов выбрать элементы через один, начиная с последнего, и вывести результат
    на экран.

    ### Sample Input
    -

    ### Sample Output
    [4, 5, 3, 2, 5, 3]

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/3_topic/3_7/6.py)

    </details>
* 3.8 Методы списков
    <details>
    <summary>Подвиг 2.</summary>
    Вводится строка из целых чисел через пробел. Если первое число не равно последнему, то нужно
    добавить значение True, а иначе - значение False. Результирующий список вывести на экран.

    Реализовать задачу без использования условных операторов.

    ### Sample Input
    8 12 2 -10 6

    ### Sample Output
    8 12 2 -10 6 True

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/3_topic/3_8/2.py)

    </details>
    <details>
    <summary>Подвиг 3.</summary>
    Имеется список городов:
    cities = ["Москва", "Казань", "Ярославль"]

    Необходимо вставить во вторую позицию этого списка строку "Ульяновск" и вывести список.

    ### Sample Input
    -

    ### Sample Output
    Москва Ульяновск Казань Ярославль

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/3_topic/3_8/3.py)

    </details>
    <details>
    <summary>Подвиг 4.</summary>
    Вводится строка с номером телефона в формате:
    +7(xxx)xxx-xx-xx

    Необходимо преобразовать ее в список lst (посимвольно, то есть, элементами списка будут являться
    отдельные символы строки). Затем, удалить первый '+', число 7 заменить на 8 и убрать дефисы.
    Отобразить полученный список на экран

    ### Sample Input
    +7(912)123-45-67

    ### Sample Output
    8(912)1234567

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/3_topic/3_8/4.py)

    </details>
    <details>
    <summary>Подвиг 5.</summary>
    В одну строчку через пробел вводятся: имя, отчество и фамилия. Необходимо представить эти данные в
    виде новой строки в формате: Фамилия И.О. (Например, Сергей Михайлович Балакирев -> Балакирев
    С.М.).

    ### Sample Input
    Сергей Михайлович Балакирев

    ### Sample Output
    Балакирев С.М.

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/3_topic/3_8/5.py)

    </details>
    <details>
    <summary>Подвиг 7.</summary>
    Вводятся целые числа в одну строчку через пробел (не менее четырех). Необходимо найти три
    наименьших числа в этой последовательности чисел и вывести их на экран в порядке возрастания.

    Реализовать программу без использования условного оператора.

    ### Sample Input
    8 11 -5 10 -1 0 7

    ### Sample Output
    -5 -1 0

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/3_topic/3_8/7.py)

    </details>
    <details>
    <summary>Подвиг 8.</summary>
    Вводятся целые числа в одну строчку через пробел. Необходимо преобразовать их в список lst , затем,
    удалить последнее значение и если оно нечетное, то в список (в конец) добавить True, иначе - False.

    Реализовать программу без использования условного оператора.

    ### Sample Input
    8 11 0 3 5 6

    ### Sample Output
    8 11 0 3 5 False

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/3_topic/3_8/8.py)

    </details>
    <details>
    <summary>Подвиг 9.</summary>
    Вводятся оценки студента (числа от 2 до 5) в одну строку через пробел. Необходимо определить
    количество двоек и вывести это значение на экран.

    ### Sample Input
    2 3 5 2 4 2 2 5

    ### Sample Output
    4

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/3_topic/3_8/9.py)

    </details>
    <details>
    <summary>Подвиг 10.</summary>
    Вводятся названия рек в одну строчку через пробел. Необходимо все их отсортировать по именам (по
    возрастанию) и в отсортированном списке удалить первый элемент. Результат отобразить на экране в
    одну строчку через пробел.

    ### Sample Input
    Лена Обь Волга Дон Енисей

    ### Sample Output
    Дон Енисей Лена Обь

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/3_topic/3_8/10.py)

    </details>
* 3.9 Вложенные списки
    <details>
    <summary>Подвиг 1.</summary>
    В список:
    a = [5.4, 6.7, 10.4]

    добавить в конец вложенный список со значениями, вводимыми в программу (целые числа вводятся в
    строчку через пробел). Результирующий список вывести на экран

    ### Sample Input
    8 11

    ### Sample Output
    [5.4, 6.7, 10.4, [8, 11]]

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/3_topic/3_9/1.py)

    </details>
    <details>
    <summary>Подвиг 2.</summary>
    Вводятся три строчки стихотворения (каждая с новой строки). Сохранить его в виде вложенного списка
    с разбивкой по строкам и словам (слова разделяются пробелом). Результирующий список вывести на
    экран.

    ### Sample Input
    Мороз и солнце день чудесный

    Еще ты дремлешь друг прелестный

    Пора красавица проснись

    ### Sample Output
    [['Мороз', 'и', 'солнце', 'день', 'чудесный'], ['Еще', 'ты', 'дремлешь', 'друг', 'прелестный'],
    ['Пора', 'красавица', 'проснись']]

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/3_topic/3_9/2.py)

    </details>
    <details>
    <summary>Подвиг 3.</summary>
    Вводится  матрица чисел из трех строк. В каждой строке числа разделяются пробелом. Необходимо
    вывести на экран последний столбец этой матрицы в виде строки из трех чисел через пробел.

    ### Sample Input
    8 11 12 1

    9 4 36 -4

    1 12 49 5

    ### Sample Output
    1 -4 5

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/3_topic/3_9/3.py)

    </details>
    <details>
    <summary>Подвиг 6.</summary>
    Имеется вложенный список из трех строк:

    t = [["Скажи-ка", "дядя", "ведь", "не", "даром"], ["Я", "Python", "выучил", "с", "каналом"],
    ["Балакирев", "что", "раздавал?"]]

    Необходимо реализовать проверку на наличие в этом списке введенного слова. Результат (True или
    False) вывести на экран. Решить задачу необходимо без применения условного оператора.

    ### Sample Input
    дядя

    ### Sample Output
    True

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/3_topic/3_9/6.py)

    </details>

## __4. Условные операторы__
* 4.1 Условный оператор if. Конструкция if-else
    <details>
    <summary>Подвиг 1.</summary>
    Вводятся два вещественных числа в одну строку через пробел. Вывести на экран наибольшее из чисел.
    Задачу решить с помощью условного оператора.

    ### Sample Input
    8.7 11.0

    ### Sample Output
    11.0

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/4_topic/4_1/1.py)

    </details>
    <details>
    <summary>Подвиг 2.</summary>
    Вводится слово. Необходимо определить, является ли это слово палиндромом (одинаково читается вперед
    и назад, например, АННА). Регистр букв не учитывать. Если введенное слово палиндром, на экран
    вывести ДА, иначе - НЕТ.

    ### Sample Input
    Шалаш

    ### Sample Output
    ДА

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/4_topic/4_1/2.py)

    </details>
    <details>
    <summary>Подвиг 3.</summary>
    Вводятся два целых положительных числа m и n в одну строку через пробел. Если число m делится
    нацело на число n, то вывести на экран частное от деления (результат деления) в виде целого числа.
    В противном случае вывести сообщение «m на n нацело не делится» (без кавычек) и вместо m и n
    подставить соответствующие числа, например: «13 на 2 нацело не делится».

    ### Sample Input 1
    8 4

    ### Sample Output 1
    2

    ### Sample Input 2
    11 2

    ### Sample Output 2
    11 на 2 нацело не делится

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/4_topic/4_1/3.py)

    </details>
    <details>
    <summary>Подвиг 4.</summary>
    Вводятся три целых положительных числа в одну строку через пробел. Убедиться, что первые два числа
    - это катеты прямоугольного треугольника, а третье - его гипотенуза. (Подсказка: проверка делается
    - по теореме Пифагора ). Если проверка проходит (истинна), то вывести на экран ДА, иначе - НЕТ.

    ### Sample Input
    3 4 5

    ### Sample Output
    ДА

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/4_topic/4_1/4.py)

    </details>
    <details>
    <summary>Подвиг 5.</summary>
    Вводится четырехзначное число. Проверить, что оно оканчивается на цифру 7. Вывести на экран ДА,
    если это так и НЕТ - в противном случае.

    ### Sample Input
    8117

    ### Sample Output
    ДА

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/4_topic/4_1/5.py)

    </details>
    <details>
    <summary>Подвиг 6.</summary>
    Вводится слово. Проверить, что в этом слове присутствуют все три буквы: t, h и o (в произвольном
    порядке). Реализовать программу с помощью одного условного оператора. Если проверка проходит,
    вывести ДА, иначе - НЕТ.

    ### Sample Input
    Python

    ### Sample Output
    ДА

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/4_topic/4_1/6.py)

    </details>
    <details>
    <summary>Подвиг 7.</summary>
    Вводится список городов в одну строку через пробел. Если в этом списке присутствует город Москва,
    то удалить его. Вывести на экран результирующий список в виде строки с городами через пробел.

    ### Sample Input
    Уфа Астрахань Москва Самара Казань

    ### Sample Output
    Уфа Астрахань Самара Казань

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/4_topic/4_1/7.py)

    </details>
    <details>
    <summary>Подвиг 8.</summary>
    Вводятся четыре целых числа a, b, c, d в одну строку через пробел. Определить, войдет ли в конверт
    с внутренними размерами a и b мм прямоугольная открытка с размерами с и d мм. Для размещения
    открытки в конверте необходим зазор в 1 мм с каждой стороны. Открытку можно поворачивать на 90
    градусов. Вывести ДА, если входит и НЕТ - если не входит.

    ### Sample Input
    12 5 7 2

    ### Sample Output
    ДА

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/4_topic/4_1/8.py)

    </details>
    <details>
    <summary>Подвиг 9.</summary>
    Вводится шестизначное число. Определить, является ли оно счастливым. (Счастливым называют такое
    шестизначное число, в котором сумма его первых трех цифр равна сумме его последних трех цифр.).
    Вывести ДА, если счастливое и НЕТ - в противном случае.

    ### Sample Input
    811235

    ### Sample Output
    ДА

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/4_topic/4_1/9.py)

    </details>
    <details>
    <summary>Подвиг 10.</summary>
    Работа светофора для пешеходов запрограммирована следующим образом: в начале каждого часа в течение
    трех минут горит зеленый сигнал, затем в течение двух минут – красный, в течение трех минут – опять
    зеленый и т. д. Дано вещественное число t, означающее время в минутах, прошедшее с начала
    очередного часа. Определить, сигнал какого цвета горит для пешеходов в этот момент. На экран
    вывести сообщение (без кавычек) "green" - для зеленого и "red" - для красного.

    ### Sample Input
    12.5

    ### Sample Output
    green

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/4_topic/4_1/10.py)

    </details>
* 4.2 Вложенные условия и множественный выбор
    <details>
    <summary>Подвиг 1.</summary>
    Имеется следующее меню:
    m = '''1. Введение в Python
    	2. Строки и списки
    	3. Условные операторы
    	4. Циклы
    	5. Словари, кортежи и множества
    	6. Выход'''
    В программе вводится целое число от 1 до 6. Нужно вывести пункт меню, связанный с этим числом.

    Реализовать программу с использованием операторов if-elif

    ### Sample Input
    2

    ### Sample Output
    2. Строки и списки

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/4_topic/4_2/1.py)

    </details>
    <details>
    <summary>Подвиг 2.</summary>
    Вводятся три целых числа в одну строку через пробел. Необходимо определить наименьшее среди них и
    вывести его на экран.

    Реализовать программу, используя условный оператор, без использования функции min.

    ### Sample Input
    8 11 -1

    ### Sample Output
    -1

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/4_topic/4_2/2.py)

    </details>
    <details>
    <summary>Подвиг 3.</summary>
    Вводится вес боксера-любителя (в кг, в виде вещественного числа). Известно, что вес таков, что
    боксер может быть отнесен к одной из весовых категорий:
    1) легкий вес – до 60 кг (включительно);
    2) первый полусредний вес – до 64 кг (включительно);
    3) полусредний вес – до 69 кг (включительно);
    4) остальные - более 69 кг.

    Вывести на экран номер категории, в которой будет выступать боксер.

    ### Sample Input
    62.4

    ### Sample Output
    2

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/4_topic/4_2/3.py)

    </details>
    <details>
    <summary>Подвиг 4.</summary>
    Вводится порядковый номер дня недели (1, 2, ..., 7). Вывести на экран его название (понедельник,
    вторник, среда, четверг, пятница, суббота, воскресенье).

    Программу реализовать с использованием операторов if-elif.

    ### Sample Input
    2

    ### Sample Output
    вторник

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/4_topic/4_2/4.py)

    </details>
    <details>
    <summary>Подвиг 5.</summary>
    Вводится порядковый номер месяца (1, 2, ..., 12). Вывести на экран количество дней в этом месяце.
    Принять, что год не является високосным. Реализовать через условный оператор, в котором следует
    использовать не более трех ветвей (блоков).
    P.S. Число дней в месяцах не високосного года, начиная с января:
    31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31

    ### Sample Input
    2

    ### Sample Output
    28

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/4_topic/4_2/5.py)

    </details>
    <details>
    <summary>Подвиг 6.</summary>
    Дата некоторого дня характеризуется двумя натуральными числами: m (порядковый номер месяца) и n
    (число). По введенным m и n (в одну строку через пробел) определить:
    а) дату предыдущего дня (принять, что m и n не характеризуют 1 января);
    б) дату следующего дня (принять, что m и n не характеризуют 31 декабря).

    В задаче принять, что год не является високосным. Вывести предыдущую дату и следующую дату (в
    формате: mm.dd, где m - число месяца; d - номер дня) в одну строчку через пробел.
    P.S. Число дней в месяцах не високосного года, начиная с января:
    31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31

    ### Sample Input
    8 31

    ### Sample Output
    08.30 09.01

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/4_topic/4_2/6.py)

    </details>
    <details>
    <summary>Подвиг 7.</summary>
     Вводится целое число k (1 <= k <= 365). Определить, каким днем недели (понедельник, вторник,
     среда, четверг, пятница, суббота или воскресенье) является k-й день не високосного года, в котором
     1 января является понедельником.

    ### Sample Input
    121

    ### Sample Output
    вторник

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/4_topic/4_2/7.py)

    </details>
* 4.3 Тернарный условный оператор
    <details>
    <summary>Подвиг 1.</summary>
    Вводится два вещественных числа, каждое с новой строки. Необходимо с помощью тернарного условного
    оператора наибольшее значение присвоить переменной d и вывести ее на экран.

    ### Sample Input
    5.4

    -3.8

    ### Sample Output
    5.4

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/4_topic/4_3/1.py)

    </details>
    <details>
    <summary>Подвиг 2.</summary>
    Вводится целое число. Необходимо переменной msg присвоить строку "кратно 3", если введенное число
    кратно 3, а иначе присвоить строку "не кратно 3". Реализовать программу с использованием тернарного
    оператора. Переменную msg отобразить на экране.

    ### Sample Input
    9

    ### Sample Output
    кратно 3

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/4_topic/4_3/2.py)

    </details>
    <details>
    <summary>Подвиг 3.</summary>
    Вводится слово. Переменной msg присвоить строку "палиндром", если введенное слово является
    палиндромом (одинаково читается и вперед и назад), а иначе присвоить строку "не палиндром".
    Проверку проводить без учета регистра. Программу реализовать с помощью тернарного условного
    оператора. Значение переменной msg отобразить на экране.

    ### Sample Input
    Казак

    ### Sample Output
    палиндром

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/4_topic/4_3/3.py)

    </details>
    <details>
    <summary>Подвиг 4.</summary>
    Вводится целое число 0 или 1. Необходимо преобразовать их в строки: 0 - в "False", 1 - в "True".
    Реализовать это с помощью тернарного условного оператора. Результат отобразить на экране.

    ### Sample Input
    1

    ### Sample Output
    True

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/4_topic/4_3/4.py)

    </details>
    <details>
    <summary>Подвиг 5.</summary>
    Вводится текущее время (секунды) в диапазоне [0; 59]. Если значение равно 59, то следующее должно
    быть 0. И так по кругу. Необходимо  вычислить следующее значение с проверкой граничного значения
    59. Реализуйте это с помощью тернарного условного оператора. Результат отобразите на экране.

    P.S. Попробуйте также реализовать эту же задачу с использованием только арифметических операций.

    ### Sample Input
    55

    ### Sample Output
    56

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/4_topic/4_3/5.py)

    </details>
    <details>
    <summary>Подвиг 6.</summary>
    Имеется список базовых нот:
    m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']

    Вводятся три целых числа в диапазоне от 1 до 7 - номера нот, в одну строчку через пробел.
    Необходимо отобразить указанные ноты в виде строки через пробел, но перед нотами до и фа
    дополнительно ставить символ диеза '#'. Реализовать эту программу с использованием тернарного
    условного оператора (он может использоваться несколько раз).

    ### Sample Input
    1 6 7

    ### Sample Output
    #до ля си

    [__Решение__](https://github.com/ShivaZoid/my_solutions/blob/main/stepik_by_Sergey_Balakirev/4_topic/4_3/6.py)

    </details>
## __5. Циклы, итераторы и генераторы списков__
* 5.1 Оператор цикла while
