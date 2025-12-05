from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from collections import Counter

router = APIRouter()

class Event(BaseModel):
    user_id: str
    action: str
    timestamp: float

events: List[Event] = []


@router.post("/events")
def ingest_event(event: Event):
    events.append(event)
    return {
        "status": "event_recorded",
        "total_events": len(events)
    }


@router.get("/metrics/actions")
def action_counts():
    """
    System-wide action counts across all users.
    Example: {"login": 10, "update_profile": 3}
    """
    counts = Counter([e.action for e in events])
    return counts


@router.get("/metrics/user/{user_id}/actions")
def user_action_counts(user_id: str):
    """
    Action counts for a specific user.
    Example: {"login": 2, "purchase": 1} for that user only.
    """
    user_events = [e.action for e in events if e.user_id == user_id]
    counts = Counter(user_events)
    return {
        "user_id": user_id,
        "actions": counts
    }


@router.get("/health")
def health():
    return {"status": "ok"}
