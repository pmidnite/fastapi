from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from ..schemas import Login
from ..database import get_db
from ..models import User
from ..routers import auth
from sqlalchemy.orm import Session
from datetime import timedelta


router = APIRouter(
	tags=['User Login']
)

@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
	user = db.query(User).filter(User.email == request.username).first()
	if not user:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
							detail= f'Invalid Credentials')
	if not auth.verify_password(request.password, user.password):
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
							detail= f'Incorrect Password')
	access_token_expires = timedelta(minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES)
	access_token = auth.create_access_token(data={"sub": user.email},
											expires_delta=access_token_expires)
	return {"access_token": access_token, "token_type": "bearer"}
