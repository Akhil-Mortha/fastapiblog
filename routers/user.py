from fastapi import APIRouter
import schemas,models
from database import get_db
from sqlalchemy.orm import Session
from fastapi  import APIRouter,Depends,status
from repository import user
router = APIRouter( 
    prefix="/user",
    tags=['users'])

@router.post('/',response_model=schemas.ShowUser)
def create_user(request: schemas.User,db: Session = Depends(get_db)):
    return user.create(request,db)

@router.get('/{id}',response_model=schemas.ShowUser)
def get_user(id:int,db: Session = Depends(get_db)):
    return user.show(id,db)