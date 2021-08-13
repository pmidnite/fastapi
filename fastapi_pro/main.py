from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


class Blog(BaseModel):
	title: str
	description: str
	published: Optional[bool]


@app.get('/blog')
def main(limit, published: bool=True, sort: Optional[str] = None):
	if published:
		return {'data': f'{limit} published blogs'}
	else:
		return {'data': f'{limit} blogs'}

@app.get('/blog/{id}')
def show_blog(id: int):
	return {'data': id}


@app.post('/blog/')
def create_blog(request: Blog):
	return {'data': f'Title: {request.title}, Description: {request.description}'}


if __name__ == '__main__':
	uvicorn.run(app, host="127.0.0.1", port=9000)