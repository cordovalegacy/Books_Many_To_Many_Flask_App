from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user


class Book:
    
    def __init__(self, book_data):
        self.id = book_data['id']
        self.title = book_data['title']
        self.num_of_pages = book_data['num_of_pages']
        self.created_at = book_data['created_at']
        self.updated_at = book_data['updated_at']

    # @classmethod
    # def favorite_books(cls, favorites_data):
    #     query = """
    #             SELECT * FROM books 
    #             WHERE books.id 
    #             IN
    #             (SELECT book_id FROM favorites WHERE user_id = %(id)s)
    #             ;"""
    #     results = connectToMySQL('books').query_db(query, favorites_data)
    #     books = []
    #     for row in results:
    #         books.append(cls(row))
    #         print(books)
    #         return books