from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Temporary in-memory list acting as a simple database
message_store = []

# Data structure matching client requests
class DeviceMessage(BaseModel):
    device_id: str
    message: str

@app.get("/")
def home():
    return {"status": "Server is running!"}

# Endpoint for Child device to post logs/messages
@app.post("/api/send")
def send_message(data: DeviceMessage):
    message_store.append(data.dict())
    return {"status": "success", "total_records": len(message_store)}

# Endpoint for Parent device to fetch all logs/messages
@app.get("/api/messages", response_model=List[DeviceMessage])
def get_messages():
    return message_store