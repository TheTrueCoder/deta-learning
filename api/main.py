from fastapi import FastAPI
# from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from random import choice

def txt_file_list(filename: str):
    with open(filename, "r") as f:
        raw = f.readlines()
        return [q.rstrip() for q in raw]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load quotes into memory for speed-quoting
quotes: str = txt_file_list("quotes.txt")

@app.get("/api/quotes")
async def quote_list(length: int = 1):
    "Responds with random star wars quotes under the 'quotes' key."
    user_quotes = [choice(quotes) for i in range(length)]
    return {'quotes': user_quotes}