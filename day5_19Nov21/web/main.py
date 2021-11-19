### FAST API with Swagger built-in -> to create pure REST APIs
###  purely for REST API
### pip3 install fastapi
### pip3 install uvicorn

from fastapi import FastAPI
from typing import Optional

app = FastAPI()

app.get('/')
async def home():
    return {'msg': 'Welcome to fast api'}

@app.get('/contact/{cid}')
def contact_details(cid:int, page:Optional[int]=1):
    if page:
        return {'contact_id':cid,'page':page}
    return {'contact_id':cid}

'''
    run this in the shell like:
    $ uvicorn main:app  --reload  # run main.py with instance of app (FastAPI's instance)
    the above didnt work..!! use the below
    $ python3 -m uvicorn main:app --reload --port 50000
'''

