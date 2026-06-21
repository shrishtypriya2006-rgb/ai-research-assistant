from google import genai

API_KEY = "YOUR_API_KEY_HERE"

client = genai.Client(api_key=API_KEY)

models = client.models.list()

for m in models:
    print(m.name)