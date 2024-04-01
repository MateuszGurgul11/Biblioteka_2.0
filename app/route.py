from flask import render_template, redirect, request, url_for
from app import app, db
from app.models import Author, Book, Borrowing

@app.route("/")
def homepage():
    books = Book.query.all()
    return render_template("index.html", title = "Biblioteka", books=books)

@app.route("/add_book", methods=['POST', 'GET'])
def add_book():
    if request.method == 'POST':
        name = request.form['name']
        page_number = request.form['page_number']
        author_name = request.form['author']
        lastname = request.form['lastname']
        age = request.form['age']

        author = Author.query.filter_by(name=author_name, lastname=lastname, age=age).first()
        if not author:
            author = Author(name=author_name, lastname=lastname, age=age)
            db.session.add(author)
        
        new_book = Book(name = name, page_number = page_number, authors = [author])
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for("homepage"))
    return render_template("add_book.html")

@app.route("/delete_book/<int:book_id>", methods=['POST', 'GET'])
def delete_book(book_id):
    if request.method == 'POST':
        book = Book.query.get_or_404(book_id)
        authors = list(book.authors)
        db.session.delete(book)
        db.session.commit()

        for author in authors:
            if not author.books:
                db.session.delete(author)
        
        db.session.commit()

        return redirect(url_for('homepage'))

@app.route("/toggle_book/<int:book_id>", methods=['POST', 'GET'])
def toggle_book(book_id):
    if request.method == 'POST':
        book = Book.query.get_or_404(book_id)
        book.is_borrowed = not book.is_borrowed
        db.session.commit()
        return redirect(url_for("homepage"))


