from fastapi import FastAPI
from .models import Notification
import datetime

app = FastAPI(
    title="Notification Service",
    description="Handles system notifications",
    version="1.0.0"
)

@app.post("/notify")
def send_notification(notification: Notification):
    timestamp = datetime.datetime.utcnow().isoformat()

    # Simulate sending notification
    print(
        f"[{timestamp}] "
        f"Notification sent | "
        f"User: {notification.user_id} | "
        f"Channel: {notification.channel} | "
        f"Message: {notification.message}"
    )

    return {
        "status": "sent",
        "user_id": notification.user_id,
        "channel": notification.channel
    }

@app.get("/health")
def health():
    return {"status": "ok"}
