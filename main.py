import uvicorn
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi.responses import RedirectResponse

from appdash import dash_app

#----------------------------------------------------------------
app = FastAPI()

@app.get("/")
async def redirect_root():
    response = RedirectResponse("http://127.0.0.1:8888/dash")
    return response

#----------------------------------------------------------------
@app.get("/status")
def get_status():
    return {"status": "ok"}

#----------------------------------------------------------------
import routes
app.mount("/dash", WSGIMiddleware(dash_app.server))

if __name__ == "__main__":
    uvicorn.run(app, port=8888)