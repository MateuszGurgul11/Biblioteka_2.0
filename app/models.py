from app import db

authors_books = db.Table('authors_books',
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primary_key=True),
    db.Column('author_id', db.Integer, db.ForeignKey('author.id'), primary_key=True)
)

class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200), index = True, nullable = False)
    page_number = db.Column(db.Integer, nullable = False)
    is_borrowed = db.Column(db.Boolean, default = False)
    authors = db.relationship('Author', secondary = authors_books, back_populates = 'books')

    def __repr__(self):
        return f"<Book {self.name}>"
    
class Author(db.Model):
    __tablename__ = 'author'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(150), index = True, nullable = False)
    lastname = db.Column(db.String(150), index = True, nullable = False)
    age = db.Column(db.Integer)
    books = db.relationship('Book', secondary = authors_books, back_populates = 'authors')

    def __repr__(self): 
        return f"<Author: {self.name} {self.lastname}>"
    

class Borrowing(db.Model):
    __tablename__ = 'borrowing'
    id = db.Column(db.Integer, primary_key = True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable = False)
    borrower_name = db.Column(db.String(200), nullable = False)
    borrowed_date = db.Column(db.DateTime, nullable = False)
    return_date = db.Column(db.DateTime)

    book = db.relationship('Book', backref = db.backref('borrowings', lazy = True))

    def __repr__(self):
        return f"<Borrowing {self.book.name} by {self.borrower_name}>"

    