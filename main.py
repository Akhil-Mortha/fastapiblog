from fastapi import FastAPI
import models
from database import engine
from routers import blog,user,authentication

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router (authentication.router)
app.include_router (blog.router)
app.include_router (user.router)


#api router operators
#Blog and User respositories
#login and verify password
#now we need the user login system so lets create the route to log in the user with the email and the password
#we are going to use this documentation of fastapi Oauth2 with password (and hashing)Bearer with jwt tokens