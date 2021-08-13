from pydantic import BaseModel
from passlib.context import CryptContext
from typing import List, Optional


class BlogBase(BaseModel):
	title: str
	description: str


class Blog(BlogBase):
	class Config:
		orm_mode = True


class User(BaseModel):
	name: str
	email: str
	password: str

	@property
	def hash_password(self):
		pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
		return pwd_context.hash(self.password)
	

class ShowUser(BaseModel):
	name: str
	email: str
	blogs: List[Blog] = []

	class Config:
		orm_mode = True

class ShowBlog(BaseModel):
	title: str
	description: str
	publisher: ShowUser

	class Config:
		orm_mode = True

class Login(BaseModel):
	username: str
	password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None