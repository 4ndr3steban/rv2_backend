from fastapi import HTTPException, status
from sqlalchemy import select, insert
from sqlalchemy.orm import Session
from config.db import engine
from config.models import Tuser, Tproduct, Tchallenge, Timpact, Tredeemhistory, Tbadge, Tchallengehistory
from schemas.user import User
from schemas.product import Product
from schemas.challenge import Challenge
from schemas.impact import Impact
from settings import settings


def search_user(db: Session, id: int):

    try:
        db_user = db.query(Tuser).filter(Tuser.id == id).all()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"fail to search user ({e})")
    user_rh = db.query(Tredeemhistory).filter(Tredeemhistory.id_user == id).all()
    user_ch = db.query(Tchallengehistory).filter(Tchallengehistory.id_user == id).all()
    user_bg = db.query(Tbadge).filter(Tbadge.id_user == id).all()

    return {"user":db_user,  "redeemHistory":user_rh,  "challengeHistory":user_ch,  "badges":user_bg}


def search_challenges(db: Session):

    try:
        challenges = db.query(Tchallenge).all()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"fail to search user ({e})")
    
    return challenges
    

def search_products(db: Session):

    try:
        products = db.query(Tproduct).all()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"fail to search user ({e})")
    
    return products


def search_microchallenges(db: Session):
    try:
        microchallenges = db.query(Tchallenge).filter(Tchallenge.challenge_type == "micro").all()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"fail to search user ({e})")
    
    return microchallenges


def search_macrochallenges(db: Session):
    try:
        macrochallenges = db.query(Tchallenge).filter(Tchallenge.challenge_type == "macro").all()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"fail to search user ({e})")
    
    return macrochallenges


def search_impact(db: Session):
    try:
        impact = db.query(Timpact).all()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"fail to search user ({e})")
    
    return impact