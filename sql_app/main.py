from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine
from starlette.staticfiles import StaticFiles

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


# Define route for homepage
@app.get("/user")
async def read_root():
    # Read the HTML file and return it
    with open("templates/user.html", "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content, status_code=200)


@app.get("/doc")
async def read_docs():
    with open("templates/docs.html", "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content, status_code=200)


@app.get("/visits")
async def read_visits():
    with open("templates/visits.html", "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content, status_code=200)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_name(db, name=user.name)
    if db_user:
        raise HTTPException(status_code=400, detail="name already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(db: Session = Depends(get_db)):
    users = crud.get_users(db)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: str, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/docs", response_model=schemas.Doc)
def create_doc_for_user(
    doc: schemas.DocCreate, db: Session = Depends(get_db)
):
    return crud.create_user_doc(db=db, doc=doc)


@app.get("/records/", response_model=list[schemas.Visit])
def read_records(db: Session = Depends(get_db)):
    records = crud.get_records(db)
    return records


@app.post("/visits/", response_model=schemas.Visit)
def create_visit(visit: schemas.VisitCreate, db: Session = Depends(get_db)):
    db_visit = crud.create_visit(db=db, visit=visit)
    return db_visit

