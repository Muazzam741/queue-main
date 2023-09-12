from database import Base
from sqlalchemy import String, Integer, Column, Text


class QueueEntry(Base):
    __tablename__ = 'Entry'
    instance_id = Column(String(255), primary_key=True)
    entry_position = Column(Integer, nullable=False, unique=True)
    member_id = Column(Integer, nullable=False, unique=True)
    initial_wait = Column(Integer, nullable=False)
    predicted_processing_period = Column(Integer, nullable=False)
