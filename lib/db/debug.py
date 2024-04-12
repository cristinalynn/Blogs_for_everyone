from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from models import Author, Blog, Reader

# Creates the engine
engine = create_engine('sqlite:///info.db')

# Creates a session
Session = sessionmaker(bind=engine)
session = Session()
breakpoint()
# if name == 'main':
    # engine = create_engine("sqlite:///info.db")
    # session = Session(engine, future=True)
