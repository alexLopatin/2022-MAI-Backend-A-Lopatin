from LinkedList import LinkedList, Node


class LRUCache:
    def __init__(self, capacity: int = 10) -> None:
        self.capacity = capacity
        self.queue_list = LinkedList()
        self.dict: dict[str, str] = {}
        self.key_queue_dict: dict[str, 'Node'] = {}
        self.count: int = 0

    def get(self, key: str) -> str:
        if self.dict.get(key) is None:
            return ''

        self.queue_list.hoist(self.key_queue_dict[key])
        return dict.get(self.dict, key)

    def set(self, key: str, value: str) -> None:
        self.dict[key] = value

        if self.key_queue_dict.get(key) is None:
            self.key_queue_dict[key] = self.queue_list.prepend(key)
            self.count += 1

            if self.count > self.capacity:
                self.rem(self.queue_list.end.value)

    def rem(self, key: str) -> None:
        if self.dict.get(key) is None:
            return

        self.queue_list.remove(self.key_queue_dict[key])
        del self.key_queue_dict[key]
        del self.dict[key]
        self.count -= 1
