from fastapi import FastAPI


app = FastAPI()

@app.get('/key')
def home():
    return {'key':'Hello'}