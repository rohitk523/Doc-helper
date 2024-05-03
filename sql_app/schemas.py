from pydantic import BaseModel


class DocBase(BaseModel):
    title: str
    description: str | None = None


class DocCreate(DocBase):
    pass


class Doc(DocBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    docs: list[Doc] = []

    class Config:
        orm_mode = True

class VisitBase(BaseModel):
    user_id: int
    doc_id: int


class VisitCreate(VisitBase):
    pass


class Visit(VisitBase):
    id: int

    class Config:
        orm_mode = True