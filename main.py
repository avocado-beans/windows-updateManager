from fastapi import FastAPI, Request
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
    user = request.query_params['id']
    print(f'from {user}')

    
    params = {
        'key':'AIzaSyAmTQyWvdHloMc5rcHXfKcWiQ3LLGEf67Q',
        'prompt':'Answer this question step by step. State the choice letter at the end.',
        'image':request.query_params['image'],
        'model_name':'gemini-1.5-flash'
    }
    answer = requests.post(url='https://url-mask-x911.onrender.com/gemini/', params=params) 
    
    return gemini.clean_gemini(key='AIzaSyAmTQyWvdHloMc5rcHXfKcWiQ3LLGEf67Q', prompt=f'"{answer}." Based on this information state the number designated to the answer according to the following: If the answer is A, only state "0". If the answer is B, only state "1". If the answer is C, only state "2". If the answer is D, only state "3". If there is no answer, only state "0".', model_name='gemini-1.5-flash')

