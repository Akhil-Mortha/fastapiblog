from sqlalchemy.orm import Session
import models,schemas
from fastapi import HTTPException,status

def get_all(db:Session):
    blogs=db.query(models.Blog).all()
    return blogs


def create(request: schemas.Blog,db:Session):
    new_blog = models.Blog(title=request.title,body=request.body,user_id=1) #200 foe ok
                                                                   # how do i rememder                                                               
    db.add(new_blog)                                               #fastapi is smart enough to give us all the codes ina very nice autocompletion  so what we can do here we can import the status  from the fastapiand then use it                                                              #
    db.commit()
    db.refresh(new_blog)
    return new_blog

def destroy(id:int,db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"blog with id{id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'

def update(id:int,request:schemas.Blog,db:Session):
    blog=db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"blog with id{id} not found")
    blog.update(request.model_dump())
    db.commit()
    return 'updated'

def show(id:int,db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"blog with the id {id} is not available")
        #response.status_code = status.HTTP_404_NOT_FOUND
        #return {'detail':f"blog with the id {id} is not available"}
    
    return blog


