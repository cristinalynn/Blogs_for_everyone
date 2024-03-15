from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from models import Author, Blog, Reader

#Creates the engine
engine = create_engine('sqlite:///info.db')

#Creates a session
Session = sessionmaker(bind=engine)
session = Session()

#Faker
faker = Faker()

#Create instances of classes here...
def seed_data():

    # Authors
    for _ in range(5):
        author = Author(name=faker.name())
        session.add(author)
    session.commit()
    print("Number of authors inserted:", session.query(Author).count())

    # Blogs
    authors = session.query(Author).all()
    for _ in range(10):
        blog = Blog(title=faker.catch_phrase(), author=faker.random_element(authors))
        session.add(blog)
    session.commit()
    print("Number of blogs inserted:", session.query(Blog).count())

    # Readers
    for _ in range(10):
        reader = Reader(name=faker.name())
        session.add(reader)
    session.commit()
    print("Number of readers inserted:", session.query(Reader).count())

if __name__ == "__main__":
    seed_data()
    session.close()