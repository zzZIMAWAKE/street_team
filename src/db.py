import sqlalchemy
from sqlalchemy.orm import sessionmaker

engine = sqlalchemy.create_engine("postgres://admin:hunter2@localhost:5432/backend")
Session = sessionmaker(bind=engine)
