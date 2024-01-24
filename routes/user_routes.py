from fastapi import APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from config.db import engine
from core.crud import search_user, search_challenges, search_impact

# Instancia para manejar el endpoint para el manejo de la db de MySql
router = APIRouter(prefix="/user",
                    tags=["user routes"],
                    responses={status.HTTP_404_NOT_FOUND: {"response": "not found"}})


@router.get("/test", response_model=list, status_code = status.HTTP_200_OK)
async def savequery(id: int):

    ans = search_impact(Session(engine))

    return ans