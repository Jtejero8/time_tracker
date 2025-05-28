from . import models, database
from sqlalchemy.orm import Session
import datetime, csv
from fastapi.responses import StreamingResponse
from .auth import get_user_by_token

session = database.SessionLocal()

def clock_in(token):
    user = get_user_by_token(token)
    new_session = models.WorkSession(user_id=user.id)
    session.add(new_session)
    session.commit()
    return {"message": "Clock-in registered"}

def clock_out(token):
    user = get_user_by_token(token)
    ws = session.query(models.WorkSession).filter_by(user_id=user.id, end_time=None).first()
    if ws:
        ws.end_time = datetime.datetime.utcnow()
        session.commit()
        return {"message": "Clock-out registered"}
    return {"error": "No active session found"}

def get_summary(token):
    user = get_user_by_token(token)
    sessions = session.query(models.WorkSession).filter_by(user_id=user.id).all()
    summary = []
    for s in sessions:
        total = (s.end_time - s.start_time).total_seconds()/3600 if s.end_time else None
        summary.append({"date": s.start_time.date(), "hours": total})
    return summary

def export_csv(token):
    user = get_user_by_token(token)
    sessions = session.query(models.WorkSession).filter_by(user_id=user.id).all()
    def generate():
        yield "date,start_time,end_time,total_hours\n"
        for s in sessions:
            total = (s.end_time - s.start_time).total_seconds()/3600 if s.end_time else 0
            yield f"{s.start_time.date()},{s.start_time},{s.end_time},{total}\n"
    return StreamingResponse(generate(), media_type="text/csv")