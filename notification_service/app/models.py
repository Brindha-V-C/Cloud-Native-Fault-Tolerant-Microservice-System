from pydantic import BaseModel

class Notification(BaseModel):
    user_id: str
    channel: str   # email / sms / in-app
    message: str
