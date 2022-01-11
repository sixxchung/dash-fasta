import uvicorn
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi.responses import RedirectResponse

from dashApp import apps

#----------------------------------------------------------------
appMain = FastAPI()

@appMain.get("/")
async def redirect_root():
    response = RedirectResponse("http://127.0.0.1:8000/dash")
    return response


#----------------------------------------------------------------
@appMain.get("/status")
def get_status():
    return {"status": "ok"}

#----------------------------------------------------------------
import routes
appMain.mount("/dash", WSGIMiddleware(apps.server))

if __name__ == "__main__":
    uvicorn.run(appMain, port=8000)