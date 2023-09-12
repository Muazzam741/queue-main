# items = UnicodeSetAttribute(default=set()) # list of token IDs waiting in the queue
from database import Base
from sqlalchemy import String, Integer, Column


class SmartQueue(Base):
    __tablename__ = 'Smart_queue'

    merchant_id = Column(String(255), primary_key=True, nullable=False)
    session = Column(String(255), nullable=False)
    current_wait_period = Column(Integer, nullable=False, default=0)
    completed_wait_period = Column(Integer, default=0)
    current_items_count = Column(Integer, default=0)
    completed_items_count = Column(Integer, default=0)
