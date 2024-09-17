from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy.orm import relationship


engine = create_engine('sqlite:///ecommerce.db', echo=True)
SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass

#
# class User(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True)
#     username = Column(String(50))
#     password = Column(String())
#     profile = relationship('Profile', uselist=False, back_populates='user')
#
# class Profile(Base):
#     __tablename__ = 'profiles'
#     id = Column(Integer, primary_key=True)
#     full_name = Column(String(100))
#     user_id = Column(Integer, ForeignKey('users.id'))
#     user = relationship('User', back_populates='profile')