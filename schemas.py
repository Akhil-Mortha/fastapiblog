from typing import List,Optional
from pydantic import BaseModel

class BlogBase(BaseModel):
    title: str
    body: str
class Blog(BlogBase):
    class config(): #we can do it without class also
        orm_mode=True



class User(BaseModel):
    name: str
    email: str
    password:str

class ShowUser(BaseModel):
    name: str
    email: str
    blogs :List[Blog]=[]
    class config():
        orm_mode=True

class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser
    class config():
        orm_mode=True
       

class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None


class ShoeAll(BaseModel):
    creator: ShowUser



