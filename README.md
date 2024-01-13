
## Лабораторная работа "Обучение основам работы с базами данных"

# Введение в базы данных. Теоритеческая часть.

![image](https://github.com/Anastasia567874/lab_bd/assets/144477949/aec7a169-3b9c-465c-b58c-12fb77190512)

База данных — это упорядоченный набор структурированной информации или данных, которые обычно хранятся в электронном виде в компьютерной системе. 
База данных обычно управляется системой управления базами данных (СУБД). 
Данные вместе с СУБД, а также приложения, которые с ними связаны, называются системой баз данных, или, для краткости, просто базой данных.

Базы данных используются для решения множества задач. Например, они могут использоваться для хранения информации о клиентах и заказах в компании, для анализа больших объемов данных, для поддержки электронной коммерции, а также для управления информацией о научных исследованиях.

Существует несколько типов БД, включая реляционные, иерархические, сетевые и объектно-ориентированные. Реляционные БД являются наиболее распространенным типом и основываются на принципе таблиц, состоящих из строк и столбцов. 
Каждая таблица представляет отдельную сущность, а столбцы представляют атрибуты этой сущности. Связи между таблицами устанавливаются с помощью ключей, которые позволяют объединять данные из разных таблиц.

Центральным понятием в БД является язык структурированных запросов (SQL), который позволяет выполнять различные операции с данными, такие как выборка, вставка, обновление и удаление. SQL является стандартным языком взаимодействия с реляционными БД. 

# Sqlitestudio и sql-запросы

Теперь рассмотрим пример базы данных с несколькими таблицами. Для этого скачайте приложение Sqlitestudio, а также файл bookstore.db из данного репозитория. 
1. Откройте приложение и добавьте туда скачанную базу данных. 
![image](https://github.com/Anastasia567874/lab_bd/assets/144477949/593c32d7-a46c-4769-b5e7-0f9852b609b7)

2. Нажав на иконку БД, можно увидеть 3 таблицы - books, genres, users. Открыв каждую из них можно будет увидеть их содержимое в разделе Data:
   ![image](https://github.com/Anastasia567874/lab_bd/assets/144477949/265b872f-7979-4fa5-a77f-b2b1cba2f7ff)
   
4. Теперь попробуем сделать пару sql-запросов с целью найти нужные данные в таблицах. Для начала откройте поле для запросов.
   ![image](https://github.com/Anastasia567874/lab_bd/assets/144477949/1775aa04-67fd-4e29-8ce6-1b126a51c1df)

Общая структура запроса выглядит так: 
```
SELECT (столбцы или * для всех сразу) FROM (номер таблицы)
```
Также запрос может содержать необязательные параметры:
- WHERE (условие)
- GROUP BY (столбец, по которому группируем)
- HAVING (условие на уровне сгруппированных данных)
- ORDER BY (столбец, по которому сортируем вывод)

Примеры:
SELECT * FROM books - выводит все данные из таблицы books

![image](https://github.com/Anastasia567874/lab_bd/assets/144477949/0e9dd0bd-344c-49be-9ddc-f0bea284a6d4)


SELECT title, author FROM books WHERE age_limit < 18 - выводит название и автора книг, где возрастной лимит меньше 18

![image](https://github.com/Anastasia567874/lab_bd/assets/144477949/25492aa1-23dc-4774-8cd7-ea4db69a3c8e)

JOIN — необязательный элемент, используется для объединения таблиц по ключу, который присутствует в обеих таблицах. Перед ключом ставится оператор ON.
```
SELECT books.title, genres.title 
FROM books
JOIN genres ON books.id = genres.id;
```

![image](https://github.com/Anastasia567874/lab_for_inf/assets/144477949/dc4bac75-b130-481b-a032-2d79f079b883)


Теперь попробуй самостоятельно вывести, это твоё первое задание:
1) Все книги с жанром "Роман".
2) Название и автора книг, где имя автора начинается с буквы "А" и возрастное ограничение меньше 18, отсортировав по названию.


# Создание собственной БД

   Итак, мы уже имеем небольшое представление о том, как и для чего используются базы данных. Мы даже умееем делать некоторые простые sql-запросы с целью получения каких-либо данных. В этой же части мы научимся создавать простую базу данных с помощью Python. Для этого мы будет использовать orm-библиотеку SQLAlchemy. Её надо скачать.

1. Сначала нам надо создать форму для создания и подключения к базе данных. 
![image](https://github.com/Anastasia567874/lab_bd/assets/144477949/ab85e0c1-c9c7-4e8c-bf39-c1943e4804f0)


Разберем основные моменты:

Создадим функцию global_init, которая будет инициализировать нашу БД. Дальше работаем в ней. Для начала нужно создать движок, который создается один раз и хранит в себе все подключения к серверу БД:
```
engine = sa.create_engine(conn_str, echo=True)
```
В качестве параметра мы передаем строку подключения, для разных систем БД строка выглядит по разному. 

Для взаимодействия необходимо создать сессию базы данных. Для этого используем метод-фабрику sessionmaker (параметр bind привязывает сессию к движку нашей БД).
```
__factory = orm.sessionmaker(bind=engine)
```

После можем импортировать все наши модели и по метаданным моделей создадутся все наши таблицы и БД:
```
from . import __all_models
SqlAlchemyBase.metadata.create_all(engine)
```

Также необходимо создать базовую модель, от которой впоследствии мы будем наследоваться при создании других.
```
SqlAlchemyBase = dec.declarative_base()
```

2. Создание формы
   
Создание каждом из форм необходимо делать в отдельном файле!
   
   Допустим, мы хотим сделать таблицу, которая будет содержать книжки. Она должна включать в себя: id книги, название, автора, возрастное ограничение, аннотацию и id жанра (для жанра потом будет другая табличка).
   
   ![image](https://github.com/Anastasia567874/lab_bd/assets/144477949/d2c32067-b41d-4f74-97bc-00526fb0cc36)

   Для начала нам необходимо импортировать все необходимое - Типы данных для таблицы, столбцы, базовый класс, от которого мы наследуемся при создании таблицы и так далее.
   
Теперь рассмотрим сам процесс создания таблицы. Мы объявляем класс Book, в качестве аргументов выступает SqlAlchemyBase - базовый класс для создания моделей, а также SerializerMixin - сериализатор, предоставляющий удобные методы для преобразования объектов моделей в форматы, такие как JSON или XML, а затем обратно в объекты моделей. )

Сразу после необходимо дать имя нашей таблице, для этого пишем:
   ```
__ tablename __ = 'books'
   ```
В каждой из последующих строк мы описываем создание каждой колонки. В качестве параметров могут идти name (если не указано, используется имя атрибута), type - тип данных в столбце, autoincrement - задает автоинкремент значения столбца, index - если равен True, то для столбца будет создаваться индекс, nullable - если равен False, то к определению столбца в бд будет добавляться ограничение NOT NULL, primary_key - если равен True, то столбец будет считаться первичным ключом, unique - поддерживаются только уникальные значения столбца.

Теперь похожим образом создадим ещё одну таблицу с жанрами.

![image](https://github.com/Anastasia567874/lab_bd/assets/144477949/ce73d4a9-946f-4a5f-a89b-1e0cd21b35ec)

Мы хотим связать нашу таблицу с книгами с таблицей с жанрами через id жанра. Для установки отношений между моделями применяется функция relationship(). Она принимает множество параметров, из которых самый первый параметр указывает на связанную модель. А параметр back_populates представляет атрибут связанной модели, с которой будет сопоставляться текущая модель. Также в подчиненной модели определяем атрибут-столбец с внешним ключом:
```
genre_id = Column(Integer, ForeignKey("genres.id"))
```
Теперь наши таблицы связаны через внешний ключ. 

3. Основные функции для работы с БД.
   Рассмотрим функцию добавления новой книги.
![image](https://github.com/Anastasia567874/lab_bd/assets/144477949/dd1e03ec-c303-4e3e-af78-09f83a69619c)

Взаимодействие с БД происходит через созданную ранее функцию создания сессии - create_session(), для удобства:
```
db_sess = db_session.create_session()
```
Для добавления в базу данных используется метод add(), в него мы передаем объект модели. Для подтверждения изменений у объекта  вызывается метод commit(). Для получения объектов из базы данных необходимо вызывать метод query(), в него также передаем объект модели. 

Внутри метода query() мы создаем условие с использованием exists() и оператора where(). exists() создает подзапрос, который проверяет наличие записи в таблице genres. Genre.title == form['genre'] сравнивает столбец title в таблице genres с указанными данными в форме. scalar() возращает нам булевое значение - True, если запись есть, и False в обратном случае.

Далее идет проверка, если переданный в форме жанр уже существует, то используя filter() для фильтрации и функцию firts(), которая возращает первое вхождение, мы получаем id жанра. Если жанра не существует, то создаем новый, передавая новое название. Также не забываем добавить саму книгу.

Помимо добавления новых книг должна быть возможность их получения и удаления. Создадим и их.
![image](https://github.com/Anastasia567874/lab_bd/assets/144477949/e83a97b8-53d6-4ccf-a8bf-d6d652cd169f)

Удаление книги:
Создаем сессию. С помощью метода get(), который возращает экземпляр, основанный на заданном идентификаторе первичного ключа и метода delete() удаляем книгу. 

Получение всех книг:
Создаем сессию. С помощью метода all(), который возращает результаты query() в виде списка, поочереди выводим информацию о каждой из книг.

   Итак, мы описали основные функции для взаимодействия с нашей базой данных. Теперь пришло время и тебе поработать. Твоя задача создать форму для пользователей, а также недостоющие функции получения, создания и удаления данных из таблиц с жанрами и пользователями. Желаем успехов!




