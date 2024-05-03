from pydantic import BaseModel


class DocBase(BaseModel):
    title: str
    description: str | None = None


class DocCreate(DocBase):
    pass


class Doc(DocBase):
    doc_id: str
    owner_id: str

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    name: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    user_id: str
    docs: list[Doc] = []

    class Config:
        orm_mode = True

class VisitBase(BaseModel):
    user_id: str
    doc_id: str


class VisitCreate(VisitBase):
    pass


class Visit(VisitBase):
    visit_id: str

    class Config:
        orm_mode = True