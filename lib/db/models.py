from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

engine = create_engine('sqlite:///info.db')
Base = declarative_base()

class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    blogs = relationship('Blog', back_populates='author')

    def __repr__(self):
        return f'<Author(id={self.id}, name={self.name})>'
class Blog(Base):
    __tablename__= 'blogs'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'))
    author = relationship('Author', back_populates='blogs')

    def __repr__(self):
        return f'<Blog(id={self.id}, title={self.title}, authir_id={self.author_id})>'
    
class Reader(Base):
    __tablename__ = 'readers'

    id = Column(Integer, primary_key= True)
    name = Column(String, nullable=False)

    def __repr__(self):
        return f'<Reader(id={self.id}, name={self.name})>'
    
Base.metadata.create_all(engine)

