import uvicorn

from . import app
from dotenv import load_dotenv
load_dotenv()
from os import getenv
uvicorn.run("app:app", host=getenv("HOST"), port=getenv("PORT"), reload=True)
