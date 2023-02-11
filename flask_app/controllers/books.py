from flask_app import app
from flask import render_template, redirect, request

@app.route('/create_book')
def create_book():
    return render_template('create_book_page.html')