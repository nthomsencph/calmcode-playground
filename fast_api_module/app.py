from fastapi import FastAPI
import time
import asyncio
from ItemFactory import Item

app = FastAPI()

@app.get("/")
def root():
    return {"message": "hello world again!"}


@app.get("/users/{user_id}")
def read_user(user_id: int):

    """
    We accept a user ID here. We will return a JSON blob with it.
    """
    return {"user_id": user_id}


@app.post("/items/")
def create_item(item: Item):
    return f"{item.name} costs {item.price}."


@app.get("/sleep_slow")
def sleep_slow():
    r = time.sleep(1)
    return {"status": "Done"}


@app.get("/sleep_fast")
async def sleep_fast():
    r = await asyncio.sleep(1)
    return {"status": "Done"}


