import unittest
from src.memory import Memory
from collections import deque

msg1 = {"role": "system", "content": "You are a helpful assistant."},
msg2 = {"role": "user", "content": "Who won the world series in 2020?"}


class TestMemory(unittest.TestCase):
    def setUp(self):
        self.memory = Memory(system_message="You are a helpful assistant.")

    def test_append(self):
        self.memory.append("user1", msg1)
        self.memory.append("user1", msg2)
        self.assertEqual(
            self.memory.storage["user1"], deque([msg1, msg2]))

    def test_get(self):
        self.memory.append("user1", msg1)
        self.assertEqual(self.memory.get("user1"), [msg1])

    def test_remove(self):
        self.memory.append("user1", "Hello")
        self.memory.remove("user1")
        self.assertEqual(self.memory.get("user1"), [])
