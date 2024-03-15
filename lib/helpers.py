from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from db.models import (Author, Reader, Blog)
from sqlalchemy import func

engine = create_engine("sqlite:///db/info.db")
session = Session(engine, future=True)
class Library:

    # Create
    def create_author(self, name):
        author = Author(name=name)
        session.add(author)
        session.commit()

    def create_book(self, title, author_id):
        blog = Blog(title=title, author_id=author_id)
        session.add(blog)
        session.commit()

    def create_reader(self, name):
        reader = Reader(name=name)
        session.add(reader)
        session.commit()

    # Delete 
    def delete_author(self, author_id):
        author = session.query(Author).get(author_id)
        if author:
            session.delete(author)
            session.commit()

    def delete_blog(self, blog_id):
        blog = session.query(Blog).get(blog_id)
        if blog:
            session.delete(blog)
            session.commit()

    def delete_reader(self, reader_id):
        reader = session.query(Reader).get(reader_id)
        if reader:
            session.delete(reader)
            session.commit()

    # Get All
    def get_all_authors(self):
        return session.query(Author).all()

    def get_all_blogs(self):
        return session.query(Blog).all()

    def get_all_readers(self):
        return session.query(Reader).all()
    
    # Find By...
    def find_author_by_name(self, name):
        return session.query(Author).filter_by(name=name).first()

    def find_blog_by_title(self, title):
        return session.query(Blog).filter_by(title=title).first()
    
    def find_blog_by_id(self, blog_id):
        blog = session.query(Blog).filter_by(id=blog_id).first()
        return blog

    def find_reader_by_name(self, name):
        return session.query(Reader).filter_by(name=name).first()
