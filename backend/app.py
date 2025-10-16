from fastapi import FastAPI, Request
from pydantic import BaseModel, EmailStr
from motor.motor_asyncio import AsyncIOMotorClient
import os, datetime

app = FastAPI()

MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("MONGODB_DB", "devops_login_demo")

mongo_client = AsyncIOMotorClient(MONGODB_URI)
db = mongo_client[DB_NAME]
audits = db["login_audits"]

class LoginEvent(BaseModel):
    email: EmailStr

@app.get("/api/health")
async def health():
    # Round trip a ping to Mongo for a real health signal
    await db.command("ping")
    return {"ok": True}

@app.post("/api/audit")
async def audit_login(evt: LoginEvent, request: Request):
    doc = {
        "email": evt.email,
        "ip": request.client.host,
        "ts": datetime.datetime.utcnow()
    }
    res = await audits.insert_one(doc)
    return {"inserted_id": str(res.inserted_id)}
