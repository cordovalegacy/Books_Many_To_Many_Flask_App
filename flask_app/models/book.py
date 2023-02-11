from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user


class Book:
    
    def __init__(self, book_data):
        self.id = book_data['id']
        self.title = book_data['title']
        self.num_of_pages = book_data['num_of_pages']
        self.created_at = book_data['created_at']
        self.updated_at = book_data['updated_at']

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