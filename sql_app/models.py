from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    docs = relationship("Doc", back_populates="owner")
    visits = relationship("Visit", back_populates="user")


class Doc(Base):
    __tablename__ = "docs"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="docs")
    visits = relationship("Visit", back_populates="doc")


class Visit(Base):
    __tablename__ = "visits"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    doc_id = Column(Integer, ForeignKey("docs.id"))

    user = relationship("User", back_populates="visits")
    doc = relationship("Doc", back_populates="visits")
