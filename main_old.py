from fastapi import FastAPI
import uvicorn
from fastapi.responses import HTMLResponse,JSONResponse

app = FastAPI(title="test api")

@app.get("/")
def home():
    return {"message": "Hello, World!"}

@app.get("/greet/{name}", response_class=HTMLResponse)
def greet(name: str):
    return f"<h1>Hello, {name}!</h1>"            # ✅ HTMLResponse — return STRING

@app.get("/greet-json/{name}")
def greet_json(name: str):
    return {"message": f"Hello, {name}!"}        # ✅ JSON — return dict

@app.get("/add",response_class=JSONResponse)
def add(a: int,b: int)-> dict:
    return {"result" : a + b}

@app.get("/status")
def status():
    return {"status": "OK", "app": "FastAPI", "version": "1.0"}

if __name__ =="__main__":
    uvicorn.run(app,host="localhost",port=8000)