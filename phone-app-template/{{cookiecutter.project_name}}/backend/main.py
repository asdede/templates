from fastapi import FastAPI

app = FastAPI()

@app.get("/process")
def process():
    return {"msg":"Roses are red, violet's are blue, beer is sweet, and so are you."}