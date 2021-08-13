from fastapi import APIRouter, Depends, status
from .. import schemas
from sqlalchemy.orm import Session
from ..database import get_db
from blog.db_utils import user


router = APIRouter(
	prefix='/user',
	tags=['Users']
)


@router.post('/')
def create_user(request: schemas.User, db: Session = Depends(get_db)):
	return user.create(request, db)


@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
	return user.show(id, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: int, db: Session = Depends(get_db)):
	return user.delete(id, db)