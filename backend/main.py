from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Monta a pasta frontend para servir arquivos estáticos
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")

# Rota principal
@app.get("/", response_class=HTMLResponse)
def read_root():
    with open("frontend/Login.html") as f:
        return f.read()