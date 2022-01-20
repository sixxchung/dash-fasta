from fastapi import APIRouter

router = APIRouter(prefix='/status', tags=['common'])

#----------------------------------------------------------------
@router.get("/")
def get_status():
    return {"status": "ok"}