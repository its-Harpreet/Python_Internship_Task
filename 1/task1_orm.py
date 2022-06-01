from datetime import datetime
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Column,String,Integer, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base= declarative_base()

class News(Base):
    __tablename__='news'

    id= Column(Integer,primary_key=True)
    headline= Column(String, nullable=False)
    content= Column(String, nullable=False)
    created_at= Column(DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.id}|{self.headline}|{self.content}"

if __name__=="__main__":
    engine= create_engine('sqlite:///task1__db.sqlite3')
    Base.metadata.create_all(engine)
