from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: str):
    return db.query(models.User).filter(models.User.user_id == user_id).first()


def get_user_by_name(db: Session, name: str):
    return db.query(models.User).filter(models.User.name == name).first()


def get_users(db: Session, skip: str = 0):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(name=user.name, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_docs(db: Session, skip: str = 0):
    return db.query(models.Doc).offset(skip).limit(limit).all()


def create_user_doc(db: Session, doc: schemas.DocCreate, user_id: str):
    db_doc = models.Doc(**doc.dict(), owner_id=user_id)
    db.add(db_doc)
    db.commit()
    db.refresh(db_doc)
    return db_doc

def create_visit(db: Session, visit: schemas.VisitCreate):
    db_visit = models.Visit(**visit.dict())
    db.add(db_visit)
    db.commit()
    db.refresh(db_visit)
    return db_visit