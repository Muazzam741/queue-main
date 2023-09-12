from database import Base,engine
from smartqueue import SmartQueue
from queueentry import QueueEntry
from dailyqueueInstance import DailyQueueInstance
from queuedefinition import QueueDefinition

print("Creating database ......")

Base.metadata.create_all(engine)
