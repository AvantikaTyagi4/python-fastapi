from fastapi import FastAPI

app = FastAPI()

# @app.get('/')
# def index():
#     return "hello"

# to return JSOn
@app.get('/')
def index():
    return {"data":{"name": "Jack"}}

@app.get('/about')
def about():
    return {'data':'about page'}