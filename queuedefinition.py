from database import Base
from sqlalchemy import String, Integer, Column, Text
import smartqueue


# This class defines the queue definition
# It defines the queue operating hours, start time, end time, etc. It also defines the queue capacity.
#

class QueueDefinition(Base):
    merchant_id = Column(String, unique=True)  # foreign key
    queue_id = Column(String, primary_key=True)  # primary key
    queue_name = Column(String,unique=True)
    queue_description = Column(String)
    queue_capacity = Column(Integer)
    entry_start_time = Column(String)
    entry_end_time = Column(String)
    operating_days = Column(map)

    class Config:
        orm_mode = True
