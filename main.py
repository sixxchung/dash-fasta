import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from fastapi.middleware.wsgi import WSGIMiddleware
from app_dash import dash_app

from routers import model_get

app = FastAPI()
app.mount("/dash", WSGIMiddleware(dash_app.server))
app.include_router(model_get.router)

@app.get("/")
async def redirect_root():
    response = RedirectResponse("http://127.0.0.1:8888/dash")
    return response

#----------------------------------------------------------------
if __name__ == "__main__":
    uvicorn.run(app, port=8888)