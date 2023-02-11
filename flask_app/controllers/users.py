from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.user import User
from flask_app.models.book import Book

@app.route('/')
def index():
    users = User.display_all_users()
    return render_template('home_page.html', all_users = users)

@app.route('/create')
def create_page():
    return render_template('create_page.html')

@app.route('/create/user', methods=['POST'])
def create_user():
    author_data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name']
    }
    User.save(author_data)
    return redirect('/')

@app.route('/display_user/<int:id>')
def display_user(id):
    single_user_data = {
        'user_id': id
    }
    return render_template('single_user_page.html', single_user = User.display_single_user(single_user_data), non_favorite_books = Book.non_favorite_books(single_user_data), user_instance = User.join_users_and_books(single_user_data))

@app.route('/add_books_to_favorites', methods=['POST'])
def add_books_to_favorites():
    favorite_book = {
        'book_id': request.form['book_id'],
        'user_id': request.form['user_id']
    }
    User.save_book_to_user(favorite_book)
    return redirect(f"/display_user/{request.form['user_id']}")

@app.route('/unfavorite/<int:id>')
def unfavorite(id):
    data = {
        'id': id
    }
    User.unfavorite(data)
    return redirect('/display_user/{id}')
