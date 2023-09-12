from database import Base
from sqlalchemy import String, Integer, Column, Text


class DailyQueueInstance(Base):
    merchant_id = Column(String, unique=True)
    day = Column(String)
    instance_id = Column(String)
    current_wait_period = Column(Integer)
    completed_wait_period = Column(Integer)
    unprocessed_count = Column(Integer)
    processed_count = Column(Integer)
    head = Column(Integer)
