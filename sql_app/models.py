from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
import uuid
from .database import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(String, primary_key=True, default=uuid.uuid4)
    name = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    visits = relationship("Visit", back_populates="user")


class Doc(Base):
    __tablename__ = "docs"

    doc_id = Column(String, primary_key=True, default=uuid.uuid4)
    name = Column(String, index=True)
    speciality = Column(String, index=True)

    visits = relationship("Visit", back_populates="doc")


class Visit(Base):
    __tablename__ = "visits"

    visit_id = Column(String, primary_key=True, default=uuid.uuid4)
    user_id = Column(String, ForeignKey("users.user_id"))
    doc_id = Column(String, ForeignKey("docs.doc_id"))
    symptoms = Column(String, index=True)
    disease = Column(String, index=True)

    user = relationship("User", back_populates="visits")
    doc = relationship("Doc", back_populates="visits")
