#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/22 0022 19:03
# @Author  : CarryChang
# @Software: PyCharm
# @email: coolcahng@gmail.com
# @web ：CarryChang.top
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
# get way
async def get():
    return {"Hello": "World"}
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
@app.put("/item/{item_id}")
async def update_item(item_id: int):
    return {"item_id": item_id}
