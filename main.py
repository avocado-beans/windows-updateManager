from fastapi import FastAPI, Request
import gemini
import asyncio
import base64
app = FastAPI()

@app.post("/gemini/")
async def read_items(request: Request):
    
    with open("question.png", "wb") as image:
        image.write(base64.b64decode(request.query_params['image']))
        
    return gemini.answer(request.query_params['key'], request.query_params['prompt'], "question.png", request.query_params['model_name'])
