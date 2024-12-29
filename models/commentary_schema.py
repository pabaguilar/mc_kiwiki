from datetime import datetime, timezone, timedelta
from typing import Optional, List

from pydantic import BaseModel, Field, field_serializer


class commentary(BaseModel):
    user: str = Field(...) #El ObjectId del usuario que está comentando
    entry: str = Field(...) #El ObjectId de la entrada en la que está comentando
    entry_version: str = Field(...) #El ObjectId de la version de la entrada en la que esta comentando
    content: str = Field(...)
    date: datetime = Field(default_factory=lambda: datetime.now(timezone(timedelta(hours=2)))) #Para que cuando se actualice el campo tome la hora actual, el timedelta sirve para declarar que la zona horaria es CEST (+2)
    entryRating: Optional[int] = Field(None,ge=0,le=10) #La puntuacion que le da el usuario a la entrada del 0 al 10
    commentaryInReply: Optional[str] = None
    replies: Optional[List[str]] = []

    model_config = {
        "json_schema_extra": {
            "example": {
                "user": "507f1f77bcf86cd799439011",
                "entry": "507f1f77bcf86cd799439022",
                "entry_version": "507f1f77bcf86cd799439033",
                "content": "Este es un comentario de prueba.",
                "entryRating": 8,
                "commentaryInReply": "507f1f77bcf86cd799439044",
                "replies": [
                    "507f1f77bcf86cd799439055",
                    "507f1f77bcf86cd799439066"
                ]
            }
        }
    }

    @field_serializer("date", mode="plain")
    def serialize_date(self, value: datetime) -> str:
        return value.isoformat()

class commentaryUpdate(BaseModel):
    content: str = Field(...)

    model_config = {
        "json_schema_extra": {
            "example": {
                "content": "Este es un comentario de prueba."
            }
        }
    }