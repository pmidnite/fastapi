from sqlalchemy.orm import Session
from .. import schemas, models


def create(request: schemas.User, db: Session):
	new_user = models.User(name=request.name, email=request.email, password=request.hash_password)
	db.add(new_user)
	db.commit()
	db.refresh(new_user)
	return new_user


def show(id:int, db: Session):
	user = db.query(models.User).filter(models.User.id == id).first()
	if not user:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
							detail=f'User with id {id} not exist')
	return user

def delete(id: int, db: Session):
	user = db.query(models.User).filter(models.User.id == id).\
								delete(synchronize_session=False)
	db.commit()
	return {'response': f"User with id={id} is deleted"}