from fastapi import FastAPI

app = FastAPI()

@app.get('/save')
def save_data():
    ...

@app.get('/get')
def get_data():
    ...



