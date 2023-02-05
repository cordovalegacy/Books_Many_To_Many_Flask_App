from flask_app.config.mysqlconnection import connectToMySQL


class Book:
    
    def __init__(self, book_data):
        self.id = book_data['id']
        self.title = book_data['title']
        self.num_of_pages = book_data['num_of_pages']
        self.created_at = book_data['created_at']
        self.updated_at = book_data['updated_at']