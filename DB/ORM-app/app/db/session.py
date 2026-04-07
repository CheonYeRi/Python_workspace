from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+mysqlconnector://user:1234@Localhost/codingon"

engine = create_engine(DATABASE_URL,)
SessionLocal = sessionmaker(autocommit= False, autoflush=False, bind=engine)
#DB랑 연결이 되는 함수

Base = declarative_base()