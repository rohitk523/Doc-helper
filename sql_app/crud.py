from sqlalchemy.orm import Session
import uuid
from . import models, schemas


def get_user(db: Session, user_id: str):
    return db.query(models.User).filter(models.User.user_id == user_id).first()


def get_user_by_name(db: Session, name: str):
    return db.query(models.User).filter(models.User.name == name).first()


def get_users(db: Session):
    return db.query(models.User).all()


def create_user(db: Session, user: schemas.UserCreate):
    user_id = str(uuid.uuid4())
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(user_id= user_id,name=user.name, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_records(db: Session):
    return db.query(models.Visit).all()


def create_user_doc(db: Session, doc: schemas.DocCreate):
    doc_id = str(uuid.uuid4())
    db_doc = models.Doc(doc_id = doc_id,**doc.dict())
    db.add(db_doc)
    db.commit()
    db.refresh(db_doc)
    return db_doc

def create_visit(db: Session, visit: schemas.VisitCreate):
    visit_id = str(uuid.uuid4())
    db_visit = models.Visit(
        visit_id=visit_id,
        user_id=visit.user_id,
        doc_id=visit.doc_id,
        symptoms=visit.symptoms,
        disease=visit.disease,
    )
    db.add(db_visit)
    db.commit()
    db.refresh(db_visit)
    return db_visit