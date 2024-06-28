import google.generativeai as genai
import time

def clean_gemini(key, prompt, model_name):
    genai.configure(api_key=key)
    model = genai.GenerativeModel(model_name=model_name)
    generation_config = genai.GenerationConfig(temperature=0.0)
    response = model.generate_content(prompt, generation_config=generation_config)
    return(response.text)
