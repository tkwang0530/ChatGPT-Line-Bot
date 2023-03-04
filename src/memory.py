from typing import Dict, List
from collections import defaultdict, deque


class MemoryInterface:
    def append(self, user_id: str, message: Dict) -> None:
        pass

    def get(self, user_id: str) -> List[Dict]:
        pass

    def remove(self, user_id: str) -> None:
        pass


class Memory(MemoryInterface):
    def __init__(self, system_message, message_list_limit=10):
        self.message_list_limit = message_list_limit
        self.storage = defaultdict(deque)
        self.system_message = system_message

    def initialize(self, user_id: str):
        self.storage[user_id] = deque([{
            'role': 'system', 'content': self.system_message
        }])

    def append(self, user_id: str, message: Dict) -> None:
        if self.storage[user_id] == []:
            self.initialize(user_id)
        self.storage[user_id].append(message)
        if len(self.storage[user_id]) > self.message_list_limit:
            self.storage[user_id].popleft()

    def get(self, user_id: str) -> List[Dict]:
        return list(self.storage[user_id])

    def remove(self, user_id: str) -> None:
        self.storage[user_id] = deque([])
