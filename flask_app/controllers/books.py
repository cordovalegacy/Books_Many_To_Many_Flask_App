from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.book import Book

@app.route('/create_book_page')
def create_book_page():
    return render_template('create_book_page.html')

@app.route('/create/book', methods=['POST'])
def create_book():
    new_book_data = {
        'title': request.form['title'],
        'num_of_pages': request.form['num_of_pages']
    }
    Book.save_books(new_book_data)
    return redirect('/')

@app.route('/single_book_page/<int:id>')
def single_book_page(id):
    data = {
        'id': id
    }
    return render_template('single_book_page.html', single_book_data = Book.display_single_book(data))