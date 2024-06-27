pfrom fastapi import FastAPI, Request
import gemini
import asyncio
import base64
import requests

app = FastAPI()


@app.get("/")
async def confirm(request: Request):
    return "Your server is working!"
    
@app.post("/")
async def read_items(request: Request):
    params = {
        'key':request.query_params['key'],
        'prompt':request.query_params['prompt'],
        'image':request.query_params['image'],
        'model_name':request.query_params['model_name']
    }
    answer = requests.post(url=request.query_params['url'], params=params)    
    return answer.text

