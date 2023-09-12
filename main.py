from fastapi import FastAPI,status,HTTPException
import queueentry
import smartqueue
import queuedefinition
from pydantic import BaseModel
from queuemanager import QueueManager

app = FastAPI()

total_wait_limit = 10
class QueueEntry(BaseModel):
    instance_id: str
    entry_position: int
    member_id: int
    initial_wait: int
    predicted_processing_period: int

    class Config:
        orm_mode = True


class SmartQueue(BaseModel):
    merchant_id: str
    session: str
    current_wait_period: int
    completed_wait_period: int
    current_items_count: int
    completed_items_count: int

    class Config:
        orm_mode = True


class QueueDefinition(BaseModel):
    merchant_id: str  # foreign key
    queue_id: str  # primary key
    queue_name: str
    queue_description: str
    queue_capacity: int
    entry_start_time: str
    entry_end_time: str
    operating_days: map

    class Config:
        orm_mode = True


class DailyQueueInstance(BaseModel):
    merchant_id: str
    day: str
    instance_id: str
    current_wait_period: int
    completed_wait_period: int
    unprocessed_count: int
    processed_count: int
    head: int

    class Config:
        orm_mode = True


# Create a Queue item
@app.post('/item',response_model=DailyQueueInstance,status_code=status.HTTP_201_CREATED)
def create_queue_item(item: DailyQueueInstance):
    if item.current_wait_period < total_wait_limit
    table.put_item(Item=item.model_dump())
    return item.model_dump()


# Retrieve a Queue item
@app.get("/queue/{queue_id}")
def read_queue_item(queue_id: str):
    response = table.get_item(Key={"id": queue_id})
    item = response.get("Item")
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


# Update a Queue item
@app.put("/queue/{queue_id}")
def update_queue_item(queue_id: str, item: QueueItem):
    table.update_item(
        Key={"id": queue_id},
        AttributeUpdates={
            'name': {'Value': item.name, 'Action': 'PUT'},
            'description': {'Value': item.description, 'Action': 'PUT'}
        }
    )
    return {"id": queue_id, **item.dict()}


# Delete a Queue item
@app.delete("/queue/{queue_id}")
def delete_queue_item(queue_id: str):
    table.delete_item(Key={"id": queue_id})
    return {"status": "success"}
