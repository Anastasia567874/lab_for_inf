from data import db_session
from data.db_session import create_session, global_init
from data.books import Book
from data.genres import Genre
from data.users import User
import os

db_session.global_init("db/book_store.db")


def create_book(form):
    db_sess = db_session.create_session()
    #db_sess.query(Genre).filter(Genre.title == new_genre).first().id
    genre_exists = db_sess.query(Genre).filter(Genre.title == form['genre']).scalar()
    if genre_exists:
        genre = db_sess.query(Genre).filter(Genre.title == form['genre']).first().id
    else:
        genre_new = Genre(title=form['genre'])
        db_sess.add(genre_new)
        db_sess.commit()
        genre = genre_new.id
    book = Book(
        title=form['title'],
        author=form['author'],
        age_limit=form['age_limit'],
        annotation=form['annotation'],
        genre_id=genre

    )
    db_sess.add(book)
    db_sess.commit()
    return "Успешно создана книга"


def del_book(book_id):
    db_sess = db_session.create_session()
    book = db_sess.query(Book).get(book_id)
    db_sess.delete(book)
    db_sess.commit()
    return "Успешно удалена книга"


def get_books():
    db_sess = db_session.create_session()
    books = db_sess.query(Book).all()
    for book in books:
        print('---------')
        print(f'id - {book.id}')
        print(f'{book.author} - {book.title}. Ограничение по возрасту: {book.age_limit}+.')
        print(book.annotation)
        genre = db_sess.query(Genre).get(book.genre_id)
        print(f'Книга написана в жанре "{genre.title}"')
    return books


def creat_user(form):
    db_sess = db_session.create_session()
    user = User(
        nickname=form['name'],
        books=form['books']
    )
    db_sess.add(user)
    db_sess.commit()
    return "Успешно создан пользователь"


def get_users():
    db_sess = db_session.create_session()
    users = db_sess.query(User).all()
    for user in users:
        print('---------')
        print(f'Имя пользователя: {user.nickname}, id - {user.id}')
        print('Сохраненная литература:')
        for i in user.books.split():
            book = db_sess.query(Book).get(int(i))
            print(book.title)


def del_user(user_id):
    db_sess = db_session.create_session()
    user = db_sess.query(User).get(user_id)
    db_sess.delete(user)
    db_sess.commit()
    return "Успешно удален пользователь"


def add_user_book(user_id, book_id):
    db_sess = db_session.create_session()
    user = db_sess.query(User).get(user_id)
    db_sess.delete(user)
    user.books += ' ' + str(book_id)
    print(user.books)
    db_sess.add(user)
    db_sess.commit()
    return "Успешно добавлена книга в список пользователя"


def creat_genre(form):
    db_sess = db_session.create_session()
    genre = Genre(
        title=form['title']
    )
    db_sess.add(genre)
    db_sess.commit()
    return "Успешно создан жанр"


def get_genres():
    db_sess = db_session.create_session()
    genres = db_sess.query(Genre).all()
    for genre in genres:
        print('---------')
        print(f'Жанр: {genre.title}, id - {genre.id}')


def del_genre(genre_id):
    db_sess = db_session.create_session()
    genre = db_sess.query(Genre).get(genre_id)
    db_sess.delete(genre)
    db_sess.commit()
    return "Успешно удален жанр"


get_users()
form={'name': 'Sat', 'books': ''}
print(creat_user(form))
get_users()
form1 = {'title':'KGBT+',
         'author':'Пелевин',
         'age_limit': 18,
            'annotation': """Книга представляет собой нечто среднее между мемуарами,
             тренингом по достижению успеха и сборником мемов. 
             Все это щедро приправлено фирменной авторской психоделикой, 
             без которой не обходится ни одно произведение Пелевина.""",
'genre': 'Роман'
         }
print(create_book(form1))
print(add_user_book(1, 1))
get_users()
form3={'title':'Поэзия'}
print(creat_genre(form3))
get_genres()
print(del_genre(2))
get_genres()
