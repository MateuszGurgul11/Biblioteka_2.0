from flask import render_template, redirect, request, url_for
from app import app, db
from app.models import Author, Book, Borrowing

@app.route("/")
@app.route("/index")
def homepage():
    books = Book.query.all()
    return render_template("index.html", title = "Biblioteka", books=books)

@app.route("/add_book", methods=['POST', 'GET'])
def add_book():
    if request.method == 'POST':
        name = request.form['name']
        page_number = request.form['page_number']
        author_name = request.form['author']

        author = Author.query.filter_by(name = author_name).first()
        if not author:
            author = Author(name = author_name)
            db.session.add(author)
            db.session.commit()
        
        new_book = Book(name = name, page_number = page_number, authors = [author])
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for("homepage"))
    return render_template("add_book.html")

