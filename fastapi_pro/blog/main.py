from fastapi import FastAPI
from . import models
from .database import engine
from .routers import blogs, users, login

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(login.router)
app.include_router(blogs.router)
app.include_router(users.router)

# def get_db():
# 	db = SessionLocal()
# 	try:
# 		yield db
# 	finally:
# 		db.close()


# @app.post('/blog', status_code=status.HTTP_201_CREATED, tags=['Blogs'])
# def create_a_blog(request: schemas.Blog, db: Session = Depends(get_db)):
# 	new_blog = models.Blog(title=request.title, description=request.description, publisher_id=1)
# 	db.add(new_blog)
# 	db.commit()
# 	db.refresh(new_blog)
# 	return new_blog


# @app.get('/blog', response_model=List[schemas.ShowBlog], tags=['Blogs'])
# def get_blogs(db: Session = Depends(get_db)):
# 	blogs = db.query(models.Blog).all()
# 	return blogs


# @app.get('/blog/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog, tags=['Blogs'])
# def get_a_blog(id: int, response: Response, db: Session = Depends(get_db)):
# 	blog = db.query(models.Blog).filter(models.Blog.id == id).first()
# 	if not blog:
# 		response.status_code = status.HTTP_404_NOT_FOUND
# 		return {"response": f"Blog with id: {id} is not available"}
# 	return blog


# @app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['Blogs'])
# def delete_a_blog(id: int, response: Response, db: Session = Depends(get_db)):
# 	deleted_blog = db.query(models.Blog).filter(models.Blog.id == id).\
# 										delete(synchronize_session=False)
# 	db.commit()
# 	return {'response': f"Blog with id {id} is deleted"}


# @app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['Blogs'])
# def update_a_blog(id: int, request: schemas.Blog, response: Response, db: Session = Depends(get_db)):
# 	blog = db.query(models.Blog).filter(models.Blog.id == id)
# 	if not blog.first():
# 		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
# 							detail=f'Blog with id {id} not found')
# 	blog.update({'title': request.title}, synchronize_session=False)
# 	db.commit()
# 	return {'response': f'Title update to {request.title} for Blog id: {id}'}


# @app.post('/user', tags=['Users'])
# def create_user(request: schemas.User, db: Session = Depends(get_db)):
# 	new_user = models.User(name=request.name, email=request.email, password=request.hash_password)
# 	db.add(new_user)
# 	db.commit()
# 	db.refresh(new_user)
# 	return new_user


# @app.get('/user/{id}', response_model=schemas.ShowUser, tags=['Users'])
# def get_a_user(id: int, db: Session = Depends(get_db)):
# 	user = db.query(models.User).filter(models.User.id == id).first()
# 	if not user:
# 		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
# 							detail=f'User with id {id} not exist')
# 	return user