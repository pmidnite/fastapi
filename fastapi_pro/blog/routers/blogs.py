from fastapi import APIRouter, status, Depends, Response
from typing import List
from .. import schemas, models
from ..database import get_db
from sqlalchemy.orm import Session
from blog.db_utils import blog
from ..oauth2 import get_current_user


router = APIRouter(
	prefix="/blog",
	tags=['Blogs']
)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_a_blog(request: schemas.Blog, db: Session = Depends(get_db)):
	return blog.create(request, db)


@router.get('/', response_model=List[schemas.ShowBlog])
def get_blogs(db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
	return blog.fetch_all(db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def get_a_blog(id: int, response: Response, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
	return blog.fetch_one(id, response, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_a_blog(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
	return blog.delete(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_a_blog(id: int, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
	return blog.update(id, request, db)