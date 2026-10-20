from fastapi import HTTPException

from AI_service.errors import ChatUnavailableError, InvalidChatMessageError
from AI_service.schemas.chat import MessageRequest
from AI_service.services.chat_service import send_message


def handle_send_message(
    conversation_id: str,
    request: MessageRequest,
    user: dict
) -> dict:
    try:
        return send_message(conversation_id, request, user)
    except InvalidChatMessageError as exc:
        raise HTTPException(status_code=422, detail=exc.public_message) from exc
    except ChatUnavailableError as exc:
        raise HTTPException(status_code=503, detail=exc.public_message) from exc
