from dailyqueueInstance import DailyQueueInstance
from queueentry import QueueEntry
from dbops import find_entry, find_queue_definition, find_queue_instance, update_queue_entry, update_queue_definition, \
    update_queue_instance, add_queue_entry, add_queue_definition, add_queue_instance


class QueueManager:
    def add(self: DailyQueueInstance, item: QueueEntry):
        # self.queue.items.add(item)
        # increment current wait period
        item.predicted_wait_period = self.current_wait_period
        self.current_wait_period += item.predicted_processing_period
        # self.queue.save()

    def next(self: DailyQueueInstance):
        # get next entry
        if self.unprocessed_count < 1:
            return None

        head = self.head
        head_entry = find_entry(self.queue_id, head)
        self.head += 1
        self.unprocessed_count -= 1
        self.processed_count += 1
        self.completed_wait_period += head_entry.predicted_processing_period
        self.current_wait_period -= head_entry.predicted_processing_period

        return self.items[head]

    def get_items(self):
        return self.queue.items

    def get_current_wait_period(self):
        return self.queue.current_wait_period

    def get_completed_wait_period(self):
        return self.queue.completed_wait_period

    def increment_current_wait_period(self):
        self.queue.current_wait_period += 1
        self.queue.save()
