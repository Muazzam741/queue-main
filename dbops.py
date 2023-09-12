from queueentry import QueueEntry
from queuedefinition import QueueDefinition
from dailyqueueInstance import DailyQueueInstance


# static funtion to find queue entry from database using queue id and qntry id
def find_entry(queue_id, entry_id) -> QueueEntry:
    return None


# static function to find queue definition from database using queue id
def find_queue_definition(queue_id) -> QueueDefinition:
    return None


# static function to find daily queue instance from database using merchant id and day
def find_queue_instance(merchant_id, day) -> DailyQueueInstance:
    return None


# static function to update queue entry in database
def update_queue_entry(queue_entry: QueueEntry):
    return None


# static function to update queue definition in database
def update_queue_definition(queue_definition: QueueDefinition):
    return None


# static function to update daily queue instance in database
def update_queue_instance(queue_instance: DailyQueueInstance):
    return None


# static function to add queue entry in database
def add_queue_entry(queue_entry: QueueEntry):
    return None


# static function to add queue definition in database
def add_queue_definition(queue_definition: QueueDefinition):
    return None


# static function to add daily queue instance in database
def add_queue_instance(queue_instance: DailyQueueInstance):
    return None
