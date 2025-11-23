from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from typing import List

from api.db import get_session
from api.ai.schemas import EmailMessageSchema
from api.ai.services import generate_email_message
from .model import ChatMessagePayload, ChatMessage, ChatMessageListItems


router = APIRouter()

@router.get("/")
def chat_health():
    return {"status": "ok"}


@router.get("/recent", response_model=List[ChatMessageListItems])
def get_recent_chat_messages(session: Session = Depends(get_session)):
    query = select(ChatMessage)
    result = session.exec(query).fetchall()[:10]
    return result

@router.post("/", response_model=EmailMessageSchema)
def chat_create_message(payload: ChatMessagePayload, session: Session = Depends(get_session)):
    data = payload.model_dump()
    
    obj = ChatMessage.model_validate(data)
    session.add(obj)
    session.commit()
    session.refresh(obj)
    response = generate_email_message(payload.message)
    return response