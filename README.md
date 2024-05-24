# АСИНХРОННЫЙ ПАРСЕР PEP

Проект позволяет парсить данные о документах PEP. Данные берутся с адреса
https://peps.python.org/
Проект собирает данные обо всех документах PEP,считает количество PEP в каждом статусе и общее количество PEP, сохраняет результат в два csv-файла: в первый файл - список всех PEP, во второй - сводку по статусам PEP

Для запуска проекта из корня выполнить команду:
```sh
scrapy crawl pep
```
Результат сохранится в папку results/ в корневой директории
- Пример файла с общей информацией pep_2024-05-24T07-27-52.csv:
>number,name,status
>1,PEP Purpose and Guidelines,Active
>201,Lockstep Iteration,Final
>204,Range Literals,Rejected
>206,Python Advanced Library,Withdrawn
>203,Augmented Assignments,Final
>205,Weak References,Final
>207,Rich Comparisons,Final
>202,List Comprehensions,Final
>208,Reworking the Coercion Model,Final
>333,Python Web Server Gateway Interface v1.0,Final
>200,Python 2.0 Release Schedule,Final
>160,Python 1.6 Release Schedule,Final
>102,Doing Python Micro Releases,Superseded
- Пример файла с подсчетом статусов status_summary_2024-05-24_10-28-06.csv:
 >Статус	Количество
 >Active	35
 >Accepted	28
 >Deferred	36
 >Final	305
 >Provisional	1
>Rejected	123
>Superseded	23
>Withdrawn	61
>Draft	28
>Total	640

Проект написан на Python с использованием фреймворка Scrapy
Автор: Корсаков Сергей [mortodello](https://github.com/mortodello/scrapy_parser_pep)