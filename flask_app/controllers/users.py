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
        'id': id
    }
    return render_template('single_user_page.html', single_user = User.display_single_user(single_user_data), favorite_books = Book.favorite_books(single_user_data))

@app.route('/joining_table', methods = ['POST'])
def joining_table():
    users_and_books = {
        'book_id': request.form['book_id'],
        'user_id': request.form['user_id']
    }
    User.join_users_and_books(users_and_books)
    return redirect(f"/display_user/{request.form['user_id']}")
