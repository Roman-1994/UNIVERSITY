# __Тестовое задание Metasharks__
***
## Задание: Реализовать веб-сервис для организации учебного процесса в ВУЗе
~~~
Основные сущности:
    1. Куратор
    2. Направление подготовки
    3. Учебная дисциплина
    4. Учебная группа
    5. Студент
    
    Администратором сервиса формируются направления подготовки, имеющие
    свой перечень учебных дисциплин. За каждым направлением закреплен куратор.
    Куратор зачисляет студентов и формирует учебные группы на основании
    направлений. Каждая группа может состоять максимум из 20 студентов.
    
    Функционал администратора:
        1. Управление направлениями подготовки
        2. Управление учебными дисциплинами
        3. Формирование отчета в виде эксель файла
    
    Функционал куратора:
        1. Управление студентами
        2. Управление учебными группами
~~~
***
## Выполнение задания
~~~
Для реализации поставленной задачи была использована СУБД PostgreSQL,
созданы требуемы сущности. Созданы пользовательские ограничения доступа. 
Для асинхронных задач (форирования отчета) были использованы Celery,
брокер Redis и библиотека openpyxl. Авторизация пользователей реализована 
при помощи библиотеки Djoser. Дополнительно был установлен swagger и flower.
~~~
### Шаги для запуска проекта:
~~~
1. sudo docker-compose build
2. sudo docker-compose up
~~~
