from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.book import Book
from flask_app.models import user

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
    return render_template('single_book_page.html', single_book_data = Book.display_single_book(data), non_favorite_users = user.User.non_favorite_users(data))

@app.route('/add_users_favorites', methods=['POST'])
def add_users_favorites():
    user_favorite = {
        'book_id': request.form['book_id'],
        'user_id': request.form['user_id']
    }
    Book.save_user_to_book(user_favorite)
    return redirect(f"/single_book_page/{request.form['book_id']}")