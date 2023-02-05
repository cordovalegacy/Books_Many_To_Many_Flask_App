from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.book import Book

class User:

    def __init__(self, user_data):
        self.id = user_data['id']
        self.first_name = user_data['first_name']
        self.last_name = user_data['last_name']
        self.created_at = user_data['created_at']
        self.updated_at = user_data['updated_at']

    @classmethod
    def save(cls, author_data):
        query = """
                INSERT INTO users (first_name, last_name) 
                VALUES (%(first_name)s, %(last_name)s)
                ;"""
        return connectToMySQL('books').query_db(query, author_data)

    @classmethod
    def display_all_users(cls):
        query = """
                SELECT * FROM users
                ;"""
        results = connectToMySQL('books').query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def display_single_user(cls, single_user_data):
        query = """
                SELECT * FROM users 
                WHERE id = %(id)s
                ;"""
        results = connectToMySQL('books').query_db(query, single_user_data)
        return cls(results[0])

    @classmethod
    def join_users_and_books(cls, users_and_books_data):
        query = """
                INSERT INTO users_books (user_id, book_id)
                VALUES (%(user_id)s, %(book_id)s)
                ;"""
        return connectToMySQL('books').query_db(query, users_and_books_data)
