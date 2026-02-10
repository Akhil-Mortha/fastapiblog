from fastapi  import APIRouter,Depends,status,HTTPException
from sqlalchemy.orm import Session
from typing import List
import schemas,models,oauth2
from database import get_db
from repository import blog

router = APIRouter(
    prefix="/blog",
    tags=['blogs']
                   
                   
                   )



@router.get('/',response_model=schemas.ShowUser)#List[schemas.ShowAll] if u want other creators too
def all(db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)

@router.post('/',status_code=status.HTTP_201_CREATED)                               #201 for created
def create(request: schemas.Blog, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)): #202 for accepted
    return blog.create(request,db)

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.destroy(id,db)

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id:int,request: schemas.Blog,db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id,request,db)

#@app.get('/blog',response_model=List[schemas.ShowBlog],tags=['blogs'])
#def all(db: Session = Depends(get_db)):
    blogs=db.query(models.Blog).all()
    return blogs

#particular block with id getting# we can see all the codes in pythone documentation foe http status codee here we can see

@router.get('/{id}',status_code=200,response_model=schemas.ShowBlog)
def show(id:int,db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):  # in sqlalchemy there is on where condition
    return blog.show(id,db)