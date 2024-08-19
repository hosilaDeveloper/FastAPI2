from fastapi import FastAPI

app = FastAPI()

fake_db = [{'Hello Developer'}]


@app.get("/", description='get request')
async def root():
    return fake_db


@app.post('/create/')
async def create(item: dict):
    fake_db.append(item)
    return fake_db


@app.put('/update/')
async def update(item: dict):
    fake_db.append(item)
    return fake_db


@app.delete('/delete/')
async def delete(item: dict):
    fake_db.append(item)
    return fake_db
