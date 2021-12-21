import uvicorn
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware

from dashApp import apps

#----------------------------------------------------------------
appMain = FastAPI()
@appMain.get("/")
def read_main():
    return {
        "routes": [
            {"method":"GET", "path":"/",       "summary":"Landing"},
            {"method":"GET", "path":"/status", "summary":"App status"},
            {"method":"GET", "path":"/dash",   "summary":"Sub-mounted Dash application"},
        ]
    }

#----------------------------------------------------------------
@appMain.get("/status")
def get_status():
    return {"status": "ok"}

#----------------------------------------------------------------
import routes
appMain.mount("/dash", WSGIMiddleware(apps.server))

if __name__ == "__main__":
    uvicorn.run(appMain, port=8000)