from fastapi import Response, HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, models



def create(request: schemas.Blog, db: Session):
	new_blog = models.Blog(title=request.title, description=request.description, publisher_id=1)
	db.add(new_blog)
	db.commit()
	db.refresh(new_blog)
	return new_blog


def fetch_all(db: Session):
	blogs = db.query(models.Blog).all()
	return blogs


def fetch_one(id: int, response: Response, db: Session):
	blog = db.query(models.Blog).filter(models.Blog.id == id).first()
	if not blog:
		response.status_code = status.HTTP_404_NOT_FOUND
		return {"response": f"Blog with id: {id} is not available"}
	return blog


def delete(id: int, db: Session):
	deleted_blog = db.query(models.Blog).filter(models.Blog.id == id).\
										delete(synchronize_session=False)
	db.commit()
	return {'response': f"Blog with id {id} is deleted"}


def update(id: int, request: schemas.Blog, db: Session):
	blog = db.query(models.Blog).filter(models.Blog.id == id)
	if not blog.first():
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
							detail=f'Blog with id {id} not found')
	blog.update({'title': request.title}, synchronize_session=False)
	db.commit()
	return {'response': f'Title update to {request.title} for Blog id: {id}'}