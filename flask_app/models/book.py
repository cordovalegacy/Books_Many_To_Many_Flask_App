from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user


class Book:
    
    def __init__(self, book_data):
        self.id = book_data['id']
        self.title = book_data['title']
        self.num_of_pages = book_data['num_of_pages']
        self.created_at = book_data['created_at']
        self.updated_at = book_data['updated_at']
        self.authors = []

    @classmethod
    def save_books(cls, data):
        query = """
                INSERT INTO books (title, num_of_pages)
                VALUES (%(title)s, %(num_of_pages)s)
                ;"""
        return connectToMySQL('books').query_db(query, data)

    @classmethod
    def non_favorite_books(cls, non_favorites_data):
        query = """
                SELECT * FROM books 
                WHERE books.id 
                NOT IN
                (SELECT book_id FROM users_books WHERE user_id = %(user_id)s)
                ;"""
        results = connectToMySQL('books').query_db(query, non_favorites_data)
        # print(results)
        books = []
        for row in results:
            print(row)
            books.append(cls(row))
        return books

    @classmethod
    def display_single_book(cls, data):
        query = """
                SELECT * FROM books
                LEFT JOIN users_books ON books.id = users_books.book_id
                LEFT JOIN users ON users.id = users_books.user_id
                WHERE books.id = %(id)s
                ;"""
        results = connectToMySQL('books').query_db(query, data)
        result = cls(results[0])
        for row in results:
            if row['users.id'] == None:
                break
            data = {
                'id': row['users.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'created_at': row['created_at'],
                'updated_at':row['updated_at']
            }
            result.authors.append(user.User(data))
        print(result)
        return result
            
    @classmethod
    def display_all_books(cls):
        query = """
                SELECT * FROM books
                ;"""
        return connectToMySQL('books').query_db(query)

    @classmethod
    def save_user_to_book(cls, book_users_can_favorite):
        query = """
                INSERT INTO users_books (user_id, book_id)
                VALUES (%(user_id)s, %(book_id)s)
                ;"""
        return connectToMySQL('books').query_db(query, book_users_can_favorite)